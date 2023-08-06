import json

from PaasSdk import Config as Config
from PaasSdk.PaasSendExampleApi import PaasSendExampleApi as PaasSendExampleApi
from PaasSdk import RequestModel as models
from PaasSdk import ResponseModel as responseModels

class CreateRequestClient:
    def __init__(
            self,
            config: Config):
        self.config = config

    def CreateApplications(self, request: models.CreateApplicationsRequestModel):
        data = PaasSendExampleApi.CreateApplications(self, self.config, request)
        return responseModels.CreateApplicationsResponseModel.from_map(self, data)

    def QueryAppIdCostRecordDay(self, request: models.AccountsAppIdDayRequestModel):
        data = PaasSendExampleApi.QueryAppidCostRecordDay(self, self.config, request)
        return responseModels.AccountsAppIdDayResponseModel.from_map(self, data)

    def QueryAppidInfo(self):
        data = PaasSendExampleApi.QueryAppidInfo(self, self.config)
        return responseModels.AppIdInfoResponseModel.from_map(self, data)

    def QueryAccountAppInfo(self):
        data = PaasSendExampleApi.QueryAccountAppInfo(self, self.config)
        return responseModels.AppIdInfoResponseModel.from_map(self, data)

