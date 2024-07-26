VISUALISING FOURIER AND LAPLACE TRANSFORM
This project helps visualise complex transforms like fourier transform and laplace transform using simple python libraries.
Libraries used in this project: 
Flask - Used for creating User Interface (with the help of HTML)
Numpy - Used for computing discrete fourier transform and also in laplace transform calculations 
MatplotLib - Used to plot graphs 
Scipy - Used to compute the symbolic Integration in Laplace transform
mpld3 - Converts the python plots to HTML plots 
sympy - Used throughout the program in the various steps to compute the transforms

DESCRIPTION OF CODE

1. FOURIER TRANSFORM
In this project we compute the Discrete Fourier Transform or DFT of a given function. This is done by computing the fourier transform of the signal at large number or points and then plotting them to get a very accurate representation of its fourier transform 
we compute the complex exponential part of the transform separately and then take the dot product of this with the function value at the point to get the value of fourier transform.
Then we improve visualisation using various features of matplotlib

2. LAPLACE TRANSFORM
To compute the integral in the laplace transform we use the quad function present in the scipy library
Then we use np.linspace to store values related to plotting the graphs
We also construct the unit step function using the heaviside feature present in sympy.
