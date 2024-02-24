from gen_maze import generate_maze, visualize_maze, visualize_maze_with_path
from a_star import a_star

def main():
    maze_size = 101
    maze = generate_maze(maze_size)

    start = (0, 0)
    goal = (maze_size - 1, maze_size - 1)

    print("Original Maze:")
    visualize_maze(maze)

    path = a_star(maze, start, goal)

    if path:
        print("\nMaze with A* Path:")
        visualize_maze_with_path(maze, path)
    else:
        print("\nNo path found!")

if __name__ == "__main__":
    main()
