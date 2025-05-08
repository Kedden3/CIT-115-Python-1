# Inter Planetery Weights Calculator

# 1. Named constants for each planet surface gravity Factors

n_MERCURY_GRAVITY  = 0.38
n_VENUS_GRAVITY    = 0.91
n_MOON_GRAVITY     = 0.165
n_MARS_GRAVITY     = 0.38
n_JUPITER_GRAVITY  = 2.34
n_SATURN_GRAVITY   = 0.93
n_URANUS_GRAVITY   = 0.92
n_NEPTUNE_GRAVITY  = 1.12
n_PLUTO_GRAVITY    = 0.066

# 2. Prompt the user name and earth weight conversion 

s_Name = input("What is your name: ")
n_Earth_weight = float(input("What is your weight: "))


# 3. Multiple the earth weight by each of the planet's Surface Gravity Factor
                       
n_mercury_weight = n_Earth_weight * n_MERCURY_GRAVITY
n_venus_weight   = n_Earth_weight * n_VENUS_GRAVITY
n_moon_weight    = n_Earth_weight * n_MOON_GRAVITY                      
n_mars_weight    = n_Earth_weight * n_MARS_GRAVITY
n_jupiter_weight = n_Earth_weight * n_JUPITER_GRAVITY
n_saturn_weight  = n_Earth_weight * n_SATURN_GRAVITY
n_uranus_weight  = n_Earth_weight * n_URANUS_GRAVITY                       
n_neptune_weight = n_Earth_weight * n_NEPTUNE_GRAVITY
n_pluto_weight   = n_Earth_weight * n_PLUTO_GRAVITY
                       
# 4. Output
                       
print(s_Name, "here are your weights on our solar system's planets: ")
print("Weight on Mercury :    ", format(n_mercury_weight,'10.2f'))                       
print("Weight on Venus :      ", format(n_venus_weight,'10.2f'))
print("Weight on Moon :       ", format(n_moon_weight,'10.2f'))
print("Weight on Mars :       ", format(n_mars_weight,'10.2f'))
print("Weight on Jupiter :    ", format(n_jupiter_weight,'10.2f'))
print("Weight on Saturn :     ", format(n_saturn_weight,'10.2f'))                       
print("Weight on Uranus :     ", format(n_uranus_weight,'10.2f'))
print("Weight on Neptune :    ", format(n_neptune_weight,'10.2f'))
print("Weight on Pluto :      ", format(n_pluto_weight,'10.2f'))                       
