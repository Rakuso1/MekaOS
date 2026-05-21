def fire_weapon(meka):

    if meka.overheated:
        print("REACTOR OVERHEATED Cannot fire weapon until cooled down.")
        return
    
    if meka.ammo <= 0:
        print("WARNING: NO AMMO REMAINING")
        return
    
    meka.ammo -= 1
    meka.heat += 20

    print(">>WEAPON FIRED")

    if meka.heat >= 100:
        meka.overheated = True
        meka.reactor_online = False
        print(">>REACTOR OVERHEAT")