def max_rain_water(water):
    total_water = 0
    for i in range(len(water)):
        max_l = max(water[0:i+1])
        max_r = max(water[i::])
        current_water = min(max_l, max_r) - water[i]
        total_water += current_water
    print(total_water)

def max_rain_water_optimized(water):
    max_l = water[0]
    max_r = water[-1]
    total_water = 0
    i = 1
    j = -2

    while max_l <= max_r:
        if max_l < water[i]:
            max_l = water[i]
            i += 1
        elif max_l > water[i]:
            total_water += max_l - water[i]
            i += 1

    while max_l > max_r:
        if max_r < water[j]:
            max_r = water[j]
            j -= 1
        elif max_r > water[j]:
            total_water += max_r - water[j]
            j -= 1

    print(total_water)


rain_water = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
max_rain_water_optimized(rain_water)
