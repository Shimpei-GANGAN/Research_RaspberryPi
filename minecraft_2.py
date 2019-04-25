#  setblock 2 for Python3
import mcpi.minecraft as mine
import mcpi.block as block

#  空間を初期化する
mc = mine.Minecraft.create()
mc.setBlocks( -10, 0, -10, 10, 99, 10, block.AIR.id)
mc.setBlocks( -10, -1, -10, 10, -99, 10, block.GRASS.id)
x = 0
y = 0
z = 0

#  プレイヤーを移動
mc.player.setPos(x, y, z-9)

#  石ブロックをセット
mc.setBlocks(x-3, y+3, z-3, x, y+3, z, block.STONE.id)
#  砂ブロックをセット
mc.setBlocks(x-3, y+6, z-3, x+3, y+6, z+3, block.SAND.id)
