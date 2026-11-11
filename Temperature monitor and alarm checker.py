
# TEMPERATURE MONITOR AND ALARM CHECKER

# Set the safe temperature limit
SAFE_LIMIT = 80

# Create an empty list to store temperatures
temperatures = []

print("====================================")
print("   MACHINE TEMPERATURE MONITOR")
print("====================================")

# Collect 5 temperature readings
for i in range(5):
    reading = float(input(f"Enter temperature reading {i + 1}: "))
    temperatures.append(reading)

# Calculate highest, lowest and average
highest = max(temperatures)
lowest = min(temperatures)
average = sum(temperatures) / len(temperatures)

# Display temperature results
print("\n========== MONITOR REPORT ==========")

print("Temperature Readings:", temperatures)
print("Highest Temperature:", highest, "°C")
print("Lowest Temperature:", lowest, "°C")
print("Average Temperature:", round(average, 2), "°C")
print("Safe Temperature Limit:", SAFE_LIMIT, "°C")

# Check for dangerous temperatures
print("\n========== ALARM CHECK ==========")

if highest > SAFE_LIMIT:
    print("WARNING! HIGH TEMPERATURE DETECTED!")
    for temp in temperatures:
        if temp > SAFE_LIMIT:
            print("ALARM:", temp, "°C is above the safe limit.")
else:
    print("NORMAL: All temperatures are within the safe limit.")

# MY OWN TWIST: Temperature Status and Recommendation
print("\n========== MY OWN TWIST ==========")

if average > SAFE_LIMIT:
    print("MACHINE STATUS: CRITICAL")
    print("Recommendation: Stop the machine and inspect it.")
elif average >= 60:
    print("MACHINE STATUS: HOT")
    print("Recommendation: Monitor the machine closely.")
else:
    print("MACHINE STATUS: NORMAL")
    print("Recommendation: Machine temperature is okay.")

print("\nTemperature monitoring completed.")





#I added an extra feature that automatically checks the average temperature and gives the machine a health status.
NORMAL: Average temperature is below 60°C.
HOT: Average temperature is between 60°C and 80°C.
CRITICAL: Average temperature is above 80°C.
It also recommends what the operator should do.
