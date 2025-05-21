from flask import Blueprint, render_template, request, redirect, url_for

length_bp = Blueprint('length', __name__)

# conversion factors to length
conversion_factors = {
    "mm": 0.001,       # 1 millimeter = 0.001 meters
    "cm": 0.01,        # 1 centimeter = 0.01 meters
    "m": 1,            # base unit
    "km": 1000,        # 1 kilometer = 1000 meters
    "inch": 0.0254,    # 1 inch = 0.0254 meters
    "foot": 0.3048,    # 1 foot = 0.3048 meters
    "yard": 0.9144,    # 1 yard = 0.9144 meters
    "mile": 1609.34    # 1 mile = 1609.34 meters
}


@length_bp.route('/', methods=['GET', 'POST'])
def length():
    select_length = {
        "mm": "millimeter",
        "cm": "centimeter",
        "m": "meter",
        "km": "kilometer",
        "inch": "inch",
        "foot": "foot",
        "yard": "yard",
        "mile": "mile"
    }

    results = None

    if request.method == 'POST':
        try:
            value = float(request.form['length_value'])
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']

            # Convert to meters, then to target unit
            value_in_meters = value * conversion_factors[from_unit]
            converted_value = value_in_meters / conversion_factors[to_unit]

            results = f"{value} {select_length[from_unit]} = {converted_value:.4f} {select_length[to_unit]}"
        except Exception as e:
            results = f"Error: {e}"

    return render_template('index.html', select_length=select_length, results=results)
