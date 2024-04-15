import os
from time import sleep

from SimConnect import *

# Create SimConnect link
sm = SimConnect()
# Note the default _time is 2000 to be refreshed every 2 seconds
aq = AircraftRequests(sm, _time=1000)
# Use _time=ms where ms is the time in milliseconds to cache the data.
# Setting ms to 0 will disable data caching and always pull new data from the sim.
# There is still a timeout of 4 tries with a 10ms delay between checks.
# If no data is received in 40ms the value will be set to None
# Each request can be fine tuned by setting the time param.

# To find and set timeout of cached data to 200ms:
# altitude = aq.find("PLANE_ALTITUDE")
#
# altitude.time = 200

# Get the aircraft's current altitude
# altitude = aq.get("PLANE_ALTITUDE")
# altitude = altitude + 1000
# print(aq.get("PLANE_ALTITUDE"))
# Set the aircraft's current altitude
# aq.set("PLANE_ALTITUDE", altitude)
ae = AircraftEvents(sm)

while True:
    # print(aq.find("CRASH_FLAG").defined)
    print("CATEGORY", aq.get("CATEGORY"))
    print("GROUND_ALTITUDE", aq.get("GROUND_ALTITUDE"))
    print("REALISM", aq.get("REALISM"))
    print("REALISM_CRASH_DETECTION", aq.get("REALISM_CRASH_DETECTION"))
    print("AMBIENT_TEMPERATURE", aq.get("AMBIENT_TEMPERATURE"))
    print("G_FORCE", aq.get("G_FORCE"))
    print("MACH_MAX_OPERATE	", aq.get("MACH_MAX_OPERATE"))
    print("MAX_G_FORCE	", aq.get("MAX_G_FORCE"))
    print("MAX_GROSS_WEIGHT	", aq.get("MAX_GROSS_WEIGHT"))
    print("EMPTY_WEIGHT", aq.get("EMPTY_WEIGHT"))
    print("TOTAL_WEIGHT", aq.get("TOTAL_WEIGHT"))
    print("FUEL_TOTAL_CAPACITY", aq.get("FUEL_TOTAL_CAPACITY"))
    print("FUEL_TOTAL_QUANTITY", aq.get("FUEL_TOTAL_QUANTITY"))
    print("PLANE_ALTITUDE", aq.get("PLANE_ALTITUDE"))
    print("PLANE_ALT_ABOVE_GROUND", aq.get("PLANE_ALT_ABOVE_GROUND"))
    print("PLANE_BANK_DEGREES", aq.get("PLANE_BANK_DEGREES"))
    print("VERTICAL_SPEED", aq.get("VERTICAL_SPEED"))
    print("AIRSPEED_BARBER_POLE", aq.get("AIRSPEED_BARBER_POLE"))
    print("AIRSPEED_INDICATED", aq.get("AIRSPEED_INDICATED"))
    print("AIRSPEED_MACH", aq.get("AIRSPEED_MACH"))
    print("BARBER_POLE_MACH", aq.get("BARBER_POLE_MACH"))
    print("HYDRAULIC_SYSTEM_INTEGRITY", aq.get("HYDRAULIC_SYSTEM_INTEGRITY"))
    print("LEADING_EDGE_FLAPS_LEFT_PERCENT", aq.get("LEADING_EDGE_FLAPS_LEFT_PERCENT"))
    # print(aq.set("LEADING_EDGE_FLAPS_LEFT_PERCENT",1))
    # print(aq.set("TRAILING_EDGE_FLAPS_LEFT_PERCENT",1))
    # TOGGLE_HYDRAULIC_FAILURE = ae.Failures.get("TOGGLE_HYDRAULIC_FAILURE")
    # TOGGLE_HYDRAULIC_FAILURE()
    # TOGGLE_ELECTRICAL_FAILURE = ae.find("TOGGLE_PITOT_BLOCKAGE")
    # print("TOGGLE_PITOT_BLOCKAGE", TOGGLE_ELECTRICAL_FAILURE())
    print("HYDRAULIC_PRESSURE", aq.get("HYDRAULIC_PRESSURE:1"))
    print("PRESSURIZATION_CABIN_ALTITUDE", aq.get("PRESSURIZATION_CABIN_ALTITUDE"))
    if aq.get("SIM_ON_GROUND") == 1:
        print("on ground")
    else:
        print("in air")

    if aq.get("CRASH_SEQUENCE") == 11:
        print("crashed")
    print("-------------------")
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

sm.exit()
quit()
