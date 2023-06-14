class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
        self.solution = []

    def solve(self, start_x, start_y):
        if self._explore(start_x, start_y):
            print("Maze solved!")
            print("Solution path:")
            for step in self.solution:
                print(step)
        else:
            print("No solution found.")

    def _explore(self, x, y):
        if x < 0 or x >= len(self.maze) or y < 0 or y >= len(self.maze[0]) or self.maze[x][y] == 1 or self.visited[x][y]:
            return False

        self.solution.append((x, y))
        self.visited[x][y] = True

        if self.maze[x][y] == 9:
            return True

        if self._explore(x + 1, y):
            return True
        if self._explore(x - 1, y):
            return True
        if self._explore(x, y + 1):
            return True
        if self._explore(x, y - 1):
            return True

        self.solution.pop()
        return False

def main():
    maze = [[0, 0, 0, 0, 0],
            [1, 1, 0, 1, 0],
            [0, 0, 0, 0, 1],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 9]]

    solver = MazeSolver(maze)
    solver.solve(0, 0)

if __name__ == "__main__":
    main()
