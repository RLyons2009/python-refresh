import time
def lights():
    global light
    light = True
    while light == True:
        print("🟢 Lights are Green - Go")
        time.sleep(4.5)
        print("--- Slow Down ---")
        time.sleep(0.5)
        print("🟠 Lights are turning Red - Slow Down")
        light = "Red"
        time.sleep(2.5)
        print("--- Stop ---")
        time.sleep(0.5)
        light = False
    print("🔴 Lights are Red - Stop")
    time.sleep(4.5)
    print("--- Speed Up ---")
    time.sleep(0.5)
    print("🟠 Lights are turning Green - Speed up")
    time.sleep(2.5)
    print("--- Go ---")
    time.sleep(0.5)
    light = True
    lights()
lights()