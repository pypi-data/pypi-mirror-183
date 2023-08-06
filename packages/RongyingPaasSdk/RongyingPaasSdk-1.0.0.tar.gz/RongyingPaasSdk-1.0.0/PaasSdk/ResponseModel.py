import time
from typing import List


class BaseResponseModel:
    def __init__(self,
                 Flag: int = None,
                 Msg: str = None):
        self.Msg = Msg
        self.Flag = Flag

class CreateApplicationsResponseModel(BaseResponseModel):
    def __init__(self, Flag: int = None, Msg: str = None,
                 AppToken: str = None,
                 AppId: str = None):
        super().__init__(Flag, Msg)
        self.AppToken = AppToken
        self.AppId = AppId

    # def to_map(self):
    #     result = dict()
    #     if self.Flag is not None:
    #         result['Flag'] = self.Flag
    #     if self.Msg is not None:
    #         result['Msg'] = self.Msg
    #     if self.AppToken is not None:
    #         result['AppToken'] = self.AppToken
    #     if self.AppId is not None:
    #         result['AppId'] = self.AppId
    #     return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flag') is not None:
            self.Flag = m.get('Flag')
        if m.get('Msg') is not None:
            self.Msg = m.get('Msg')
        if m.get('AppToken') is not None:
            self.AppToken = m.get('AppToken')
        if m.get('Appid') is not None:
            self.AppId = m.get('Appid')
        return self

class AccountsAppIdDayDetail:
    def __init__(self,
                 CostTimeDay: time = None,
                 CostMoneySum: float = None):
        self.CostTimeDay = CostTimeDay
        self.CostMoneySum = CostMoneySum

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTimeDay') is not None:
            self.CostTimeDay = m.get('CostTimeDay')
        if m.get('CostMoneySum') is not None:
            self.CostMoneySum = m.get('CostMoneySum')
        return self

class AccountsAppIdDayResponseModel(BaseResponseModel):
    def __init__(self, Flag: int = None, Msg: str = None,
                 Total: int = None,
                 Data: List[AccountsAppIdDayDetail] = None):
        super().__init__(Flag, Msg)
        self.Data = Data
        self.Total = Total

    def from_map(self, m: dict = None):
        m = m or dict()
        self.Data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AccountsAppIdDayDetail()
                self.Data.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.Total = m.get('Total')
        if m.get('Flag') is not None:
            self.Flag = m.get('Flag')
        if m.get('Msg') is not None:
            self.Msg = m.get('Msg')
        return self

class AppIdInfoDetail:
    def __init__(self,
                 CompanyName: str = None,
                 OrderTime: time = None,
                 Banlance: float = None,
                 AmountFe: float = None,
                 AppId: str = None,
                 AppToken: str = None,
                 Fee: float = None,
                 MinConsumption: int = None,
                 AmountFee: float = None,
                 ClickType: str = None,
                 Status: int = None):
        self.CompanyName = CompanyName
        self.OrderTime = OrderTime
        self.Banlance = Banlance
        self.AmountFe = AmountFe
        self.AppId = AppId
        self.AppToken = AppToken
        self.Fee = Fee
        self.MinConsumption = MinConsumption
        self.AmountFee = AmountFee
        self.ClickType = ClickType
        self.Status = Status

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompanyName') is not None:
            self.CompanyName = m.get('CompanyName')
        if m.get('OrderTime') is not None:
            self.OrderTime = m.get('OrderTime')
        if m.get('Banlance') is not None:
            self.Banlance = m.get('Banlance')
        if m.get('AmountFe') is not None:
            self.AmountFe = m.get('AmountFe')
        if m.get('AppId') is not None:
            self.AppId = m.get('AppId')
        if m.get('AppToken') is not None:
            self.AppToken = m.get('AppToken')
        if m.get('Fee') is not None:
            self.Fee = m.get('Fee')
        if m.get('MinConsumption') is not None:
            self.MinConsumption = m.get('MinConsumption')
        if m.get('AmountFee') is not None:
            self.AmountFee = m.get('AmountFee')
        if m.get('ClickType') is not None:
            self.ClickType = m.get('ClickType')
        if m.get('Status') is not None:
            self.Status = m.get('Status')
        return self

class AppIdInfoResponseModel(BaseResponseModel):
    def __init__(self, Flag: int = None, Msg: str = None,
                 Total: int = None,
                 Data: List[AppIdInfoDetail] = None):
        super().__init__(Flag, Msg)
        self.Data = Data
        self.Total = Total

    def from_map(self, m: dict = None):
        m = m or dict()
        self.Data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AppIdInfoDetail()
                self.Data.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.Total = m.get('Total')
        if m.get('Flag') is not None:
            self.Flag = m.get('Flag')
        if m.get('Msg') is not None:
            self.Msg = m.get('Msg')
        return self
