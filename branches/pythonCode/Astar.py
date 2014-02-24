__author__ = 'Brad'
class Astar(object):
    def __init__(self,successors,heuristic_to_goal,move_cost=1):
        self.successors = successors
        self.move_cost = move_cost
        self.heuristic_to_goal = heuristic_to_goal
    def compute_path(self,start,end,notmovecells,ai_group):
        if end == None:
            return 1,None
        closed=[]
        closed=closed
        for i in notmovecells:
            closed.append(self.Node(i))
        open=[]
        path=[]
        moves=0
        flag1=0
        flag2=1
        startNode= self.Node(start,self.heuristic_to_goal(start,end))
        open.append(startNode)
        endNode= self.Node(end)
        currentNode=startNode
        for i in closed:
            if i.coord==endNode.coord:
                return 0,None
        while len(open)<15:
            closed=list(set(closed))
            for i in self.successors(currentNode.coord,ai_group,notmovecells):
                for j in open:
                    if i == j.coord:
                        flag1=1
                for j in closed:
                    if i == j.coord:
                        flag1=1
                if flag1==0:
                    open.append(self.Node(i,self.heuristic_to_goal(i,end),currentNode))
                flag1=0
            closed.append(currentNode)
            del open[0]
            if len(open)==0:
                return 0,None
            open.sort(key=lambda x: x.h)
            currentNode=open[0]
            if currentNode.coord == endNode.coord:
                path,moves=self.returnpath(currentNode)
                return path,moves
        moves=99
        return path,moves

    def returnpath(self,currentNode):
        pth=[]
        dist=0
        n=currentNode
        while n.pred:
            pth.append(n.coord)
            dist=dist+1
            n=n.pred
        pth.reverse()
        return pth,dist


    class Node(object):
        def __init__(self, coord, h=None,pred=None):
            self.coord = coord
            self.h=h
            self.pred = pred
