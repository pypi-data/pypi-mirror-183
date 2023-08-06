# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.

class CreateApplicationsRequestModel:
    def __init__(self,
                 AppName: str = None,
                 CallbackUrl: str = None,
                 SeatStatusUrl: str = None,
                 StatusUrl: str = None):
        self.AppName = AppName
        self.CallbackUrl = CallbackUrl
        self.SeatStatusUrl = SeatStatusUrl
        self.StatusUrl = StatusUrl

    def to_map(self):
        result = dict()
        if self.AppName is not None:
            result['AppName'] = self.AppName
        if self.CallbackUrl is not None:
            result['CallbackUrl'] = self.CallbackUrl
        if self.SeatStatusUrl is not None:
            result['SeatStatusUrl'] = self.SeatStatusUrl
        if self.StatusUrl is not None:
            result['StatusUrl'] = self.StatusUrl
        return result


class AccountsAppIdDayRequestModel:
    def __init__(self,
                 Type: int = None,
                 StartTime: str = None,
                 EndDate: str = None):
        self.Type = Type
        self.StartTime = StartTime
        self.EndDate = EndDate

    def to_map(self):
        result = dict()
        if self.Type is not None:
            result['Type'] = self.Type
        if self.StartTime is not None:
            result['StartTime'] = self.StartTime
        if self.EndDate is not None:
            result['EndDate'] = self.EndDate
        return result
