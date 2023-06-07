glucose_level = int(input("Glucose Level : "))

if glucose_level <= 70:
    print("Low glucose level")

elif glucose_level >= 140:
    print("High glucose level")

else:
    print("Normal range")


heart_rate = 180
if heart_rate < 40:
    print("Low heart rate")
elif heart_rate >= 180:
    print("Hight heart rate")
else:
    print("Normal range")

seats = 100
while seats > 0:
    print("Sell tickets")
    seats = seats - 1

temperature = 40

if temperature < 35:
    print("Hypothermia")

elif temperature > 39:
    print("Fever")
else:
    print("Normal temperature")