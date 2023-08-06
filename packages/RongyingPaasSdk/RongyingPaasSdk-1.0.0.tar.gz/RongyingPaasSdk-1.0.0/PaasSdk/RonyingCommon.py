import base64
import hashlib
import requests


class RongyingCommon:

    def getmd5string(str):
        hmd5 = hashlib.md5()
        hmd5.update(str.encode('utf-8'))
        sig = hmd5.hexdigest()
        return sig.upper()

    def getbase64string(str):
        return base64.b64encode(str)

    def sendpost(url, body, auth):
        try:
            headers = {'content-type': 'application/json;charset=utf-8', 'Authorization': auth,
                       'Accept': 'application/json'}
            req = requests.post(url, json=body, headers=headers)
            return req.json()
        except:
            return "请求失败"
            exit()
