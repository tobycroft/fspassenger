from SimConnect import *

# Create SimConnect link
sm = SimConnect()
# Note the default _time is 2000 to be refreshed every 2 seconds
aq = AircraftRequests(sm, _time=2000)
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
# print(aq.find("CRASH_FLAG").defined)
print("CATEGORY", aq.get("CATEGORY").decode())
print("GROUND_ALTITUDE", aq.get("GROUND_ALTITUDE"))
print("REALISM", aq.get("REALISM"))
print("REALISM_CRASH_DETECTION", aq.get("REALISM_CRASH_DETECTION"))
print("AMBIENT_TEMPERATURE", aq.get("AMBIENT_TEMPERATURE"))
if aq.get("SIM_ON_GROUND") == 1:
    print("on ground")
else:
    print("in air")

if aq.get("CRASH_SEQUENCE") == 11:
    print("crashed")

# ae.Failures.get()
# Trigger a simple event
# event_to_trigger = ae.find("AP_MASTER")  # Toggles autopilot on or off
# event_to_trigger()

# Trigger an event while passing a variable
# target_altitude = 4000
# event_to_trigger = ae.find("AP_MASTER")  # Sets AP autopilot hold level
# event_to_trigger(target_altitude)
sm.exit()
quit()
