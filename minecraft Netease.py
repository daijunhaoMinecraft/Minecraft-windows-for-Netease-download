import webbrowser
import requests
import json
payload = {"os":"10.0","version":100000000,"entity_id":1}
header = {"content-type":"application/json"}
# 字典转换为json串
data = json.dumps(payload)
url = 'https://x19apigatewayobt.nie.netease.com/cpp-game-client-info'
response = requests.post(url,data=data,headers=header)
res=json.loads(response.text)
res1=res['entity']
print("网易我的世界基岩版url获取器1.0(By daijunhao),(github:daijunhaoMinecraft)")
print("github链接：https://github.com/daijunhaoMinecraft/Minecraft-windows-for-Netease-download")
print("返回代码:"+str(res['code']))
print("返回值:"+res['message'])
print("下载地址:"+res1['url'])
print("大小:"+str(res1['size'])+"KB")
print("md5值:"+res1['md5'])
input("按下Enter键打开浏览器下载")
webbrowser.open(res1['url'])