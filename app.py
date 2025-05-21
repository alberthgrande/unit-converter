from flask import Flask, render_template
from routes.Length import length_bp
from routes.Temperature import temperature_bp
from routes.Weight import weight_bp


app = Flask(__name__)

# register the blueprint
app.register_blueprint(length_bp)
app.register_blueprint(temperature_bp, url_prefix='/temperature')
app.register_blueprint(weight_bp, url_prefix='/weight')

if __name__ == "__main__":
    app.run(debug=True, port=3000)
