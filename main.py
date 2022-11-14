import pygame
import easygui
import sys


#   game_progress:      player      shen
#   walking:            0,0         800, 160
#   shen_is_running     200,200     800, 160
#   shen_is_dying       300,300     600, 260


def shen_is_running():
    global screen
    player.move([1, 1])
    shen.move([-2, 1])

    wait = 16
    if footprint % wait == 0:
        shen.image = shen.images[2]
    elif footprint % wait == wait / 2:
        shen.image = shen.images[3]


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
        box_appear("啊!", large, 'n')
        screen.blit(little.render("(痛苦的喊叫)", True, (0, 0, 0)), [140, 555])


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
        box_appear("沈子昕!", middle, 'h')
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
        screen.blit(little.render("(又是痛苦的喊叫)", True, (0, 0, 0)), [140, 555])
    elif footprint == 66:
        box_appear("你能不能帮我回教室拿一下药", little, 's')
    elif footprint == 67:
        box_appear("就在我的书包里", little, 's')
    elif footprint == 68:
        screen.blit(dialog_box, [0, 450])
        screen.blit(little.render("(然后他就晕倒了)", True, (0, 0, 0)), [30, 470])
        if_mouse_bottom_down = False
        wait_for_mouse = True


def get_the_medicine():
    global screen, wait_for_mouse, if_mouse_bottom_down
    if footprint <= 5:
        screen.blit(schoolbag_yellow_surface, [150, 25])
    if footprint == 1:
        box_appear("他的包可真乱啊", little, 'h')
    elif footprint == 2:
        box_appear("这是...", little, 'h')
    elif footprint == 3:
        box_appear("药！", middle, 'h')
    elif footprint == 4:
        box_appear("但，为什么上面有一个锁啊?", little, 'h')
    elif footprint == 5:
        box_appear("诶！药瓶上好像有他的字", little, 'h')
    elif footprint == 6:
        screen.blit(see_see_surface, [0, 25])
        wait_for_mouse = True
        if_mouse_bottom_down = False
    elif footprint == 7:
        box_appear("什么鬼!!!!!!", middle, 'h')
    elif footprint == 8:
        box_appear("你让我给你拿药还要我找密码给你开锁?", little, 'h')
    elif footprint == 9:
        box_appear("算了，要不是看在两年多同桌的分上，才懒得理你呢！", little, 'h')
    elif footprint == 10:
        box_appear("讲台，记住了", little, 'h')


def get_the_password():
    if footprint <= 5:
        screen.blit(password_prompt_surface, [0, 25])
    if footprint == 1:
        box_appear("终于找到了!", middle, 'h')
    elif footprint == 2:
        box_appear("上面写得是...", little, 'h')
    elif footprint == 3:
        box_appear("你就不能直接一点吗!!!   真是的，麻烦死了", little, 'h')
    elif footprint == 4:
        box_appear("那就来吧", little, 'h')
    elif footprint == 5:
        password = ""
        while password != "1244":
            password = easygui.enterbox(msg="四位密码", title="药罐上的密码锁")
            if password == "1244":
                easygui.msgbox("不错不错，看来你的数学还是可以的")
            else:
                easygui.msgbox("要不再试试?")
        player.rect.top = 250
        player.rect.left = 0
        player.image = pygame.transform.scale(player.image, [90, 100])
        shen.image = shen.images[1]
        shen.rect.top = 250
        shen.rect.left = 450


def find_shen():
    if footprint <= 25:
        player.move([4, 0])
    elif footprint <= 50:
        player.image = player.images[1]
        screen.blit(dialog_box, [0, 450])
        screen.blit(little.render("胡:", True, (0, 0, 0)), [20, 470])
        text = little.render("嗯？", True, (0, 0, 0))
        screen.blit(text, [30, 500])
        return
    elif footprint <= 52:
        player.move([0, 5])
        screen.blit(dialog_box, [0, 450])
        screen.blit(little.render("胡:", True, (0, 0, 0)), [20, 470])
        text = little.render("嗯？", True, (0, 0, 0))
        screen.blit(text, [30, 500])
        player.image = player.images[1]
    elif footprint <= 54:
        player.move([0, -5])
        screen.blit(dialog_box, [0, 450])
        screen.blit(little.render("胡:", True, (0, 0, 0)), [20, 470])
        text = little.render("嗯？", True, (0, 0, 0))
        screen.blit(text, [30, 500])
        player.image = player.images[1]
    elif footprint <= 56:
        player.move([0, 5])
        screen.blit(dialog_box, [0, 450])
        screen.blit(little.render("胡:", True, (0, 0, 0)), [20, 470])
        text = little.render("嗯？", True, (0, 0, 0))
        screen.blit(text, [30, 500])
        player.image = player.images[1]
    elif footprint <= 58:
        player.move([0, -5])
        screen.blit(dialog_box, [0, 450])
        screen.blit(little.render("胡:", True, (0, 0, 0)), [20, 470])
        text = little.render("嗯？", True, (0, 0, 0))
        screen.blit(text, [30, 500])
        player.image = player.images[1]
    elif footprint == 59:
        box_appear("你..", middle, 'h')
    elif footprint == 60:
        box_appear("你好了?", middle, 'h')
    elif footprint <= 150:
        player.move([3, 0])
    elif footprint == 151:
        box_appear("哈哈，不好意思，骗了你", little, 's')
    elif footprint == 152:
        box_appear("对现实中的我说：‘万物皆虚，万事皆允’", little, 's')
    elif footprint == 153:
        box_appear("他会给你一个好东西。", little, 's')
    elif footprint == 154:
        box_appear("(虽然这好像有点中二)", little, 's')
    elif footprint == 155:
        box_appear("至于我的病，很抱歉，只是我瞎说的。", little, 's')
    elif footprint == 156:
        box_appear("那个药，你可以吃吃看", little, 's')
    elif footprint <= 160:
        screen.blit(dialog_box, [0, 450])
        screen.blit(little.render("胡:", True, (0, 0, 0)), [20, 470])
        text = little.render("啊呜", True, (0, 0, 0))
        screen.blit(text, [30, 500])
    elif footprint <= 170:
        screen.blit(dialog_box, [0, 450])
        screen.blit(little.render("胡:", True, (0, 0, 0)), [20, 470])
        text = little.render("啊呜.", True, (0, 0, 0))
        screen.blit(text, [30, 500])
    elif footprint <= 180:
        screen.blit(dialog_box, [0, 450])
        screen.blit(little.render("胡:", True, (0, 0, 0)), [20, 470])
        text = little.render("啊呜..", True, (0, 0, 0))
        screen.blit(text, [30, 500])
    elif footprint <= 190:
        screen.blit(dialog_box, [0, 450])
        screen.blit(little.render("胡:", True, (0, 0, 0)), [20, 470])
        text = little.render("啊呜...", True, (0, 0, 0))
        screen.blit(text, [30, 500])
    elif footprint <= 200:
        screen.blit(dialog_box, [0, 450])
        screen.blit(little.render("胡:", True, (0, 0, 0)), [20, 470])
        text = little.render("啊呜....", True, (0, 0, 0))
        screen.blit(text, [30, 500])
    elif footprint == 201:
        box_appear("啊呜.....", little, 'h')
    elif footprint == 202:
        box_appear("甜的", little, 'h')
    elif footprint == 203:
        box_appear("不然呢，这是被我掰成一粒一粒的芝麻糖", little, 's')
    elif footprint == 204:
        box_appear("好吃吧", little, 's')
    elif footprint == 205:
        box_appear("切，就知道玩我", little, 'h')
    elif footprint == 206:
        box_appear("哈哈", little, 's')
    elif footprint == 207:
        box_appear("非常谢谢你玩完了我的游戏，", little, 's')
    elif footprint == 208:
        box_appear("它的流程可能有点短，但两个周末和信息培训的摸鱼时间就只能做到这些了", little, 's')
    elif footprint == 209:
        box_appear("最后，再一次祝你生日快乐！", little, 's')


def box_appear(t, size, p):
    global screen, if_mouse_bottom_down, wait_for_mouse
    if_mouse_bottom_down = False
    wait_for_mouse = True
    screen.blit(dialog_box, [0, 450])
    if p == "s":
        screen.blit(little.render("沈:", True, (0, 0, 0)), [20, 470])
    elif p == "h":
        screen.blit(little.render("胡:", True, (0, 0, 0)), [20, 470])
    else:
        screen.blit(little.render("某人:", True, (0, 0, 0)), [20, 470])
    text = size.render(t, True, (0, 0, 0))
    screen.blit(text, [30, 500])


def stand():
    if player.image_style % 3 != 0:
        player.image_style = player.image_style // 3 * 3 + 3
    player.image = player.images[player.image_style]


class player_class(pygame.sprite.Sprite):

    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.images = [0]
        for i in range(1, 13):
            self.images.append(pygame.transform.scale(pygame.image.load("p" + str(i) + ".png"), (90, 110)))
        self.image = self.images[1]
        self.image_style = 1
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    def path_pd(self):
        if self.rect.top > 440 or self.rect.top < 320:
            return True
        else:
            return False

    def move(self, speed):
        global game_progress

        if self.rect[0] > 480 and self.rect[1] > 420 and game_progress == "find medicine p":
            game_progress = "find medicine c"
            shen.rect[0] = 800
            player.rect[0] = 315
            player.rect[1] = 300

        if game_progress != "find medicine c" and game_progress != "find password":
            if speed[0] > 0 and self.rect[0] < width - self.rect[2]:
                self.rect = self.rect.move(speed)
            elif speed[0] < 0 < self.rect[0]:
                self.rect = self.rect.move(speed)
            elif speed[1] > 0 and self.rect[1] < height - self.rect[3] + 12:
                self.rect = self.rect.move(speed)
            elif speed[1] < 0 < self.rect[1]:
                self.rect = self.rect.move(speed)

        elif game_progress == "find medicine c" or game_progress == "find password":
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
            elif speed[0] > 0 and self.rect[0] < width - self.rect[2] and self.path_pd():
                self.rect = self.rect.move(speed)
            elif speed[0] < 0 < self.rect[0] and self.path_pd():
                self.rect = self.rect.move(speed)

        # 走路动态
        wait = 16
        if speed[1] != 0:
            if speed[1] > 0:
                if footprint % wait == 0:
                    self.image = self.images[1]
                    self.image_style = 1
                elif footprint % wait == wait / 2:
                    self.image = self.images[2]
                    self.image_style = 2
            else:
                if footprint % wait == 0:
                    self.image = self.images[4]
                    self.image_style = 4
                elif footprint % wait == wait / 2:
                    self.image = self.images[5]
                    self.image_style = 5

        else:
            if speed[0] < 0:
                if footprint % wait == 0:
                    self.image = self.images[7]
                    self.image_style = 7
                elif footprint % wait == wait / 2:
                    self.image = self.images[8]
                    self.image_style = 8
            else:
                if footprint % wait == 0:
                    self.image = self.images[10]
                    self.image_style = 10
                elif footprint % wait == wait / 2:
                    self.image = self.images[11]
                    self.image_style = 11


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

    # 验证
    key = easygui.enterbox(msg="输入给你这个游戏的人的学号", title="密钥")
    if key == "21":
        easygui.msgbox("回答正确!")
        easygui.msgbox("本游戏故事情节纯属虚构，切勿当真")
    else:
        easygui.msgbox("回答错误，即将退出")
        sys.exit()

    pygame.init()
    pygame.key.set_repeat(1, int(1000 / 30))

    if_mouse_bottom_down = True
    wait_for_mouse = False
    check_this_bag = False
    check_the_podium = False
    allow_self_move = False

    width, height = 800, 600
    fps = 30
    footprint = 0
    before = 0

    game_progress = "walking"  # 游戏进程

    player_start_x = 0
    player_start_y = 0
    shen_start_x = 800
    shen_start_y = 160

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
    see_see_surface = pygame.image.load("see see.png")
    check_the_podium_surface = pygame.image.load("check the podium.png")
    classroom_podium_surface = pygame.transform.scale(pygame.image.load("classroom podium.png"), (width, height))
    password_prompt_surface = pygame.image.load("password prompt.png")

    background = {"walking": playground_surface,
                  "shen is running": playground_surface,
                  "shen is dying": playground_surface,
                  "say help": playground_surface,
                  "find medicine p": playground_surface2,
                  "find medicine c": classroom_surface,
                  "get the medicine": classroom_surface,
                  "find password": classroom_surface,
                  "get the password": classroom_surface,
                  "find shen": playground_surface
                  }

    pygame.display.set_caption("送给你的生日礼物")
    pygame.display.set_icon(pygame.image.load("tb.ico"))
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
                        game_progress = "get the medicine"
                        footprint = 0
                        before = player.rect[0]
                        player.rect.left = 800
                        allow_self_move = False
                        check_this_bag = False

                if check_the_podium:
                    if event.key == pygame.K_SPACE:
                        game_progress = "get the password"
                        footprint = 0
                        player.rect.left = 800
                        allow_self_move = False
                        check_the_podium = False
            if event.type == pygame.KEYUP:
                stand()

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

            elif game_progress == "find medicine c" and player.rect.top > 420 and 105 < player.rect.left < 293:
                screen.blit(classroom_schoolbag_surface, [0, 0])

            elif game_progress == "get the medicine":
                get_the_medicine()

                if footprint == 11:
                    game_progress = "find password"
                    footprint = 0
                    allow_self_move = True
                    player.rect.left = before

            elif game_progress == "find password" and player.rect.top < 320 and 370 < player.rect.left < 500:
                screen.blit(classroom_podium_surface, [0, 0])

            elif game_progress == "get the password":
                get_the_password()

                if footprint == 6:
                    game_progress = "find shen"
                    footprint = 0

            elif game_progress == "find shen":
                find_shen()

            screen.blit(shen.image, shen.rect)  # shen显示

            player.image = pygame.transform.scale(player.image, [player.rect.width, player.rect.height])
            screen.blit(player.image, player.rect)  # 玩家显示

            if (game_progress == "find medicine c" or game_progress == "find password") and player.rect.top <= 440:
                # 大面积桌子遮挡
                screen.blit(desk_surface, [0, 0])

            if game_progress == "find medicine c" and player.rect.top > 420 and 105 < player.rect.left < 293:
                # 查看shen的书包的提示
                screen.blit(check_this_bag_surface, [player.rect.left + 170, player.rect.top + 70])
                check_this_bag = True

            if game_progress == "find password" and player.rect.top < 320 and 370 < player.rect.left < 500:
                # 查看shen的讲台的提示
                screen.blit(check_the_podium_surface, [player.rect.left + 100, player.rect.top + 30])
                check_the_podium = True

            if not if_mouse_bottom_down:
                down_to_continue = little.render("单击鼠标以继续", True, (0, 0, 0))
                screen.blit(down_to_continue, (635, 560))

            pygame.display.flip()  # 刷新

        clock.tick(fps)  # 控制帧率
