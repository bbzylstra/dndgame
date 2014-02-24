__author__ = 'Brad'
def successors(point,group,notmovecells):
    successors=[]
    closedpoints=notmovecells
    for x in group.sprites():
        closedpoints.append(x.squareNumber2d)
    if (point[0]+1,point[1]) not in closedpoints:
        successors.append((point[0]+1,point[1]))
    if (point[0]-1,point[1]) not in closedpoints:
        successors.append((point[0]-1,point[1]))
    if (point[0],point[1]+1) not in closedpoints:
        successors.append((point[0],point[1]+1))
    if (point[0],point[1]-1) not in closedpoints:
        successors.append((point[0],point[1]-1))
    return successors
def heuristic_to_goal(point,goal):
    position=point
    Heuristic=0
    while position != goal:
        if position[0] < goal[0]:
            position=(position[0]+1,position[1])
            Heuristic=Heuristic+1
        elif position[0] > goal[0]:
            position=(position[0]-1,position[1])
            Heuristic=Heuristic+1
        elif position[1] < goal[1]:
            position=(position[0],position[1]+1)
            Heuristic=Heuristic+1
        elif position[1] > goal[1]:
            position=(position[0],position[1]-1)
            Heuristic=Heuristic+1
    return Heuristic
