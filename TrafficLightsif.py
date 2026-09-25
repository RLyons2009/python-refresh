import time
light = "Green"
def lights():
    global light
    if light == "Green":
        print("🟢 Lights are Green - Go")
        light = "AmberG"
        time.sleep(4.5)
        print("--- Slow Down ---")
        time.sleep(0.5)
        lights()
    elif light == "AmberG":
        print("🟠 Lights are turning Red - Slow Down")
        light = "Red"
        time.sleep(2.5)
        print("--- Stop ---")
        time.sleep(0.5)
        lights()
    elif light == "Red":
        print("🔴 Lights are Red - Stop")
        light = "AmberR"
        time.sleep(4.5)
        print("--- Speed Up ---")
        time.sleep(0.5)
        lights()
    else:
        print("🟠 Lights are turning Green - Speed up")
        light = "Green"
        time.sleep(2.5)
        print("--- Go ---")
        time.sleep(0.5)
        lights()
lights()