from queue import PriorityQueue
from gen_maze import manhattan_distance, Cell

def forward_repeated_a_star(maze, start, goal):
    while True:
        path, blocked_cells = a_star(maze, start, goal)
        if path is not None:
            return path  # path to target is found

        if blocked_cells is None:
            break  # No path exists

        try:
            update_blocked_cells(maze, blocked_cells)
        except Exception as e:
            print(f"Error updating blocked cells: {e}")
            break

        # Check if the blocked cells are still valid coordinates after update
        if any(not (0 <= cell[0] < len(maze) and 0 <= cell[1] < len(maze[0])) for cell in blocked_cells):
            break

    return None  

def a_star(maze, start, goal):
    open_list = PriorityQueue()
    open_dict = {start: maze[start[0]][start[1]].f}
    closed_set = set()

    while open_list:
        current_node = min(open_dict, key=open_dict.get)
        del open_dict[current_node]

        if current_node == goal:
            return reconstruct_path(start, goal, maze), None

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
            return None, get_blocked_cells(closed_set, maze)  # Return the blocked cells

    # No path found
    return None, None

def get_blocked_cells(closed_set, maze):
    blocked_cells = set()
    for node in closed_set:
        blocked_cells.update(get_neighbors(node, maze))
    return blocked_cells

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

def update_blocked_cells(maze, blocked_cells):
    for cell in blocked_cells:
        maze[cell[0]][cell[1]].blocked = True
