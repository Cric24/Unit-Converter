from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Conversion functions
def convert_length(value, from_unit, to_unit):
    conversions = {
        'meters_to_kilometers': value / 1000,
        'kilometers_to_meters': value * 1000,
        'meters_to_miles': value * 0.000621371,
        'miles_to_meters': value / 0.000621371,
        'meters_to_feet': value * 3.28084,
        'feet_to_meters': value / 3.28084,
        'meters_to_inches': value * 39.3701,
        'inches_to_meters': value / 39.3701,
        'kilometers_to_miles': value * 0.621371,
        'miles_to_kilometers': value / 0.621371,
        'feet_to_inches': value * 12,
        'inches_to_feet': value / 12,
        'miles_to_inches': value * 63360,
        'inches_to_miles': value / 63360,
        'kilometers_to_feet': value * 3280.84,
        'feet_to_kilometers': value / 3280.84,
        'kilometers_to_inches': value * 39370.1,
        'inches_to_kilometers': value / 39370.1,
        'miles_to_feet': value * 5280,
        'feet_to_miles': value / 5280,
        'yards_to_meters': value * 0.9144,
        'meters_to_yards': value / 0.9144,
        'yards_to_feet': value * 3,
        'feet_to_yards': value / 3,
        'yards_to_inches': value * 36,
        'inches_to_yards': value / 36,
    }
    key = f"{from_unit}_to_{to_unit}"
    return conversions.get(key, "Invalid conversion")


def convert_weight(value, from_unit, to_unit):
    conversions = {
        'grams_to_kilograms': value / 1000,
        'kilograms_to_grams': value * 1000,
        'grams_to_pounds': value * 0.00220462,
        'pounds_to_grams': value / 0.00220462,
        'kilograms_to_pounds': value * 2.20462,
        'pounds_to_kilograms': value / 2.20462,
        'grams_to_ounces': value * 0.035274,
        'ounces_to_grams': value / 0.035274,
        'kilograms_to_ounces': value * 35.274,
        'ounces_to_kilograms': value / 35.274,
        'pounds_to_ounces': value * 16,
        'ounces_to_pounds': value / 16,
    }
    key = f"{from_unit}_to_{to_unit}"
    return conversions.get(key, "Invalid conversion")



def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        return value * 9/5 + 32
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        return (value - 32) * 5/9
    elif from_unit == 'celsius' and to_unit == 'kelvin':
        return value + 273.15
    elif from_unit == 'kelvin' and to_unit == 'celsius':
        return value - 273.15
    elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
        return (value - 273.15) * 9/5 + 32
    return "Invalid conversion"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['GET'])
def convert():
    unit_type = request.args.get('unit_type')
    value = float(request.args.get('value'))
    from_unit = request.args.get('from_unit')
    to_unit = request.args.get('to_unit')

    if unit_type == 'length':
        result = convert_length(value, from_unit, to_unit)
    elif unit_type == 'weight':
        result = convert_weight(value, from_unit, to_unit)
    elif unit_type == 'temperature':
        result = convert_temperature(value, from_unit, to_unit)
    else:
        result = "Invalid unit type"
    
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
