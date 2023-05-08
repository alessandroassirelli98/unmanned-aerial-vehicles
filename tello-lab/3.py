import get_key as kp

from djitellopy import tello 
from time import sleep

# --- Initialization
kp.init() 
drone = tello.Tello()
drone.connect()
print(f"Current battery: {drone.get_battery()}%")

drone.enable_mission_pads()
drone.set_mission_pad_detection_direction(2)
drone.takeoff()

mission_start = False

def look_for_pad():
    pass

try:
    while True:
        if kp.getKey("q"):
            drone.land()

        if (drone.get_battery()):
            print("Landing in 10 seconds because of low battery")
            sleep(10)
            drone.land()
        
        pad = drone.get_mission_pad_id()

        print("pad: ", pad)
        print("stat: ", drone.get_current_state)

        if pad == 1 and not mission_start:
            mission_start = True
        else:
            print("Please takeoff from pad 1")
            sleep(10)
            drone.land()

        if mission_start:
            drone.go_xyz_speed_mid(0, 0, 70, 1)
        
except KeyboardInterrupt:
    drone.land()


    
    

    
