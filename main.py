maze = [
    ['S', '.', '.', '#', '.'],
    ['#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '.'],
    ['.', '.', '.', 'G', '.']
]


def find_start_goal(maze):
    start = None
    goal = None

    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 'S':
                start = (row, col)
            elif maze[row][col] == 'G':
                goal = (row, col)

    return start, goal


def get_neighbors(position, maze):
    row, col = position

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    neighbors = []

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]):
            if maze[new_row][new_col] != '#':
                neighbors.append((new_row, new_col))

    return neighbors


def heuristic(current, goal):
    return abs(goal[0] - current[0]) + abs(goal[1] - current[1])


def reconstruct_path(came_from, start, goal):
    path = []
    current = goal

    while current != start:
        path.append(current)
        current = came_from[current]

    path.append(start)
    path.reverse()

    return path


def a_star(maze, start, goal):

    open_list = [start]
    closed_list = []

    came_from = {}
    g_score = {start: 0}

    while open_list:

        current = min(
            open_list,
            key=lambda node: g_score[node] + heuristic(node, goal)
        )

        open_list.remove(current)

        if current == goal:
            return reconstruct_path(came_from, start, goal)

        closed_list.append(current)

        for neighbor in get_neighbors(current, maze):

            new_g = g_score[current] + 1

            if neighbor not in g_score or new_g < g_score[neighbor]:

                g_score[neighbor] = new_g
                came_from[neighbor] = current

                if neighbor not in open_list and neighbor not in closed_list:
                    open_list.append(neighbor)

    return None


def print_maze(maze, path):

    solved_maze = [row[:] for row in maze]

    if path:
        for row, col in path:
            if solved_maze[row][col] not in ['S', 'G']:
                solved_maze[row][col] = '*'

    for row in solved_maze:
        print(" ".join(row))


def main():

    start, goal = find_start_goal(maze)

    path = a_star(maze, start, goal)

    if path:
        print("Shortest Path:")
        print(path)
        print()

        print("Solved Maze:")
        print_maze(maze, path)

    else:
        print("No path found.")


main()