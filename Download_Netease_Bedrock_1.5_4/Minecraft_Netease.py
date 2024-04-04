# -*- coding:utf-8 -*-
import sys

import wx
from Taowa_wx import *
from Taowa_skin import *

皮肤_加载(皮肤.Areo)

import time
import winreg
import requests
import json
import datetime
import pyperclip3 as pycopy
import webbrowser
import os
import logging
import shutil
import subprocess
from urllib.parse import urlparse
#获取当前执行exe的路径
pathx_pyinstaller = os.path.dirname(os.path.realpath(sys.argv[0]))
#忽略证书警告
requests.packages.urllib3.disable_warnings()
#请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
}

versions = "1.6"

# 获取当前系统的桌面绝对路径
def desktop_path():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    path = winreg.QueryValueEx(key, "Desktop")[0]
    return path
desktop_path = desktop_path()

logging.basicConfig(level=logging.INFO,filename=f'{desktop_path}/Download_Netease_Bedrock_Debug.log',format=('%(asctime)s - %(levelname)s - %(message)s'))

class uqdate_Frame(wx_Frame):
    def __init__(self):
        wx_Frame.__init__(self, None, title='软件更新', size=(504, 518),name='frame',style=541072384)
        self.启动窗口 = wx_StaticText(self)
        self.Centre()
        self.单选框1 = wx_RadioButton(self.启动窗口,size=(120, 24),pos=(11, 374),name='radioButton',label='ghproxy源')
        self.单选框1.SetValue(True)
        self.单选框2 = wx_RadioButton(self.启动窗口,size=(120, 24),pos=(11, 410),name='radioButton',label='不使用加速源')
        self.进度条1 = wx_Gauge(self.启动窗口,range=100,size=(468, 24),pos=(11, 13),name='gauge',style=4)
        self.进度条1.SetValue(0)
        self.标签1 = wx_StaticTextL(self.启动窗口,size=(209, 24),pos=(11, 49),label='下载速度:',name='staticText',style=1)
        self.标签2 = wx_StaticTextL(self.启动窗口,size=(209, 24),pos=(11, 74),label='剩余时间:',name='staticText',style=1)
        self.标签3 = wx_StaticTextL(self.启动窗口,size=(209, 24),pos=(11, 99),label='文件大小:',name='staticText',style=1)
        self.标签4 = wx_StaticTextL(self.启动窗口,size=(209, 24),pos=(11, 150),label='当前下载进度:',name='staticText',style=1)
        self.单选框3 = wx_RadioButton(self.启动窗口,size=(120, 24),pos=(11, 340),name='radioButton',label='自定义加速源')
        self.编辑框1 = wx_TextCtrl(self.启动窗口,size=(214, 118),pos=(11, 206),value='由于下载更新地址是在github网站上,可能会有一小部分人访问不了,所以就有了github加速源选择\\n\n比如文件是https://mirror.ghproxy.com/https://github.com/xxx,那么就截取https://mirror.ghproxy.com这一部分\n需要注意检查更新地址无法加速',name='text',style=1073745968)
        self.start_uqdate = wx_Button(self.启动窗口,size=(80, 32),pos=(381, 410),label='检查更新',name='button')
        self.start_uqdate.Bind(wx.EVT_BUTTON,self.start_uqdate_按钮被单击)
        self.no_uqdate = wx_Button(self.启动窗口,size=(80, 32),pos=(283, 410),label='不检查更新',name='button')
        self.no_uqdate.Bind(wx.EVT_BUTTON,self.no_uqdate_按钮被单击)
        self.start_download = wx_Button(self.启动窗口,size=(80, 32),pos=(381, 358),label='开始下载文件',name='button')
        self.start_download.Disable()
        self.start_download.Bind(wx.EVT_BUTTON,self.start_download_按钮被单击)
        self.Uqdate_text = wx_TextCtrl(self.启动窗口,size=(182, 136),pos=(274, 204),value='',name='text',style=1073745968)
        self.标签6 = wx_StaticTextL(self.启动窗口,size=(209, 24),pos=(11, 124),label='已下载大小:',name='staticText',style=1)
        self.编辑框3 = wx_TextCtrl(self.启动窗口,size=(234, 22),pos=(140, 341),value='',name='text',style=0)



    def start_uqdate_按钮被单击(self,event):
        uqdate_json = json.loads(requests.get("https://api.github.com/repos/daijunhaoMinecraft/Minecraft-windows-for-Netease-download/releases/latest",headers=headers,verify=False).text)
        if uqdate_json['name'] == versions:
            message_info = wx.MessageDialog(None, caption="info",message="未发现新版本",style=wx.OK | wx.ICON_INFORMATION)
            if message_info.ShowModal() == wx.ID_OK:
                self.Destroy()
                myApp().MainLoop()
        elif uqdate_json['name'] != versions:
            self.Uqdate_text.SetLabel(f"当前版本:{str(versions)}\n最新版本:{str(uqdate_json['name'])}\n更新内容:\n{str(uqdate_json['body'])}\n下载地址:{str(uqdate_json['assets'][0]['browser_download_url'])}\n软件更新时间:{str(uqdate_json['created_at'])}")
            message_info = wx.MessageDialog(None, caption="info",message="发现新版本",style=wx.OK | wx.ICON_WARNING)
            if message_info.ShowModal() == wx.ID_OK:
                self.start_download.Enable()


    def no_uqdate_按钮被单击(self,event):
        self.Destroy()
        myApp().MainLoop()


    def start_download_按钮被单击(self,event):
        uqdate_json = json.loads(requests.get("https://api.github.com/repos/daijunhaoMinecraft/Minecraft-windows-for-Netease-download/releases/latest",headers=headers, verify=False).text)
        if self.单选框1.GetValue() == True:
            response = requests.get("https://mirror.ghproxy.com/"+uqdate_json['assets'][0]['browser_download_url'], stream=True, headers=headers, verify=False)
        elif self.单选框2.GetValue() == True:
            response = requests.get(uqdate_json['assets'][0]['browser_download_url'], stream=True, headers=headers,verify=False)
        else:
            response = requests.get(f"{self.编辑框3.GetValue()}/"+uqdate_json['assets'][0]['browser_download_url'], stream=True, headers=headers,verify=False)
        total_size = int(response.headers.get('content-length', 0))
        downloaded_size = 0
        chunk_size = 1024

        start_time = time.time()

        with open(f"{pathx_pyinstaller}\\{uqdate_json['assets'][0]['name']}", "wb") as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                downloaded_size += len(data)
                progress = int(downloaded_size / total_size * 100)
                self.进度条1.SetValue(progress)

                elapsed_time = time.time() - start_time
                speed = downloaded_size / (1024 * elapsed_time)
                remaining_time = (total_size - downloaded_size) / (speed * 1024)

                self.标签1.SetLabel(f"下载速度: {speed / 1024:.2f} MB/s")
                self.标签3.SetLabel(f"文件大小: {total_size / (1024 * 1024):.2f} MB")
                self.标签2.SetLabel(f"剩余时间: {remaining_time:.2f} 秒")
                self.标签6.SetLabel(f"已下载大小: {downloaded_size / (1024 * 1024):.2f} MB")
                self.标签4.SetLabel(f"当前下载进度:{progress}%")
                wx.Yield()
        subprocess.Popen(f"{pathx_pyinstaller}\\{uqdate_json['assets'][0]['name']}", creationflags=subprocess.CREATE_NO_WINDOW)
        sys.exit()


class uqdate_myApp(wx.App):
    def  OnInit(self):
        self.frame = uqdate_Frame()
        self.frame.Show(True)
        return True


class Frame(wx.Frame):
    def __init__(self):
        wx_Frame.__init__(self, None,title=f'网易我的世界基岩版下载地址获取器v{str(versions)}(By daijunhao),(github:daijunhaoMinecraft);仅供学习交流,严禁用于商业用途,请于24小时内删除',size=(1474, 815), name='frame', style=541072384)
        icon = wx.Icon(f'{os.path.dirname(os.path.abspath(__file__))}\\Minecraft.Windows.ico')
        self.SetIcon(icon)
        self.启动窗口 = wx_StaticText(self)
        self.Centre()
        self.read_github = wx_TextCtrl(self.启动窗口,size=(231, 20),pos=(22, 57),value='',name='text',style=0)
        self.标签3 = wx_StaticTextL(self.启动窗口,size=(110, 25),pos=(22, 27),label='github源代码链接',name='staticText',style=1)
        self.标签3.Disable()
        self.标签4 = wx_StaticTextL(self.启动窗口,size=(110, 25),pos=(22, 81),label='gitee源代码链接',name='staticText',style=1)
        self.read_gitee = wx_TextCtrl(self.启动窗口,size=(231, 20),pos=(22, 111),value='',name='text',style=0)
        self.标签5 = wx_StaticTextL(self.启动窗口,size=(110, 25),pos=(22, 142),label='返回代码',name='staticText',style=1)
        self.read_code = wx_TextCtrl(self.启动窗口,size=(110, 20),pos=(22, 172),value='',name='text',style=0)
        self.read_download = wx_TextCtrl(self.启动窗口,size=(231, 20),pos=(22, 300),value='',name='text',style=0)
        self.read_Value = wx_TextCtrl(self.启动窗口,size=(110, 20),pos=(22, 236),value='',name='text',style=0)
        self.标签6 = wx_StaticTextL(self.启动窗口,size=(110, 25),pos=(22, 206),label='返回值',name='staticText',style=1)
        self.标签7 = wx_StaticTextL(self.启动窗口,size=(110, 25),pos=(22, 270),label='下载地址',name='staticText',style=1)
        self.标签8 = wx_StaticTextL(self.启动窗口,size=(110, 25),pos=(22, 335),label='大小',name='staticText',style=1)
        self.read_debug = wx_TextCtrl(self.启动窗口,size=(682, 249),pos=(755, 54),value='',name='text',style=1073745968)
        self.read_md5 = wx_TextCtrl(self.启动窗口,size=(231, 20),pos=(22, 430),value='',name='text',style=0)
        self.read_size = wx_TextCtrl(self.启动窗口,size=(231, 20),pos=(22, 367),value='',name='text',style=0)
        self.标签9 = wx_StaticTextL(self.启动窗口,size=(110, 25),pos=(22, 399),label='MD5值',name='staticText',style=1)
        self.github = wx_Button(self.启动窗口,size=(80, 32),pos=(266, 51),label='copy',name='button')
        self.github.Bind(wx.EVT_BUTTON,self.github_按钮被单击)
        self.gitee = wx_Button(self.启动窗口,size=(80, 32),pos=(265, 105),label='copy',name='button')
        self.gitee.Bind(wx.EVT_BUTTON,self.gitee_按钮被单击)
        self.return_code = wx_Button(self.启动窗口,size=(80, 32),pos=(138, 167),label='copy',name='button')
        self.return_code.Bind(wx.EVT_BUTTON,self.return_code_按钮被单击)
        self.Return_value = wx_Button(self.启动窗口,size=(80, 32),pos=(138, 230),label='copy',name='button')
        self.Return_value.Bind(wx.EVT_BUTTON,self.Return_value_按钮被单击)
        self.Netease_Minecraft_download = wx_Button(self.启动窗口,size=(80, 32),pos=(261, 294),label='copy',name='button')
        self.Netease_Minecraft_download.Bind(wx.EVT_BUTTON,self.Netease_Minecraft_download_按钮被单击)
        self.size_Minecraft = wx_Button(self.启动窗口,size=(80, 32),pos=(261, 360),label='copy',name='button')
        self.size_Minecraft.Bind(wx.EVT_BUTTON,self.size_Minecraft_按钮被单击)
        self.MD5_Minecraft = wx_Button(self.启动窗口,size=(80, 32),pos=(261, 424),label='copy',name='button')
        self.MD5_Minecraft.Bind(wx.EVT_BUTTON,self.MD5_Minecraft_按钮被单击)
        self.标签10 = wx_StaticTextL(self.启动窗口,size=(120, 25),pos=(757, 22),label='输出日志:',name='staticText',style=1)
        self.OpenWeb = wx_Button(self.启动窗口,size=(240, 82),pos=(452, 107),label='使用浏览器下载',name='button')
        self.OpenWeb.Bind(wx.EVT_BUTTON,self.OpenWeb_按钮被单击)
        self.GET_Download = wx_Button(self.启动窗口,size=(240, 82),pos=(453, 200),label='使用Wget下载(默认保存位置为桌面)',name='button')
        self.GET_Download.Bind(wx.EVT_BUTTON,self.GET_Download_按钮被单击)
        self.zip_GET_download = wx_Button(self.启动窗口,size=(240, 82),pos=(452, 293),label='使用Wget下载并解压(默认保存位置为桌面)',name='button')
        self.zip_GET_download.Bind(wx.EVT_BUTTON,self.zip_GET_download_按钮被单击)
        self.Minecrat_for_Netease = wx_Button(self.启动窗口,size=(240, 82),pos=(452, 387),label='重新安装基岩版文件',name='button')
        self.Minecrat_for_Netease.SetForegroundColour((255, 0, 0, 255))
        self.Minecrat_for_Netease.Bind(wx.EVT_BUTTON,self.Minecrat_for_Netease_按钮被单击)
        self.标签11 = wx_StaticTextL(self.启动窗口,size=(80, 24),pos=(755, 327),label='当前任务进度:',name='staticText',style=1)
        self.进度条1 = wx_Gauge(self.启动窗口,range=100,size=(680, 24),pos=(755, 358),name='gauge',style=4)
        self.进度条1.SetValue(0)
        self.标签12 = wx_StaticTextL(self.启动窗口,size=(348, 24),pos=(755, 398),label='当前执行任务进度:',name='staticText',style=1)
        self.标签14 = wx_StaticTextL(self.启动窗口,size=(678, 24),pos=(755, 461),label='当前下载进度:',name='staticText',style=1)
        self.进度条2 = wx_Gauge(self.启动窗口,range=100,size=(680, 24),pos=(755, 492),name='gauge',style=4)
        self.进度条2.SetValue(0)
        self.标签15 = wx_StaticTextL(self.启动窗口,size=(677, 24),pos=(755, 528),label='当前正在下载文件:',name='staticText',style=1)
        self.标签16 = wx_StaticTextL(self.启动窗口,size=(675, 24),pos=(755, 549),label='下载速度:',name='staticText',style=1)
        self.标签17 = wx_StaticTextL(self.启动窗口,size=(675, 24),pos=(755, 572),label='剩余时间:',name='staticText',style=1)
        self.标签18 = wx_StaticTextL(self.启动窗口,size=(675, 24),pos=(755, 595),label='文件大小:',name='staticText',style=1)
        self.标签19 = wx_StaticTextL(self.启动窗口,size=(675, 24),pos=(755, 618),label='当前下载进度:',name='staticText',style=1)
        self.Bedrock_Netease = wx_RadioButton(self.启动窗口,size=(181, 24),pos=(27, 617),name='radioButton',label='netease版基岩版安装路径:')
        self.Bedrock_Netease.SetValue(True)
        self.Bedrock_4399 = wx_RadioButton(self.启动窗口,size=(181, 24),pos=(27, 656),name='radioButton',label='4399版基岩版安装路径:')
        self.Bedrock_user_select = wx_RadioButton(self.启动窗口,size=(181, 24),pos=(27, 693),name='radioButton',label='自定义基岩版安装路径:')
        self.Bedrock_Netease_Path = wx_TextCtrl(self.启动窗口,size=(491, 22),pos=(214, 620),value='',name='text',style=0)
        self.Bedrock_4399_Path = wx_TextCtrl(self.启动窗口,size=(491, 22),pos=(214, 659),value='',name='text',style=0)
        self.Bedrock_user_select_Path = wx_TextCtrl(self.启动窗口,size=(491, 22),pos=(214, 697),value='',name='text',style=0)
        self.select_files = wx_Button(self.启动窗口,size=(80, 32),pos=(709, 690),label='选择文件夹',name='button')
        self.select_files.Bind(wx.EVT_BUTTON,self.select_files_按钮被单击)
        self.标签20 = wx_StaticTextL(self.启动窗口,size=(675, 24),pos=(755, 640),label='已下载大小：',name='staticText',style=1)
        try:
            def windowsmc_Netease_path():
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Netease\MCLauncher')
                path = winreg.QueryValueEx(key, "MinecraftBENeteasePath")[0]
                return path
            self.Bedrock_Netease_Path.SetLabel(f"{windowsmc_Netease_path()}")
        except FileNotFoundError:
            self.Bedrock_Netease.Disable()
            self.Bedrock_Netease_Path.SetLabel("当前不可用,请检查你是否安装该版本")
        try:
            def windowsmc_4399_path():
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Netease\PC4399_MCLauncher')
                path = winreg.QueryValueEx(key, "MinecraftBENeteasePath")[0]
                return path
            self.Bedrock_4399_Path.SetLabel(f"{windowsmc_4399_path()}")
        except FileNotFoundError:
            self.Bedrock_4399.Disable()
            self.Bedrock_4399_Path.SetLabel("当前不可用,请检查你是否安装该版本")

        global pathx
        global res1
        global res
        pathx = os.path.dirname(os.path.abspath(__file__))
        payload = {"os": "10.0", "version": 100000000, "entity_id": 1}
        header = {"content-type": "application/json"}
        # 字典转换为json串
        data = json.dumps(payload)
        url_post = 'https://x19apigatewayobt.nie.netease.com/cpp-game-client-info'
        response = requests.post(url_post, data=data, headers=header)
        res = json.loads(response.text)
        res1 = res['entity']
        self.read_github.AppendText("https://github.com/daijunhaoMinecraft/Minecraft-windows-for-Netease-download")
        self.read_gitee.AppendText("https://gitee.com/dai-junhao-123/Minecraft-windows-for-Netease-download")
        self.read_code.AppendText(str(res['code']))
        self.read_Value.AppendText(res['message'])
        self.read_download.AppendText(res1['url'])
        self.read_size.AppendText(str(res1['size']) + "KB")
        self.read_md5.AppendText(res1['md5'])
        self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]')+"程序启动\n")
        logging.info("程序启动")
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.auto_progress, self.timer)
        self.timer.Start(100)


    def download(self,name,url,save):
        response = requests.get(url, stream=True, headers=headers,verify=False)
        total_size = int(response.headers.get('content-length', 0))
        downloaded_size = 0
        chunk_size = 1024

        start_time = time.time()

        with open(f"{save}\\{name}", "wb") as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                downloaded_size += len(data)
                progress = int(downloaded_size / total_size * 100)
                self.进度条2.SetValue(progress)

                elapsed_time = time.time() - start_time
                speed = downloaded_size / (1024 * elapsed_time)
                remaining_time = (total_size - downloaded_size) / (speed * 1024)
                self.标签15.SetLabel(f"当前正在下载文件:{name}")
                self.标签16.SetLabel(f"下载速度: {speed / 1024:.2f} MB/s")
                self.标签18.SetLabel(f"文件大小: {total_size / (1024 * 1024):.2f} MB")
                self.标签17.SetLabel(f"剩余时间: {remaining_time:.2f} 秒")
                self.标签20.SetLabel(f"已下载大小: {downloaded_size / (1024 * 1024):.2f} MB")
                self.标签19.SetLabel(f"当前下载进度:{progress}%")
                wx.Yield()

    def auto_progress(self, event):
        self.标签12.SetLabel(f"当前执行任务进度:{self.进度条1.GetValue()}%")

    def github_按钮被单击(self,event):
        pycopy.copy(self.read_github.GetLabelText())
        self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "github链接复制成功,请粘贴到浏览器上打开\n")


    def gitee_按钮被单击(self,event):
        pycopy.copy(self.read_gitee.GetLabelText())
        self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "github链接复制成功,请粘贴到浏览器上打开\n")

    def return_code_按钮被单击(self,event):
        pycopy.copy(self.read_code.GetLabelText())
        self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "返回代码复制成功\n")


    def Return_value_按钮被单击(self,event):
        pycopy.copy(self.read_Value.GetLabelText())
        self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "返回值复制成功\n")


    def Netease_Minecraft_download_按钮被单击(self,event):
        pycopy.copy(self.read_download.GetLabelText())
        self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "网易我的世界基岩版下载链接复制成功\n")


    def size_Minecraft_按钮被单击(self,event):
        pycopy.copy(self.read_size.GetLabelText())
        self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "压缩包大小复制成功\n")


    def MD5_Minecraft_按钮被单击(self,event):
        pycopy.copy(self.read_md5.GetLabelText())
        self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "MD5值复制成功\n")


    def OpenWeb_按钮被单击(self,event):
        webbrowser.open(res1['url'])
        self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "浏览器打开成功\n")


    def GET_Download_按钮被单击(self,event):
        logging.info("用户选择:使用GET下载")
        Confirm_the_information=wx.MessageDialog(None, u"是否继续执行GET下载?", u"确认信息", wx.YES_NO | wx.ICON_INFORMATION)
        if Confirm_the_information.ShowModal()==wx.ID_YES:
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "------使用GET下载(Debug)------\n")
            logging.info("------使用GET方式下载(Debug)------")
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "正在执行禁用按钮命令\n")
            logging.info("正在执行禁用按钮命令")
            self.OpenWeb.Disable()
            self.GET_Download.Disable()
            self.zip_GET_download.Disable()
            self.Minecrat_for_Netease.Disable()
            self.进度条1.SetValue(25)
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在执行下载命令\n")
            logging.info("完成,正在执行下载命令")
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_GET_Download!\n")
            logging.info("Start_GET_Download!")
            self.download(f"{urlparse(res1['url']).path.split('/')[-1]}",f"{res1['url']}", f"{desktop_path}")
            self.进度条1.SetValue(50)
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S') + " All done]"+"完成下载!\n")
            logging.info("完成下载,正在执行解禁按钮命令")
            self.OpenWeb.Enable()
            self.GET_Download.Enable()
            self.zip_GET_download.Enable()
            self.Minecrat_for_Netease.Enable()
            self.进度条1.SetValue(75)
            logging.info("Done!")
            self.进度条1.SetValue(100)
            download_stats = wx.MessageDialog(None, u"执行完成!", u"stats",wx.OK | wx.ICON_INFORMATION)
            if download_stats.ShowModal() == wx.ID_OK:
                download_stats.Destroy()
                self.进度条1.SetValue(0)


    def zip_GET_download_按钮被单击(self,event):
        logging.info("用户选择:使用GET下载并解压")
        Confirm_the_information = wx.MessageDialog(None, u"是否继续执行GET下载并解压缩?", u"确认信息",wx.YES_NO | wx.ICON_INFORMATION)
        if Confirm_the_information.ShowModal() == wx.ID_YES:
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "------使用GET下载并解压(Debug)------\n")
            logging.info("------使用GET下载并解压(Debug)------")
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "正在执行禁用按钮命令\n")
            logging.info("正在执行禁用按钮命令")
            self.OpenWeb.Disable()
            self.GET_Download.Disable()
            self.zip_GET_download.Disable()
            self.Minecrat_for_Netease.Disable()
            self.进度条1.SetValue(10)
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在执行删除旧版本目录操作\n")
            logging.info("完成,正在执行删除旧版本目录操作")
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_del/rmtree!\n")
            logging.info("Start_del/rmtree")
            logging.info("当前执行命令:del和rmtree")
            shutil.rmtree(f"{desktop_path}\\windowsmc", ignore_errors=True)
            os.system(f"del /f /s /q {desktop_path}\\Minecraft.7z")
            self.进度条1.SetValue(30)
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在执行下载命令\n")
            logging.info("完成,正在执行下载命令")
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_GET_Download!\n")
            logging.info("Start_GET_Download!")
            logging.info("Downloading...")
            self.download(f"{res1['url']}",f"{desktop_path}","Minecraft.7z")
            self.进度条1.SetValue(40)
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成下载,正在执行解压命令\n")
            logging.info("完成下载,正在执行解压命令")
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_7z_unpack!\n")
            logging.info("Start_7z_unpack!")
            logging.info("当前正在执行7z命令行解压命令")
            os.system(f"{pathx}\\bz\\bz.exe x -o:{desktop_path}\\ {desktop_path}\\Minecraft.7z")
            self.进度条1.SetValue(80)
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在删除临时文件\n")
            logging.info("完成,正在删除临时文件")
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "start_del!\n")
            logging.info("start_del!")
            logging.info("当前执行命令:del")
            os.system(f"del /f /s /q {desktop_path}\\Minecraft.7z")
            self.进度条1.SetValue(90)
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S') + " All done]"+"完成!\n")
            logging.info("完成,正在执行解禁按钮命令")
            self.OpenWeb.Enable()
            self.GET_Download.Enable()
            self.zip_GET_download.Enable()
            self.Minecrat_for_Netease.Enable()
            self.进度条1.SetValue(100)
            logging.info("Done!")
            download_zip_stats = wx.MessageDialog(None, u"执行完成!", u"stats", wx.OK | wx.ICON_INFORMATION)
            if download_zip_stats.ShowModal() == wx.ID_OK:
                self.进度条1.SetValue(0)
                download_zip_stats.Destroy()


    def Minecrat_for_Netease_按钮被单击(self,event):
        if self.Bedrock_Netease.GetValue() == True:
            windowsmc = self.Bedrock_Netease_Path.GetValue()
        elif self.Bedrock_4399_Path.GetValue() == True:
            windowsmc = self.Bedrock_4399_Path.GetValue()
        elif self.Bedrock_user_select.GetValue() == True:
            if os.path.exists(f"{self.Bedrock_user_select_Path.GetValue()}"):
                windowsmc = self.Bedrock_user_select_Path.GetValue()
            else:
                files_Error = wx.MessageDialog(None, caption="Error", message="你选择的文件路径并没有此文件夹",style=wx.OK | wx.ICON_ERROR)
                if files_Error.ShowModal() == wx.ID_OK:
                    pass
                    return
        try:
            windowsmc = windowsmc
        except Exception:
            files_Error = wx.MessageDialog(None, caption="Error", message="你选择的文件路径并没有此文件夹",style=wx.OK | wx.ICON_ERROR)
            if files_Error.ShowModal() == wx.ID_OK:
                pass
                return
        logging.info("用户选择:重新安装基岩版文件/安装基岩版文件")
        warning = wx.MessageDialog(None, u"是否继续执行?(这可能会导致你的基岩版被删除重新下载)", u"警告",wx.YES_NO | wx.ICON_WARNING)
        if warning.ShowModal() == wx.ID_YES:
            logging.warning("用户继续执行")
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "------重新安装基岩版文件(Debug)------\n")
            logging.info("------重新安装基岩版文件(Debug)------")
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "正在执行禁用按钮命令\n")
            logging.info("正在执行禁用按钮命令")
            self.OpenWeb.Disable()
            self.GET_Download.Disable()
            self.zip_GET_download.Disable()
            self.Minecrat_for_Netease.Disable()
            self.进度条1.SetValue(10)
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在执行删除旧版本目录操作/电脑上的网易我的世界基岩版\n")
            logging.info("完成,正在执行删除旧版本目录操作/电脑上的网易我的世界基岩版")
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_del/rmtree!\n")
            logging.info("Start_del/rmtree!")
            logging.info("当前执行命令:del和rmtree")
            shutil.rmtree(f"{windowsmc}\\windowsmc", ignore_errors=True)
            os.system(f"del /f /s /q {desktop_path}\\Minecraft.7z")
            self.进度条1.SetValue(20)
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在执行下载命令\n")
            logging.info("完成,正在执行下载命令")
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_GET_Download!\n")
            logging.info("Start_GET_Download!")
            logging.info("Downloading...")
            self.download("Minecraft.7z", f"{res1['url']}",f"{windowsmc}")
            self.进度条1.SetValue(30)
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成下载,正在执行解压命令\n")
            logging.info("完成下载,正在执行解压命令")
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_7z_unpack!\n")
            logging.info("Start_7z_unpack!")
            logging.info("当前正在执行7z命令行解压命令")
            os.system(f"{pathx}\\bz\\bz.exe x -o:{windowsmc}\\ {windowsmc}\\Minecraft.7z")
            self.进度条1.SetValue(40)
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在下载.checkInfo文件\n")
            logging.info("完成,正在下载.checkInfo文件")
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_GET_Download!\n")
            logging.info("Start_GET_Download")
            logging.info("Downloading...")
            self.download(".checkInfo","https://gitee.com/dai-junhao-123/Minecraft-windows-for-Netease-download/raw/main/.checkInfo",f"{windowsmc}\\windowsmc")
            self.进度条1.SetValue(50)
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在删除临时文件\n")
            logging.info("完成,正在删除临时文件")
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "start_del!\n")
            logging.info("start_del!")
            logging.info("正在执行命令:del")
            os.system(f"del /f /s /q {windowsmc}\\Minecraft.7z")
            self.进度条1.SetValue(60)
            self.read_debug.AppendText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S') + " All done]"+"完成!\n")
            logging.info("完成,正在执行解禁按钮命令")
            self.OpenWeb.Enable()
            self.GET_Download.Enable()
            self.zip_GET_download.Enable()
            self.Minecrat_for_Netease.Enable()
            self.进度条1.SetValue(80)
            logging.info("Done!")
            self.进度条1.SetValue(100)
            Reload_stats = wx.MessageDialog(None, u"执行完成!", u"stats", wx.OK | wx.ICON_INFORMATION)
            if Reload_stats.ShowModal() == wx.ID_OK:
                self.进度条1.SetValue(0)
                Reload_stats.Destroy()


    def select_files_按钮被单击(self,event):
        select_file_dlg = wx.DirDialog(self, message="选择一个文件夹", style=wx.DD_DEFAULT_STYLE)
        if select_file_dlg.ShowModal() == wx.ID_OK:
            self.Bedrock_user_select_Path.SetLabel(select_file_dlg.GetPath())

class myApp(wx.App):
    def  OnInit(self):
        self.frame = Frame()
        self.frame.Show(True)
        return True

if __name__ == '__main__':
    app = uqdate_myApp()
    app.MainLoop()