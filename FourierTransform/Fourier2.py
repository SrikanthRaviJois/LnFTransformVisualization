from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt
import mpld3
import sympy as sp

app = Flask(__name__)

# Define default function
default_function = "sin(2*pi*x) + sin(pi*x) + sin(5*pi*x) + sin(2.5*pi*x) + sin(3.33*pi*x)"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        func_str = request.form['function']
    else:
        func_str = default_function
    
    # Generate x values
    N = 1000            # Number of points
    L = 150.0           # Length of interval
    dx = L / N          # Sampling interval
    x = np.linspace(-L/2, L/2, N, endpoint=False)  # x values

    # Convert string function to a lambda function
    x_sym = sp.symbols('x')
    try:
        func = sp.lambdify(x_sym, sp.sympify(func_str), 'numpy')
        y = func(x)
    except Exception as e:
        return render_template('index3.html', plot_html="", error=f"Error in function: {e}")

    # Compute Fourier Transform manually
    def manual_dft(y):
        N = len(y)
        n = np.arange(N)
        k = n.reshape((N, 1))
        M = np.exp(-2j * np.pi * k * n / N)
        return np.dot(M, y)

    fourier = manual_dft(y)
    
    # Shift the zero-frequency component to the center
    fourier = np.fft.fftshift(fourier)

    # Frequencies for plotting the Fourier transform
    freq = np.fft.fftshift(np.fft.fftfreq(N, d=dx))

    # Create the plot
    fig, axs = plt.subplots(2, 1, figsize=(10, 6))

    axs[0].plot(x, y, label='Original Function')
    axs[0].set_title('Original Function')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('Amplitude')
    axs[0].legend()

    axs[1].plot(freq, np.abs(fourier), label='Fourier Transform')
    axs[1].set_title('Fourier Transform of Function')
    axs[1].set_xlabel('Frequency')
    axs[1].set_ylabel('Amplitude')
    axs[1].legend()

    plt.tight_layout()

    # Convert plot to HTML
    plot_html = mpld3.fig_to_html(fig)
    return render_template('index3.html', plot_html=plot_html, error=None)

if __name__ == '__main__':
    app.run(debug=True, port=8000)  # Run the app on port 8000
