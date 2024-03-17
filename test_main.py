import pygame
import time

pygame.init()
# 创建一个游戏的窗口 480 * 700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1.加载图像数据
bg = pygame.image.load('./images/background.png')  # 背景图片
# 2.绘制图像
screen.blit(bg, (0, 0))
# 3.更新屏幕的显示
# pygame.display.update()

# 绘制飞机图像
hero = pygame.image.load('./images/me1.png')
screen.blit(hero, (150, 400))
pygame.display.update()

# 创建一个时钟对象
clock = pygame.time.Clock()

# 定义飞机的起飞位置
hero_rect = pygame.Rect(150, 400, 102, 126)

# 游戏循环 == 》意味着游戏开始
while True:
    # 可以指定循环体内部的代码执行的频率
    clock.tick(60)

    # 修改飞机的位置
    hero_rect.y -= 1

    # 调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    if hero_rect.y == -102:
        hero_rect.y = 700

    # 调用update()方法更新显示
    pygame.display.update()

pygame.quit()
