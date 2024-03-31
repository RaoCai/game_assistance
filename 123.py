import pyautogui
import pytesseract
from PIL import Image
import sys
from pytesseract import Output


sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8')


def find_string_on_screen(string):
    # 截屏，并保存为图片以供扫描
    screenshot = pyautogui.screenshot()
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
            print(data, x)
            found = True
            break

    return (x, y, width, height)


# 调用函数
string = "试"

coordinates = find_string_on_screen(string)

if coordinates is not None:
    print("yes")
    pyautogui.moveTo(coordinates, duration=0.5)
else:
    print('nope')
