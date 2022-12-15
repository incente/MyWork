import pyautogui, time, random

print("Welcome to the afk bot!")
t = int(input("How long do you want to be afk in seconds? "))
print(f"Start countdown from {t}")

def rand(x, y):
    return random.randint(x, y)

while t > 0:
    print(t)
    pyautogui.moveTo(rand(1, 1000), rand(1, 1000))
    time.sleep(1)
    t -= 1
