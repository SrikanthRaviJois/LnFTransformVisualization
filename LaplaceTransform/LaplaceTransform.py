from flask import Flask, render_template, jsonify, request
import numpy as np
from scipy.integrate import quad
from sympy import symbols, lambdify, Heaviside

app = Flask(__name__)

# Define the numerical Laplace transform function
def laplace_transform_num(f, s, upper_limit=np.inf):
    integrand = lambda t: np.exp(-s * t) * f(t)
    result, _ = quad(integrand, 0, upper_limit)
    return result

# Route to serve index.html
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle AJAX request for updated plot data
@app.route('/update_plot', methods=['POST'])
def update_plot():
    # Get function expression from POST request
    data = request.json
    function_expression = data['functionExpression']

    # Define symbols and create the function f(t)
    t = symbols('t')
    heaviside = Heaviside(t)
    f_sym = lambdify(t, function_expression, modules=['numpy', {'Heaviside': heaviside}])

    # Generate values for t and s and compute f(t) and F(s) for these values
    t_vals = np.linspace(0, 100, 400)
    f_vals = f_sym(t_vals)
    
    s_vals = np.linspace(0.1, 100, 400)
    F_s_vals = [laplace_transform_num(f_sym, s) for s in s_vals]

    # Prepare data to send back as JSON
    response_data = {
        't_vals': t_vals.tolist(),
        'f_vals': f_vals.tolist(),
        's_vals': s_vals.tolist(),
        'F_s_vals_real': [result.real for result in F_s_vals],
        'F_s_vals_imag': [result.imag for result in F_s_vals]
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
