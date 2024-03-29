# -*- coding:utf-8 -*-
import wx
import winreg
import requests
import json
import datetime
import pyperclip3 as pycopy
import webbrowser
import time
import os
from colorama import Fore,Back,Style,init
import logging
import shutil
from urllib.parse import urlparse
from tqdm.tk import tqdm
requests.packages.urllib3.disable_warnings()
init(autoreset=True)

# 获取当前系统的桌面绝对路径
def desktop_path():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    path = winreg.QueryValueEx(key, "Desktop")[0]
    return path
desktop_path1 = desktop_path()

logging.basicConfig(level=logging.INFO,filename=f'{desktop_path1}/Download_Netease_Bedrock_Debug.log',format=('%(asctime)s - %(levelname)s - %(message)s'))
try:
    def windowsmc_path():
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Netease\MCLauncher')
        path = winreg.QueryValueEx(key, "MinecraftBENeteasePath")[0]
        return path
    windowsmc_path1 = windowsmc_path()
except FileNotFoundError as e:
    print(Back.RED+"出错了,此程序5秒后退出:",e)
    time.sleep(5)
    exit()

def download_nofilename(url, save):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'}
    download_file = requests.get(url,headers=headers,verify=False,stream=True)
    download_file_size = int(download_file.headers['Content-Length'])/1024
    file_name = os.path.basename(urlparse(url).path)
    with open(file=f"{save}\\{file_name}", mode="wb") as f:
        for data in tqdm(iterable=download_file.iter_content(1024),total=download_file_size,unit='k',desc=f"正在下载文件...[{file_name}]"):
            f.write(data)
def download(url, save, name):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'}
    download_file = requests.get(url,headers=headers,verify=False,stream=True)
    download_file_size = int(download_file.headers['Content-Length'])/1024
    with open(file=f"{save}\\{name}", mode="wb") as f:
        for data in tqdm(iterable=download_file.iter_content(1024),total=download_file_size,unit='k',desc=f"正在下载文件...[{name}]"):
            f.write(data)

class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='网易我的世界基岩版下载地址获取器v1.5_3(By daijunhao),(github:daijunhaoMinecraft),仅供学习交流,严禁用于商业用途,请于24小时内删除', size=(950, 670),name='frame',style=541072384)
        icon = wx.Icon(f'{os.path.dirname(os.path.abspath(__file__))}\\Minecraft.Windows.ico')
        self.SetIcon(icon)
        self.启动窗口 = wx.Panel(self)
        self.Centre()
        self.read_github = wx.TextCtrl(self.启动窗口,size=(231, 20),pos=(22, 57),value='',name='text',style=wx.TE_READONLY)
        self.标签3 = wx.StaticText(self.启动窗口,size=(110, 25),pos=(22, 18),label='github源代码链接',name='staticText',style=2321)
        self.标签4 = wx.StaticText(self.启动窗口,size=(110, 25),pos=(22, 118),label='gitee源代码链接',name='staticText',style=2321)
        self.read_gitee = wx.TextCtrl(self.启动窗口,size=(231, 20),pos=(22, 158),value='',name='text',style=wx.TE_READONLY)
        self.标签5 = wx.StaticText(self.启动窗口,size=(110, 25),pos=(22, 204),label='返回代码',name='staticText',style=2321)
        self.read_code = wx.TextCtrl(self.启动窗口,size=(110, 20),pos=(22, 236),value='',name='text',style=wx.TE_READONLY)
        self.read_download = wx.TextCtrl(self.启动窗口,size=(231, 20),pos=(22, 392),value='',name='text',style=wx.TE_READONLY)
        self.read_Value = wx.TextCtrl(self.启动窗口,size=(110, 20),pos=(22, 308),value='',name='text',style=wx.TE_READONLY)
        self.标签6 = wx.StaticText(self.启动窗口,size=(110, 25),pos=(22, 274),label='返回值',name='staticText',style=2321)
        self.标签7 = wx.StaticText(self.启动窗口,size=(110, 25),pos=(22, 360),label='下载地址',name='staticText',style=2321)
        self.标签8 = wx.StaticText(self.启动窗口,size=(110, 25),pos=(22, 454),label='大小',name='staticText',style=2321)
        self.read_debug = wx.TextCtrl(self.启动窗口,size=(427, 20),pos=(426, 53),value='',name='text',style=wx.TE_READONLY)
        self.read_md5 = wx.TextCtrl(self.启动窗口,size=(231, 20),pos=(22, 557),value='',name='text',style=wx.TE_READONLY)
        self.read_size = wx.TextCtrl(self.启动窗口,size=(231, 20),pos=(22, 487),value='',name='text',style=wx.TE_READONLY)
        self.标签9 = wx.StaticText(self.启动窗口,size=(110, 25),pos=(22, 530),label='MD5值',name='staticText',style=2321)
        self.github = wx.Button(self.启动窗口,size=(80, 32),pos=(266, 51),label='copy',name='button')
        self.github.Bind(wx.EVT_BUTTON,self.github_按钮被单击)
        self.gitee = wx.Button(self.启动窗口,size=(80, 32),pos=(265, 152),label='copy',name='button')
        self.gitee.Bind(wx.EVT_BUTTON,self.gitee_按钮被单击)
        self.return_code = wx.Button(self.启动窗口,size=(80, 32),pos=(138, 231),label='copy',name='button')
        self.return_code.Bind(wx.EVT_BUTTON,self.return_code_按钮被单击)
        self.Return_value = wx.Button(self.启动窗口,size=(80, 32),pos=(138, 302),label='copy',name='button')
        self.Return_value.Bind(wx.EVT_BUTTON,self.Return_value_按钮被单击)
        self.Netease_Minecraft_download = wx.Button(self.启动窗口,size=(80, 32),pos=(261, 386),label='copy',name='button')
        self.Netease_Minecraft_download.Bind(wx.EVT_BUTTON,self.Netease_Minecraft_download_按钮被单击)
        self.size_Minecraft = wx.Button(self.启动窗口,size=(80, 32),pos=(261, 477),label='copy',name='button')
        self.size_Minecraft.Bind(wx.EVT_BUTTON,self.size_Minecraft_按钮被单击)
        self.MD5_Minecraft = wx.Button(self.启动窗口,size=(80, 32),pos=(261, 556),label='copy',name='button')
        self.MD5_Minecraft.Bind(wx.EVT_BUTTON,self.MD5_Minecraft_按钮被单击)
        self.标签10 = wx.StaticText(self.启动窗口,size=(200, 25),pos=(426, 18),label='日志(更多详细请看cmd后台窗口)',name='staticText',style=2321)
        self.OpenWeb = wx.Button(self.启动窗口,size=(273, 82),pos=(544, 150),label='使用浏览器下载',name='button')
        self.OpenWeb.Bind(wx.EVT_BUTTON,self.OpenWeb_按钮被单击)
        self.GET_Download = wx.Button(self.启动窗口,size=(273, 82),pos=(545, 243),label='使用GET下载(默认保存位置为桌面)',name='button')
        self.GET_Download.Bind(wx.EVT_BUTTON,self.GET_Download_按钮被单击)
        self.zip_GET_download = wx.Button(self.启动窗口,size=(273, 82),pos=(544, 336),label='使用GET下载并解压(默认保存位置为桌面)',name='button')
        self.zip_GET_download.Bind(wx.EVT_BUTTON,self.zip_GET_download_按钮被单击)
        self.Minecrat_for_Netease = wx.Button(self.启动窗口,size=(273, 82),pos=(544, 430),label='重新安装基岩版文件/安装基岩版文件',name='button')
        self.Minecrat_for_Netease.SetForegroundColour((255, 0, 0, 255))
        self.Minecrat_for_Netease.Bind(wx.EVT_BUTTON,self.Minecrat_for_Netease_按钮被单击)

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
        self.read_github.SetLabelText("https://github.com/daijunhaoMinecraft/Minecraft-windows-for-Netease-download")
        self.read_gitee.SetLabelText("https://gitee.com/dai-junhao-123/Minecraft-windows-for-Netease-download")
        self.read_code.SetLabelText(str(res['code']))
        self.read_Value.SetLabelText(res['message'])
        self.read_download.SetLabelText(res1['url'])
        self.read_size.SetLabelText(str(res1['size']) + "KB")
        self.read_md5.SetLabelText(res1['md5'])
        self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]')+"程序启动")
        logging.info("程序启动")


    def github_按钮被单击(self,event):
        pycopy.copy(self.read_github.GetLabelText())
        self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "github链接复制成功,请粘贴到浏览器上打开")


    def gitee_按钮被单击(self,event):
        pycopy.copy(self.read_gitee.GetLabelText())
        self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "github链接复制成功,请粘贴到浏览器上打开")

    def return_code_按钮被单击(self,event):
        pycopy.copy(self.read_code.GetLabelText())
        self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "返回代码复制成功")


    def Return_value_按钮被单击(self,event):
        pycopy.copy(self.read_Value.GetLabelText())
        self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "返回值复制成功")


    def Netease_Minecraft_download_按钮被单击(self,event):
        pycopy.copy(self.read_download.GetLabelText())
        self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "网易我的世界基岩版下载链接复制成功")


    def size_Minecraft_按钮被单击(self,event):
        pycopy.copy(self.read_size.GetLabelText())
        self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "压缩包大小复制成功")


    def MD5_Minecraft_按钮被单击(self,event):
        pycopy.copy(self.read_md5.GetLabelText())
        self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "MD5值复制成功")


    def OpenWeb_按钮被单击(self,event):
        webbrowser.open(res1['url'])
        self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "浏览器打开成功")


    def GET_Download_按钮被单击(self,event):
        logging.info("用户选择:使用GET下载")
        Confirm_the_information=wx.MessageDialog(None, u"是否继续执行GET下载?", u"确认信息", wx.YES_NO | wx.ICON_INFORMATION)
        if Confirm_the_information.ShowModal()==wx.ID_YES:
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "------使用GET下载(Debug)------")
            logging.info("------使用GET方式下载(Debug)------")
            time.sleep(1)
            self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "正在执行禁用按钮命令")
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "正在执行禁用按钮命令")
            logging.info("正在执行禁用按钮命令")
            time.sleep(1)
            self.OpenWeb.Disable()
            self.GET_Download.Disable()
            self.zip_GET_download.Disable()
            self.Minecrat_for_Netease.Disable()
            self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在执行下载命令")
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在执行下载命令")
            logging.info("完成,正在执行下载命令")
            time.sleep(1)
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_GET_Download!")
            logging.info("Start_GET_Download!")
            download_nofilename(f"{res1['url']}", f"{desktop_path1}")
            self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S') + " All done]"+"完成下载!")
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S') + " All done]" + "完成下载!\n")
            logging.info("完成下载,正在执行解禁按钮命令")
            self.OpenWeb.Enable()
            self.GET_Download.Enable()
            self.zip_GET_download.Enable()
            self.Minecrat_for_Netease.Enable()
            logging.info("Done!")
            download_stats = wx.MessageDialog(None, u"执行完成!", u"stats",wx.OK | wx.ICON_INFORMATION)
            if download_stats.ShowModal() == wx.ID_OK:
                download_stats.Destroy()


    def zip_GET_download_按钮被单击(self,event):
        logging.info("用户选择:使用GET下载并解压")
        Confirm_the_information = wx.MessageDialog(None, u"是否继续执行GET下载并解压缩?", u"确认信息",wx.YES_NO | wx.ICON_INFORMATION)
        if Confirm_the_information.ShowModal() == wx.ID_YES:
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "------使用GET下载并解压(Debug)------")
            logging.info("------使用GET下载并解压(Debug)------")
            time.sleep(1)
            self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "正在执行禁用按钮命令")
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "正在执行禁用按钮命令")
            logging.info("正在执行禁用按钮命令")
            time.sleep(1)
            self.OpenWeb.Disable()
            self.GET_Download.Disable()
            self.zip_GET_download.Disable()
            self.Minecrat_for_Netease.Disable()
            self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在执行删除旧版本目录操作")
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在执行删除旧版本目录操作")
            logging.info("完成,正在执行删除旧版本目录操作")
            time.sleep(1)
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_del/rmtree!")
            logging.info("Start_del/rmtree")
            logging.info("当前执行命令:del和rmtree")
            shutil.rmtree(f"{desktop_path1}\\windowsmc", ignore_errors=True)
            os.system(f"del /f /s /q {desktop_path1}\\Minecraft.7z")
            self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在执行下载命令")
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在执行下载命令")
            logging.info("完成,正在执行下载命令")
            time.sleep(1)
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_GET_Download!")
            logging.info("Start_GET_Download!")
            logging.info("Downloading...")
            download(f"{res1['url']}",f"{desktop_path1}","Minecraft.7z")
            self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成下载,正在执行解压命令")
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成下载,正在执行解压命令")
            logging.info("完成下载,正在执行解压命令")
            time.sleep(1)
            self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_7z_unpack!")
            logging.info("Start_7z_unpack!")
            logging.info("当前正在执行7z命令行解压命令")
            os.system(f"{pathx}\\7z.exe x {desktop_path1}\\Minecraft.7z -o{desktop_path1}\\")
            self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在删除临时文件")
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在删除临时文件")
            logging.info("完成,正在删除临时文件")
            time.sleep(1)
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "start_del!")
            logging.info("start_del!")
            logging.info("当前执行命令:del")
            os.system(f"del /f /s /q {desktop_path1}\\Minecraft.7z")
            self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S') + " All done]"+"完成!")
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S') + " All done]" + "完成!\n")
            logging.info("完成,正在执行解禁按钮命令")
            self.OpenWeb.Enable()
            self.GET_Download.Enable()
            self.zip_GET_download.Enable()
            self.Minecrat_for_Netease.Enable()
            logging.info("Done!")
            download_zip_stats = wx.MessageDialog(None, u"执行完成!", u"stats", wx.OK | wx.ICON_INFORMATION)
            if download_zip_stats.ShowModal() == wx.ID_OK:
                download_zip_stats.Destroy()


    def Minecrat_for_Netease_按钮被单击(self,event):
        logging.info("用户选择:重新安装基岩版文件/安装基岩版文件")
        warning = wx.MessageDialog(None, u"是否继续执行?(这可能会导致你的基岩版被删除重新下载)", u"警告",wx.YES_NO | wx.ICON_WARNING)
        if warning.ShowModal() == wx.ID_YES:
            logging.warning("用户继续执行")
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "------重新安装基岩版文件(Debug)------")
            logging.info("------重新安装基岩版文件(Debug)------")
            time.sleep(1)
            self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "正在执行禁用按钮命令")
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "正在执行禁用按钮命令")
            logging.info("正在执行禁用按钮命令")
            time.sleep(1)
            self.OpenWeb.Disable()
            self.GET_Download.Disable()
            self.zip_GET_download.Disable()
            self.Minecrat_for_Netease.Disable()
            self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在执行删除旧版本目录操作/电脑上的网易我的世界基岩版")
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在执行删除旧版本目录操作/电脑上的网易我的世界基岩版")
            logging.info("完成,正在执行删除旧版本目录操作/电脑上的网易我的世界基岩版")
            time.sleep(1)
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_del/rmtree!")
            logging.info("Start_del/rmtree!")
            logging.info("当前执行命令:del和rmtree")
            shutil.rmtree(f"{windowsmc_path1}\\windowsmc", ignore_errors=True)
            shutil.rmtree(f"{desktop_path1}\\windowsmc", ignore_errors=True)
            os.system(f"del /f /s /q {desktop_path1}\\Minecraft.7z")
            self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在执行下载命令")
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在执行下载命令")
            logging.info("完成,正在执行下载命令")
            time.sleep(1)
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_GET_Download!")
            logging.info("Start_GET_Download!")
            logging.info("Downloading...")
            download(f"{res1['url']}",f"{desktop_path1}","Minecraft.7z")
            self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成下载,正在执行解压命令")
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成下载,正在执行解压命令")
            logging.info("完成下载,正在执行解压命令")
            time.sleep(1)
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_7z_unpack!")
            logging.info("Start_7z_unpack!")
            logging.info("当前正在执行7z命令行解压命令")
            os.system(f"{pathx}\\7z.exe x {desktop_path1}\\Minecraft.7z -o{desktop_path1}\\")
            self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在移动windowsmc文件")
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在移动windowsmc文件")
            logging.info("完成,正在移动windowsmc文件")
            time.sleep(1)
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_move!")
            logging.info("Start_move!")
            logging.info("正在执行命令:move")
            os.system(f"move {desktop_path1}\\windowsmc {windowsmc_path1}\\")
            self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在下载.checkInfo文件")
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在下载.checkInfo文件")
            logging.info("完成,正在下载.checkInfo文件")
            time.sleep(1)
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_GET_Download!")
            logging.info("Start_GET_Download")
            logging.info("Downloading...")
            download("https://gitee.com/dai-junhao-123/Minecraft-windows-for-Netease-download/raw/main/.checkInfo",f"{desktop_path1}",".checkInfo")
            self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在移动.checkInfo文件")
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在移动.checkInfo文件")
            logging.info("完成,正在移动.checkInfo文件")
            time.sleep(1)
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_move!")
            logging.info("Start_move!")
            logging.info("正在执行命令:move")
            os.system(f"move {desktop_path1}\\.checkInfo {windowsmc_path1}\\windowsmc")
            self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在删除临时文件")
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在删除临时文件")
            logging.info("完成,正在删除临时文件")
            time.sleep(1)
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "start_del!")
            logging.info("start_del!")
            logging.info("正在执行命令:del")
            os.system(f"del /f /s /q {desktop_path1}\\Minecraft.7z")
            self.read_debug.SetLabelText(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S') + " All done]"+"完成!")
            print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S') + " All done]" + "完成!\n")
            logging.info("完成,正在执行解禁按钮命令")
            self.OpenWeb.Enable()
            self.GET_Download.Enable()
            self.zip_GET_download.Enable()
            self.Minecrat_for_Netease.Enable()
            logging.info("Done!")
            Reload_stats = wx.MessageDialog(None, u"执行完成!", u"stats", wx.OK | wx.ICON_INFORMATION)
            if Reload_stats.ShowModal() == wx.ID_OK:
                Reload_stats.Destroy()

class myApp(wx.App):
    def  OnInit(self):
        self.frame = Frame()
        self.frame.Show(True)
        return True

if __name__ == '__main__':
    app = myApp()
    app.MainLoop()