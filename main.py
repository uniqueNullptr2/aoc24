import argparse
import day01
import day02
import day03
import day04
import day05
import day06
import day07
import day08
import day09
import day10
import day11
import day12
import day13
from os.path import join
DAYS = [
        day01.run,
        day02.run,
        day03.run,
        day04.run,
        day05.run,
        day06.run,
        day07.run,
        day08.run,
        day09.run,
        day10.run,
        day11.run,
        day12.run,
        day13.run,
    ]
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--day', default=len(DAYS)-1, type=int)
    parser.add_argument('-i', '--input', default=None, help="name of input file. defaults to dayXX.txt where x is the zeropadded number of day")
    parser.add_argument('-D', '--dir', default="./inputs", help="Input directory")
    parser.add_argument('-a', '--all', action="store_true", help="If used will run all days regardless of the other inputs for days. in this case a file by the name of dayXX.txt should exist for all days.")
    args = parser.parse_args()
    return args


def main():
    
    args = parse_args()
    
    if args.all :
        for i, day in enumerate(DAYS):
            file = f"day{i+1:02}.txt"
            path = join(args.dir, file)
            resa, resb = day(path)
            print(f"Day {i+1:02}: A: {resa}, B: {resb}")
    else:
        if args.day > len(DAYS):
            print("that day does not exist yet")
            exit(-1)
        
        file = args.input
        if file is None:
            file = f"day{args.day:02}.txt"
        path = join(args.dir, file)
        resa, resb = DAYS[args.day-1](path)
        print(f"Day {args.day:02}: A: {resa}, B: {resb}")
    



if __name__ == "__main__":
    main()