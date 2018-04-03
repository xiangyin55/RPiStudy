from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

msg = ("I am going to kill you!")


mc.postToChat(msg)

time.sleep(1)
pos = mc.player.getPos()

mc.postToChat("You are located at x=" +str(pos.x) + ", Y=" +str(pos.y) + ", Z=" +str(pos.z))

time.sleep(2)
mc.postToChat("Get ready to fall from the sky! Mwahahahahahahahahahahahaha!!")

time.sleep(5)
mc.player.setPos(pos.x, pos.y + 600, pos.z)

