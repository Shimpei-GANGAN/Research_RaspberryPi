#setblock for Python3
import mcpi.minecraft as mine
import mcpi.block as block

mc = mine.Minecraft.create()
x, y, z = mc.player.getPos()
mc.setBlock( x, y+3, z+5, block.WOOD_PLANKS.id)
