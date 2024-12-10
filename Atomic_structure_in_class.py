#importing all the packages
import numpy as np
import matplotlib.pyplot as plt
from pymatgen.core.periodic_table import Element
from pymatgen.core.periodic_table import Species

#demonstration of pymatgen
class ElectronicConfiguration():
    def __init__(self, symbol, oxidation_state=0):
        self.symbol = symbol
        self.oxidation_state = oxidation_state
        self.element = Species(symbol, oxidation_state= oxidation_state)
        self.elec_structure = sorted(self.element.full_electronic_structure, key=lambda x: x[0])
        self.Z= Element(symbol).number
   
    def plot_initial_configuration(self):
        plt.figure(figsize=(10, 10))
        ax = plt.subplot(polar=True)
        ax.set_facecolor("#d5de9c")
        
        rticks = []
        rlabels = []
        print(self.elec_structure)
        
        for i, shell in enumerate(self.elec_structure):
            
            # Draw the shell
            r = 0.5 * (i + 1)
            rad = [r] * 1000
            theta = [2 * np.pi * j / 1000 for j in range(1000)]
            ax.plot(theta, rad, "k-", lw=1)
            
            # Draw the electrons
            rad = [r] * shell[2]
            theta = [2 * np.pi * j / shell[2] for j in range(shell[2])]
            ax.plot(theta, rad, "ro", markersize=15)
            
            rticks.append(r)
            rlabels.append(f"{shell[0]}{shell[1]}")
        
        ax.set_rmax(r + 0.5)
        ax.set_thetagrids([0, 90, 180, 270], [""] * 4, color="k")
        ax.set_rgrids(rticks, rlabels)
        ax.set_title(f"Initial Electronic Structure of {self.symbol}", fontsize=20)
        plt.grid(True)
        plt.show()


# class for atomic properties calculation

class AtomicProperties():
    def __init__(self, symbol, oxidation_state=0):
        self.symbol = symbol
        self.oxidation_state = oxidation_state
        self.element = Species(symbol, oxidation_state= oxidation_state)
        self.elec_structure = sorted(self.element.full_electronic_structure, key=lambda x: x[0])
        self.Z= Element(symbol).number
   
    
    def sigma(self):
        """
        Calculate the shielding constant (sigma) based on the electron configuration.
        """
        sigma = -0.35
        N, last_orbital, electrons = self.elec_structure[-1]
        for i in range(len(self.elec_structure) - 1, -1, -1):
            n, orbital, electrons = self.elec_structure[i]

            if last_orbital in ['s', 'p']:
                if n == N:
                    sigma += electrons * 0.35
                if n == N - 1:
                    sigma += electrons * 0.85
                if n <= N - 2:
                    sigma += electrons * 1
                if n > N:
                    continue
            else:
                if n == N and orbital == last_orbital:
                    sigma += 0.35 * electrons
                elif n > N:
                    continue
                else:
                    sigma += 1 * electrons

        return sigma

    def Z_eff(self):
        """
        Calculate the effective nuclear charge (Z_eff).
        """
        sigma_value = self.sigma()
        Zeff = self.Z - sigma_value
        return Zeff

    def compute_radius(self):
        """
        Calculate the atomic radius based on the effective nuclear charge.
        """
        Zeff = self.Z_eff()
        N, _, _ = self.elec_structure[-1]
        radius = (N**2) * 0.529 / Zeff
        return radius

def plot_electronic_configuration(atom,oxidation_state):
    config =ElectronicConfiguration(symbol=atom, oxidation_state=oxidation_state)
    config.plot_initial_configuration()

def plot_atomic_number_versus_radii(atoms, observed_radii, oxidation_state=0 ):
    """
    Calculate and plot atomic numbers versus radii for a given list of atoms.
    """
    radii = []
    atomic_numbers = []

    for atom in atoms:
        exercise = AtomicProperties(symbol=atom, oxidation_state=oxidation_state)
        radius = exercise.compute_radius()
        radii.append(radius)
        atomic_numbers.append(exercise.Z)

    # Missing part: Plot the atomic radius versus atomic number for the elements given in the list "atoms". Also plot the experimental values to compare.
    

    return radii, atomic_numbers

# Example Usage
if __name__ == "__main__":
    plot_electronic_configuration() # missing element and oxidation state
    atoms = [] # Missing part: choose your own list of atoms
    observed_radii =[] # Missing part: fill in the corresponding observed atomic radius from the given table
    radii, atomic_numbers = plot_atomic_number_versus_radii(atoms,observed_radii, 0)
    print("Radii:", radii)
    print("Atomic Numbers:", atomic_numbers)

        