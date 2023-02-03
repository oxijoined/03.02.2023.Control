def convert_temperature(temp, from_unit, to_unit):
    if from_unit == "C" and to_unit == "F":
        return (temp * 9 / 5) + 32
    elif from_unit == "F" and to_unit == "C":
        return (temp - 32) * 5 / 9
    else:
        return "Invalid input"


print("60°C -", convert_temperature(60, "C", "F"), "°F")
print("45°F -", convert_temperature(45, "F", "C"), "°C")
