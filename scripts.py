import pyautogui
import pytesseract
from PIL import Image
import sys
from pytesseract import Output
import time


sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8')


def locating(string):
    # 截屏，并保存为图片以供扫描
    screenshot = pyautogui.screenshot(region=(0, 140, max, max))
    screenshot.save('screenshot.png')

    # 调用pytesseract扫描图片中所有文字的信息，包括坐标
    text = pytesseract.image_to_data(
        "screenshot.png", lang='chi_sim', config=r"--psm 3 --oem 3", output_type=Output.DICT
    )

    # print(text)

    # 在提取的文字框中查找特定字符串的位置，并返回坐标
    for i, data in enumerate(text['text']):
        if data == string[0]:
            (x, y, width, height) = (
                text['left'][i], text['top'][i], text['width'][i], text['height'][i])
            # print(data, x)
            pyautogui.moveTo((x, y, width, height), duration=0.5)
            break

    return (x, y, width, height)


def instant_position():
    a = pyautogui.position()
    b = 0
    while True:
        if b != a:
            b = a
            print(b)
        a = pyautogui.position()
        time.sleep(0.5)
