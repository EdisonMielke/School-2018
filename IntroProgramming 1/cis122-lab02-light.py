'''
CIS 122 Fall 2018 Lab 2
Author: Edison N. Mielke
Description: Calculate the average amount of time in seconds light will take to reach the
surface of the Earth and Pluto using average distances.
'''
#The speed of light is 186,282 miles per second
#The average distance of the sun from the Earth is 93,000,000 miles
#The average distance of the sun from Pluto is 3,670,050,000 miles

#I have to use the round() function
Sp_o_light = 186282
Earth_dis_sun_avg = 93000000
Pluto_dis_sun_avg = 3670050000
def Lightspeed(sp):
    return sp / 186282

print ("Light travels from the sun to the Earth in " + str(round((Lightspeed(Earth_dis_sun_avg)),2)) + " seconds.")
print()
print ("Light travels from the sun to the Earth in " + str(round((Lightspeed(Pluto_dis_sun_avg)),2)) + " seconds.")
