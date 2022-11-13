import pygame
# import easygui
import sys


#   game_progress:      player      shen
#   walking:            0,0         800, 160
#   shen_is_running     200,200     800, 160
#   shen_is_dying       300,300     600, 260


def shen_is_running():
    global screen
    player.move([1, 1])
    shen.move([-2, 1])
    screen.blit(shen.image, shen.rect)


def shen_is_dying():
    global screen, if_mouse_bottom_down, wait_for_mouse
    if footprint == 1:
        shen.image = shen.images[4]
    elif 0 < footprint < 30:
        shen.move([-1, 1])
    elif footprint == 30:
        player.image = player.images[12]
        shen.image = shen.images[5]
    elif 30 < footprint < 60:
        shen.move([-1, 0])
    elif footprint == 60:
        box_appear("啊!", large, 's')
        screen.blit(little.render("(痛苦的喊叫)", True, (0, 0, 0)), [140, 565])


def say_help():
    global screen, if_mouse_bottom_down, wait_for_mouse
    if footprint == 1:
        box_appear("怎么回事?", little, 'h')
    elif footprint <= 30:
        if footprint == 30:
            if_mouse_bottom_down = False
            wait_for_mouse = True
        player.move([1, 0])
        screen.blit(dialog_box, [0, 450])
        screen.blit(little.render("胡:", True, (0, 0, 0)), [20, 470])
        text = little.render("那是......", True, (0, 0, 0))
        screen.blit(text, [30, 500])
    elif footprint == 31:
        box_appear("!", middle, 'h')
    elif footprint <= 60:
        player.move([4, 0])
    elif footprint == 61:
        box_appear("你怎么了?", little, 'h')
    elif footprint == 62:
        box_appear("救命!", middle, 's')
    elif footprint == 63:
        box_appear("我得了一种家族里遗传的疾病", little, 's')
    elif footprint == 64:
        box_appear("现在似乎发作了", little, 's')
    elif footprint == 65:
        box_appear("啊!", large, 's')
        screen.blit(little.render("(又是痛苦的喊叫)", True, (0, 0, 0)), [140, 565])
    elif footprint == 66:
        box_appear("你能不能帮我回教室拿一下药", little, 's')
    elif footprint == 67:
        box_appear("就在我的书包里", little, 's')
    elif footprint == 68:
        screen.blit(dialog_box, [0, 450])
        screen.blit(little.render("(然后他就晕倒了)", True, (0, 0, 0)), [30, 470])
        if_mouse_bottom_down = False
        wait_for_mouse = True


def box_appear(t, size, p):
    global screen, if_mouse_bottom_down, wait_for_mouse
    if_mouse_bottom_down = False
    wait_for_mouse = True
    screen.blit(dialog_box, [0, 450])
    if p == "s":
        screen.blit(little.render("沈:", True, (0, 0, 0)), [20, 470])
    else:
        screen.blit(little.render("胡:", True, (0, 0, 0)), [20, 470])
    text = size.render(t, True, (0, 0, 0))
    screen.blit(text, [30, 500])


class player_class(pygame.sprite.Sprite):

    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.images = [0]
        for i in range(1, 13):
            self.images.append(pygame.transform.scale(pygame.image.load("p" + str(i) + ".png"), (90, 110)))
        self.image = self.images[1]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    def move(self, speed):
        global game_progress

        if self.rect[0] > 480 and self.rect[1] > 420 and game_progress == "find medicine p":
            game_progress = "find medicine c"
            shen.rect[0] = 800
            player.rect[0] = 315
            player.rect[1] = 300

        if game_progress != "find medicine c":
            if speed[0] > 0 and self.rect[0] < width - self.rect[2]:
                self.rect = self.rect.move(speed)
            elif speed[0] < 0 < self.rect[0]:
                self.rect = self.rect.move(speed)
            elif speed[1] > 0 and self.rect[1] < height - self.rect[3] + 12:
                self.rect = self.rect.move(speed)
            elif speed[1] < 0 < self.rect[1]:
                self.rect = self.rect.move(speed)

        elif game_progress == "find medicine c":
            degree = 1
            if speed[1] > 0 and self.rect[1] < height - self.rect[3] + 50 and 200 < self.rect[0] \
                    and self.rect.left + (self.rect.top - 300) / 2 < 320:
                self.rect[2] += degree
                self.rect[3] += degree
                speed[0] -= 1
                self.rect = self.rect.move(speed)
            elif speed[1] < 0 and 300 < self.rect[1] and 200 < self.rect[0] \
                    and self.rect.left + (self.rect.top - 300) / 2 < 320:
                self.rect[2] -= degree
                self.rect[3] -= degree
                speed[0] += 1
                self.rect = self.rect.move(speed)
            elif speed[0] > 0 and self.rect[0] < width - self.rect[2] and self.rect.top > 440:
                self.rect = self.rect.move(speed)
            elif speed[0] < 0 < self.rect[0] and self.rect.top > 440:
                self.rect = self.rect.move(speed)

        wait = 16
        if speed[1] != 0:
            if speed[1] > 0:
                if footprint % wait == 0:
                    self.image = self.images[1]
                elif footprint % wait == wait / 2:
                    self.image = self.images[2]
            else:
                if footprint % wait == 0:
                    self.image = self.images[4]
                elif footprint % wait == wait / 2:
                    self.image = self.images[5]

        else:
            if speed[0] < 0:
                if footprint % wait == 0:
                    self.image = self.images[7]
                elif footprint % wait == wait / 2:
                    self.image = self.images[8]
            else:
                if footprint % wait == 0:
                    self.image = self.images[10]
                elif footprint % wait == wait / 2:
                    self.image = self.images[11]

        self.image = pygame.transform.scale(self.image, [self.rect.width, self.rect.height])


class shen_class(pygame.sprite.Sprite):

    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.images = [0]
        for i in range(1, 4):
            self.images.append(pygame.transform.scale(pygame.image.load("szx" + str(i) + ".png"), (90, 110)))
        for i in range(4, 6):
            self.images.append(pygame.transform.scale(pygame.image.load("szx" + str(i) + ".png"), (110, 90)))
        self.image = self.images[1]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    def move(self, speed):
        self.rect = self.rect.move(speed)


# **********************************************************************************************************************
# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':

    '''
    # 验证
    key = easygui.enterbox(msg="输入给你这个游戏的人的学号", title="密钥")
    if key == "21":
        easygui.msgbox("回答正确!")
        easygui.msgbox("本游戏故事情节纯属虚构，切勿当真")
    else:
        easygui.msgbox("回答错误，即将退出")
        sys.exit()
    '''

    pygame.init()
    pygame.key.set_repeat(1, int(1000 / 30))

    if_mouse_bottom_down = True
    wait_for_mouse = False
    check_this_bag = False
    open_this_bag = False

    width, height = 800, 600
    fps = 30
    footprint = 0

    f = open("game progress.txt", "r")
    game_progress = f.readline()[:-1]  # 游戏进程

    player_start_xy = f.readline()[:-1].split(" ")
    shen_start_xy = f.readline()[:-1].split(" ")
    player_start_x = int(player_start_xy[0])
    player_start_y = int(player_start_xy[1])
    shen_start_x = int(shen_start_xy[0])
    shen_start_y = int(shen_start_xy[1])

    allow_self_move = bool(int(f.readline()))

    player = player_class((player_start_x, player_start_y))
    shen = shen_class((shen_start_x, shen_start_y))
    clock = pygame.time.Clock()

    large = pygame.font.Font('C:/Windows/Fonts/simfang.ttf', 80)
    middle = pygame.font.Font('C:/Windows/Fonts/simfang.ttf', 40)
    little = pygame.font.Font('C:/Windows/Fonts/simfang.ttf', 20)

    dialog_box = pygame.transform.scale(pygame.image.load("dialog box.png"), (width, 150))
    playground_surface = pygame.transform.scale(pygame.image.load("playground.jpg"), (width, height))
    playground_surface2 = pygame.transform.scale(pygame.image.load("playground2.jpg"), (width, height))
    classroom_surface = pygame.transform.scale(pygame.image.load("classroom.jpg"), (width, height))
    desk_surface = pygame.transform.scale(pygame.image.load("classroom desk.png"), (width, height))
    classroom_schoolbag_surface = pygame.transform.scale(pygame.image.load("classroom schoolbag.png"), (width, height))
    check_this_bag_surface = pygame.image.load("check this bag.png")
    schoolbag_yellow_surface = pygame.image.load("schoolbag_yellow.png")

    background = {"walking": playground_surface,
                  "shen is running": playground_surface,
                  "shen is dying": playground_surface,
                  "say help": playground_surface,
                  "find medicine p": playground_surface2,
                  "find medicine c": classroom_surface
                  }

    screen = pygame.display.set_mode((width, height))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if wait_for_mouse:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    wait_for_mouse = False
                    if_mouse_bottom_down = True
            if event.type == pygame.KEYDOWN:
                if allow_self_move:
                    if event.key == pygame.K_UP:
                        player.move([0, -2])
                    elif event.key == pygame.K_DOWN:
                        player.move([0, 2])
                    elif event.key == pygame.K_LEFT:
                        player.move([-2, 0])
                    elif event.key == pygame.K_RIGHT:
                        player.move([2, 0])

                if check_this_bag:
                    if event.key == pygame.K_SPACE:
                        open_this_bag = True

        screen.blit(background[game_progress], (0, 0))
        if if_mouse_bottom_down:
            footprint += 1
            if footprint == 800:
                footprint = 0
            if game_progress == "walking":
                player.move([1, 1])

                if footprint == 200:
                    game_progress = "shen is running"
                    footprint = 0

            elif game_progress == "shen is running":
                shen_is_running()

                if footprint == 100:
                    game_progress = "shen is dying"
                    footprint = 0

            elif game_progress == "shen is dying":
                shen_is_dying()

                if footprint == 62:
                    game_progress = "say help"
                    footprint = 0

            elif game_progress == "say help":
                say_help()

                if footprint == 68:
                    game_progress = "find medicine p"
                    footprint = 0
                    allow_self_move = True

            if game_progress == "find medicine c" and player.rect.top > 420 and 105 < player.rect.left < 293:
                screen.blit(classroom_schoolbag_surface, [0, 0])

            screen.blit(shen.image, shen.rect)  # shen显示
            screen.blit(player.image, player.rect)  # 玩家显示

            if game_progress == "find medicine c" and player.rect.top <= 440:  # 大面积桌子遮挡
                screen.blit(desk_surface, [0, 0])

            if game_progress == "find medicine c" and player.rect.top > 420 and 105 < player.rect.left < 293:
                # 查看shen的书包
                screen.blit(check_this_bag_surface, [player.rect.left + 170, player.rect.top + 70])
                check_this_bag = True

            if open_this_bag:
                wait_for_mouse = True
                if_mouse_bottom_down = False
                screen.blit(schoolbag_yellow_surface, [150, 25])

            if not if_mouse_bottom_down:
                down_to_continue = little.render("单击鼠标以继续", True, (0, 0, 0))
                screen.blit(down_to_continue, (635, 570))

            pygame.display.flip()  # 刷新
        clock.tick(fps)  # 控制帧率
