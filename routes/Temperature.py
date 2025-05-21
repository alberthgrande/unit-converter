from flask import Blueprint, render_template, request, redirect, url_for

temperature_bp = Blueprint('temperature', __name__)


def convert_temperature(value, from_temperature, to_temperature):
    if from_temperature == to_temperature:
        return value

    # Convert from input temperature to Celsius
    if from_temperature == "fahrenheit":
        value = (value - 32) * 5/9
    elif from_temperature == "kelvin":
        value = value - 273.15
    # else from_unit == "celsius", no change needed

    # Convert from Celsius to target temperature
    if to_temperature == "fahrenheit":
        return (value * 9/5) + 32
    elif to_temperature == "kelvin":
        return value + 273.15
    elif to_temperature == "celsius":
        return value


@temperature_bp.route('/', methods=['GET', 'POST'])
def temperature():
    select_temperature = {
        "celsius": "celsius",
        "fahrenheit": "fahrenheit",
        "kelvin": "kelvin"
    }

    results = None

    if request.method == 'POST':
        try:
            value = float(request.form['temperature_value'])
            from_temperature = request.form['from_temperature']
            to_temperature = request.form['to_temperature']

            converted_value = convert_temperature(value, from_temperature, to_temperature)

            results = f'{value} {select_temperature[from_temperature].capitalize()} = {converted_value:.2f} {select_temperature[to_temperature].capitalize()}'
        except Exception as e:
            results = f'Error: {e}'

    return render_template('temperature.html', select_temperature=select_temperature, results=results, )