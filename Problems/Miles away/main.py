def mi_to_km(miles):
    miles_to_km = float(miles) * 1.609
    return round(miles_to_km, 2)

km = mi_to_km(100)
print(km)