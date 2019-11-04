from random import randint

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter



class Sandpile:
    """
    Class representing sandpile model for Self-Organized Criticality

    variables
    number_radial = number representing r values (must be odd number)
    number_angles = numer representing thera values
    array = array representing sandpile with r and theta
    max_peak = maximum sand grains on position [r][theta]
    topple_count = sums how many topples occured during simulation
    mass_count = sums whole mass gathered during simulation
    mass_fallen_count = sums mass that was 'thrown" out outside disk
    mass_left_count = sums mass 'left' on disk
    mass_when_iteration = array consisting of mass during every iteration
    when_topple = array consisting of iteration when topple occured

    angles_array = angles array for plotting (required by matplotlib)
    radial_array = radial array for plotting (required by matplotlib)
    """

    #initialization of sandpile
    def __init__(self, number_radial, number_angles, max_peak):
        """
        Initialisation function for Sandpile class
        :param number_radial:
        :param number_angles:
        :param max_peak:
        """
        self.number_radial = number_radial
        self.number_angles = number_angles
        self.array = np.zeros((self.number_radial, self.number_angles))
        self.max_peak = max_peak
        self.topple_count = 0
        self.mass_count = 0
        self.mass_fallen_count = 0
        self.mass_left_count = 0
        self.mass_when_iteration = []
        self.when_topple = []

        self.number_of_simulations = 0

        self.angles_array = np.linspace(0, 2 * np.pi, number_angles + 1)
        self.radial_array = np.linspace(0, number_radial, number_radial + 1)

    def add_grain(self, radial_position):
        """
        Adds grain to chosen radial position and random angle position
        :param radial_position:
        :return:
        """

        self.mass_count += 1
        self.array[radial_position][randint(0, self.number_angles - 1)] += 1

    def topple(self, radial_position, angle_position, iteration):
        """
        Topple function, gathers data, strips current sandpile location, distributes taken grains to 3 nearby locations
        :param radial_position:
        :param angle_position:
        :param iteration:
        :return:
        """
        #gather data
        self.topple_count += 1
        self.when_topple.append(iteration)
        #execute topple
        taken_grains = 3
        self.array[radial_position][angle_position] -= taken_grains

        #one grain topples downwards
        if radial_position < self.number_radial - 1:
            self.array[radial_position + 1][angle_position] += 1
        else:
            self.mass_fallen_count += 1

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

    def check_pile(self, iteration):
        """
        Function checking every sandpile location, if grains of sand exceed max topple starts
        :param iteration:
        :return:
        """

        for r in range(0, self.number_radial, 1):
            for theta in range(0, self.number_angles, 1):

                if self.array[r][theta] < self.max_peak:
                    self.array[r][theta] = self.array[r][theta]

                else:
                    self.topple(r, theta, iteration)

    def simulate(self, number_of_simulations):
        """
        Main function, starts sandpile simulation
        :param number_of_simulations:
        :return:
        """
        self.number_of_simulations = number_of_simulations

        for iteration_num in range(0, number_of_simulations, 1):
            self.add_grain(0)
            self.check_pile(iteration_num)
            self.mass_when_iteration.append(self.mass_count - self.mass_fallen_count)
            print(self.array)

    def count_mass_left(self):
        """
        Function for counting how much mass is left on disk
        :return:
        """
        self.mass_left_count = int(np.sum(self.array))

    def plot(self, type='sandpile'):
        """
        Plotting function
        :param type:
        :return:
        """

        #plot sandpile after simulation
        if type == 'sandpile':
            fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
            cb = ax.pcolormesh(self.angles_array, self.radial_array, self.array, edgecolors='k', linewidths=1)
            ax.set_yticks([])
            ax.set_theta_zero_location('N')
            ax.set_theta_direction(-1)
            plt.colorbar(cb, orientation='vertical')
            plt.show()

        #plot iteration / mass of left pile on plate
        if type == 'mass':
            simulation_array = []
            for i in range(0, self.number_of_simulations, 1):
                simulation_array.append(i)

            plt.plot(simulation_array, self.mass_when_iteration)
            plt.title("Left Mass on pile during iterations")
            plt.xlabel("Iteration")
            plt.ylabel("Mass of Pile on plate")
            plt.show()


        #plot iteration / topple
        if type == 'topple':
            lists = sorted(Counter(self.when_topple).items())
            when_topple, topple_count = zip(*lists)

            plt.bar(when_topple, topple_count)
            plt.xlabel('Iteration Number')
            plt.ylabel('Topple Count')
            plt.show()

    def analyze_data(self):
        """
        Function for analyzing data and executes plotting.
        :return:
        """
        data = {"Topple Count": self.topple_count, "Fallen mass": self.mass_fallen_count}
        print(data)

        self.plot()
        self.plot(type='mass')
        self.plot(type='topple')



SANDPILE = Sandpile(5, 36, 5)
SANDPILE.simulate(1000)
SANDPILE.analyze_data()

