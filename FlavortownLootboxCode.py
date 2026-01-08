import random
import time
import os

print("\033[93mWelcome To The Unofficial Flavortown Lootbox\033[0m")

colors = {
    "LEGENDARY": "\033[93m", #HOLY MOLY!!!!!
    "MYTHICAL": "\033[95m",
    "RARE": "\033[94m",
    "UNCOMMON": "\033[92m",
    "COMMON": "\033[0;31m",
    "Default": "\033[0m"
}

flash_colors = [
    "\033[91m",  # red
    "\033[93m",  # LEGENDARYYYYYY!!!!
    "\033[92m",  # green
    "\033[94m",  # blue
    "\033[95m",  # purple
]

crate = [
    "+----------+",
    "|##########|",
    "|##########|",
    "|####||####|",
    "|##########|",
    "|##########|",
    "|##########|",
    "|##########|",
    "|##########|",
    "+----------+",
]

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def print_crate(color):
    for line in crate:
        print(color + line + colors["Default"])

print("Choosing a crate for you...")
time.sleep(1)
for _ in range(10):
    clear()
    print_crate(random.choice(flash_colors))
    time.sleep(0.15)
random_number = random.randint(1, 100)

if random_number == 50:
    LOOT = "LEGENDARY"
elif random_number <= 10:
    LOOT = "UNCOMMON"
elif random_number <= 40:
    LOOT = "RARE"
elif random_number <= 60:
    LOOT = "MYTHICAL"
else:
    LOOT = "COMMON"

LOOT = "LEGENDARY"

clear()
print_crate(colors[LOOT])

print("\n" + colors[LOOT] + f"You got: {LOOT}!" + colors["Default"])