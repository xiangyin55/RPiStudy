from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
x, y, z = mc.player.getPos()

mc.setBlock(x+1, y, z, 1)
tnt = 46
mc.setBlock(x, y, z+1, tnt, 1)

