import numpy as np
import math

#     x (N 0)
#     ^
#     |
#     |
#     |
# -----------> y(E 90)
#     |
#     |
#     |

def get_forward_position(x0, y0, theta, d):
    """ Get the coordinate of the point that is `d` meters forward.
        @paras theta: degree
    """
    r = math.radians(theta)
    return x0 + d * (math.sin(r)), y0 + d * (math.cos(r))


def get_distance(pts, x0, y0):
    """ Get the shortest distance from (x0, y0) to a list of points (these points belong to a curve in most cases).
        Also return the coordinate of the nearest point.
        @paras pts: N x 2 np.array [[x1, y1], [x2, y2] ...]
        @return distance
        @return (xc, yc)
    """
    cur_pt = np.array([x0, y0])
    distances = np.sum((pts - cur_pt) ** 2, 1)
    index = np.argmin(distances)
    return distances[index], pts[index]


def get_theta(xc, yc, x0, y0):
    """ Get the angle between the cutting point and the current point.
    """
    if abs(y0 - yc) < 0.000001:
        res = -90
    elif (x0 - xc) * (y0 - yc) > 0:
        res = -math.degrees(math.atan((x0 - xc) / (y0 - yc)))
    else: # (x0 - xc) * (y0 - yc) <= 0
        res = math.degrees(math.atan((xc - x0) / (y0 - yc)))
    if res > 0:
        return res, res - 180
    else:
        return res, 180 + res


def get_diff_theta(cur_theta, target_thetas):
    t1 = cur_theta - target_thetas[0]
    t2 = cur_theta - target_thetas[1]
    if abs(t1) < abs(t2):
        return t1
    else:
        return t2


# unit test
def main():
    print(get_theta(2, 2, 1, 1))
    print(get_theta(2, 1, 1, 1))
    print(get_theta(0.9, 2, 1, 1))
    print(get_theta(1, -1, 0, 0))


if __name__ == "__main__":
    main()
