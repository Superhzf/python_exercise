class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y, dx, dy = 0, 0, 0, 1 #position & direction
        obstacles = set(map(tuple, obstacles))
        dis2 = 0

        for command in commands:
            if command == -2: dx, dy = -dy, dx #ccw (left)
            if command == -1: dx, dy = dy, -dx #cw (right)
            if 1 <= command <= 9:
                for _ in range(command):
                    if (x+dx, y+dy) in obstacles: break
                    x += dx
                    y += dy
                dis2 = max(dis2, x**2 + y**2)
        return dis2
