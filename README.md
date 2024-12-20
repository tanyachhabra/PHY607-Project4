# Overview

This Python script provides a comprehensive tool for analyzing atomic properties and electronic configurations using the pymatgen library. The script includes two main classes: ElectronicConfiguration and AtomicProperties, which offer various methods to visualize and calculate atomic characteristics.

## Dependencies

- NumPy
- Matplotlib
- Pymatgen

## Installation

Pymatgen can be installed using the following command in bash:

```bash
pip install Pymatgen
```
## Features

### 1. Electronic Configuration Visualization

The ElectronicConfiguration class allows you to:

- Create a polar plot of an atom's electronic structure
- Visualize electron distribution across different shells
- Customize the plot with color and styling

### 2. Atomic Properties Calculation

The AtomicProperties class provides methods to:

- Calculate shielding constant (σ)
- Compute effective nuclear charge ($\text{Z}_{eff}$)
- Estimate atomic radius

## In-class exercise

1. Make a polar plot for any element with a stable oxidization state, for example: $\text{Fe}^{2+}$, $\text{Fe}^{3+}$, $\text{Mg}^{2+}$, $\text{Ca}^{2+}$, $\text{Na}^{+}$, $\text{Al}^{3+}$, etc

2. Choose the list of elements from the table provided and put it in the atoms array in the format:
   ```python
   atoms= ["Na", "Mg"]
   ```

   Write this list in the increasing value of atomic number. 

   Also write the corresponding observed values of atomic radii from the table. Use this to write the observed_radii list:

   ```python
   observed_radii= [2.17, 1.68]
   ```

3. Write the code to get the plot for atomic radii versus atomic number in the plot_atomic_number_versus_radii function. Plot for both the experimental and calculated values.
