def zero_fuel(dist_pump, mpg, fuel_left): 
    return True if dist_pump <= mpg * fuel_left else False