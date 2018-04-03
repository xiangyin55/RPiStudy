from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
diamond = 57
mc.postToChat("Diamond transporter")
time.sleep(5)

ts1 = mc.player.getTilePos()
mc.setBlock(ts1.x, ts1.y - 1, ts1.z, diamond)
mc.postToChat("First transport Block Created")
time.sleep(2)
mc.postToChat("Find another location in 30 seconds")
time.sleep(30)
ts2 = mc.player.getTilePos()
mc.setBlock(ts2.x, ts2.y - 1, ts2.z, diamond)
mc.postToChat("second transport block created")
time.sleep(2)
while True:
	x, y, z = mc.player.getTilePos()
	if(x == ts1.x) and (y == ts1.y + 1) and (z == ts1.z):
		mc.player.setPos(ts2.x, ts2.y + 1, ts2.z)
	if(x == ts2.x) and (y == ts2.y + 1) and (z == ts2.z):
		mc.player.setPos(ts1.x, ts1.y + 1, ts1.z)
