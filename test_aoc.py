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
import day14
import day15
import day16
import day17
import day18
import day19
import day20
import day21
import day22


def test_day01():
    input="""3   4
4   3
2   5
1   3
3   9
3   3
"""
    a,b = day01.run(input)
    assert a == 11
    assert b == 31

def test_day02():
    input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
    a,b = day02.run(input)
    assert a == 2
    assert b == 4

def test_day03():
    input_a = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    input_b = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    a,_ = day03.run(input_a)
    _,b = day03.run(input_b)

    assert a == 161
    assert b == 48


def test_day04():
    input="""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""
    a,b = day04.run(input)
    assert a == 18
    assert b == 9

def test_day05():
    input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
    a,b = day05.run(input)
    assert a == 143
    assert b == 123

def test_day06():
    input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
    a,b = day06.run(input)
    assert a == 41
    assert b == 6

def test_day07():
    input="""190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
    a,b = day07.run(input)
    assert a == 3749
    assert b == 11387

def test_day08():
    input="""............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
    a,b = day08.run(input)
    assert a == 14
    assert b == 34

def test_day09():
    input="2333133121414131402"
    a,b = day09.run(input)
    assert a == 1928
    assert b == 2858

def test_day10():
    input="""89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""
    a,b = day10.run(input)
    assert a == 36
    assert b == 81

def test_day11():
    input="125 17"
    a,b = day11.run(input)
    assert a == 55312
    assert b == 65601038650482

def test_day12():
    input="""RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""
    a,b = day12.run(input)
    assert a == 1930
    assert b == 1206

def test_day13():
    input="""Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""
    a,b = day13.run(input)
    assert a == 480
    assert b == 875318608908

def test_day14():
    input="""p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""
    data = day14.parse(input)
    a = day14.part_a(data,11,7)
    assert a == 12

def test_day15():
    input="""##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""
    a,b = day15.run(input)
    assert a == 10092
    assert b == 9021

def test_day16():
    input="""###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""
    a,b = day16.run(input)
    assert a == 7036
    assert b == 45

def test_day17():
    input="""Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""
    a,b = day17.run(input,b=False)
    assert a == "4,6,3,5,6,3,5,2,1,0"
    # assert b == 117440


def test_day18():
    input = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
"""
    a,b = day18.run(input,d=7,c=12)
    assert a == 22
    assert b == "6,1"

def test_day19():
    input="""r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""
    a,b = day19.run(input)
    assert a == 6
    assert b == 16

def test_day20():
    input="""###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""
    a,b = day20.run(input,ev=20)
    assert a == 5
    # assert b == 16


def test_day21():
    input="""029A
980A
179A
456A
379A
"""
    a,b = day21.run(input)
    assert a == 126384
    # assert b == 
# def test_dayXX():
#     input="""
# """
#     a,b = dayXX.run(input)
#     assert a == 
#     assert b == 