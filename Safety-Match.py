import matplotlib.pyplot as plt
import cv2
import numpy as np
import win32api
import win32gui
import win32con
from PIL import ImageGrab
import time
import pyautogui
import random
import sys
import os
from PIL import Image


WINDOW_TITLE = "浙电安全学习平台"
TIME_INTERVAL_MAX = 3 # 假设最小时间间隔
TIME_INTERVAL_MIN = 3.3 # 假设最大时间间隔

# 设置屏幕截图时图片边缘的左侧和顶部空白区域的尺寸
MARGIN_LEFT = 15
MARGIN_LEFT_EXTRA = 0 #这个值在第4列（第10截图）及之后使用
MARGIN_HEIGHT = 168
# 设置游戏界面的行列数和每个点击点的尺寸
H_NUM = 6       # 游戏界面的行数
V_NUM = 3       # 游戏界面的列数
POINT_WIDTH = 60# 每个点击点的宽度
POINT_HEIGHT = 60 # 每个点击点的高度
EMPTY_ID = 0  # 设置空白位置的标识
# # 设置子图片裁剪区域的左上角和右下角坐标
# SUB_LT_X = 8
# SUB_LT_Y = 8
# SUB_RB_X = 27
# SUB_RB_Y = 27
MAX_ROUND = 200  # 设置最大循环次数，用于控制程序的执行次数

#【10】◊◊◊ 找积分图像（zj10.bmp）◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊
def zj_10(image_path="D:\\python\\zj\\zj10.bmp"):
    time.sleep(1)
    start_time = time.time()
    while time.time() - start_time < 20:
        # 截取屏幕截图并查找图像的位置
        screenshot = pyautogui.screenshot()
        x_y = pyautogui.locateCenterOnScreen(image_path, confidence=0.8,region=(0, 0, screenshot.width, screenshot.height))
        if x_y is not None:
            x, y = x_y
            # print(f"积分图像在 ({x}, {y}) 的位置。")
            pyautogui.moveTo(x, y, duration=0.5)
            time.sleep(1)
            pyautogui.click()
            # print(f"积分图像在 ({x}, {y}) 的位置，已点击。")
            break
        else:
            # print("未找到积分图像，等待2秒后继续查找。")
            time.sleep(2)
            del screenshot  # 显式删除截图对象释放内存
    # 如果程序未找到图像，则输出提示信息
    else:
        print("已超过20秒没有找到积分图像，退出程序。")
# ◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊

#【26】◊◊◊找我的字图像（zj26.bmp）◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊
def zj_26(image_path="D:\\python\\zj\\zj26.bmp"):
    time.sleep(1)
    start_time = time.time()
    while time.time() - start_time < 20:
        # 截取屏幕截图并查找图像的位置
        screenshot = pyautogui.screenshot()
        x_y = pyautogui.locateCenterOnScreen(image_path, confidence=0.8,region=(0, 0, screenshot.width, screenshot.height))
        if x_y is not None:
            x, y = x_y
            # print(f"我的字图像在 ({x}, {y}) 的位置。")
            pyautogui.moveTo(x, y, duration=0.5)
            time.sleep(1)
            pyautogui.click()
            # print(f"我的字图像在 ({x}, {y}) 的位置，已点击。")
            break
        else:
            # print("未找到我的字图像，等待2秒后继续查找。")
            time.sleep(2)
            del screenshot  # 显式删除截图对象释放内存
    # 如果程序未找到图像，则输出提示信息
    else:
        print("已超过20秒没有找到我的字图像，退出程序。")
# ◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊

#【26a】◊◊◊找更多字图像（zj26a.bmp）◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊
def zj_26a(image_path="D:\\python\\zj\\zj26a.bmp"):
    time.sleep(1)
    start_time = time.time()
    while time.time() - start_time < 20:
        # 截取屏幕截图并查找图像的位置
        screenshot = pyautogui.screenshot()
        x_y = pyautogui.locateCenterOnScreen(image_path, confidence=0.8,region=(0, 0, screenshot.width, screenshot.height))
        if x_y is not None:
            x, y = x_y
            # print(f"更多字图像在 ({x}, {y}) 的位置。")
            pyautogui.moveTo(x, y, duration=0.5)
            time.sleep(1)
            pyautogui.click()
            # print(f"更多字图像在 ({x}, {y}) 的位置，已点击。")
            break
        else:
            # print("未找到更多字图像，等待2秒后继续查找。")
            time.sleep(2)
            del screenshot  # 显式删除截图对象释放内存
    # 如果程序未找到图像，则输出提示信息
    else:
        print("已超过20秒没有找到更多字图像，退出程序。")
# ◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊

#【26b】◊◊◊找连连看字图像（zj26b.bmp）◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊
def zj_26b(image_path="D:\\python\\zj\\zj26b.bmp"):
    time.sleep(1)
    start_time = time.time()
    while time.time() - start_time < 20:
        # 截取屏幕截图并查找图像的位置
        screenshot = pyautogui.screenshot()
        x_y = pyautogui.locateCenterOnScreen(image_path, confidence=0.8,region=(0, 0, screenshot.width, screenshot.height))
        if x_y is not None:
            x, y = x_y
            # print(f"连连看字图像在 ({x}, {y}) 的位置。")
            pyautogui.moveTo(x, y, duration=0.5)
            time.sleep(1)
            pyautogui.click()
            # print(f"连连看字图像在 ({x}, {y}) 的位置，已点击。")
            break
        else:
            # print("未找到连连看字图像，等待2秒后继续查找。")
            time.sleep(2)
            del screenshot  # 显式删除截图对象释放内存
    # 如果程序未找到图像，则输出提示信息
    else:
        print("已超过20秒没有找到连连看字图像，退出程序。")
# ◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊

#【26c】◊◊◊找开始游戏字图像（zj26c.bmp）◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊
def zj_26c(image_path="D:\\python\\zj\\zj26c.bmp"):
    time.sleep(1)
    start_time = time.time()
    while time.time() - start_time < 20:
        # 截取屏幕截图并查找图像的位置
        screenshot = pyautogui.screenshot()
        x_y = pyautogui.locateCenterOnScreen(image_path, confidence=0.8,region=(0, 0, screenshot.width, screenshot.height))
        if x_y is not None:
            x, y = x_y
            # print(f"开始游戏字图像在 ({x}, {y}) 的位置。")
            pyautogui.moveTo(x, y, duration=0.5)
            time.sleep(1)
            pyautogui.click()
            # print(f"开始游戏字图像在 ({x}, {y}) 的位置，已点击。")
            break
        else:
            # print("未找到开始游戏字图像，等待2秒后继续查找。")
            time.sleep(2)
            del screenshot  # 显式删除截图对象释放内存
    # 如果程序未找到图像，则输出提示信息
    else:
        print("已超过20秒没有找到开始游戏字图像，退出程序。")
# ◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊

#【30gd】◊◊◊找关闭浙电学习窗口图像为基准，把鼠标加偏移量（x-?, y+?）目的移到更多字图像◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊
def zj_30gd(image_path="D:\\python\\zj\\zj30a.bmp"):
    time.sleep(1)
    start_time = time.time()
    while time.time() - start_time < 20:
        # 截取屏幕截图并查找图像的位置
        screenshot = pyautogui.screenshot()
        x_y = pyautogui.locateCenterOnScreen(image_path, confidence=0.8,region=(0, 0, screenshot.width, screenshot.height))
        if x_y is not None:
            x, y = x_y
            print(f"关闭浙电学习窗口图像（zj30a）在 ({x}, {y}) 的位置需加偏移量。")
            pyautogui.moveTo(x-370, y+410, duration=0.5)
            time.sleep(1)
            pyautogui.click()
            print(f"关闭浙电学习窗口图像（zj30a）在 ({x}, {y}) 的位置，把鼠标加偏移量（更多字图像）并点击。")
            break
        else:
            print("未找到关闭浙电学习窗口图像（zj30a），等待1秒后再重新查找。")
            time.sleep(1)
            del screenshot  # 显式删除截图对象释放内存
    # 如果程序未找到图像，则输出提示信息
    else:
        print("已超过20秒没有找到关闭浙电学习窗口图像（zj30a）所以没点击更多字图像），那么退出程序。")
# ◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊

#【30llk】◊◊◊找关闭浙电学习窗口图像为基准，把鼠标加偏移量（x-?, y+?）目的移到连连看字图像◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊
def zj_30llk(image_path="D:\\python\\zj\\zj30a.bmp"):
    time.sleep(1)
    start_time = time.time()
    while time.time() - start_time < 20:
        # 截取屏幕截图并查找图像的位置
        screenshot = pyautogui.screenshot()
        x_y = pyautogui.locateCenterOnScreen(image_path, confidence=0.8,region=(0, 0, screenshot.width, screenshot.height))
        if x_y is not None:
            x, y = x_y
            print(f"关闭浙电学习窗口图像（zj30a）在 ({x}, {y}) 的位置需加偏移量。")
            pyautogui.moveTo(x-190, y+130, duration=0.5)
            time.sleep(1)
            pyautogui.click()
            print(f"关闭浙电学习窗口图像（zj30a）在 ({x}, {y}) 的位置，把鼠标加偏移量（连连看字图像）并点击。")
            break
        else:
            print("未找到关闭浙电学习窗口图像（zj30a），等待1秒后再重新查找。")
            time.sleep(1)
            del screenshot  # 显式删除截图对象释放内存
    # 如果程序未找到图像，则输出提示信息
    else:
        print("已超过20秒没有找到关闭浙电学习窗口图像（zj30a）所以没点击连连看字图像），那么退出程序。")
# ◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊

#【30ksyx】◊◊◊找关闭浙电学习窗口图像为基准，把鼠标加偏移量（x-?, y+?）目的移到开始游戏字图像◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊
def zj_30ksyx(image_path="D:\\python\\zj\\zj30a.bmp"):
    time.sleep(1)
    start_time = time.time()
    while time.time() - start_time < 20:
        # 截取屏幕截图并查找图像的位置
        screenshot = pyautogui.screenshot()
        x_y = pyautogui.locateCenterOnScreen(image_path, confidence=0.8,region=(0, 0, screenshot.width, screenshot.height))
        if x_y is not None:
            x, y = x_y
            print(f"关闭浙电学习窗口图像（zj30a）在 ({x}, {y}) 的位置需加偏移量。")
            pyautogui.moveTo(x-250, y+450, duration=0.5)
            time.sleep(1)
            pyautogui.click()
            print(f"关闭浙电学习窗口图像（zj30a）在 ({x}, {y}) 的位置，把鼠标加偏移量（开始游戏字图像）并点击。")
            break
        else:
            print("未找到关闭浙电学习窗口图像（zj30a），等待1秒后再重新查找。")
            time.sleep(1)
            del screenshot  # 显式删除截图对象释放内存
    # 如果程序未找到图像，则输出提示信息
    else:
        print("已超过20秒没有找到关闭浙电学习窗口图像（zj30a）所以没点击开始游戏字图像），那么退出程序。")
# ◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊



def getGameWindow():
    window = win32gui.FindWindow(None, WINDOW_TITLE)  # 查找指定标题的窗口
    while not window:
        print('找不到浙电安全学习平台窗口，5秒后重新定位浙电安全学习平台窗口...')
        time.sleep(5)
        window = win32gui.FindWindow(None, WINDOW_TITLE)
    win32gui.SetForegroundWindow(window)
    # 将找到的窗口移动到指定区（400，0）并改变窗口大小（450X780）
    #x, y, width, height = 400, 0, 450, 780   #原来便用的窗口大小
    x, y, width, height = 400, 0, 480, 780
    win32gui.MoveWindow(window, x, y, width, height, True)
    pos = win32gui.GetWindowRect(window)
    print("浙电安全学习平台窗口在 " + str(pos))
    zj_26("D:\\python\\zj\\zj26.bmp")  # 找我的字图像
    zj_30gd("D:\\python\\zj\\zj30a.bmp")  # 找更多字图像
    zj_30llk("D:\\python\\zj\\zj30a.bmp")  # 找连连看字图像
    zj_30ksyx("D:\\python\\zj\\zj30a.bmp")  # 找开始游戏字图像
    time.sleep(1)  #加点时间截图正确
    return (pos[0], pos[1])

def getScreenImage():
    print('截屏中...')
    scim = ImageGrab.grab()   # 使用ImageGrab模块捕获整个屏幕并保存为PNG图片
    scim.save('D:\\python\\zj\\lian\\screen.png')
    return cv2.imread("D:\\python\\zj\\lian\\screen.png")  # 使用OpenCV读取PNG图片

def getAllSquare(screen_image, game_pos, MARGIN_BETWEEN_SQUARES=15):
    # 根据安全连连看位置设置的起始坐标（加上左边距和上边距）
    game_x = game_pos[0] + MARGIN_LEFT
    game_y = game_pos[1] + MARGIN_HEIGHT
    all_square = []      # 初始化一个空列表用于存放所有正方形区域
    for x in range(0, H_NUM):  # x 是行号
        for y in range(0, V_NUM):  # y 是列号
            # 计算每行的起始Y坐标（不需要额外的逻辑，因为每行的高度和边距是固定的）
            start_y = game_y + y * (POINT_HEIGHT + MARGIN_BETWEEN_SQUARES)
            # 调整game_x使第2列的图向右偏一点
            if x == 3:
                start_x = game_x + x * (POINT_WIDTH + 21)
            elif x == 4:
                start_x = game_x + x * (POINT_WIDTH + 20)
            elif x == 5:
                start_x = game_x + x * (POINT_WIDTH + 19)
            else:
                start_x = game_x + x * (POINT_WIDTH + MARGIN_BETWEEN_SQUARES)

            # 考虑到最后一个正方形的右边和下边可能不需要边距，所以我们需要做一些边界检查
            end_y = min(start_y + POINT_HEIGHT, screen_image.shape[0])
            end_x = min(start_x + POINT_WIDTH, screen_image.shape[1])

            # 切割图像区域
            square = screen_image[start_y:end_y, start_x:end_x]
            all_square.append(square)
            # #显示图像↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓显示图像
            # plt.ion()  # 交互式模式，使得图像可以连续显示
            # fig, ax = plt.subplots()  # 创建一个figure和axes对象
            # for i, square in enumerate(all_square):
            #     ax.clear()  # 清除之前的图像
            #     ax.imshow(square)  # 显示新的图像
            #     ax.set_title(f'Image {i + 1}')
            #     ax.axis('off')  # 不显示坐标轴
            #     plt.draw()  # 更新图像
            #     plt.pause(0.2)  # 暂停0.2秒，但这里不会阻塞，因为我们在交互模式下
            # #plt.ioff()  # 关闭交互模式。如果你要自己点关闭就用上
            # #plt.show(block=True)  # 显示最终图像并阻塞，直到用户关闭窗口，如果你要自己点关闭就用上
            # time.sleep(0.5)  # 等待0.5秒
            # plt.close(fig)  # 关闭figure窗口
            # #显示图像↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑显示图像
            # # 打印列表查看
            #print(all_square)
            # #返回最终结果列表
            return all_square

def isImageExist(img, img_list):  #isImageExist图像存在
    i = 0
    for existed_img in img_list:  # 遍历已存在的图片列表
        b = np.subtract(existed_img, img)
        if not np.any(b):
            return i
        i = i + 1
    return -1

def get_images_as_arrays(directory):
    image_arrays = []  # 初始化一个空列表用于存放所有图像片段（NumPy数组）
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 检查文件扩展名是否为常见的图像格式
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
                # 构建文件的完整路径
                file_path = os.path.join(root, file)
                # 使用Pillow打开图像
                with Image.open(file_path) as img:
                    # 无需在with语句块内执行np.array(img)，但这样做也没问题
                    # 使用asarray()将PIL图像转换为NumPy数组
                    image_array = np.array(img)  # 这里通常不会有黄色底色警告
                # 将NumPy数组添加到列表中（此时img对象可能已关闭，但image_arrays已经创建）
                image_arrays.append(image_array)
                # # 打印列表查看
                #print(image_arrays)
    return image_arrays

# # 上面使用函数
# image_dir = "D:\\path\\to\\your\\images"#你的图片所放的路径
# all_square2 = get_images_as_arrays(image_dir)

def getAllSquareTypes(all_square):
    print("初始化图片类型的消息...")
    types = []
    number = []
    nowid = 0  # 初始化当前ID
    for square in all_square:  # 遍历所有图片
        nid = isImageExist(square, types)  # 调用isImageExist函数判断图片是否存在
        if nid == -1:
            types.append(square)
            number.append(1)
        else:
            number[nid] = number[nid] + 1
            if (number[nid] > number[nowid]):
                nowid = nid
    global EMPTY_ID   # 将当前ID设置为全局变量EMPTY_ID
    EMPTY_ID = nowid
    print('EMPTY_ID = ' + str(EMPTY_ID))  # 打印EMPTY_ID的值
    return types  # 返回图片类型列表

def findAndClickIcon(icon_path, screen_image, game_pos):   #findAndClickIcon查找和单击图标？？
    # 将PIL图像转换为OpenCV图像
    opencv_image = np.array(screen_image)
    # 转换颜色空间
    gray_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)

    # 加载图标模板
    template = cv2.imread(icon_path, 0)
    w, h = template.shape[::-1]

    # 使用模板匹配
    res = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    # 如果有匹配，则模拟点击
    for pt in zip(*loc[::-1]):
        cv2.rectangle(opencv_image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        # 转换为游戏窗口的坐标
        game_x = pt[0] + game_pos[0] + MARGIN_LEFT
        game_y = pt[1] + game_pos[1] + MARGIN_HEIGHT
        # 模拟点击
        pyautogui.click(game_x + w // 2, game_y + h // 2)
        print(f"Clicked at ({game_x + w // 2}, {game_y + h // 2})")
        # 等待一段时间，防止过快点击
        time.sleep(3)

def getAllSquareRecord(all_square_list, types):
    print("Change map...")  #打印提示信息
    record = []  # 初始化记录列表
    line = []    # 初始化临时存储列表
    for square in all_square_list:  # 遍历所有方块
        num = 0
        for type in types:          # 遍历类型列表
            res = cv2.subtract(square, type) # 使用OpenCV库计算方块和类型的差值
            if not np.any(res): # 如果差值为0，说明方块和类型相同
                line.append(num)  # 将计数器的值添加到临时列表中
                break # 跳出内层循环
            num += 1  # 计数器加1
        if len(line) == V_NUM:  # 如果临时列表的长度等于某个常数V_NUM（未在代码中定义）
            print(line)   # 打印临时列表
            record.append(line)   # 将临时列表添加到记录列表中
            line = []  # 清空临时列表
    return record # 返回记录列表

##### 定义函数：canConnect，判断两点是否同一个点######
def canConnect(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return False
    return True


def autoRelease(result, game_x, game_y):
    for i in range(len(result)):
        for j in range(len(result[0])):
            if result[i][j] != EMPTY_ID:
                for m in range(len(result)):
                    for n in range(len(result[0])):
                        if result[m][n] != EMPTY_ID and (i != m or j != n):
                            if canConnect(i, j, m, n, result):
                                result[i][j] = EMPTY_ID
                                result[m][n] = EMPTY_ID
                                print('Remove ：' + str(i + 1) + ',' + str(j + 1) + ' and ' + str(m + 1) + ',' + str(n + 1))
                                x1 = game_x + j * POINT_WIDTH
                                y1 = game_y + i * POINT_HEIGHT
                                x2 = game_x + n * POINT_WIDTH
                                y2 = game_y + m * POINT_HEIGHT

                                win32api.SetCursorPos((x1 + 15, y1 + 18))
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x1 + 15, y1 + 18, 0, 0)
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x1 + 15, y1 + 18, 0, 0)
                                time.sleep(random.uniform(TIME_INTERVAL_MIN, TIME_INTERVAL_MAX))

                                win32api.SetCursorPos((x2 + 15, y2 + 18))
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x2 + 15, y2 + 18, 0, 0)
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x2 + 15, y2 + 18, 0, 0)
                                time.sleep(random.uniform(TIME_INTERVAL_MIN, TIME_INTERVAL_MAX))
                                return True
    return False


def autoRemove(squares, game_pos):
    # 将游戏位置转换为屏幕上的坐标
    game_x = game_pos[0] + MARGIN_LEFT
    game_y = game_pos[1] + MARGIN_HEIGHT

    # 循环执行，直到无法自动消除方块为止
    while True:
        # 调用autoRelease函数尝试自动消除方块
        if not autoRelease(squares, game_x, game_y):
            # 如果无法消除方块，则退出程序
            return sys.exit()

if __name__ == '__main__':
    time.sleep(2)
    game_pos = getGameWindow()  # 获取游戏（安全连连看）窗口的位置
    if game_pos is None:
        sys.exit()  #没有（安全连连看）窗口退出
    time.sleep(1)  # 加点时间截图正确
    screen_image = getScreenImage()   # 获取屏幕截图
    all_squares_list = getAllSquare(screen_image, game_pos)  # 从屏幕截图中获取所有方块的位置信息

    # 获取指定目录下的所有图像文件，使用函数
    image_dir = "D:\\python\\zj\\lian"
    all_square2 = get_images_as_arrays(image_dir)
    # # 打印列表查看
    #print(all_square2)
    types = getAllSquareTypes(all_squares_list)  # 获取所有方块的类型
    result = np.transpose(getAllSquareRecord(all_squares_list, types))  # 获取所有方块的记录，并进行转置这里不懂？？？
    print('The total elimination amount is ' + str(autoRemove(result, game_pos)))  # 调用autoRemove函数进行自动消除方块，并打印消除的总数量
    # findAndClickIcon("D:\\python\\zj\\lian\\icon_template.png", "D:\\python\\zj\\lian\\screen.png", None)

    # # 假设autoRemove函数会处理自动点击逻辑
    # autoRemove(all_squares, game_pos)

    # 程序结束，等待2秒
    time.sleep(2)
