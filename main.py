from meka import Meka
from railgun import fire_weapon
from reactor import cool_reactor
from radar import enemy_scan
from ui import display_hud

meka = Meka()

while True:
    command = input("MekaOS> ")

    if command == "status":
        display_hud(meka)

    elif command == "fire":
        fire_weapon(meka)

    elif command == "cool":
        cool_reactor(meka)

    elif command == "scan":
        enemy_scan(meka)

    elif command == "exit":
        break