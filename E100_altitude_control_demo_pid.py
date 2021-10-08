"""
University of Michigan
ENG100-400
"""

import sys
sys.path.append('C:\\AirSim\\PythonClient')
sys.path.append('C:\\AirSim\\PythonClient\\multirotor')

############### import a few useful libraries ###########

import setup_path 
import time
import numpy as np
import math
import matplotlib.pyplot as plt

############### establish the link to AirSim ###########

import airsim              # import AirSim API
import E100_functions      # import drone simulator library

dt = E100_functions.dt()  
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

#### Copy and paste the above in your own flight controller #####

# Modify the following PID parameters to observe the altitude control performance
K_P = 1
K_I = 0.0
K_D = 1
#############

target_alt = 10
integration_term = 0
alt_flag = 1
throttle = 0.5  # initialize Throttle
alt_log = []
wind_flag = 1

start = time.time()
while True:
           
    now = time.time()
    if now-start>35 and wind_flag==1:  # At 35seconds, turn on the wind if it has not been turned on yet.
        E100_functions.set_wind(client,0,0,-7)  #Turn on a downward wind with a magnitude of 7
        wind_flag=0  # We don't need to keep turning on the wind once it has started. Set the flag to 0 so that the wind will not be turned on again.
    elif now - start > 70 and now-start<73:  # Allow the quadcopter to land for 3 seconds.
        target_alt = 0
    elif now - start >= 73:
        break
   
    #################### get sensor readings #####################      
    altitude = E100_functions.get_altitude(client,0) # read quadcopter's altitude 
    alt_log.append(altitude)  # record the altitude reading
    plt.plot(alt_log)  # plot the altitude versus time
    
    ##############################################################
    #Altitude hold (PID controller)##########################
    ##############################################################
    if alt_flag == 1:  # When the program runs the first time, the error is still undefined.
        error_old = target_alt-altitude
        alt_flag = 0
    else:
        error_old = error    # Move e(t) to e(t-dt) 
    error= target_alt-altitude  # Determine the current error e(t)
    integration_term += error*dt  # This is a shorthand for integration_term = integration_term + error*dt
    differential_term = (error - error_old)/dt    
    if K_P*error + K_I*integration_term + K_D*differential_term <0:
        throttle = 0  # Make sure we don't send a negative throttle signal to the drone.
    else:
        throttle = K_P*error + K_I*integration_term + K_D*differential_term
    if throttle >= 1:
        throttle = 1
        
    ####### change the engine throttle ###################################
    E100_functions.set_quadcopter(client,0,0,0,throttle)
      

#### Copy and paste the following in your own flight controller #####    

############### release the link to AirSim ###########
client.armDisarm(False)
client.enableApiControl(False)
