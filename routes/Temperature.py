from flask import Blueprint, render_template, request, redirect, url_for

temperature_bp = Blueprint('temperature', __name__)


@temperature_bp.route('/', methods=['GET', 'POST'])
def temperature():
    return render_template('temperature.html')