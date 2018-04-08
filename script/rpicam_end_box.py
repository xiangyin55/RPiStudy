#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import time

file_dir = "/mnt/dietpi_userdata/rpicam"

ctime = time.localtime(time.time())
list = os.listdir(file_dir)
for f in list:
        path = os.path.join(file_dir,f)
        print(path)
        cmd = "bypy -v upload "+path+" /rpicam/"+time.strftime('%Y/%Y%m/%Y%m%d/',ctime) + os.path.basename(path)
        os.system("echo exec:" + cmd + " >> /var/log/lighttpd/rpicam`date +%Y%m%d`.log 2>&1" )
        os.system(cmd +" >> /var/log/lighttpd/rpicam`date +%Y%m%d`.log 2>&1")
        os.remove(path)
