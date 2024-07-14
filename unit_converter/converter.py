class UnitConverter:
    def __init__(self):
        self.conversion_factors = {
            'meters_to_feet': 3.28084,
            'feet_to_meters': 0.3048,
            'liters_to_gallons': 0.264172,
            'gallons_to_liters': 3.78541,
            'kilograms_to_pounds': 2.20462,
            'pounds_to_kilograms': 0.453592,
            'celsius_to_fahrenheit': (lambda c: (c * 9/5) + 32),
            'fahrenheit_to_celsius': (lambda f: (f - 32) * 5/9)
        }
    
    def convert(self, value, from_unit, to_unit):
        key = f'{from_unit}_to_{to_unit}'
        
        if key in self.conversion_factors:
            conversion = self.conversion_factors[key]
            if callable(conversion):
                return conversion(value)
            else:
                return value * conversion
        else:
            raise ValueError(f'Unsupported conversion: {from_unit} to {to_unit}')

