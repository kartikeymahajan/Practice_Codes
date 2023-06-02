'''4. Write to_celsius function that accepts a temperature in Fahrenheit as input and
returns a temperature in Celsius.'''

def to_celsius(temp):
    # (32°F − 32) × 5/9 = 0°C
    #  °C = [(°F-32)×5]/9.
    return f'{int(((temp-32)*5)/9)}°C'

obj = to_celsius(100)
print(obj)

