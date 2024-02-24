from copy import deepcopy
from gen_maze import visualize_maze, visualize_maze_with_path, load_mazes
from repeated_forward import forward_repeated_a_star
from a_star import a_star

def main():
    maze_size = 101
    folder_path = "mazes" 
    maze_index_to_test = 0

    loaded_mazes = load_mazes(folder_path)

    if 0 <= maze_index_to_test < len(loaded_mazes):
        original_maze = loaded_mazes[maze_index_to_test]

        start = (maze_size - 1, maze_size - 1)
        goal = (0, 0)
        # start = (100, 1)
        # goal = (0,94)

        # maze_a_star = deepcopy(original_maze)
        maze_rfa_star = deepcopy(original_maze)

        # path_a_star = a_star(maze_a_star, start, goal)

        # if path_a_star:
        #     print("A* Path:")
        #     for step in path_a_star:
        #         print(step)
        #     print(f"Path length (A*): {len(path_a_star)}")
        #     visualize_maze_with_path(original_maze, path_a_star)
        #     print("\n")
        # else:
        #     print("\nNo path found for A*.")

        path_rfa_star = forward_repeated_a_star(maze_rfa_star, start, goal)

        if path_rfa_star:
            print("RFA* Path:")
            for step in path_rfa_star:
                print(step)
            print(f"Path length (RFA*): {len(path_rfa_star)}")
            visualize_maze_with_path(original_maze, path_rfa_star)
        else:
            print("\nNo path found for RFA*.")

        # if path_a_star == path_rfa_star:
        #     print("\nPaths are the same!")
        # else:
        #     print("\nPaths are different.")
    else:
        print(f"Invalid maze index {maze_index_to_test}. Please choose a valid index.")

if __name__ == "__main__":
    main()

