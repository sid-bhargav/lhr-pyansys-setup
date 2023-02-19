# CALCULATOR FOR Y+ IN METRIC

import argparse
import math

def calc(manual):
    yplus = 5
    velocity = 13 # m/s
    density = 1.2 # kg/m^3
    viscosity = 1.789e-5 # Pa s
    if manual:
        yplus = input("Target y+: ")
        # velocity = input("Velocity (m/s): ")
        # density = ("Density (kg/m^3): ")
        # viscosity = ("Viscosity (Pa s): ")
    length = input("Chord Length (in): ")

    length = float(length)*0.0254
    Re = (density*velocity*length)/(viscosity)
    friction_coeff = 0.058*(Re**-0.2)
    friction_vel = math.sqrt(0.5*friction_coeff*(velocity**2.0))
    height = (2.0*float(yplus)*viscosity)/(density*friction_vel)
    print("Height: ", height, "m")


if __name__ =="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--manual', '-m', default=False, action="store_true", help="Assign non-default values")
    args = parser.parse_args()

    calc(args.manual)