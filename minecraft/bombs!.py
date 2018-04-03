from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
tnt = 46
while True:
	x, y, z = mc.player.getTilePos()
	mc.setBlock(x, y, z, tnt, 1)
	time.sleep(0.1)
	
