# -*- coding: utf-8 -*-
import time
from PaasSdk import Config
from PaasSdk.RonyingCommon import RongyingCommon as RongyingCommon
from PaasSdk import RequestModel as models
import PaasSdk.DeveloperCenterConfig as urlConfig


def HttpRequestAppId(config: Config, url: str, body: dict()):
    dt = time.strftime("%Y%m%d%H%M%S", time.localtime())
    sig = RongyingCommon.getmd5string(config.AccountSid + ':' + config.AppId + ':' + dt)
    auth = RongyingCommon.getbase64string((config.AppId + ":" + config.AppIdToken + ":" + dt).encode('utf-8'))
    return RongyingCommon.sendpost(url + sig, body, auth)


def HttpRequestAccount(config: Config, url: str, body: dict()):
    dt = time.strftime("%Y%m%d%H%M%S", time.localtime())
    sig = RongyingCommon.getmd5string(config.AccountSid + ':' + config.AccountToken + ':' + dt)
    auth = RongyingCommon.getbase64string((config.AccountSid + ":" + config.AccountToken + ":" + dt).encode('utf-8'))
    url = url + sig
    return RongyingCommon.sendpost(url, body, auth)


class PaasSendExampleApi:
    def __init__(self):
        pass

    '''
    创建应用
    '''
    def CreateApplications(self, config: Config, request: models.CreateApplicationsRequestModel):
        return HttpRequestAccount(config, urlConfig.Host + urlConfig.AppCreateAppCodeUrl, request.to_map())

    def QueryAppidCostRecordDay(self, config: Config, request: models.AccountsAppIdDayRequestModel):
        url = urlConfig.Host + urlConfig.AppCostDayCodeUrl
        return HttpRequestAppId(config, url, request.to_map())

    def QueryAppidInfo(self, config: Config):
        url = urlConfig.Host + urlConfig.AppQueryAppDetailCodeUrl
        return HttpRequestAppId(config, url, None)

    def QueryAccountAppInfo(self, config: Config):
        url = urlConfig.Host + urlConfig.AppQueryAccountAppCodeUrl
        return HttpRequestAccount(config, url, None)
