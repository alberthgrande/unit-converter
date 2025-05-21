from flask import Blueprint, render_template, request, redirect, url_for

weight_bp = Blueprint('weight', __name__)

# conversion factors for weight
conversion_factors = {
    "milligram": 0.001,
    "gram": 1,
    "kilogram": 1000,
    "ounce": 28.3495,
    "pound": 453.592
}


@weight_bp.route('/', methods=['GET', 'POST'])
def weight():
    select_weight = {
        "milligram": "milligram",
        "gram": "gram",
        "kilogram": "kilogram",
        "ounce": "ounce",
        "pound": "pound",
    }

    results = None

    if request.method == 'POST':
        try:
            value = float(request.form['weight_value'])
            from_weight = request.form['from_weight']
            to_weight = request.form['to_weight']

            # Corrected conversion
            value_in_grams = value * conversion_factors[from_weight]
            converted_weight = value_in_grams / conversion_factors[to_weight]

            results = f'{value} {select_weight[from_weight]} = {converted_weight:.2f} {select_weight[to_weight]}'
        except Exception as e:
            results = f'Error: {e}'

    return render_template('weight.html', select_weight=select_weight, results=results)
