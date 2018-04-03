from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

msg = ("I am going to kill you!")


mc.postToChat(msg)

time.sleep(1)
pos = mc.player.getPos()

mc.postToChat("You are located at x=" +str(pos.x) + ", Y=" +str(pos.y) + ", Z=" +str(pos.z))

