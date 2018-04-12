#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# 
import itchat, time
import os
from itchat.content import *

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
  stime = time.strftime('%Y/%Y%m/%Y%m%d/', time.localtime())
  wxfile = "/root/weixin/"+ stime + msg.FileName
  imgfile = "/root/photos/"+stime + msg.FileName
  byfile = "/weixin/"+ stime + msg.FileName
  upcmd = "bypy -v upload "+wxfile+" " + byfile " >bypy.file 2>&1 &"
  imgcmd = "export DISPLAY=:0.0 && nohup /usr/bin/feh -g 1280x768 -rZFD 30 -Smtime /root/photos  >feh.file 2>&1 &"
  if not os.path.exists(wxdir) : 
    os.makedirs(wxdir)
  if not os.path.exists(phdir) :
    os.makedirs(phdir) 
  msg.download(wxfile)
  os.system(upcmd)
  os.sys
  if msg.Type == 'Picture':
    msg.download(imgfile)
    os.system("killall feh")
    os.system(imgcmd)


itchat.auto_login()
itchat.run()
