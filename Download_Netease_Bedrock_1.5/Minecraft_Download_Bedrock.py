# -*- coding:utf-8 -*-
import wx
import winreg
import os
import sys
import requests
import logging
import datetime
import time

def desktop_path():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    path = winreg.QueryValueEx(key, "Desktop")[0]
    return path
desktop_path1 = desktop_path()

logging.basicConfig(level=logging.INFO,filename=f'{desktop_path1}/Download_Netease_Bedrock_Debug.log',format=('%(asctime)s - %(levelname)s - %(message)s'))

class Frame(wx.Frame):
    def __init__(self):
        global pathx
        pathx = os.path.dirname(os.path.abspath(__file__))
        wx.Frame.__init__(self, None, title='启动窗口', size=(717, 451),name='frame',style=541072384)
        self.启动窗口 = wx.Panel(self)
        self.Centre()
        self.标签1 = wx.StaticText(self.启动窗口,size=(612, 20),pos=(38, 91),label='请选择版本',name='staticText',style=17)
        标签1_字体 = wx.Font(9,70,90,700,False,'Microsoft YaHei UI',28)
        self.标签1.SetFont(标签1_字体)
        self.Minecraft_4399 = wx.Button(self.启动窗口,size=(633, 123),pos=(36, 273),label='4399版',name='button')
        self.Minecraft_4399.Bind(wx.EVT_BUTTON,self.Minecraft_4399_按钮被单击)
        self.Netease = wx.Button(self.启动窗口,size=(630, 123),pos=(37, 135),label='网易版',name='button')
        self.Netease.Bind(wx.EVT_BUTTON,self.Netease_按钮被单击)

        # 当前版本
        version = "1.5_fix"
        # 更新检测
        header = {"content-type": "application/json"}
        logging.info(f"当前版本:{version}")
        logging.info("检测最新版本中...")
        uqdate_latest_version_url = "https://gitee.com/dai-junhao-123/Minecraft-windows-for-Netease-download/raw/main/Uqdate/Latest_uqdate.txt"
        uqdate_latest_version = requests.get(uqdate_latest_version_url, headers=header).text
        uqdate_latest_version_url_text = f"https://gitee.com/dai-junhao-123/Minecraft-windows-for-Netease-download/raw/main/Uqdate/Msg/uqdate_{uqdate_latest_version}.txt"
        uqdate_latest_version_text = requests.get(uqdate_latest_version_url_text, headers=header).text
        uqdate_latest_version_url_download = f"https://gitee.com/dai-junhao-123/Minecraft-windows-for-Netease-download/raw/main/Uqdate/Url/uqdate_{uqdate_latest_version}.txt"
        uqdate_latest_version_download = requests.get(uqdate_latest_version_url_download, headers=header).text
        if uqdate_latest_version != version:
            logging.info(f"发现更新,最新版本:{uqdate_latest_version}")
            NO_Latest = wx.MessageDialog(None, caption="Uqdate",message=f"发现新版本!\n当前版本:{version}\n最新版本:{uqdate_latest_version}\n更新内容如下:\n{uqdate_latest_version_text}\n是否开始更新?",style=wx.YES_NO | wx.ICON_WARNING)
            if NO_Latest.ShowModal() == wx.ID_YES:
                logging.info("用户选择更新")
                print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "------更新(Debug)------")
                logging.info("------更新(Debug)------")
                time.sleep(1)
                print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "正在执行禁用窗口命令")
                logging.info("正在执行禁用窗口命令")
                self.启动窗口.Disable()
                print(datetime.datetime.now().strftime(
                    '[date:%Y-%m-%d time:%H:%M:%S]') + "完成,正在执行下载更新命令(文件默认保存桌面)")
                logging.info("完成,正在执行下载更新命令(文件默认保存桌面)")
                time.sleep(1)
                print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Start_Wget_Download_Uqdate!")
                logging.info("Start_Wget_Download_Uqdate")
                logging.info("Downloading...")
                os.system(
                    f"{pathx}\\aria2c.exe -d --out=Minecraft_Netease_{uqdate_latest_version}.exe -d {desktop_path1} {uqdate_latest_version_download}")
                print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "完成,3秒后程序退出")
                logging.info("完成,3秒后程序退出")
                time.sleep(3)
                os.system(f"start {desktop_path1}\\Minecraft_Download_Bedrock_{uqdate_latest_version}.exe")
                logging.info("执行命令:start")
                print(datetime.datetime.now().strftime('[date:%Y-%m-%d time:%H:%M:%S]') + "Done!")
                logging.info("Exit")
                sys.exit()
            if NO_Latest.ShowModal() == wx.ID_NO:
                logging.warning("用户取消更新")
        else:
            logging.info("当前是最新版本!")
            YES_Latest = wx.MessageDialog(None, caption="Uqdate", message="当前是最新版本!",style=wx.OK | wx.ICON_INFORMATION)
            if YES_Latest.ShowModal() == wx.ID_OK:
                YES_Latest.Destroy()

        try:
                def windowsmc_path():
                    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Netease\MCLauncher')
                    path = winreg.QueryValueEx(key, "MinecraftBENeteasePath")[0]
                    return path
                windowsmc_path1 = windowsmc_path()
        except FileNotFoundError as Error:
            self.Netease.Disable()
            self.Netease.SetLabelText("网易版(当前不可用)")
        try:
            def windowsmc_path():
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Netease\PC4399_MCLauncher')
                path = winreg.QueryValueEx(key, "MinecraftBENeteasePath")[0]
                return path
            windowsmc_path1 = windowsmc_path()
        except FileNotFoundError as Error:
            self.Minecraft_4399.Disable()
            self.Minecraft_4399.SetLabelText("4399版(当前不可用)")

    def Minecraft_4399_按钮被单击(self,event):
        os.system(f"start {os.path.dirname(os.path.abspath(__file__))}\\versions\\Minecraft_4399.exe")
        sys.exit()

    def Netease_按钮被单击(self,event):
        os.system(f"start {os.path.dirname(os.path.abspath(__file__))}\\versions\\Minecraft_Netease.exe")
        sys.exit()
class myApp(wx.App):
    def  OnInit(self):
        self.frame = Frame()
        self.frame.Show(True)
        return True

if __name__ == '__main__':
    app = myApp()
    app.MainLoop()