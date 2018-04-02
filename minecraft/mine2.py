#-*- coding:utf-8 -*-

#利用mcpi里的block实现
#当玩家在海面上（或者陆地）行走时，会在玩家脚下生成一个玻璃
#假若玩家不断走动，玻璃桥也会不断增长

import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

while True:
	pos = mc.player.getTilePos()
	mc.setBlock(pos.x, pos.y-1, pos.z, block.GLASS.id)  #将玩家脚下的方块替换成玻璃
