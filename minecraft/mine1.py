#-*- coding:utf-8 -*-

#一个传送地毯，用if函数实现。
#主要用途：当玩家站在一定的区域内，会被传送到指定位置

import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

while True:
    time.sleep(3)
    pos = mc.player.getTilePos()  #得到玩家目前坐标
    print pos.x, pos.y, pos.z

    if pos.x>=14 and pos.z>=-2:
        mc.player.setTilePos(13,6,5)  #假若玩家当前坐标符合上面的判断条件，则会被传送到指定位置（13,6,5）
        mc.postToChat('I am back !!!')  #传送成功就在窗口打出“change!!!”
    else:
        pass
