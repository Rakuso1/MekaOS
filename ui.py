import os

def make_bar(value, max_value=100):

    filled = int(value / 10)
    empty = 10 - filled

    return "█" * filled + "-" * empty

def display_hud(meka):

    os.system("cls" if os.name == "nt" else "clear")

    print("========================")
    print("      メカOS")
    print("========================")

    print(f"\nPOWER  [{make_bar(meka.power)}] {meka.power}%")
    print(f"HEAT   [{make_bar(meka.heat)}] {meka.heat}%")
    print(f"ARMOR  [{make_bar(meka.armor)}] {meka.armor}%")
    print(f"SHIELD [{make_bar(meka.shield)}] {meka.shield}%")
    print(f"AMMO   [{make_bar(meka.ammo * 10)}] {meka.ammo}")

    if meka.heat >= 70:
        print("\nWARNING: HIGH HEAT")

    if meka.overheated:
        print("\nSTATUS: OVERHEATED")
    else:
        print("\nSTATUS: COMBAT READY")