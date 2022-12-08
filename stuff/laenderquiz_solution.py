import pyautogui, countries_list, time


time.sleep(10)

for i in range(len(countries_list.countries)):
    pyautogui.write(countries_list.countries[i])
    time.sleep(0.01)
