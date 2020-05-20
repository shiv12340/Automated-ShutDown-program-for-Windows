import pyautogui, time
pyautogui.FAILSAFE = False
pyautogui.click(x=1365, y=767, button='left')
pyautogui.hotkey('alt', 'f4')
time.sleep(0.1)
pyautogui.click(700, 391)


