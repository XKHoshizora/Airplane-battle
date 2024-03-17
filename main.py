"""
飞机大战
"""

# 导入Pygame模块
import pygame
from pygame.locals import *  # 这个模块包含了 Pygame 定义的各种常量，包括按键ASCII码等
import sys

# 版本
version = 'Ver.0.1'

# 初始化 pygame 组件(使用 pygame 模块之前必须先初始化组件)
pygame.init()

# 加载窗口图标图
icon = pygame.image.load('./images/life.png')
# 加载游戏背景图，仍未显示
background = pygame.image.load('./images/background.png')
# 加载玩家的飞机图，仍未显示(此处如果使用 convert() 则在飞机外有黑色矩形框)
player = pygame.image.load('./images/me1.png')

# 为了之后可以在更换图片时可以自动初始化坐标，先提取载入图片的尺寸信息
# 背景图信息
background_width = background.get_width()
background_height = background.get_height()
print('背景图尺寸：', background_width, '×', background_height)
# 玩家图信息
player_width = player.get_width()
player_height = player.get_height()
print('玩家图尺寸：', player_width, '×', player_height)

# 创建游戏窗口 screen，可根据背景图尺寸自动调整窗口大小
screen = pygame.display.set_mode((background_width, background_height))
# 设置窗口图标
pygame.display.set_icon(icon)
# 给游戏窗口命名
pygame.display.set_caption('飞机大战' + ' ' + version)

# 在游戏窗口显示游戏背景图，并初始化坐标
screen.blit(background, (0, 0))
# 在游戏窗口显示玩家的飞机图，并初始化坐标，使飞机位于底部中心位置
screen.blit(player, (background_width / 2 - player_width / 2, background_height - player_height))

# 创建一个背景图坐标的对象
background_pos = pygame.Rect(
    0,  # x坐标
    0,  # y坐标
    background_width,  # 矩形对象的宽
    background_height  # 矩形对象的高
)
# 创建一个玩家坐标的对象 Rect(x, y, width, height)
player_pos = pygame.Rect(
    background_width / 2 - player_width / 2,  # x坐标
    background_height - player_height,  # y坐标
    player_width,  # 矩形对象的宽
    player_height  # 矩形对象的高
)

# 刷新屏幕进行显示
pygame.display.update()

# 创建游戏时钟对象
clock = pygame.time.Clock()

# 按 Enter 键开始游戏
# begin = True
# while begin:
#     for event in pygame.event.get():
#         if event.type == KEYDOWN:
#             if event.key == K_KP_ENTER:
#                 begin = False
#     else:
#         break

# 进入游戏循环
while True:
    # 监测玩家动作
    for event in pygame.event.get():

        # 退出部分
        '''
        如果Event对象是一个停止事件，就会调用pygame.quit()和sys.exit()函数。
        pygame.quit()是pygame.init()函数的一种相反的函数，它运行的代码会使得Pygame库停止工作。
        在调用sys.exit()终止程序之前，总是应该先调用pygame.quit()。
        通常，由于程序退出之前，Python总是会关闭pygame，这不会真的有什么问题。
        但是，在IDLE中有一个bug，如果一个Pygame程序在调用pygame.quit()之前就终止了，将会导致IDLE挂起。
        '''
        if event.type == QUIT:
            # 若玩家关闭窗口（即右上角叉号），则退出
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:  # 此处比较的是事件类型
            # 若玩家按下键盘，则已经为键盘类型，接下来判断是哪个按键
            if event.key == K_ESCAPE:  # 此处比较按键的ASCII码，K_ESCAPE 的ASCII码为27
                # 且按下的是 Esc 键，则退出
                pygame.quit()
                sys.exit()

        # 操作部分
        # 若玩家按下其他按键，继续判断

    # 更新 clock 对象，传入可选参数可使游戏运行速度永不高于传入参数数值（可用于控制飞机飞行速度）
    clock.tick(240)

    # 移动玩家的坐标
    # 先更改y坐标
    player_pos.y -= 1
    # 在新坐标重新绘制图像
    screen.blit(background, background_pos)
    screen.blit(player, player_pos)

    # 玩家靠近窗口边缘时触发操作（不需要下边缘操作）
    # 接近上边缘
    if player_pos.y == -player_height:
        player_pos.y = background_height
    # 接近左边缘
    elif player_pos.x == -player_width:
        player_pos.x = background_width
    # 接近右边缘
    elif player_pos.x == player_width:
        player_pos.x = -background_width

    # 以上操作完成，刷新屏幕进行显示
    pygame.display.update()

# 测试时可用于延迟结束程序
# pygame.time.delay(1000)
