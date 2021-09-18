maze = [["#","S","#","#","#","#","#","#","#","#","#","#","#","#","X","#"],
        ["#"," "," "," ","#","#","#","#","#"," "," "," "," "," "," ","#"],
        ["#"," ","#","#","#","#","#","#","#","#","#"," ","#","#","#","#"],
        ["#"," "," "," "," "," "," "," "," "," "," "," ","#","#","#","#"],
        ["#","#","#","#","#","#","#","#","#"," ","#"," ","#","#","#","#"],

        
        ]
def createMaze():

    

    for x in maze:
        for y in x:
            print(y,end='')
        print()

def startpoint():
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 'S':
                return row, col


def is_valid_position(maze, pos_r, pos_c):
    if pos_r < 0 or pos_c < 0:
        return False
    if pos_r >= len(maze) or pos_c >= len(maze[0]):
        return False
    if maze[pos_r][pos_c] == ' ':
        return True
    return False
def solvemaze(maze,start):
    stack=[]
    stack.append(start)
    
    while len(stack)>0:
        maze[start[0]][start[1]]="S"
        pos_r, pos_c = stack.pop()
        try:
            if maze[pos_r+1][pos_c]=='E':
                exit
            if maze[pos_r-1][pos_c]=='E':
                exit
            if maze[pos_r][pos_c+1]=='E':
                exit
            if maze[pos_r][pos_c-1]=='E':
                exit
        except:
            continue
            
        
        maze[pos_r][pos_c] = '.'
        # Check for all possible positions and add if possible
        if is_valid_position(maze, pos_r - 1, pos_c):
            stack.append((pos_r - 1, pos_c))
        if is_valid_position(maze, pos_r + 1, pos_c):
            stack.append((pos_r + 1, pos_c))
        if is_valid_position(maze, pos_r, pos_c +1):
            stack.append((pos_r, pos_c + 1))
        if is_valid_position(maze, pos_r, pos_c -1):
            stack.append((pos_r, pos_c - 1))
        
        
        
        


        # To follow the maze
        
        
        


    # We didn't find a path, hence we do not need to return the path
    createMaze()
    return False
        


createMaze()
start= startpoint()
print(" Trying to solve the puzzle!")
solvemaze(maze,start)