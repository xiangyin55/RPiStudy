#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# 
import itchat, time
import os
from itchat.content import *

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
  stime = time.strftime('%Y/%Y%m/%Y%m%d/', time.localtime())
  wxdir = "/root/weixin/"+ stime 
  phdir = "/root/photos/"+stime
  byfile = "/weixin/"+ time.strftime('%Y/%Y%m/', time.localtime()) + msg.FileName
  upcmd = "bypy -v upload " + wxdir + msg.FileName + " " + byfile + " >bypy.file 2>&1 &"
  imgcmd = "export DISPLAY=:0.0 && nohup /usr/bin/feh -g 1280x768 -rZFD 30 -Smtime /root/photos  >feh.file 2>&1 &"
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
