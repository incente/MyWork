import pyautogui, time

pyautogui.PAUSE = 0.3

for i in range(999):
    pyautogui.write('Geh schlafen, es ist schon spät. ;)')
    pyautogui.press('enter')
    time.sleep(0.5)