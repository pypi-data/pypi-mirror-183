from ..utils import request, fileLoad, graphql_request
import json


class DataManageModel(object):
    _kindUrlMap = {}
    _kindNameMap = {}
    _weatherUrl = ''
    _baseUri = ''

    def __init__(self, simulationId):
        self.simulationId = simulationId

    def _fetchItemData(self, url, kind):
        '''
            获取dataType类型对应所有数据项的 itemID 列表
            
            :params: dataType enum类型，数据的种类标识，比如Transformer, Load, HeatPrice等等
            
            :return: list类型，返回该种类下所有数据项的itemID的列表
        '''
        r = request('GET',
                    url,
                    params={
                        "simu_id": self.simulationId,
                        "kind": kind
                    })
        data = json.loads(r.text)
        return data

    def _saveItemData(self, url, data):
        r = request('POST', url, data=json.dumps(data))
        dataList = json.loads(r.text)

    def GetDataItem(self, id: str):
        '''
            获取itemID对应的元素信息
            
            :params: itemID string类型，代表数据项的标识符，可以在所有类型的数据项中实现唯一标识
            
            :return: dict类型，为源数据的引用，返回该数据项的信息
        '''

    def GetItemIDList(self, dataType):
        '''
            获取dataType类型对应所有数据项的itemID列表
            
            :params: dataType enum类型，数据的种类标识，比如Transformer, Load, HeatPrice等等
            
            :return: list类型，返回该种类下所有数据项的itemID的列表
        '''
        assert (dataType in self._kindNameMap
                or dataType in self._kindUrlMap), "数据类型不存在"
        kind = self._kindNameMap.get(dataType, dataType)

        dataList = self._fetchItemData(self._kindUrlMap[kind], kind)

        return dataList['results']

    def AddDataItem(self, dataType, data):
        '''
            向dataType类型的数据库中添加内容为data的数据项
            
            :params: dataType enum类型，数据的种类标识，比如Transformer, Load, HeatPrice等等
            :params: data dict类型，表示添加的数据内容，其数据结构应满足对应数据项的结构要求
            
            :return: string类型，返回新添加数据项的itemID，如果数据结构不满足要求，应当抛出异常
        '''
        assert (dataType in self._kindNameMap
                or dataType in self._kindUrlMap), "数据类型不存在"
        kind = self._kindNameMap.get(dataType, dataType)
        self._saveItemData(self._kindUrlMap[kind], [data])

    # def UpdateDataItem(self, dataType, data):
    #     '''
    #         向dataType类型的数据库中添加内容为data的数据项

    #         :params: dataType enum类型，数据的种类标识，比如Transformer, Load, HeatPrice等等
    #         :params: data dict类型，表示添加的数据内容，其数据结构应满足对应数据项的结构要求

    #         :return: string类型，返回新添加数据项的itemID，如果数据结构不满足要求，应当抛出异常
    #     '''
    #     assert (dataType in self._kindNameMap
    #             or dataType in self._kindUrlMap), "数据类型不存在"
    #     kind = self._kindNameMap.get(dataType, dataType)
    #     self._saveItemData(self._kindUrlMap[kind], [data])

    def SetProjectPosition(self, longitude, latitude):
        '''
            将项目的经纬度位置坐标设置为(longitude, latitude)
            
            :params: longitude float类型，表示经度，范围为气象数据源的经度范围
            :params: latitude float类型，表示纬度，范围为气象数据源的纬度范围
        '''
        r = request('GET',
                    self._baseUri + 'rest/weather_param/',
                    params={"simu": 533})
        param = json.loads(r.text)
        id = param['results'][0]['id']
        r = request('PUT',
                    self._baseUri + 'rest/weather_param/' + str(id) + '/',
                    data=json.dumps({
                        "id": id,
                        "lat": latitude,
                        "lng": longitude,
                        "simu": self.simulationId,
                        "simu_id": self.simulationId,
                    }))
        r = request('GET',
                    self._baseUri + 'load_weather/',
                    params={
                        "lat": latitude,
                        "lng": longitude,
                        "simu": self.simulationId,
                        "simu_id": self.simulationId,
                    })

    def GetAtmosData(self, startDate, endDate):
        '''
            获取在startDate到endDate之间的气象数据
            
            :params: startDate dateTime类型，表示开始时间
            :params: endDate dateTime类型，表示结束时间
            
            :return: list<dict>类型，为源数据的引用，返回当前项目位置对应时间范围内的气象数据序列，每个元素用字典进行表示，字典的key即区分不同的气象数据项（如风速、太阳辐照等）以及标识当前时间点
        '''
        pass

        r = request('GET',
                    self._weatherUrl,
                    params={
                        "time_after": endDate,
                        "time_before": startDate,
                        "sid": self.simulationId,
                    })
        weatherData = json.loads(r.text)
        return weatherData['results']


class IESSimulationDataManageModel(DataManageModel):
    _baseUri = 'api/ieslab-simulation/'
    _weatherUrl = 'api/ieslab-simulation/rest/weather_data/'
    _kindNameMap = {
        "光伏": "PhotovoltaicSys",
        "风机": "WindPowerGenerator",
        "燃气轮机": "GasTurbine",
        "热泵": "HeatPump",
        "燃气锅炉": "GasBoiler",
        "热管式太阳能集热器": "HPSolarCollector",
        "电压缩制冷机": "CompRefrg",
        "吸收式制冷机": "AbsorptionChiller",
        "蓄电池": "Battery",
        "储水罐": "WaterTank",
        "变压器": "Transformer",
        "传输线": "TransferLine",
        "模块化多电平变流器": "MMC",
        "离心泵": "CentrifugalPump",
        "管道": "Pipe",
        "采暖制冷负荷": "thermalLoads",
        "电负荷": "electricLoads",
        "燃料": "fuels",
        "热": "HVACHeating",
        "冷": "HVACCooling",
        "常数电价": "常数电价",
        "分时电价": "分时电价",
        "阶梯电价": "阶梯电价",
        "分时阶梯电价": "分时阶梯电价",
    }
    _kindUrlMap = {
        "PhotovoltaicSys": "api/ieslab-simulation/rest/dpcs/",
        "WindPowerGenerator": "api/ieslab-simulation/rest/dpcs/",
        "GasTurbine": "api/ieslab-simulation/rest/dpcs/",
        "HeatPump": "api/ieslab-simulation/rest/dhscs/",
        "GasBoiler": "api/ieslab-simulation/rest/dhscs/",
        "HPSolarCollector": "api/ieslab-simulation/rest/dhscs/",
        "CompRefrg": "api/ieslab-simulation/rest/dhscs/",
        "AbsorptionChiller": "api/ieslab-simulation/rest/dhscs/",
        "Battery": "api/ieslab-simulation/rest/escs/",
        "WaterTank": "api/ieslab-simulation/rest/escs/",
        "Transformer": "api/ieslab-simulation/rest/dstcs/",
        "TransferLine": "api/ieslab-simulation/rest/dstcs/",
        "MMC": "api/ieslab-simulation/rest/dstcs/",
        "CentrifugalPump": "api/ieslab-simulation/rest/hstcs/",
        "Pipe": "api/ieslab-simulation/rest/hstcs/",
        "thermalLoads": "api/ieslab-simulation/rest/thermalLoads/",
        "electricLoads": "api/ieslab-simulation/rest/electricLoads/",
        "fuels": "api/ieslab-simulation/rest/fuels/",
        "HVACHeating": "api/ieslab-simulation/rest/hots/",
        "HVACCooling": "api/ieslab-simulation/rest/colds/",
        "常数电价": "api/ieslab-simulation/rest/elects/",
        "分时电价": "api/ieslab-simulation/rest/elects/",
        "阶梯电价": "api/ieslab-simulation/rest/elects/",
        "分时阶梯电价": "api/ieslab-simulation/rest/elects/",
    }
    pass


class IESPlanDataManageModel(DataManageModel):
    _baseUri = 'api/ieslab-plan/'
    _weatherUrl = 'api/ieslab-plan/rest/weather_data/'
    _kindNameMap = {
        "光伏": "PhotovoltaicSys",
        "风机": "WindPowerGenerator",
        "燃气轮机": "GasTurbine",
        "热泵": "HeatPump",
        "燃气锅炉": "GasBoiler",
        "热管式太阳能集热器": "HPSolarCollector",
        "电压缩制冷机": "CompRefrg",
        "吸收式制冷机": "AbsorptionChiller",
        "蓄电池": "Battery",
        "储水罐": "WaterTank",
        "变压器": "Transformer",
        "传输线": "TransferLine",
        "模块化多电平变流器": "MMC",
        "离心泵": "CentrifugalPump",
        "管道": "Pipe",
        "采暖制冷负荷": "thermalLoads",
        "电负荷": "electricLoads",
        "燃料": "fuels",
        "热": "HVACHeating",
        "冷": "HVACCooling",
        "常数电价": "常数电价",
        "分时电价": "分时电价",
        "阶梯电价": "阶梯电价",
        "分时阶梯电价": "分时阶梯电价",
    }
    _kindUrlMap = {
        "PhotovoltaicSys": "api/ieslab-plan/rest/dpcs/",
        "WindPowerGenerator": "api/ieslab-plan/rest/dpcs/",
        "GasTurbine": "api/ieslab-plan/rest/dpcs/",
        "HeatPump": "api/ieslab-plan/rest/dhscs/",
        "GasBoiler": "api/ieslab-plan/rest/dhscs/",
        "HPSolarCollector": "api/ieslab-plan/rest/dhscs/",
        "CompRefrg": "api/ieslab-plan/rest/dhscs/",
        "AbsorptionChiller": "api/ieslab-plan/rest/dhscs/",
        "Battery": "api/ieslab-plan/rest/escs/",
        "WaterTank": "api/ieslab-plan/rest/escs/",
        "Transformer": "api/ieslab-plan/rest/dstcs/",
        "TransferLine": "api/ieslab-plan/rest/dstcs/",
        "MMC": "api/ieslab-plan/rest/dstcs/",
        "CentrifugalPump": "api/ieslab-plan/rest/hstcs/",
        "Pipe": "api/ieslab-plan/rest/hstcs/",
        "thermalLoads": "api/ieslab-plan/rest/thermalLoads/",
        "electricLoads": "api/ieslab-plan/rest/electricLoads/",
        "fuels": "api/ieslab-plan/rest/fuels/",
        "HVACHeating": "api/ieslab-plan/rest/hots/",
        "HVACCooling": "api/ieslab-plan/rest/colds/",
        "常数电价": "api/ieslab-plan/rest/elects/",
        "分时电价": "api/ieslab-plan/rest/elects/",
        "阶梯电价": "api/ieslab-plan/rest/elects/",
        "分时阶梯电价": "api/ieslab-plan/rest/elects/",
    }
    pass