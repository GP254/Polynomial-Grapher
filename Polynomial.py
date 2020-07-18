import matplotlib.pyplot as plt
import numpy as np


class Polynomial:

    def __init__(self, degree, coeffs):
        self.degree = degree
        self.coeffs = coeffs

    def __str__(self):
        eqn = ""
        coeffs = self.coeffs
        curr_degree = self.degree

        def coeff_to_term(coeff, degree):
            term = ""
            if abs(coeff) != 1 or degree == 0:
                term += f'{coeff}'
            if degree == 1:
                term += 'x'
            elif degree > 1:
                term += f'x^{degree}'
            return term

        while curr_degree >= 0:
            curr_coeff = coeffs[-curr_degree-1]
            if curr_coeff == 0:
                curr_degree -= 1
                continue
            if eqn == "":
                eqn += f'{coeff_to_term(curr_coeff, curr_degree)}'
            else:
                if curr_coeff > 0:
                    eqn += f' + {coeff_to_term(curr_coeff, curr_degree)}'
                else:
                    eqn += f' - {coeff_to_term(abs(curr_coeff), curr_degree)}'
            curr_degree -= 1
        if eqn == "":
            eqn = "0"
        return eqn

    def graph(self, x_range, data_points, title):
        x1 = x_range[0]
        x2 = x_range[1]
        x_values = np.linspace(x1, x2, data_points)
        y_values = np.zeros(len(x_values))

        curr_degree = self.degree
        while curr_degree >= 0:
            curr_coeff = self.coeffs[-curr_degree - 1]
            y_values += curr_coeff * (x_values ** curr_degree)
            curr_degree -= 1

        plt.title(title)
        plt.plot(x_values, y_values)
        plt.show()

    def derivative(self):
        new_coeff = []
        curr_degree = self.degree
        while curr_degree > 0:
            new_coeff.append(self.coeffs[-curr_degree-1]*curr_degree)
            curr_degree -= 1
        new_deg = self.degree - 1
        if len(new_coeff) == 0:
            new_coeff = [0]
        return Polynomial(new_deg, new_coeff)

    def second_derivative(self):
        first_deriv = self.derivative()
        second_deriv = first_deriv.derivative()
        return second_deriv

    def y_int(self):
        return self.coeffs[-1]
