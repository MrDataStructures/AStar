from gen_maze import generate_maze, visualize_maze, visualize_maze_with_path
from a_star import a_star

def main():
    maze_size = 10 #change this value and run this file to test out difference sized mazes
    maze = generate_maze(maze_size)
    maze[0][0].blocked = False
    maze[maze_size - 1][maze_size - 1].blocked = False
    visualize_maze(maze)

    start = (maze_size - 1, maze_size - 1) #bottom right of the maze
    goal = (0, 0) # top left of the maze

    path = a_star(maze, start, goal)

    if path:
        print("\nPath Found:")
        for step in path:
            print(step)
        
        visualize_maze_with_path(maze, path)
    else:
        print("\nNo path found.")

if __name__ == "__main__":
    main()
