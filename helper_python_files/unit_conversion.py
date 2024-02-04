import sys
import pint
from numpy import pi


# Create a unit registry
# ureg = pint.UnitRegistry()

# General unit conversion function
# @brief convert_unit(from_unit, to_unit, radius=1, value=1)
# @remarks Receives the from_unit and to_unit and returns the multiplication factor needs to be multiplied to convert from_unit to to_unit
# @param[in] - from_unit = units need to be converted, to_unit = to unit that we need to convert, radius = in case of rpm(default = 1), value = (for future use)
# @return - multiplication factor needs to be multiplied to convert from_unit to to_unit
# @author Abdur Rahaman
def convert_unit(from_unit, to_unit, radius=1, value=1):
    if to_unit.lower() == 'rpm':
        value /= 2 * pi * radius
        to_unit = 'meter/min'
    elif to_unit.lower() == 'rps':
        value /= 2 * pi * radius
        to_unit = 'meter/sec'
    elif from_unit.lower() == 'rpm':
        value *= 2 * pi * radius
        from_unit = 'meter/min'
    elif from_unit.lower() == 'rps':
        value *= 2 * pi * radius
        from_unit = 'meter/sec'
    if from_unit.lower() == 'g' or from_unit.lower() == 'g-unit':  # edge cases covered for gravity
        if to_unit.lower() == 'm/s**2' or to_unit.lower() == 'meter/s**2' or to_unit.lower() == 'm/min**2' or to_unit.lower() == 'meter/min**2':
            from_unit = 'gravity'
    if to_unit.lower() == 'g' or to_unit.lower() == 'g-unit':  # edge case covered for gravity
        if from_unit.lower() == 'm/s**2' or from_unit.lower() == 'meter/s**2' or from_unit.lower() == 'm/min**2' or from_unit.lower() == 'meter/min**2':
            to_unit = 'gravity'
    if from_unit.lower() == 'nm':  # edge cases covered for nm to bar
        if to_unit.lower() == 'bar':
            from_unit = 'N/m**2'
    if to_unit.lower() == 'nm':  # edge case covered for bar to nm
        if from_unit.lower() == 'bar':
            to_unit = 'N/m**2'
    if from_unit.lower() == '°f' and to_unit.lower() == '°c':
        converted_value = '5 / 9 - 160/9'  # (value - 32) * 5 / 9
    elif from_unit.lower() == 'fahrenheit' and to_unit.lower() == 'celsius':
        converted_value = '5 / 9 - 160/9'  # (value - 32) * 5 / 9
    elif from_unit.lower() == '°c' and to_unit.lower() == '°f':
        converted_value = '9 / 5 + 32'
    elif from_unit.lower() == 'celsius' and to_unit.lower() == 'fahrenheit':
        converted_value = '9 / 5 + 32'
    else:
        quantity = value * pint.UnitRegistry()(from_unit)
        converted_quantity = quantity.to(to_unit)
        converted_value = converted_quantity.magnitude
    return converted_value


# getiing the system arguments and printing the result so that in VBA script we can extract it
args = sys.argv[1:]
if args[1].lower() == 'rpm' or args[2].lower() == 'rpm' or args[1].lower() == 'rps' or args[2].lower() == 'rps':
    result = convert_unit(args[1], args[2], float(args[3]))
else:
    result = convert_unit(args[1], args[2])
print(result, end='')

