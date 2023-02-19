# PARSER TO GET FINAL RESULTS (AVERAGED) FROM RSM FLUENT FILE

import statistics
import os
import argparse
import glob

def initialize(filename):
    with open(filename, 'r') as file:
        counter = -3
        for _ in file:
            counter += 1
        print("Number of Iterations:", counter, "\n")
        return counter

def parse(filename, maxiter, avgrange):
    with open(filename, 'r') as file:
        counter, name, values = 0, "", []
        for line in file:
            if counter == 0: 
                name = line
            counter += 1
            line_list = line.split()
            if str.isdigit(line_list[0]):
                if int(line_list[0]) in list(range(maxiter-avgrange, maxiter+1,1)) and len(line_list) == 2:
                    values.append(float(line_list[1]))
        print("{}: {}".format(name, str(statistics.mean(values))))


if __name__ =="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', '-s', default=os.path.join(os.getcwd(), 'dp0'), help="Path to \'[SIMNAME]_files\dp0\' directory")
    parser.add_argument('--value', '-v', default=False, nargs='+', type=int, help="Obtain values for discrete simulations based on cell number (can take more than one)")
    parser.add_argument('--range', '-r', nargs=2, type=int, default=False, help="Obtain results from inclusive range of sims based on cell number; takes 2 values")
    parser.add_argument('--avgfactor', '-a', default=0.1, type=float, help="Percentage factor defining number of values average is taken over based on maxiter")
    args = parser.parse_args()

    if args.value:
        values = [args.value] if type(args.value) is int else args.value
    elif args.range:
        values = [i for i in range(args.range[0], args.range[1]+1, 1)]

    for value in values:
        print(f"\n================\nSIMULATION FFF-{value}")
        files = glob.glob(os.path.join(args.source, 'FFF-'+str(value), 'Fluent', '*.out'))
        maxiter = initialize(files[0])
        avgrange = int(args.avgfactor*maxiter)

        for file in files:
            parse(file, maxiter, avgrange)
            
    print("================\n")