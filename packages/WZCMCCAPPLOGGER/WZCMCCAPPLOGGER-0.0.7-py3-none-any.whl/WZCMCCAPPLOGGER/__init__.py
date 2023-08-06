
import WZCMCCAPPLOGGER.GetNetWorkInfo
import WZCMCCAPPLOGGER.LogUploader
import requests
import json


name = "WZCMCCAPPLOGGER"

#API  DB  Redis
#log_type="DB"
url ='192.168.5.103:82'

def InsertLog(APPID,loginfo):

    mac = WZCMCCAPPLOGGER.GetNetWorkInfo.get_mac_address();
    pcname = WZCMCCAPPLOGGER.GetNetWorkInfo.get_hostName();
    ip = WZCMCCAPPLOGGER.GetNetWorkInfo.get_hostip();

    jsondata = {'APPID':APPID,'loginfo':loginfo}
    re = requests.post(url='http://'+url+'/WZGJGLLOGAPI/CMCCAPILOG/SetLog', json=jsondata)#返回
    result =json.loads(re.text)
    if(result['Tag']>0):
        return "添加成功"
    else:
        return "添加失败"

__version__ = "0.79.0"

