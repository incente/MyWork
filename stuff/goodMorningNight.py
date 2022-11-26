import random, pyautogui, datetime

start = "Guten Morgen "

bae = ["Bae", "Shawty", "Babygirl", "Baby", "Bubbe", "Bubbesyx", "Mami", "Babymami", "Babe", "Love", "Liebste", "Süße", "Honey", "Darling", "Sweetie"]
rand = random.randrange(len(bae))
baeRand = bae[rand]

middle = ", ich wünsche dir einen "

adj = ["erholsamen", "geruhsamen", "erfolgreiche", "stressfreien", "unterhaltsamen", "spannenden", "tollen", "schönen", "herrrlichen", "super tollen", "angenehmen", "coolen", "wundervollen", "traumhaften", "strahlenden", "fabelhaften", "fröhlichen", "heiteren", "entspannten", "relaxten", "lustigen", "spassigen", "super-genialen"]
rand1 = random.randrange(len(adj))
adjRand = adj[rand1]

emj = ["<3", ";*", ":*"]
emjs = ""
for a in emj:
    rand2 = random.randrange(len(emj))
    emjs += emj[rand2]

emjs1 = ""
for a in emj:
    rand3 = random.randrange(len(emj))
    emjs1 += emj[rand3]

last = " Viel Spaß heute. Wir hören uns später. Bussii " + emjs1

result = start + baeRand + middle + adjRand + " Tag! " + emjs + last
print(result)

#a == "23:17:00"
#nw = datetime.datetime.now()
#n = nw.strftime("%H:%M:%S")



#if n == a:
    #pyautogui.write(result)
    #pyautogui.press('enter')
    #print("success")