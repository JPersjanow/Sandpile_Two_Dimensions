from random import randint

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as c

from matplotlib import animation


class Sandpile:
    """
    Class representing sandpile model for Self-Organized Criticality

    :params
    numer_radial = number representing r values
    number_angles = numer representing fi values
    array = array representing sandpile with r and fi
    max_peak = maximum sand grains on position [r][fi]
    """

    #initialization of sandpile
    def __init__(self, number_radial, number_angles, max_peak):
        self.number_radial = number_radial
        self.number_angles = number_angles
        self.array = np.zeros((self.number_radial, self.number_angles))
        self.max_peak = max_peak
        self.topple_count = 0
        self.mass_count = 0

        self.angles_array = np.linspace(0, 2 * np.pi, number_angles)
        self.radial_array = np.linspace(0, number_radial, number_radial + 1)

    def add_grain(self, radial_position):
        self.mass_count += 1
        self.array[radial_position][randint(0, self.number_angles - 1)] += 1

    def topple(self, radial_position, angle_position):
        self.topple_count += 1
        self.array[radial_position][angle_position] -= 3

        #one grain topples downwards
        if radial_position < self.number_radial - 1:
            self.array[radial_position + 1][angle_position] += 1

        #one grain topples LEFT

        if angle_position == 0:
            self.array[radial_position][self.number_angles - 1] += 1
        else:
            self.array[radial_position][angle_position - 1] += 1

        #one grain topples RIGHT

        if angle_position == self.number_angles - 1:
            self.array[radial_position][0] += 1
        else:
            self.array[radial_position][angle_position + 1] += 1

    def check_pile(self):
        for r in range(0, self.number_radial, 1):
            for fi in range(0, self.number_angles, 1):

                if self.array[r][fi] < self.max_peak:
                    self.array[r][fi] = self.array[r][fi]

                else:
                    self.topple(r, fi)

    def simulate(self, number_of_simulations):

        for i in range(0, number_of_simulations, 1):
            self.add_grain(0)
            self.check_pile()
            print(self.array)

    def update(self):

        self.add_grain(0)
        self.check_pile()

    def plot(self):
        # A, B = np.meshgrid(self.angles_array, self.radial_array)

        fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
        cb = ax.pcolormesh(self.angles_array, self.radial_array, self.array, edgecolors='k', linewidths=1)
        ax.set_yticks([])
        ax.set_theta_zero_location("N")
        ax.set_theta_direction(-1)
        plt.colorbar(cb, orientation='vertical')
        plt.show()


SANDPILE = Sandpile(5, 36, 5)
SANDPILE.simulate(1000)
SANDPILE.plot()
SANDPILE.simulate(100)
SANDPILE.plot()