def fire_weapon(meka):
    if meka.ammo <= 0:
        print("WARNING: No ammo left!")
        return
    
    meka.ammo -= 1
    meka.heat += 20

    print(">>WEAPON FIRED")