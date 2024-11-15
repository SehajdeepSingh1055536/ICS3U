# Function to calculate wind chill
def calculate_wind_chill(temp, wind_speed):
    # Calculate wind chill temperature based on the formula
    wind_chill = 13.12 + (0.6215 * temp) - (11.37 * (wind_speed ** 0.16)) + (0.3965 * temp * (wind_speed ** 0.16))
    return wind_chill

# Function to determine risk level based on wind chill temperature
def interpret_wind_chill(wind_chill):
    if 0 <= wind_chill <= -10:
        return "Low risk"
    elif -10 > wind_chill >= -28:
        return "Moderate risk of hypothermia"
    elif -28 > wind_chill >= -40:
        return "High risk of frostbite"
    elif -40 > wind_chill >= -48:
        return "Severe risk of frostbite: exposed skin freezes in 5-10 minutes"
    elif -48 > wind_chill >= -55:
        return "Severe risk of frostbite: exposed skin freezes in 2-5 minutes"
    else:
        return "Extreme risk: exposed skin freezes in under 2 minutes"

# Sample temperatures and wind speeds for testing
temperatures = [-5, -20, -30, -45]
wind_speeds = [10, 20, 40]

# Loop through each temperature and wind speed to calculate wind chill and interpret the output
for temp in temperatures:
    for wind_speed in wind_speeds:
        wind_chill = calculate_wind_chill(temp, wind_speed)
        risk_level = interpret_wind_chill(wind_chill)
        print(f"WC = {wind_chill:.2f} °C, T = {temp} °C, W = {wind_speed} km/h -> {risk_level}")
