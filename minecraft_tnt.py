#----------------
#  coding:utf-8
#-----------------
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
mc.postToChat("Hello world")

#  ポジションの取得
x, y, z = mc.player.getPos()

#  TNTブロックの設置
mc.setBlocks( x+1, y+1, z+1, x+11, y+11, z+11, 46, 1)
