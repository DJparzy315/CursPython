def convert_temperature(value, from_unit, to_unit):
    # daca unitatile sunt la fel
    if from_unit == to_unit:
        return value

    # convertim in Celsius
    if from_unit == "C":
        c = value
    elif from_unit == "F":
        c = (value - 32) * 5 / 9
    elif from_unit == "K":
        c = value - 273.15

    # convertim din Celsius in unitatea dorita
    if to_unit == "C":
        return c
    elif to_unit == "F":
        return c * 9 / 5 + 32
    elif to_unit == "K":
        return c + 273.15


# teste
print(convert_temperature(100, "C", "F"))   # 212.0
print(convert_temperature(212, "F", "K"))   # 373.15
print(convert_temperature(0, "K", "C"))     # -273.15
