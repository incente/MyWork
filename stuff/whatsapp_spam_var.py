import pyautogui, time

msg = str(input("Message: "))
x = int(input("How often? "))

time.sleep(5)

for n in range(0, x):
    pyautogui.write(msg)
    pyautogui.press("enter")
    time.sleep(1)