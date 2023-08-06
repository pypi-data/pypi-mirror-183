import json

from PaasSdk.CreateRequestClient import CreateRequestClient as Client
from PaasSdk.Config import Config as Config
from PaasSdk import RequestModel as models
from PaasSdk import ResponseModel as responseModels

request = models.CreateApplicationsRequestModel(AppName="python测试")

config = Config(AppId="cca183a860b9469db0dd893063360308",
                AppIdToken="319e3df531cb4d629331105d9bad05cb",
                AccountSid="00000000521547df5j41k45f8629801f",
                AccountToken="201181216269332252a816unz3h8la01")
client = Client(config)
dayRequest = models.AccountsAppIdDayRequestModel(Type=1,
                                          StartTime="2022-12-01",
                                          EndDate="2022-12-29")

info = client.QueryAccountAppInfo()
print(info.Msg)
print(info.Flag)
print(info.Total)
for k in info.Data:
    print(k.CompanyName + "   " + str(k.Banlance))
# if info["Flag"] == 200:
#     print(info["Data"])
# else:
#     print(info["Msg"])

