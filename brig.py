# BRIG MODULE - CONVERT THE TEMPERATURE - 2024.11.16 - MADE BY A.RIFKY

# CTOR (CELCIUS TO REAMUR)
def ctor(celcius):
    reamur = 4/5*celcius
    return reamur

# CTOF (CELCIUS TO FAHRENHEIT)
def ctof(celcius):
    fahrenheit = (9/5*celcius)+32
    return fahrenheit

# CTOK (CELCIUS TO KELVIN)
def ctok(celcius):
    kelvin = celcius+273
    return kelvin

# FTOR (FAHRENHEIT TO REAMUR)
def ftor(fahrenheit):
    reamur = 4/9*(fahrenheit-32)
    return reamur

# FTOC (FAHRENHEIT TO CELCIUS)
def ftoc(fahrenheit):
    celcius = 5/9*(fahrenheit-32)
    return celcius

# FTOK (FAHRENHEIT TO KELVIN)
def ftok(fahrenheit):
    kelvin = 5/9*(fahrenheit-32)+273
    return kelvin
