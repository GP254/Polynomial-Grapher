from PyInquirer import prompt
from Polynomial import *
import constants

if __name__ == '__main__':

    # Introduction/rules
    print(constants.WELCOME_SCRIPT)

    # Selection Configuration To Start Program
    entry = prompt(constants.START_PROMPT)
    start = entry['Start']

    # Start program When Hit Enter
    while start:
        poly_deg = None
        while True:
            poly_deg = int(input('Enter the degree of the polynomial:'))
            if poly_deg < 0:
                print("***********ERROR DEGREE MUST BE POSITIVE INTEGER***********")
            else:
                break

        # Create temporary polynomial equation without coefficients
        terms = []
        curr_degree = poly_deg
        while curr_degree >= 0:
            terms.append(f'___x^{curr_degree}')
            curr_degree -= 1
        print(' + '.join(terms))

        # Ask user to input coefficients
        print('\nEnter The Corresponding Coefficient For Each Of The Following Terms')
        coeffs = []
        for term in terms:
            coeff = input(f'{term}:')
            if coeff.count('.') > 0:
                coeff = float(coeff)
            else:
                coeff = int(coeff)
            coeffs.append(coeff)

        # assigning variables to functions
        poly_func = Polynomial(poly_deg, coeffs)
        deriv_func = poly_func.derivative()
        sec_deriv_func = deriv_func.derivative()

        # Selection Configuration For Funcitions/Exiting Program
        while start:
            selection = prompt(constants.OPTIONS_PROMPT)['functions']
            if selection == 'Graph Polynomial':
                poly_func.graph([-100, 100], 10000, f'{poly_func}')
            elif selection == 'Graph Derivative':
                deriv_func.graph([-100, 100], 10000, f'{deriv_func}')
            elif selection == 'Graph Second Derivative':
                sec_deriv_func.graph([-100, 100], 10000, f'{sec_deriv_func}')
            elif selection == 'New Polynomial':
                break
            else:
                start = False

print("Thank You For Using This Program")
