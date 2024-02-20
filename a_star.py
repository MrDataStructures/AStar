from queue import PriorityQueue
from gen_maze import manhattan_distance, Cell

def a_star(maze, start, goal):
    open_list = PriorityQueue()
    open_dict = {start: maze[start[0]][start[1]].f}
    closed_set = set()

    while open_list:
        current_node = min(open_dict, key=open_dict.get)
        del open_dict[current_node]

        if current_node == goal:
            # we have reached the target index
            return reconstruct_path(start, goal, maze)

        closed_set.add(current_node)

        for neighbor in get_neighbors(current_node, maze):
            if neighbor in closed_set:
                continue

            new_g_score = maze[current_node[0]][current_node[1]].g + 1

            if new_g_score < maze[neighbor[0]][neighbor[1]].g or neighbor not in open_dict:
                maze[neighbor[0]][neighbor[1]].g = new_g_score
                maze[neighbor[0]][neighbor[1]].h = manhattan_distance(neighbor, goal)
                maze[neighbor[0]][neighbor[1]].f = new_g_score + maze[neighbor[0]][neighbor[1]].h
                maze[neighbor[0]][neighbor[1]].parent = current_node

                open_dict[neighbor] = maze[neighbor[0]][neighbor[1]].f

        if not open_dict:
            # If the open list is empty and the goal has not been reached, then no path exists
            break

    #no path found
    return None

def reconstruct_path(start, goal, maze):
    path = []
    current_node = goal

    while current_node != start:
        path.append(current_node)
        current_node = maze[current_node[0]][current_node[1]].parent

    path.append(start)
    return path[::-1] 

def get_neighbors(node, maze):
    neighbors = []
    x, y = node

    if 0 <= x - 1 < len(maze) and not maze[x - 1][y].blocked:
        neighbors.append((x - 1, y))
    if 0 <= x + 1 < len(maze) and not maze[x + 1][y].blocked:
        neighbors.append((x + 1, y))
    if 0 <= y - 1 < len(maze[0]) and not maze[x][y - 1].blocked:
        neighbors.append((x, y - 1))
    if 0 <= y + 1 < len(maze[0]) and not maze[x][y + 1].blocked:
        neighbors.append((x, y + 1))

    return neighbors
