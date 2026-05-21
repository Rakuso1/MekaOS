from meka import Meka
from railgun import fire_weapon
from reactor import cool_reactor

meka = Meka()

while True:
    command = input("MekaOS> ")

    if command == "status":
        print(f"POWER: {meka.power}%")
        print(f"HEAT: {meka.heat}%")
        if meka.overheated:
            print("STATUS: OVERHEATED")
        else:
            print("STATUS: COMBAT READY")
        print(f"ARMOR: {meka.armor}%")
        print(f"SHIELD: {meka.shield}%")
        print(f"AMMO: {meka.ammo}")

    elif command == "fire":
        fire_weapon(meka)

    elif command == "cool":
        cool_reactor(meka)

    elif command == "exit":
        break