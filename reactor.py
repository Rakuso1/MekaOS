def cool_reactor(meka):
    if meka.heat > 0:
        meka.heat -= 20

        if meka.heat < 0:
            meka.heat = 0

    print(f"Cooling reactor... Current heat: {meka.heat}")

    if meka.overheated and meka.heat < 50:
        meka.overheated = False
        meka.reactor_online = True
        print(">>REACTOR COOLED DOWN. Reactor back online.")