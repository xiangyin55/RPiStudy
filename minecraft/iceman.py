from mcpi.minecraft import Minecraft


mc = Minecraft.create()
while True:
	p = mc.player.getTilePos()
	mc.setBlock(p.x, p.y, p.z, 79)

