import pyautogui
import time
import scripts
import threading

'''
1. 给定坐标，门口扫荡练级
2. 自动建造
'''
# x, y = pyautogui.size()
# chance = 5
time.sleep(3)
# mouse_pos = pyautogui.position()
# field_pos = pyautogui.locateOnScreen(
#     'field.png', confidence=0.4)  # confidence parameter is important when the image has a midium lower quality
# mouse_pos = pyautogui.locateCenterOnScreen('field.png')

# print(mouse_pos)
# print(mouse_pos[0])


class Army(threading.Thread):
    def __init__(self, name, delay, chance, target):
        super().__init__(name=name)
        self.name = name  # hero's png profile path
        self.delay = delay  # estimated action time
        self.chance = chance  # hero health
        self.target = target  # position of field

    def run(self):
        time.sleep(2)
        try:
            while self.chance:
                # go to seach page
                selection = pyautogui.locateCenterOnScreen(
                    'search.png', confidence=0.6)
                pyautogui.click(selection, duration=0.3)
                time.sleep(0.2)

                # go to search bar and search
                selection = pyautogui.locateCenterOnScreen(
                    'jump.png', confidence=0.7)
                print(selection, selection.x-30)
                pyautogui.click((selection.x-400, selection.y), duration=0.3)
                pyautogui.hotkey('ctrl', 'a', 'backspace')
                pyautogui.write(f"{self.target[0]}", interval=0.1)
                time.sleep(0.2)

                selection = pyautogui.locateCenterOnScreen(
                    'jump.png', confidence=0.7)
                pyautogui.click((selection.x-200, selection.y), duration=0.3)
                pyautogui.hotkey('ctrl', 'a', 'backspace')
                pyautogui.write(f"{self.target[1]}", interval=0.1)
                time.sleep(0.2)

                selection = pyautogui.locateCenterOnScreen(
                    'jump.png', confidence=0.7)
                pyautogui.click(selection, duration=0.2)
                time.sleep(1)

                screen_width, screen_height = pyautogui.size()
                center_x = screen_width // 2
                center_y = screen_height // 2
                pyautogui.click(center_x-20, center_y-20, duration=0.2)
                time.sleep(0.2)

                # print(pyautogui.locateCenterOnScreen(
                #     'occupied.png', confidence=0.5), 'occupied')

                selection = pyautogui.locateCenterOnScreen(
                    'march1.png', confidence=0.6)
                pyautogui.moveTo(selection, duration=0.3)
                pyautogui.click()
                time.sleep(0.4)

                selection = pyautogui.locateCenterOnScreen(
                    f"{self.name}", confidence=0.5)
                # pyautogui.moveTo(selection.x, selection.y, duration=0.3)
                pyautogui.click(selection, duration=0.3)
                time.sleep(0.2)

                selection = pyautogui.locateCenterOnScreen(
                    'march2.png', confidence=0.5)
                pyautogui.click(selection, duration=0.3)
                time.sleep(self.delay)

                self.chance -= 1
        except Exception as e:
            print(e, 'something wrong, try again')
        finally:
            time.sleep(self.delay)


# scripts.instant_position()
# scripts.locating('试玩')
# name, delay, chance, target = input('name:'), int(
#     input()), int(input()), input().split()
army = Army("hero_daqiao.png", 60, 5, [541, 1134])
army.run()
