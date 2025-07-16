"""
 function answer(map) that generates the length of the shortest path from the prison door to the escape pod, 
 where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of 
 nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always 
 passable (0). The map will always be solvable, though you may or may not need to remove a wall. 
 The height and width of the map can be from 2 to 20. 
 Moves can only be made in cardinal directions; no diagonal moves are allowed.
"""
def shortest_path(start_x, start_y, map, w, h):
    """
    Returns the shortest path from the start position to the end position in the map.
    """
    # create a map of the shortest path from the start position to the end position
    print(w, h)
    maze = [[None for i in range(w)] for i in range(h)]
    print(maze)
    maze[start_x][start_y] = 1

    # create a queue of the start position
    queue = [(start_x, start_y)]
    while queue:
        # pop the first item from the queue
        x, y = queue.pop(0)
        # check all possible directions
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            # get the next position
            next_x, next_y = x + dx, y + dy
            # check if the next position is valid
            if next_x >= 0 and next_x < h and next_y >= 0 and next_y < w:
                # check if the next position is passable
                if maze[next_x][next_y] is None:
                    # check if the next position is already in the queue
                    maze[next_x][next_y] = maze[x][y] + 1
                    if maze[next_x][next_y] == 1:
                        continue
                    
                    # mark the next position as part of the shortest path
                    queue.append((next_x, next_y))
    return maze
                        
                        

def solution(map):
    w = len(map)
    h = len(map[0])
    # start position
    sp = shortest_path(0, 0, map, w, h)
    # end position
    ep = shortest_path(h - 1, w - 1, map, w, h)
    
    map_board = []

    sol = float('inf')

    for i in range(h):
        for c in range(w):
            if sp[i][c] and ep[i][c]:
                sol = min(sp[i][c] + ep[i][c] - 1, sol)
    return sol

if __name__ == "__main__":
   maze = [[0, 0, 0, 0, 0, 0],[1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0],[0, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0]] #Answer 21
   print(solution(maze))
   maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]] #Answer 7
   print(solution(maze))
   maze = [[0,1,0,0,0],[0,0,0,1,0],[1,1,1,1,0]] #Answer 7
   print(solution(maze))
   maze = [[0,1,1,1],[0,1,0,0],[1,0,1,0],[1,1,0,0]] #Answer 7
   print(solution(maze))
   maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]] #Answer 11
   print(solution(maze))