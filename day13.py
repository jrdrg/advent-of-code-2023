import util
import functools

example_input = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""

input_str = """
...##....
.#.##.#..
.#....#..
.##..##..
...##....
..####.##
#..##..##

##...##..
.##.#..#.
.#.......
...#.##.#
##..#..#.
.##..##..
.#...##..
#.#######
....####.
..##.##.#
..##.##.#
....####.
#.#######
.#...##..
.##..##..
#...#..#.
...#.##.#

...#...##...###
##.#.##.#..#.##
####.##.#..#.##
#.#.##.###.#.##
#...##.##...#.#
##..#.###...#..
#...####.###...
#.#####...##.##
#.#####...##.##
#...####.###...
##..#.###...#..
#...##.##...#.#
#.#.##.###.#.##
####.##.#..#.##
##.#.##.#..#.##

.....#.
###.###
##.#.##
..#..##
..###..
..###..
..#..##
##.#.##
###.###
.....##
###..#.
..#..##
##.####

....#....##....
.##..##.####.##
#..#.#...##...#
.##.####....###
#..#.##.####.##
#..###.#.##.#.#
.##.##.##..####

..##..##..#.#.#
.####......#.#.
.#.#.###...#..#
.##.#..##.....#
..#.#.##..###.#
..#.#.##..###.#
.##.#..##.....#
.#.#.###...#..#
.####......#.#.
..##..##..#.#.#
#...#..#...#...
.#.#.##..##...#
.#.#.##..###..#

#...##...#.#.##.#
#...##...#.#.####
#.##..##.##.##.#.
............###.#
....##.....###.##
#..#..#..#.##....
#.#....#.#..##.##
..######...####.#
#.#....#.#..#####
.#.####.#.#.###..
.##.##.##..#...##

##.##....##.##...
##....##....##.##
#.##..##..##.##..
.##.#.##.#.##.#..
..##.....###...##
####.#..#.####.##
.#..........#....
#####.##.######..
#..#.####.#..#...

#.##..###.#..
.#...###...#.
##...####....
####..#.#.#..
#.....##..###
#.....##..###
####..#.#.#..
##...####..#.
.#...###...#.
#.##..###.#..
###.#.####..#
.##.#.#...###
#.##.######.#
#..#.......#.
#..#.......#.

###...##...##
...#..#####.#
###.##.#.....
..#...#...###
..##.###.....
....#...#...#
#####...##.##
....#.##.####
....#.##.##.#

..##..###...#....
##..#######...###
##..###.......#.#
..##..#.#....####
########...###...
.####........#...
.####.#..##...###
.#..#...###.#.###
.####.#.###.##...
#.##.#..####.#...
#.##.#..##...#...

#.#....#.##
..#....#...
..#....#...
#.#....#.##
##......##.
.#.####.#..
####.#####.

...##...#..#.
########...#.
.######..#...
..#..#.....##
#.#..#.#####.
##....##.####
..####...###.
#.#..#.##.#.#
#......#.###.
.#.##.#.####.
.#.##.#.####.
#......#.###.
#.#..#.#..#.#

##....#.##.##.##.
####......#..#...
#...###..######..
#...#.##..#..#..#
.#.##.#.########.
.#.##.#.########.
....#.##..#..#..#

###..##.#
##.#..##.
##..#....
....#....
..#......
..##..##.
##.#.#..#

.....#...#.
..##...#...
##..###...#
.#..#.#.###
#.##.#.##..
.#..#.##.##
#######.##.
.........##
..##....#.#
.......#..#
.#..#.####.
#....#####.
#.##.#..#.#
#.##.#..#.#
#....#####.
.#..#.####.
.......#..#

#.####.
#.####.
...#...
##...##
....#..
#....#.
.#..#..
#..#.##
#.#....
.#..#.#
.#..#.#
#.#...#
#..#.##

.##..##..#.##
#..#..#..#.##
....####.####
....###.##.##
.####..##.###
.....#...#.##
#..##.##...##
####.###.....
.##..#....###
#..#..#..####
.##.#####.#..
......###.###
#..#####..#..
#..##.....###
#..#..#.#..##

.###..##..###
.#.#.#..#.#.#
....##..##...
....##..##...
##.#.#..#.#.#
.###..##..###
###.#....#.##

##.########.##.
###.#.#..#.####
..#...##...#..#
###.##..##.###.
#.#.##..##.#.#.
.##.#.##.#.##.#
.##.#.##.#.##.#

.#..##.
..#..##
###.###
###.###
..#..##
.#..##.
.#.##..
#...##.
#...##.
.#.##..
.#..##.
#.#..##
###.###

......#.#.#.#
......#.#.#.#
#..##...##..#
#..##..##..#.
..#.##.##.##.
#..##..#..#.#
#..#.#..#####
#..#.##.##..#
....####..##.
.##..#..##.#.
####.#...##..
.....#.####.#
#..#....###..

.#...#.#...##..
#....#.#.......
..##.#.....##..
####.###..####.
.#.#.#...#.....
##...###.......
..##.#.########
.####.....#..#.
.#.#..##.......
##.#..#.##.##.#
..#....#.#....#
..#....#.#....#
##.#..#.##.##.#
.#.#..##.......
.####.....#..#.
..##.#.########
##...###.......

.......#.#.####
.......#.#.####
..##..####.##.#
#...####.####.#
##..##.####.##.
#....##.#.###..
.####..#...#.#.
#.##.#.##.##..#
..##.......#.#.
#....##..#..#.#
..##...##..##.#
#######.#....##
#.##.#..##.#.#.

....##..#
..#.##..#
..#.###.#
#......##
...##....
.##..#.#.
#.#.#....
#..#....#
.##.###..
###.#.##.
###.#.##.

######.
.###...
##.##.#
#..##..
#..##..
##.##.#
.###...
######.
...#...
..##.##
##...##
##....#
..##.##
...#...
######.
.###...
##.##.#

....###.#..
.##.##.####
.##.##.####
....#####..
######.#..#
#####..#.#.
....##...#.
.##.##.#..#
.##.##..#.#
#..#.#.#.##
.##..###.##
....###...#
.##.##.#...
####.#.#.#.
#..#.##..#.

##..#.##.#.#..#..
..#....#..##.##.#
...##...####..###
###..#.#..#.##.##
###..#....#.##.##
...##...####..###
..#....#..##.##.#
##..#.##.#.#..#..
..#.##..#.#..#..#
..##..#...#....##
..####..##.....##

.......####..#..#
.##.#....###..##.
###..#.###.###..#
##.##...#########
....###......#..#
.#.########...##.
#.......###.####.
#...##..##.##.##.
#.#.#.#....#.....
##....###..###..#
..#.##.###.#.####
..#.##.###.#.####
##....###..###..#
#.#.#.#....#.....
#...##..##.##.##.

###..##
..#.#.#
####.#.
...#..#
##.#..#
##.#.##
...#..#
####.#.
..#.#.#

####...
...##..
###..##
##.###.
##.###.
###..##
...##..
####...
#.##...
....#..
##..###

.###...##
.###...##
.##.##.#.
....##..#
##.###.#.
.#..##..#
###.#..##
#.#.####.
#.#.####.
###.#..##
.#...#..#
##.###.#.
....##..#
.##.##.#.
.###...##

#.##.##.#..#.##.#
..##.##.####.##.#
#.###############
..#..............
#.#..##......##..
.#.##..##..##..##
#........##......
##.#..#.#..#.#..#
....####....####.
#....##......##..
...#.##.#..#.##.#
##..####.##.####.
#..#....#..#....#
.#..#..#.##.#..#.
.....##......##..

.#....#.#...##...
.#.##.#..#.####.#
#..##..#.#.#..#.#
##.##.##..##..##.
###..######.##.##
########.#.#..#.#
...##...#..####..
#......#.#......#
.##..##...##..###

..##.#.#.##.#.#
..##.#.#.##.#.#
##..#....##.###
...#..#.#..#...
.#.####..####..
..##.##..####.#
##....#.##.#.#.
...#.#...#####.
...#.#####...#.
###...#..###..#
..........###..

##....##....##.
##....##....##.
#.#.#....#.#.#.
##..##...#..##.
####......####.
#.#...##...#.##
.#####..#####..

......###..
.#..#.####.
.#..#.###..
.####...###
.####...###
.#..#.###..
.#..#.####.
......###..
..##..##...
##..###..##
.####...#..
##..###.#.#
..##...##..
##..#####.#
###.##.#...

......##.#.#.
.#.....#...#.
###.#..#...##
#..#.##.#...#
#..#.####...#
###.#..#...##
.#.....#...#.
......##.#.#.
##.######...#
...#...##.###
#....#####..#
..##..#..##.#
#.####..#.###
.##...###.#..
.#..#.###.##.
.#..#.###.##.
.##...###.#..

.###..###.##.
###.###..#.#.
..###......#.
#..#..#.#...#
.#..#.....#.#
.#.#...##.#.#
##...##..##.#
##...##..##.#
.#.#...##.#.#
.#.##.....#.#
#..#..#.#...#
..###......#.
###.###..#.#.
.###..###.##.
.###..###.##.

###.####.##
##........#
#..........
#.########.
..##....##.
.#.#.##.#.#
.#........#
#.........#
.##......##
###..##..##
#####..####
#####..####
###..##..##

##.#.#..#..
....#...##.
##..#.#..#.
...######..
#######..##
##.##..#.##
..#..####.#
###...##...
......##.#.
###.#..#..#
..##..###..
...#.#.##.#
...#.#.##.#
..##.####..
###.#..#..#
......##.#.
###...##...

#####.#.##...#.
......######...
#...#.#.#.#..##
..####.#.#.##.#
..######.#.##.#
#...#.#.#.#..##
......######...
#####.#.##...#.
.#...##..###...
.#...##..###...
#####.#.##...#.

####.#.
#..####
#..#..#
#..#..#
.##.#..
.##..##
...#..#
....##.
#..####
#..####
....##.

###...##.###...##
###.####...####.#
...#..#.##.#.##..
...#..#.##.#.##..
###.####...####.#
###...##.###...##
.#.#.#.##.#....##
.#.#.#.##.#....##
###...##.#.#...##

.##.....#
........#
#####..#.
#####..#.
####..###
....##...
....####.
#..###..#
.##..##.#
.##..##.#
#..###..#
....###..
....##...
####..###
#####..#.
#####..#.
........#

.#...##
.#...##
##.....
.#.####
##.##..
#....#.
.####..
#....#.
#....#.
.####.#
#....#.
##.##..
.#.####

..#.#.##...
..#.#.###..
##.##..###.
..####...#.
##.#....###
.#...#####.
..#.##.###.
.#....##...
.#..#.##..#
.#..#.##..#
.#....##...
..#.##.###.
.#...#####.
##.#....###
..####...#.

####.#####....#
#..#.###..#..#.
####.####....##
#######..###.##
#..###..##....#
.##..###.#...##
.##..###.#...##
#..###..##....#
#####.#..###.##
####.####....##
#..#.###..#..#.
####.#####....#
.##.####.##.#.#

####.##
..##.#.
..##...
.#.....
....##.
##..#.#
###...#
##.##.#
..##...
..##...
##.##.#

#.#.#.#.....##...
..#...#...#....#.
.##..##..##.##.##
...#.##.##......#
###..##.#.#.##.#.
.##.####..#....#.
.###..##.........
..#.###..#.####.#
.#...#.#..#.##.#.
###...######..###
#.#####...######.
###.###.#..####..
##..##.###..#...#
##..#..##.######.
##..#..##.######.

.###.#..#.###..##
####.#..#.#######
.##..#..#..#....#
##.#.####.#.####.
...#......#......
....#....#.......
......##.........
#.##..##..##.##.#
.##.######.##..##

...######...#.#
...######...#.#
..###..###....#
.##.####.##..##
.#.######.#....
###.#..#.##..##
#.#..##..#.###.
.##......##.###
###.####.###.##
.#..####..#...#
.###.##.###.###
##.######.###.#
#..##..##..#.#.

....##.....##..##
.##.##.##..#....#
..#....#.....##..
.##.##.##..#....#
##########.......
###########.####.
..#.##.#..#.#..#.
#..####..###....#
..##..##.........
..##..##...######
#........#.#....#
#.######.####..##
.###..###..#.##.#
.##....##...#..#.
....##...#.#.##.#

.##...#..####
.....####..##
#######.#..#.
#..###.#.###.
#..#.##...###
#########.#..
#..#..##...##
.##..##.#####
#..#..#..##..
#######.##.#.
####..#......
#..##.#...##.
.##...#.#..##
.##...#.#..#.
#..##.#...##.

###.#........
..#.##.......
##.##..#.....
.##.##..#####
.#....#..####
##...#..#....
###..########
.###..#..#..#
.#.#.#.......
######.......
#...#..######
.##....######
#...#.#.#####
.#.#...######
####..#..####

###....
###....
.####..
#.#.##.
..##..#
.##.#.#
#.####.
##.#.##
#.##.##
.#....#
.#.#.#.
.#..#.#
#..####
#..####
.#..#.#
.#.#.#.
.#.#..#

####..##.
.##..#..#
....#.###
....#.##.
....#.#..
.##..###.
.##..###.
....#.#..
....#.##.
....#.###
.##..#..#
####..##.
##.###...
#..#...#.
####.....

##....#####
.######.#..
#..##..#...
#..##..####
.######....
.#......#..
..#..#..###

###.#...###
...####...#
..#..#..#.#
..##.#.#..#
###.##..###
###..#....#
##...#....#
###.##..###
..##.#.#..#
..#..#..#.#
...####...#
###.#...###
..####.#.#.

...#.##..#...#...
#.#...###.##.####
....#.#.##.#.##..
.....#.#.####.#..
.#.#.#.##..#.####
.#.#...##..#.####
.....#.#.####.#..
....#.#.##.#.##..
#.#...###.##.####
...#.##..#...#...
...#....###...#..
#..###.......##..
.#.###.#.###.####

...####..
.##....##
.########
##......#
#..#..#..
....##...
#..####..

####..##.##
###.#...##.
....#..####
#...##..#..
..#..#...#.
..#..#...#.
#...##..#..
....#..####
###.#...##.
####..##.##
..###...##.
#.#.#.##.#.
.####..#...
..###..#...
#.#.#.##.#.

.....####.....#..
##.#.#..#.#.##...
.#.#......#.#.###
...###..###...#..
.#..######..#.#..
####.####.#####..
...###..###...#..
#............#.##
..#.#.##.#.#.#...
#..###..###..#...
...#......#....##
##...####...##.##
#...##..##...#.##

.####..###.
.##.###.#..
.##.###.#..
.####..###.
#.#.#.#.###
####.####..
#.....##.#.
#.....##.#.
####.####..
#.#.###.###
.####..###.

.....#..#..
#..###..###
####......#
.##.#.##.#.
#..#######.
#..#..##..#
.....#..#..

##..#....
...#.#.##
###...###
....###..
##..###..
###.###..
###....##
#....#...
####...##
##.###...
.......##
..#.###..
##..###..
...#..###
###...###

..#.##.#...####
##.#..#.##.####
.###..###......
.##....##...#..
..##..##...####
..#....#.....##
#.#..#.#.#..#..
..#.##.#...#...
#...##...##..##
.##....##.#####
#...##...#..###
.#..##..#.###..
#...##...##..##

#....#.#.
###..###.
###..###.
#....#.#.
#.#.#..#.
...##..#.
.#..###.#
#...#....
#...##...
##.###..#
#..##.##.
#..##.##.
##.###..#
#....#...
#...#....
.#..###.#
...##..#.

.#...#.#.
#.##.##..
####..#..
.#.######
...##.###
...##.###
.#.#####.
####..#..
#.##.##..
.#...#.#.
.#...#.#.

####.#..#.#####.#
##.##....##.####.
#..#.####.#..##..
#####....########
###..####..######
#####....########
#.##..##..##.##.#
##.#..##..#.####.
#..#......#..##..
..##......##....#
#............##..
##.##....##.####.
...#......#......
....#.##.#.......
.####....####..##
.#..........#..#.
.##.#.##.#.##..##

#..#...##..
..######.##
..######.##
#..#..###..
....#.#....
##....##...
#.#.#.##..#
#.#.#.##..#
##....##...
....#.#....
#..#..###..

#..#..#..#...
..##..##..##.
..#.##.#..#.#
############.
#.######.##..
#.######.#.##
#.######.#..#
#.######.##..
############.

..##..###.#..#.
...#......#..#.
#.##.......##..
.....##.#.#..#.
.....##.#.#..#.
#.##.......##..
...#......#..#.
..##..###.#..#.
#.#.##...##..##
#####.##..#..#.
#......##......
#.#..##.###...#
##.#......#..#.
##..#.#...#..#.
.#.###...######

##..#.#..##..###.
.##.#.#.#..##..#.
...#...##.#..#.##
.##.##...##..##..
.##.##...##..##..
...#...##.#..#.##
.##.#.#.#..##..#.

.#.####..####.#..
#.###.####.###.##
####..#..#..#####
..#.##.##.##.#...
#.##.#.##.#..#.##
#..#..####..#..##
#.####.##.####.##
##.###....###.###
##.#.#....#.#.###
..##...##...##...
..###..##..###...

..#.#...##....#..
####..#..#..###.#
#####.#..#..###.#
..#.#...##....#..
##.#.##.....###..
..####.########..
...##.##.#####.#.
..#.#......#....#
##..####.#.......
..##...#...#.##.#
....#.##....#..##

.#.##.##..#
####.#..##.
##..##.####
##..##.####
####.#..##.
...##.##..#
.#.........

##.#..#.#
#.#.#..##
#####.##.
##..##...
##..##...
#####..#.
#.#.#..##
##.#..#.#
.##..##..
.##..##..
##.#..#.#

###...##....#.###
#.#..#.#.#.###..#
.##.#.#.#.##.#.#.
.##.#.#.#.##.#.#.
#.#..#.#.#.###.##
###...##....#.###
...#.#.#.##..##.#
#....####..##.#..
#....####..##.#..
...#.#.#.##..##.#
###...##....#.###

..#####..
.###.....
#..###...
####.#...
###..#...
#..###...
.###.....
..#####..
#.#.#####
..#.#####
##.#.####

...#....#####..
..###..#...#.##
##..#.###.#....
##....##.###...
..#..#...#.....
#..#.##.##.##..
.#.#..##.#.#.##
##..###.....#..
.##.##...##.#..
##...##..##.###
##.#.##..##.###

...####..##.##.
...#..#####....
##..####.###..#
##..#####...##.
...#..#.#.#....
..#..#.#.......
....#....#..##.
..####.#.#.####
####.#....##...
####.#.#.......
####.####.##..#
..###.....#....
##..###.###.##.

.####.###.#..
.####.###.#..
########.###.
#.###.##....#
#...#...#....
....##.#.#..#
.##......####
#...##.....#.
#.##...##..##
####...##.##.
####...##.##.
#.##...##..##
##..##.....#.

#......#.####
.######.#...#
.........####
##....##..#..
.#.##.#..#..#
###..###...#.
..####..#.#..
###..###..##.
........#....
##....###...#
##....###...#
........#.#..
###..###..##.
..####..#.#..
###..###...#.

.##.#.#...#...#
.##.#.#...#.#.#
#.##.####..###.
....#.#.##.####
#..#.#.#.#..###
.##...##.##..##
..##.##...##.#.
..#.#..###.##.#
#####.##....#.#
#...#.#...##.##
#.###......#..#
##..#..###.#.##
..#####..#..###
..#####..#..###
##..#..###.#.##

.##.##.
.#.##.#
#....#.
#....#.
.#.##.#
.##.##.
...####
##....#
#.#.###
.####.#
###..#.
###....
.####.#
#.#.###
##....#
...####
.##.##.

####.#....####..#
####.#....####..#
#..##...##.#..#.#
#..#..######..###
#..#..#.#########
.##..#.#...#.#...
#..###......#.##.
####.#.###...##.#
####.####..#..##.
....##.#.#.......
.##..##..#..#..##
###.#.#..#...####
####.###.###.#.#.

.######
.###..#
.###..#
.######
#..#..#
.#..###
.##..#.
.###...
##.#.#.
.##....
..#..##
.....##
.##....
##.#.#.
.###...

##....#####......
##....##.#..####.
.#....#..##.#..#.
##....##.#.##..##
.#.##.#....#....#
##....######.##.#
###..###.######.#
##....#####.####.
#......##..#....#
#.#..#.#..#.#..#.
.#.##.#...##.##.#
..####..#..#.##.#
.#.##.#.#..#....#

.#.#..###.###
.#.#...##.###
##......####.
#...#.##.#...
##..#.###..#.
.####..#.###.
#...#..#..#..
.####.##..#..
.##..#..#...#
.##..#..#...#
.####.##..#..
#...#..#..#..
.####..#.###.

#...#....#.#.
##.#.#.#.##.#
###.##...#.#.
###.##...#.#.
##.#.#.####.#
#...#....#.#.
..#.######..#
#...#..####..
###..##.##.#.
...#.#.#..#..
...#.#.#..#..
###..##.##.#.
#...#..####..

..#.###
######.
..####.
###...#
###...#
..##.#.
######.
..#.###
..##.##
.....#.
###..##
..####.
######.
##...#.
####...
..#.#..
##.###.

.#..#.###.##...##
..##...#.##....#.
###########....#.
#######...###...#
#....##.#..#....#
#....#.##.#..##.#
.####.#.#.#.....#
.####....##.##..#
##..##..#..####..
.#..#.#...####..#
#.##.##.#.###..#.
#.##.##.#.#.#..#.
.#..#.#...####..#
##..##..#..####..
.####....##.##..#

##..##.##
.#..#....
..##..###
#.##.##..
.......##
..##.....
#....##..
..##...##
#....#.##
#.##.#.##
..##.....
#.##.#...
...#..###

#..##....##..##.#
.###.####.###.###
###..#..#..#####.
.#.##.##.##.#...#
.#.##.##.##.#...#
###..#..#..#####.
.###.####.###.###
#..##....##..##.#
.#.##.##.##.#.#..
....##..##.....##
#....#..#.#..####
.#...####...#.#.#
#.#.#....#.#.##.#
#..##.##.##..#...
#....#..#....##..

#....####
###......
###......
##...####
....#....
.#.#..##.
..###....
##.#.....
...#..##.
#.###.##.
#....####

#..####..#.##.#..
.########..##..##
#........#.##.#..
###.##.###.##.###
###.##.####..####
..##..##........#
..######........#
#.#.##.#.#.##.#.#
.##.##.##.####.##
#.##..##.##..#..#
.#.####.#......#.
....##....####...
.##.##.##......##

..####..##..##..#
...#..##.####.##.
.##.#.##..##..##.
...#..##.####.##.
.##..#..#....#..#
##.##.##########.
#########.##.####

.###..###.#.#.###
###....###..##.#.
###.##.###.#.#.##
###.##.###.#.#.##
###....###..##.#.
.###..###.#.#.###
.#.####.#...#.#..
##.#..#.###...#..
####..###..#.###.
#..####..##.#..#.
#.######.##..#.##
.##.##.##.##..##.
####..######.####
....##.....#.##..
####..#####...###

#...#.#.#...#
#.####.#..#..
#.####.#..#..
#...#.#.#...#
#.#.##...#.##
#####.#.#..#.
#.#....####.#
##.#.#.#####.
#####.##.#..#
....##.#...#.
.#..#...#.#..
#.#.###...##.
...#..##...#.
..##..##...#.
#.#.###...##.
.#..#...#.#..
....##.#...#.
"""

lines = util.get_lines(input_str, False)

Pattern = dict[tuple[int, int], str]


def lines_to_patterns(lines: list[str]) -> list[Pattern]:
    _, *remaining = lines
    line_groups = []
    curr_group = []
    for line in remaining:
        if line.strip() == "":
            line_groups.append(curr_group)
            curr_group = []
        else:
            curr_group.append(line)
    if len(curr_group) > 0:
        line_groups.append(curr_group)

    patterns = []
    for group in line_groups:
        pattern = {}
        for y, line in enumerate(group):
            for x, tile in enumerate(line):
                pattern[(y, x)] = tile
        patterns.append(pattern)

    return patterns

def find_vertical_reflection(pattern: Pattern):
    rows, cols = sorted(pattern.keys())[-1]
    
    for midpoint in range(0, cols):
        is_match = True
        for x in range(midpoint, cols):
            diff = x - midpoint
            m_left = midpoint - diff
            m_right = midpoint + diff + 1
            for y in range(0, rows + 1):
                l = pattern.get((y, m_left))
                r = pattern.get((y, m_right))

                if l == None or r == None:
                    continue                

                if l != r:
                    is_match = False
                    break
        if is_match:
            return midpoint + 1
    return None

def find_horizontal_reflection(pattern: Pattern):
    rows, cols = sorted(pattern.keys())[-1]
    
    for midpoint in range(0, rows):
        is_match = True
        for y in range(midpoint, rows):
            diff = y - midpoint
            m_top = midpoint - diff
            m_bottom = midpoint + diff + 1
            for x in range(0, cols + 1):
                t = pattern.get((m_top, x))
                b = pattern.get((m_bottom, x))
                
                if t == None or b == None:
                    continue                

                if t != b:
                    is_match = False
                    break
        if is_match:
            return midpoint + 1
    return None


def part1():
    patterns = lines_to_patterns(lines)
    vert = [find_vertical_reflection(p) for p in patterns]
    horiz = [find_horizontal_reflection(p) for p in patterns]

    vert = [c for c in vert if c != None]
    horiz = [100 * r for r in horiz if r != None]

    return functools.reduce(util.add, vert, 0) + functools.reduce(util.add, horiz, 0)


print("Part 1", part1())
