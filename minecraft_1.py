#setblock for Python3
import mcpi.minecraft as mine
import mcpi.block as block

mc = mine.Minecraft.create()  #  マインクラフトに接続
x, y, z = mc.player.getPos()  #  プレイヤーの位置を取得
mc.setBlock( x, y+3, z+5, block.WOOD_PLANKS.id)  #  木のブロックを設置する
