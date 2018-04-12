#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# 
import itchat, time
import os
from itchat.content import *

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
  stime = time.strftime('%Y/%Y%m/%Y%m%d/', time.localtime())
  wxdir = "/root/weixin/"+ stime #本地微信附近备份目录
  phdir = "/root/photos/"+stime  #本地相册文件存储目录
  byfile = "/weixin/"+ time.strftime('%Y/%Y%m/', time.localtime()) + msg.FileName #云端微信文件名称
  upcmd = "bypy -v upload " + wxdir + msg.FileName + " " + byfile + " >bypy.file 2>&1 &" #bypy命令上传文件
  imgcmd = "export DISPLAY=:0.0 && nohup /usr/bin/feh -g 1280x768 -rZFD 30 -Smtime /root/photos  >feh.file 2>&1 &" #播放图片文件
  if not os.path.exists(wxdir): os.makedirs(wxdir)
  if not os.path.exists(phdir): os.makedirs(phdir)
  msg.download(wxdir + msg.FileName)
  os.system(upcmd)
  os.sys
  if msg.Type == 'Picture':
    msg.download(phdir + msg.FileName)
    os.system("killall feh")
    os.system(imgcmd)


itchat.auto_login()
itchat.run()
