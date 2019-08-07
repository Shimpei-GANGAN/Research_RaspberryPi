# ------------------------------------------------------------
#   coding:utf-8
# ------------------------------------------------------------
#   Updata History
#   August  07 13:00, 2019 (Wed)
# ------------------------------------------------------------
#   xbox game padのテスト
# ------------------------------------------------------------

import pygame

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
WIDTH = 320
HEIGHT = 240

def main():
    pygame.init()
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.joystick.init()
    print("get_count: {}".format(str(pygame.joystick.get_count())))

    joystick_id = 0
    joystick = pygame.joystick.Joystick(joystick_id)
    joystick.init()
    print("get_name: {}".format(joystick.get_name()))
    print("get_numaxes: {}".format(str(joystick.get_numaxes())))
    print("get_numbuttons: {}".format(str(joystick.get_numbuttons())))
    print("get_numhats: {}".format(str(joystick.get_numhats())))

    myfont = pygame.font.Font(None, 30)
    myclock = pygame.time.Clock()
    endflag = 0

    while endflag==0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: endflag=1

        ax = joystick.get_axis( 0 )
        surface.fill(WHITE)
        bitmaptext = myfont.render("axis: {}".format(str(ax)), True, BLACK)
        pygame.display.updata()
        myclock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()