import sys
from util import Coord, LineSegment


def main(argv):
    A = Coord(float(argv[1]), float(argv[2])) # point A
    B = Coord(float(argv[3]), float(argv[4])) # point B
    C = Coord(float(argv[5]), float(argv[6])) # point C
    D = Coord(float(argv[7]), float(argv[8])) # point D

    segAB = LineSegment(A, B)
    segCD = LineSegment(C, D)
    intersect = segAB.getSegmentIntersection(segCD)


    print("Intersection Point: {}".format(intersect))



main(sys.argv)