"""
项目代码
使用Python写成
使用Python运行需要安装requests库(pip install requests)
若使用Wget下载请下载项目里面的wget.exe并把他与此py文件放在一起,否则选择Wget的选项会报错
重要的事情说三遍：严禁倒卖！严禁倒卖！严禁倒卖！
"""
import os
import webbrowser
import requests
import json
import winreg

# 获取当前系统的桌面绝对路径
def desktop_path():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    path = winreg.QueryValueEx(key, "Desktop")[0]
    return path
desktop_path1 = desktop_path()

payload = {"os":"10.0","version":100000000,"entity_id":1}
header = {"content-type":"application/json"}
# 字典转换为json串
data = json.dumps(payload)
url = 'https://x19apigatewayobt.nie.netease.com/cpp-game-client-info'
response = requests.post(url,data=data,headers=header)
res=json.loads(response.text)
res1=res['entity']
print("网易我的世界基岩版url获取器v1.1(By daijunhao),(github:daijunhaoMinecraft)")
print("严禁倒卖!此软件仅供学习和交流使用,请在下载后24小时内删除")
print("github链接：https://github.com/daijunhaoMinecraft/Minecraft-windows-for-Netease-download")
print("返回代码:"+str(res['code']))
print("返回值:"+res['message'])
print("下载地址:"+res1['url'])
print("大小:"+str(res1['size'])+"KB")
print("md5值:"+res1['md5'])
while True:
    print("输入1选择浏览器下载")
    print("输入2选择使用Wget下载(默认保存位置为桌面)")
    download_input=input("请输入:")
    if download_input=="1":
        webbrowser.open(res1['url'])
        break
    elif download_input=="2":
        print("正在下载...")
        pathx=os.path.dirname(os.path.abspath(__file__))
        os.system(f"{pathx}\\wget.exe -c -P {desktop_path1} {res1['url']}")
        input("下载完成,按下Enter键退出")
        break
