#-*- coding:utf-8 -*-
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
for a in range(30):
	mc.setBlock(pos.x+3, pos.y+a, pos.z, block.GOLD_BLOCK.id)
