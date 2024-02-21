from gen_maze import generate_maze, save_mazes
import os

def generate_and_save_mazes(num_mazes, maze_size, folder_path):
    mazes = [generate_maze(maze_size) for _ in range(num_mazes)]
    save_mazes(mazes, folder_path)

if __name__ == '__main__':
    num_mazes = 50
    maze_size = 101
    folder_path = os.path.join(os.path.dirname(__file__), "proj1", "mazes")

    generate_and_save_mazes(num_mazes, maze_size, folder_path)
