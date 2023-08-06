
import WZCMCCAPPLOGGER.GetNetWorkInfo
import WZCMCCAPPLOGGER.LogUploader
import requests
import json

'''
使用方法:
1.安装 python -m pip install WZCMCCAPPLOGGER
2.
#WZCMCCAPPLOGGER.url="192.168.5.103:82"
WZCMCCAPPLOGGER.InsertLog("[APPID]","[loginfo]");
url 可以选参数 可以输入 10.77.18.248:82 OA网段
192.168.5.103:82 内网网段
10.212.194.197:82 DCN网段

'''

name = "WZCMCCAPPLOGGER"

#API  DB  Redis
#log_type="DB"
url ='192.168.5.103:82'

def InsertLog(APPID,loginfo):

    mac = WZCMCCAPPLOGGER.GetNetWorkInfo.get_mac_address();
    pcname = WZCMCCAPPLOGGER.GetNetWorkInfo.get_hostName();
    ip = WZCMCCAPPLOGGER.GetNetWorkInfo.get_hostip();

    jsondata = {'APPID': APPID, 'loginfo': loginfo, 'mac': mac, 'pcname': pcname, 'ip': ip}
    re = requests.post(url='http://'+url+'/WZGJGLLOGAPI/CMCCAPILOG/SetLog', json=jsondata)#返回
    result =json.loads(re.text)
    if(result['Tag']>0):
        return "添加成功"
    else:
        return "添加失败"

__version__ = "0.80.0"

