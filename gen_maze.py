import random
import os
import pickle
from colorama import init, Fore, Back, Style

init(autoreset=True)

class Cell:
    def __init__(self):
        self.visited = False
        self.blocked = False
        self.g = float('inf')  # Cost from start to current cell
        self.h = 0  # Heuristic estimate of cost from current cell to goal with manhattan distance
        self.f = float('inf')  # Total estimated cost of path f = g + h
        self.parent = None  # Parent cell in the path

def generate_maze(size):
    maze = [[Cell() for _ in range(size)] for _ in range(size)]
    stack = [(0, 0)]

    while stack:
        x, y = stack[-1]

        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        unvisited_neighbors = [(nx, ny) for nx, ny in neighbors if 0 <= nx < size and 0 <= ny < size and not maze[nx][ny].visited]

        if unvisited_neighbors:
            nx, ny = random.choice(unvisited_neighbors)
            maze[nx][ny].visited = True
            maze[nx][ny].blocked = random.random() < 0.3  # 30% chance of being blocked
            maze[nx][ny].g = float('inf')
            maze[nx][ny].h = manhattan_distance((nx, ny), (0, 0))  # initialize the manhattan values of each cell while generating the maze
            maze[nx][ny].f = float('inf')
            stack.append((nx, ny))
        else:
            stack.pop()

    return maze

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def visualize_maze(maze):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            cell = maze[row][col]
            if cell.visited:
                if cell.blocked:
                    print(Back.BLACK + "  ", end="")
                else:
                    if (row, col) == (0, 0):
                        print(Back.LIGHTWHITE_EX + Fore.BLACK + "T ", end="")
                    elif (row, col) == (len(maze)-1, len(maze[0])-1):
                        print(Back.LIGHTWHITE_EX + Fore.BLACK + "A ", end="")
                    else:
                        print(Back.LIGHTWHITE_EX + "  ", end="")
            else:
                print(Back.LIGHTBLACK_EX + "  ", end="")
        print()

def visualize_manhattan(maze):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            cell = maze[row][col]
            if cell.visited:
                if cell.blocked:
                    print(Back.BLACK + "  ", end="")
                else:
                    # Print Manhattan distance on open tiles
                    print(Back.LIGHTWHITE_EX + f"{cell.h:2d} ", end="")
            else:
                print(Back.LIGHTBLACK_EX + "  ", end="")
        print()

def visualize_maze_with_path(maze, path):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            cell = maze[row][col]
            if cell.visited:
                if cell.blocked:
                    print(Back.BLACK + "  ", end="")
                else:
                    if (row, col) == (0, 0):
                        print(Back.LIGHTWHITE_EX + Fore.BLACK + "T ", end="")
                    elif (row, col) == (len(maze)-1, len(maze[0])-1):
                        print(Back.LIGHTWHITE_EX + Fore.BLACK + "A ", end="")
                    elif (row, col) in path:
                        print(Back.RED + "  ", end="")
                    else:
                        print(Back.LIGHTWHITE_EX + "  ", end="")
            else:
                print(Back.LIGHTBLACK_EX + "  ", end="")
        print()

def save_mazes(mazes, folder_path):
    os.makedirs(folder_path, exist_ok=True)
    for i, maze in enumerate(mazes):
        file_path = os.path.join(folder_path, f'maze_{i+1}.pkl')
        with open(file_path, 'wb') as file:
            pickle.dump(maze, file)
    print(f"{len(mazes)} mazes saved to {folder_path}")

def generate_and_save_mazes(num_mazes, maze_size, folder_path):
    mazes = [generate_maze(maze_size) for _ in range(num_mazes)]
    save_mazes(mazes, folder_path)

def load_mazes(folder_path):
    mazes = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".pkl"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'rb') as file:
                maze = pickle.load(file)
                mazes.append(maze)
    return mazes

# Main function
def main():
    maze_size = 15
    maze = generate_maze(maze_size)

    maze[0][0].blocked = False
    maze[maze_size-1][maze_size-1].blocked = False
    visualize_maze(maze)

if __name__ == "__main__":
    main()

