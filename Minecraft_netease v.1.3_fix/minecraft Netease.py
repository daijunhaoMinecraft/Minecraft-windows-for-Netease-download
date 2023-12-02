"""
项目代码
使用Python写成
使用Python运行需要安装requests库(pip install requests)
若使用Wget下载请下载项目里面的wget.exe并把他与此py文件放在py文件夹下,否则选择Wget的选项会报错（建议使用release里面现成的exe文件,这个exe文件里面包含wget）
若使用第三个选项的话请下载项目里面的wget.exe和7z.exe还有7z.dll这3个项目放在python文件夹下(建议使用release里面现成的exe文件,这个exe文件里面包含wget,7z.exe和7z.dll,直接双击打开就行)
重要的事情说三遍：严禁倒卖！严禁倒卖！严禁倒卖！
"""
import os
import webbrowser
import requests
import json
import winreg


def windowsmc_path():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Netease\MCLauncher')
    path = winreg.QueryValueEx(key, "MinecraftBENeteasePath")[0]
    return path
windowsmc_path1 = windowsmc_path()

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
print("网易我的世界基岩版url获取器v1.3-fix(By daijunhao),(github:daijunhaoMinecraft)")
print("更新内容：更新.checkInfo")
print("严禁倒卖!此软件仅供学习和交流使用,请在下载后24小时内删除")
print("github链接：https://github.com/daijunhaoMinecraft/Minecraft-windows-for-Netease-download")
print("返回代码:"+str(res['code']))
print("返回值:"+res['message'])
print("下载地址:"+res1['url'])
print("大小:"+str(res1['size'])+"KB")
print("md5值:"+res1['md5'])
print("当前基岩版路径:",windowsmc_path1)
while True:
    print("输入1选择浏览器下载")
    print("输入2选择使用Wget下载(默认保存位置为桌面)")
    print("输入3选择使用Wget下载并自动补齐基岩版文件")
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
    elif download_input=="3":
        print("正在执行目录删除旧版本目录操作...")
        os.system(f"rmdir /s /q {desktop_path1}\\windowsmc")
        print("正在下载...")
        pathx=os.path.dirname(os.path.abspath(__file__))
        os.system(f"{pathx}\\wget.exe -c -O {desktop_path1}\\Minecraft.7z {res1['url']}")
        print("下载完成,正在执行解压操作...")
        os.system(f"{pathx}\\7z.exe x {desktop_path1}\\Minecraft.7z -o{desktop_path1}\\")
        print("解压完成,正在删除下载好的文件")
        os.system(f"del /f /s /q {desktop_path1}\\Minecraft.7z")
        print("删除完成,正在执行移动操作")
        input("按下Enter键删除已经安装好的windowsmc文件夹(请备份好你的windowsmc文件夹!若你是新安装的,则无视直接按下Enter键)")
        print("正在执行删除操作...")
        os.system(f"rmdir /s /q {windowsmc_path1}\\windowsmc")
        print("开始执行移动操作")
        os.system(f"move {desktop_path1}\\windowsmc {windowsmc_path1}\\")
        print("完成,正在下载.checkInfo文件(网易基岩版验证文件)")
        os.system(f"{pathx}\\wget.exe -c -O {desktop_path1}\\.checkInfo https://gitee.com/dai-junhao-123/Minecraft-windows-for-Netease-download/raw/main/.checkInfo")
        print("完成,正在移动.checkInfo文件")
        os.system(f"move {desktop_path1}\\.checkInfo {windowsmc_path1}\\windowsmc\\")
        input("完成,按下Enter键退出")
        break