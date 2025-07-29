import logging
import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.utils import uri_helper

URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')

# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)

if __name__ == '__main__':
    # Initialize the low-level drivers
    cflib.crtp.init_drivers()

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:
        # Set default takeoff height to 15cm (0.15m)
        with MotionCommander(scf, default_height=0.15) as mc:
            print("Taking off to 15cm height...")
            time.sleep(10)  # Wait for stable takeoff
            print("Landing...")
            mc.stop()  # Stop movement before landing

#import logging
#import time

#import cflib.crtp
#from cflib.crazyflie import Crazyflie
#from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
#from cflib.positioning.motion_commander import MotionCommander
#from cflib.utils import uri_helper

#URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')

## Only output errors from the logging framework
#logging.basicConfig(level=logging.ERROR)

#if __name__ == '__main__':
#    # Initialize the low-level drivers
#    cflib.crtp.init_drivers()

#    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:
#        # Set default takeoff height to 15cm (0.15m)
#        with MotionCommander(scf, default_height=0.15) as mc:
#            print("Taking off to 15cm height...")
#            time.sleep(2)  # Wait for stable takeoff

#            print("Yawing 360 degrees in place...")
#            cf = scf.cf  # Get the Crazyflie instance

#            # Keep altitude at 15cm and rotate in place
#            start_time = time.time()
#            while time.time() - start_time < 4:  # Rotate for ~4 seconds
#                cf.commander.send_hover_setpoint(0, 0, 90, 0.15)  # (vx, vy, yawRate, altitude)
#                time.sleep(0.1)

#            # Stop rotation & keep hovering
#            cf.commander.send_hover_setpoint(0, 0, 0, 0.15)
#            time.sleep(1)  # Allow stabilization

#            print("Landing...")
#            mc.stop()  # Stop movement before landing

