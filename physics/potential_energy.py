from scipy.constants import g

def potential_energy(mass: float, height: float) -> float:
    # function will accept mass and height as parameters and return potential energy
    if mass < 0:
        # handling of negative values of mass
        raise ValueError("The mass of a body cannot be negative")
    if height < 0:
        # handling of negative values of height
        raise ValueError("The height above the ground cannot be negative")
    return mass * g * height


if __name__ == "__main__":
    from doctest import testmod

    testmod(name="potential_energy")
