from meka import Meka
from weapons import fire_weapon
from reactor import cool_reactor

meka = Meka()

while True:
    command = input("MekaOS> ")

    if command == "status":
        print(f"POWER: {meka.power}%")
        print(f"HEAT: {meka.heat}%")
        print(f"AMMO: {meka.ammo}")

    elif command == "fire":
        fire_weapon(meka)

    elif command == "cool":
        cool_reactor(meka)

    elif command == "exit":
        break