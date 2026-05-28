#CLIMATE DATA ANALYZER
#Phase 1: Raw Sensor Data

#Every value below is a string - wrapped in quotes
#This is how real APIs and CSV files send you data
#Notice: even numbers are in quotes here. That makes them strings.

station_id = "STATION_001"
station_location = "Atlanta, Georgia"
reading_date = "2024-06-01"

raw_temp_celsius = "34"
raw_humidity_percent = "78"
raw_precip_mm = "12"
raw_wind_kph = "21"
data_quality_flag = "1"

#Print lets you see what is inside a variable
# The Comma between items just puts a space between them in the output

print("Station:", station_id)
print("Location:", station_location)
print("Date:", reading_date)

#type() tells you what kind of data is inside a variable
# This is one of the most useful debugging tools in Python

print("Raw temp value:", raw_temp_celsius)
print("Raw temp type:", type(raw_temp_celsius))

#Phase 2: Type Casting
#First cast "1" from string to integer: int("1") gives you 1
#Then cast that integer to boolean: bool(1) gives you True
#You can chain them: bool(int("1")) — Python works from the inside out.

#int() converts a string to a whole number
# We overwrite the raw_ variables with properlu typed versions
# Notice the variable names no longer have raw_ in front

temp_celsius = int(raw_temp_celsius)
humidity_percent = int(raw_humidity_percent)
precip_mm = int(raw_precip_mm)
wind_kph = int(raw_wind_kph)

# This one takes two steps - string to int, then int to bool
is_quality_data = bool(int(data_quality_flag))

# Now check the types - compare these to what you saw in Phase 1
print("\n--- Phase 2: After Type Casting ---")
print("Temp value:", temp_celsius)
print("Temp type:", type(temp_celsius))

print("Quality flag value:", is_quality_data)
print("Quality flag type:", type(is_quality_data))

#Phase 3: Derived Float Variables
#Fahrenheit formula: multiply by 9/5. then add 32
#float() wraps the result to be explicit that this is a decimal
temp_fahrenheit = float((temp_celsius * 9/5) + 32)

# Kelvin: just add 273.15 - used in scientific and ML climate models
temp_kelvin = float(temp_celsius + 273.15)

# Heat index: a simplified approximation (real formula is more complex)
# This is what "feature engineering" looks like - creating a new variable
# from two existing ones to capture something neither measures alone
heat_index_approx = float(temp_fahrenheit + (humidity_percent * 0.05))

# Unit conversions
precip_inches = float(precip_mm / 25.4)
wind_mph = float(wind_kph / 1.609)

print("\n--- Phase 3: Derived Variables ---")
print("Temp Fahrenheit:", temp_fahrenheit)
print("Temp Kelvin:", temp_kelvin)
print("Heat Index (approx):", heat_index_approx)

# round(value, decimal_places) - cleans up long decimals
print("Precip inches:", round(precip_inches, 2))
print("Wind mph:", round(wind_mph, 2))

#round(precip_inches, 2) tells Python to round the float to 2 decimal places. Without it, you'd see something like 0.4724409448818898. That is technically correct but unreadable. ML reports always round for display.

#Phase 4: Labels and Classification

#danger_score is a counter - it starts at 0 and goes up
# Each condition that is true adds 1 to the score
# This is the manual version of what a classifier model does

danger_score = 0

if temp_celsius < 32:
    danger_score = danger_score + 1

if humidity_percent > 70:
    danger_score = danger_score + 1

if precip_mm > 10:
    danger_score = danger_score + 1

# Turn danger_score into a readable string like "2/3"
danger_score_str = str(danger_score) + "/3"

#Ternary expressions - one line if/else
# Python reads left to right: first value IF condition ELSE second value
temp_label = "EXTREME HEAT" if temp_celsius > 35 else "HIGH" if temp_celsius > 30 else "MODERATE"
humidity_label = "OPPRESSIVE" if humidity_percent > 80 else "HUMID" if humidity_percent > 60 else "NORMAL"
precip_label = "HEAVY RAIN" if precip_mm > 20 else "MODERATE RAIN" if precip_mm > 5 else "LIGHT/NONE"

print("\n--- Phase 4: Labels and Classification ---")
print("Danger Score:", danger_score_str)
print("Temp Category:", temp_label)
print("Humidity Category:", humidity_label)
print("Precipitation Category:", precip_label)

#Phase 5: Final Report

#String multiplication creates clean dividers
report_title = "CLIMATE STATION DAILY REPORT"
divider = "=" * 42
spacer = "-" * 42

print("\n" + divider)
print(report_title)
print(divider)
print("Station ID :", station_id)
print("Loaction   :", station_location)
print("Date       :", reading_date)
print("Data Valid  :", is_quality_data)
print(spacer)
print("Temperature:", temp_celsius, "C /", temp_fahrenheit, "F /", temp_kelvin, "K") 
print("HUMIDITY   :", humidity_percent, "% ->", humidity_label)
print("WIND SPEED   :", wind_kph, "kph /", round(wind_mph, 1), "mph")
print("PRECIP      :", precip_mm, "mm /", round(precip_inches, 2), "in ->", precip_label)
print(spacer)
print("HEAT INDEX  :", round(heat_index_approx, 1), "F (approx)")
print("DANGER SCORE :", danger_score_str)
print("ALERT LEVEL  :", temp_label)
print(divider)