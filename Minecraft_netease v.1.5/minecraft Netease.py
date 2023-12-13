from nicegui import ui
import json
import requests
import os
import pyperclip3 as pycopy
import datetime
import winreg
import time

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

def Wget_download():
    print(datetime.datetime.now().strftime('\n[date:%Y-%m-%d time:%H:%M:%S]') + "------使用Wget下载(Debug)------")
    time.sleep(1)
    print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "正在执行Wget下载(在执行一些指令的时候,浏览器不响应界面是正常的,等命令执行完之后刷新一下就恢复正常了)")
    time.sleep(1)
    print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_Wget_Download!")
    os.system(f"{pathx}\\wget.exe -c -P {desktop_path1} {res1['url']}")
    print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S') + " All done]" + "完成下载!")

def zip_Wget_download():
    print(datetime.datetime.now().strftime('\n[date:%Y-%m-%d time:%H:%M:%S]') + "------使用Wget下载并解压(Debug)------")
    time.sleep(1)
    print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "正在执行删除旧版本目录操作(在执行一些指令的时候,浏览器不响应界面是正常的,等命令执行完之后刷新一下就恢复正常了)")
    time.sleep(1)
    print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_del/rmdir!")
    os.system(f"rmdir /s /q {desktop_path1}\\windowsmc")
    os.system(f"del /f /s /q {desktop_path1}\\Minecraft.7z")
    print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在执行下载命令")
    time.sleep(1)
    print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_Wget_Download!")
    os.system(f"{pathx}\\wget.exe -c -O {desktop_path1}\\Minecraft.7z {res1['url']}")
    print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成下载,正在执行解压命令")
    time.sleep(1)
    print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_7z_unpack!")
    os.system(f"{pathx}\\7z.exe x {desktop_path1}\\Minecraft.7z -o{desktop_path1}\\")
    print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在删除临时文件")
    time.sleep(1)
    print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "start_del!")
    os.system(f"del /f /s /q {desktop_path1}\\Minecraft.7z")
    print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S') + " All done]" + "完成!")

def Minecraft_For_Netease():
    print(datetime.datetime.now().strftime('\n[date:%Y-%m-%d time:%H:%M:%S]') + "------重新安装基岩版文件(Debug)------")
    time.sleep(1)
    print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "正在执行删除旧版本目录操作/电脑上的网易我的世界基岩版(在执行一些指令的时候,浏览器不响应界面是正常的,等命令执行完之后刷新一下就恢复正常了)")
    time.sleep(1)
    print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_del/rmdir!")
    os.system(f"rmdir /s /q {windowsmc_path1}\\windowsmc")
    os.system(f"rmdir /s /q {desktop_path1}\\windowsmc")
    os.system(f"del /f /s /q {desktop_path1}\\Minecraft.7z")
    print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在执行下载命令")
    time.sleep(1)
    print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_Wget_Download!")
    os.system(f"{pathx}\\wget.exe -c -O {desktop_path1}\\Minecraft.7z {res1['url']}")
    print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成下载,正在执行解压命令")
    time.sleep(1)
    print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_7z_unpack!")
    os.system(f"{pathx}\\7z.exe x {desktop_path1}\\Minecraft.7z -o{desktop_path1}\\")
    print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在移动windowsmc文件")
    time.sleep(1)
    print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_move!")
    os.system(f"move {desktop_path1}\\windowsmc {windowsmc_path1}\\")
    print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在下载.checkInfo文件")
    time.sleep(1)
    print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_Wget_Download!")
    os.system(
        f"{pathx}\\wget.exe -c -O {desktop_path1}\\.checkInfo https://gitee.com/dai-junhao-123/Minecraft-windows-for-Netease-download/raw/main/.checkInfo")
    print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在移动.checkInfo文件")
    time.sleep(1)
    print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_move!")
    os.system(f"move {desktop_path1}\\.checkInfo {windowsmc_path1}\\windowsmc")
    print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在删除临时文件")
    time.sleep(1)
    print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "start_del!")
    os.system(f"del /f /s /q {desktop_path1}\\Minecraft.7z")
    print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S') + " All done]" + "完成!")

# 创建一个标签
ui.label('欢迎使用网易我的世界基岩版下载地址获取器!')
global pathx
global res1
global res
pathx = os.path.dirname(os.path.abspath(__file__))
payload = {"os": "10.0", "version": 100000000, "entity_id": 1}
header = {"content-type": "application/json"}
# 字典转换为json串
data = json.dumps(payload)
url = 'https://x19apigatewayobt.nie.netease.com/cpp-game-client-info'
response = requests.post(url, data=data, headers=header)
res = json.loads(response.text)
res1 = res['entity']
ui.link('点击前往github', 'https://github.com/daijunhaoMinecraft/Minecraft-windows-for-Netease-download')
ui.link('点击前往gitee', 'https://gitee.com/dai-junhao-123/Minecraft-windows-for-Netease-download')
ui.label("v1.5更新内容:使用Nicegui图形化界面(其实就更新了个图形化界面,可以退回v1.4)")
ui.label("返回代码:"+str(res['code']))
ui.button('点我复制返回代码', on_click=lambda e:ui.notify((pycopy.copy(str(res['code'])),"返回代码复制成功")))
ui.label("返回值:"+res['message'])
ui.button('点我复制返回值', on_click=lambda e:ui.notify((pycopy.copy(str(res['message'])),"返回值复制成功")))
ui.label("下载地址:"+res1['url'])
ui.button('点我复制下载地址', on_click=lambda e:ui.notify((pycopy.copy(str(res1['url'])),"下载地址复制成功")))
ui.label("文件大小:"+str(res1['size'])+"KB")
ui.button('点我复制文件大小', on_click=lambda e:ui.notify((pycopy.copy(str(res1['url'])),"文件大小复制成功")))
ui.label("md5值:"+res1['md5'])
ui.button('点我复制MD5值', on_click=lambda e:ui.notify((pycopy.copy(str(res1['md5'])),"MD5值复制成功")))
ui.link('网易我的世界基岩版下载地址',f'{res1['url']}')
ui.button('点我使用Wget下载(默认保存路径为桌面)', on_click=lambda e:ui.notify(Wget_download()))
ui.button('点我使用Wget下载并自动解压(默认保存路径为桌面)', on_click=lambda e:ui.notify(zip_Wget_download()))
ui.label("警告！此按钮'重新安装基岩版文件/安装基岩版文件'可能会导致你的基岩版文件被替换成新的(如果你是没有安装的,则可以无视)").style('color:red;font-size:20px;font-weight:bold')
ui.button('重新安装基岩版文件/安装基岩版文件', on_click=lambda e:ui.notify(Minecraft_For_Netease()))
ui.run()
