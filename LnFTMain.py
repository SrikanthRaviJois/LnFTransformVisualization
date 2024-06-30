from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt
import mpld3
import sympy as sp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('homepage.html')

# @app.route('/Fourier', methods=['GET', 'POST'])
# def Fourier():
#     return render_template('/FourierTransform/templates/index3.html')

# @app.route('/Laplace', methods=['GET', 'POST'])
# def Laplace():
#     return render_template('Laplace.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)  # Run the app on port 8000
