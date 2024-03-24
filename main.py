import pyautogui
import time

# '''
# 自动化操作需要预先获取几个参数，作为行动标准。 它们分别是：屏幕尺寸，鼠标位置，主城位置，地块图样，大营画像，大营体力值
# 寻找地块，首先判断是否是高级地，其次判断是否已经拥有，再次判断周边地块是否相连

# 不过以上的实现起来比较费劲，先看看自动刷级效果如何
# '''
x, y = pyautogui.size()
chance = 5
time.sleep(3)
mouse_pos = pyautogui.position()
field_pos = pyautogui.locateOnScreen(
    'field.png', confidence=0.4)  # confidence parameter is important when the image has a midium lower quality
# mouse_pos = pyautogui.locateCenterOnScreen('field.png')

print(mouse_pos)
print(mouse_pos[0])

while chance >= 0:
    pyautogui.moveTo(field_pos, duration=0.5)
    pyautogui.click()
    time.sleep(0.5)

    print(pyautogui.locateCenterOnScreen(
        'occupied.png', confidence=0.5), 'occupied')

    selection = pyautogui.locateCenterOnScreen('march1.png', confidence=0.7)
    pyautogui.moveTo(selection, duration=0.5)
    pyautogui.click()
    time.sleep(0.5)

    selection = pyautogui.locateCenterOnScreen('daqiao.png', confidence=0.5)
    pyautogui.moveTo(selection, duration=0.5)
    pyautogui.click()
    time.sleep(0.5)

    selection = pyautogui.locateCenterOnScreen('march2.png', confidence=0.5)
    pyautogui.moveTo(selection, duration=0.5)
    pyautogui.click()
    time.sleep(600)

    chance -= chance


#     time.sleep(0.1)
#     print(mouse_pos)
# print(mouse_pos)
# print(pyautogui.onScreen(100, 100))
# pyautogui.dragRel(-100, 200, duration=0.5, button='right')
# time.sleep(2)
# print(pyautogui.pixel(mouse_pos.x, mouse_pos.y))
