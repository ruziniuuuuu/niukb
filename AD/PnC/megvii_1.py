"""
两个质点初始位置，朝向角和速度分别为：（x0,y0,yaw0,v0），（x1,y1,yaw1,v1），它们在t=0时刻匀速直行运动，问它们是否会在同一时刻相交，
如果不会，找出它们距离最小的时刻，算法计算效率O(1)。
"""

import math

def f(
        x0, y0, yaw0, v0,
        x1, y1, yaw1, v1
):
    # t = 0
    # x_cur_0 = x0 + math.cos(yaw0) * t * v0
    # y_cur_0 = y0 + math.sin(yaw0) * t * v0
    # x_cur_1 = x1 + math.cos(yaw0) * t * v1
    # y_cur_1 = y1 + math.sin(yaw0) * t * v1

    t_1 = (x0 - x1) / (math.cos(yaw0) * v0 - math.cos(yaw0) * v1)
    t_2 = (y0 - y1) / (math.sin(yaw0) * v0 - math.sin(yaw0) * v1)

    if (t_1 - t_2)^2 <= 1e-10:
        print("Intersection")
        return
    
    # d2 = (x0 + math.cos(yaw0) * t * v0 - x1 - math.cos(yaw0) * t * v1)^2 + (math.sin(yaw0) * t * v0 - y_cur_1 - y1 - math.sin(yaw0) * t * v1)^2
    # 求导
    # t_d = 0
    # 0 = 2 * (x0 + math.cos(yaw0) * t * v0 - x1 - math.cos(yaw0) * t * v1) * (x0 + math.cos(yaw0) * v0 - x1 - math.cos(yaw0) * v1) * t_d
    #   + 2 * ()
    # t_d = ...

    t_min = math(t_1^2 + t_2^2)
    print(t_min)
    return
    

if __name__ == '__main__':
    f()

"""
旷视的实习笔试题，纯纯的数学题，公式太长没写全，直接给他说思路了，比较简单，考察（高中）数学基础
"""