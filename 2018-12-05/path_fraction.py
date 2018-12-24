"""
12/05/2018: Problem 6:
Given a sequence of points where consecutive points
are connected by line segments to make a path,
return the point along the path that corresponds
to a given percentage along the path.

Author: Eugene Ma
"""

import collections

Point = collections.namedtuple('Point', ['x', 'y'])

def get_dist(pt1, pt2):
    import math

    return math.sqrt((pt2.x - pt1.x) ** 2 + (pt2.y - pt1.y) ** 2)

def interpolate(pt1, pt2, t):
    dx = (pt2.x - pt1.x) * t
    dy = (pt2.y - pt1.y) * t

    return Point(pt1.x + dx, pt1.y + dy)

def get_path_accum(path_points):
    """
    Returns an array of the accumulated distance up to a given point
    for each point in the given path.
    """

    path_accum = []

    accum_dist = 0
    prev_pt = None
    for pt in path_points:
        if prev_pt is None:
            path_accum.append(accum_dist)
            prev_pt = pt
        else:
            accum_dist += get_dist(prev_pt, pt)
            path_accum.append(accum_dist)
            prev_pt = pt

    return path_accum

def get_point_for_path_frac(path_points, path_accum, frac):
    if not path_points:
        return None
    elif len(path_points) == 1:
        return path_points[0]

    # Clamp to range [0, 1]
    if frac < 0:
        frac = 0
    elif frac > 1:
        frac = 1

    if frac == 1:
        return path_points[-1]
    else:
        total_dist = path_accum[-1]
        frac_dist = frac * total_dist

        import bisect

        # Binary search to the second point
        # (which is <= the target distance).
        pt2_idx = bisect.bisect_right(path_accum, frac_dist)
        pt1_idx = pt2_idx - 1

        # We will be considering the region between point 1 and point2
        # including point 1 but excluding point 2.
        pt1 = path_points[pt1_idx]
        pt2 = path_points[pt2_idx]

        remaining_dist = frac_dist - path_accum[pt1_idx]
        if remaining_dist != 0:
            dist_between_pts = path_accum[pt2_idx] - path_accum[pt1_idx]
            # TODO: What if points are equal?
            # Then we have corner case of division by 0.
            frac_between_pts = remaining_dist / dist_between_pts

            return interpolate(pt1, pt2, frac_between_pts)
        else:
            return pt1

if __name__ == '__main__':
    path_points = [
        Point(0, 0),
        Point(100, 150),
        Point(200, 200),
        Point(300, 200),
        Point(250, 100),
        Point(50, 150),
        Point(-50, 30),
        Point(-220, -30)
    ]

    path_accum = get_path_accum(path_points)

    import turtle

    # Draw the path.
    for i, pt in enumerate(path_points):
        turtle.goto(pt.x, pt.y)
        if i == 0:
            turtle.pendown()
    turtle.penup()

    NUM_MARKS = 17

    # Draw evenly-spaced marks along the path.
    for n in range(NUM_MARKS):
        t = n / (NUM_MARKS - 1)
        pt = get_point_for_path_frac(path_points, path_accum, t)
        turtle.goto(pt.x, pt.y)
        turtle.dot(5)
        #turtle.write('({0:.2f}, {1:.2f})'.format(pt.x, pt.y))

    turtle.exitonclick()
