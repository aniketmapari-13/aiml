#smat home auto agent
import time
import random

def check_room():

    print("--- Auto Room Check ---")

    # Random sensor inputs
    
    temperature = random.randint(20, 40)
    
    motion = random.choice(["yes", "no"])
    
    light_level = random.choice(["dark", "light"])
    
    smoke = random.choice(["yes", "no"])
    
    occupancy = random.choice(["yes", "no"])
    time.sleep(2)

    # Inputs print karna
    print("\n--- Inputs Received ---")
    print(f"Temperature: {temperature}°C")
    print(f"Motion: {motion}")
    print(f"Light: {light_level}")
    print(f"Smoke: {smoke}")
    print(f"Occupancy: {occupancy}")
    time.sleep(2)
    # Sense karega, fir decision dega
    print("\n[Analyzing & Processing ...]")
    time.sleep(3)

    print("\n-- Decision Taken --")

    # Emergency Safety - Highest Priority
    if smoke == "yes":
        print("- Alarm On (EMERGENCY!)")
        print("- AC Off")
        print("- Door Unlocked")
        print("- Light On (Emergency Safety)")
        return

    # Temperature Control
    if temperature > 30 and occupancy == "yes":
        print("- AC On")
    else:
        print("- AC Off")

    # Lighting Control
    if motion == "yes" and light_level == "dark":
        print("- Light On")
    else:
        print("- Light Off")

    # Door Security
    if occupancy == "yes":
        print("- Door Locked")
    else:
        print("- Door Unlocked")

    print("- All Systems Safe / Off")


# Function call
check_room()