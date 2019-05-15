#  coding: utf-8
#  =====  ボタンが押されたらLEDを点灯させる  =====
import RPi.GPIO as GPIO
import time as t
from mcpi.minecraft import Minecraft

#  設定値
LED = 15
BUTTON = 18

#  ボタンを押したときの関数
def button_pushed(channel):
    print("Pushed!!")
    mc = Minecraft.create()
    mc.postToChat("Hello world")

    flag = GPIO.input(BUTTON)
    if flag:
        GPIO.output(LED, 1)
        x, y, z = mc.player.getPos()
        mc.setBlock( x+1, y, z+1, 46, 1)
        mc.setBlock( x+1, y+1, z+1, 50)
    else:
        GPIO.output(LED, 0)
    t.sleep(0.5)

GPIO.setmode(GPIO.BCM )
#  Ledの設定
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW )
#  Buttonの設定
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )
GPIO.add_event_detect( BUTTON, GPIO.BOTH, callback = button_pushed,
bouncetime = 200 )


try:
    while True:
        print("Please push the button.")
        t.sleep(1 )
except KeyboardInterrupt:  #  Ctrl + Cの入力時
    print("STOP")
    GPIO.remove_event_detect( BUTTON )
    GPIO.cleanup()

