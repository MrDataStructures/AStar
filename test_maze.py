from gen_maze import visualize_maze, visualize_maze_with_path, load_mazes
from a_star import a_star

def main():
    maze_size = 101
    folder_path = "proj1/mazes" 
    maze_index_to_test = 0  # Change this index to test a different maze

    loaded_mazes = load_mazes(folder_path)

    if 0 <= maze_index_to_test < len(loaded_mazes):
        maze = loaded_mazes[maze_index_to_test]

        start = (maze_size - 1, maze_size - 1)
        goal = (0, 0)

        visualize_maze(maze)
        path = a_star(maze, start, goal)

        if path:
            print("\nPath Found:")
            for step in path:
                print(step)

            visualize_maze_with_path(maze, path)
        else:
            print("\nNo path found.")
    else:
        print(f"Invalid maze index {maze_index_to_test}. Please choose a valid index.")

if __name__ == "__main__":
    main()
