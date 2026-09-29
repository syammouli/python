from collections import deque,defaultdict
import heapq
from sortedcontainers import SortedSet
#creating a graph using list type

n=4
adj=[[] for _ in range(n)]

adj[0].append(1)
adj[1].append(0)

adj[0].append(2)
adj[2].append(0)

adj[1].append(3)
adj[3].append(1)

adj[2].append(1)
adj[1].append(2)

print(adj)

edges=[
    [0,1],
    [0,2],
    [1,3],
    [3,4]
]

adjs=[[] for _ in range(n+1)]

for u,v in edges:
    adjs[u].append(v)
    adjs[v].append(u)

print(adjs)


def BFS(start,adjs):
    n=len(adjs)
    visited=[False]*n
    q=deque()
    q.append(start)
    visited[start]=True
    while q:
        node=q.popleft()
        print(node,end=" ")

        for neighbor in adjs[node]:
            if not visited[neighbor]:
                visited[neighbor]=True

                q.append(neighbor)

print("BFS")
BFS(0,adjs)


def DFS(start,adj,visited):
    visited[start]=True
    print(start,end=" ")

    for neighbor in adj[start]:
        if not visited[neighbor]:
            DFS(neighbor,adj,visited)



print("DFS")
DFS(0,adj,n*[False])

isConnected = [
    [1,1,0],
    [1,1,0],
    [0,0,1]
]

class Solution:
        def findCircleNum(self,isConnected):
            n=len(isConnected)
            adj=[[]for _ in range(n)]

            for i in range(n):
                for j in range(n):
                    if i!=j and isConnected[i][j]==1:
                        adj[i].append(j)
            visited=[False]*n
            provinces=0

            def dfs(node):
                visited[node]=True
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        dfs(neighbor)

            for city in range(n):
                if not visited[city]:
                    provinces+=1
                    dfs(city)
            return provinces

            

obj=Solution()
print("provinces")
print(obj.findCircleNum(isConnected))


grid = [
    ["1","1","0","0"],
    ["1","1","0","0"],
    ["0","0","1","0"],
    ["0","0","0","1"]
]
class Island:
    def isIsland(self, grid):
        rows=len(grid)
        cols=len(grid[0])
        directions=[
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]


        def dfs(r,c):
            grid[r][c]="0"
            for dr,dc in directions:
                
                
                nr=r+dr
                nc=c+dc

                if ( 0<=nr<rows     and 0<=nc<cols and grid[nr][nc]=="1"    ):
                    dfs(nr,nc)

        islands=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    islands+=1
                    dfs(r,c)

        return islands



print("Islands")
onjs=Island()
print(onjs.isIsland(grid))


class FillColor:
    def startFilling(self,image,sr,sc,color):
        rows=len(image)
        cols=len(image[0])

        oldColor=image[sr][sc]
        if oldColor==color:
            return
        
        direction=[
            (-1,0),
            (1,0),
            (0,1),
            (0,-1)
        ]

        def dfs(r,c):
            image[r][c]=color
            for dr,dc in direction:
                nr=r+dr
                nc=c+dc

                if (
                    0<=nr<rows and
                    0<=nc<cols and
                    image[nr][nc]==oldColor
                    ):
                     dfs(nr,nc)
               

        dfs(sr,sc)
        
        return image                   
            
sr=1
sc=1
color=3

image = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
]

objfill=FillColor()
print("filling the color with given number")

print(objfill.startFilling(image,sr,sc,3))


class RottenOranges:
    def Isrotten(self,grid):
        fresh=0
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    q.append((r,c))
        directions=[
              (-1,0),
            (1,0),
            (0,1),
            (0,-1)
        ]

        minutes=0
        while q and fresh>0:
            size=len(q)
            for _ in range(size):
                rotr,rotc=q.popleft()
                
                
                for dr,dc in directions:
                    cr=rotr+dr
                    cc=rotc+dc
                    if (0<=cr<rows and 0<=cc<cols and grid[cr][cc]==1):
                        grid[cr][cc]=2
                        q.append((cr,cc))
                        fresh-=1
           
            minutes+=1
        if fresh>0:
                    return -1
        return minutes
    

# grid = [
#     [2,1,1],
#     [1,1,0],
#     [0,1,1]
# ]
grid = [
 [2,1,1],
 [1,2,1],
 [1,1,1]
]
rotobj=RottenOranges()
print("Rotten Oranges")
print(rotobj.Isrotten(grid))


class IsCycle:
    def bfsCycle(self,start,visited,adj):
        q=deque()
        q.append((start,-1))
        visited[start]=True
        while q:
            node,parent=q.popleft()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor]=True
                    q.append((neighbor,node))
                elif neighbor!=parent:
                    return True
                
        return False


    def isCycle(self,V,adj):
        visited=[False]*V

        for node in range(V):
            if not visited[node]:
                if self.bfsCycle(node,visited,adj):
                    return True
                
        return False
    
cycleobj=IsCycle()
print("is valid cycle")
print(cycleobj.isCycle(n,adj))


class dfsSolution:


    def dfs(self,start,parent,adjs,visited):
        visited[start]=True
        for neighbor in adjs[start]:
            if not visited[neighbor]:
                if self.dfs(neighbor,start,adjs,visited):
                    return True
                
            elif neighbor !=parent:
                return True
        return False
    

    def IsCycle(self,adjs,n):
        visited=[False]*n

        for node in range(n):
            if not visited[node]:
                if self.dfs(node,-1,adjs,visited):
                    return True
                
        return False
    
objDFS=dfsSolution()
print("dfs cycle")
print(objDFS.IsCycle(adjs,len(adjs)))



grids = [
    [0,0,0],
    [0,1,0],
    [1,0,0]
]
class Distance:
    def fromOnes(self,grids):
        rows=len(grids)
        cols=len(grids[0])
        dup=[[-1]*cols for _ in range(rows)]

        q=deque()
        for r in range(rows):
            for c in range(cols):
                if grids[r][c]==1:
                    dup[r][c]=0
                    q.append((r,c))

        directions=[
            (-1,0),
            (1,0),
            (0,1),
            (0,-1)
        ]
        
        while q:
            r,c=q.popleft()
            for dr, dc in directions:
                nr=r+dr
                nc=c+dc

                if (0<=nr<rows and 0<=nc<cols and dup[nr][nc]==-1):
                    dup[nr][nc]=dup[r][c]+1
                    q.append((nr,nc))

        return dup
    

distance=Distance()
print("distance from ones")
print(distance.fromOnes(grids))
        

board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]
]


class XOXO:

    def solution(self,board):
        rows=len(board)
        cols= len(board[0])
        
        directions=[
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]

        def dfs(r,c):
            board[r][c]="S"
            for dr,dc in directions:
                nr=r+dr
                nc=r+dc
                if (0<=nr<rows
                    and 0<=nc<cols 
                    and board[nr][nc]=="O"):
                    
                    dfs(nr,nc)

        for c in range(cols):
            if board[0][c]=="O":
                dfs(0,c)
        for c in range(cols):
            if board[rows-1][c]=="O":
                dfs(rows-1,c)
        for r in range(rows):
            if board[r][0]=="O":
                dfs(r,0)
        for r in range(rows):
            if board[r][cols-1]=="O":
                dfs(r,cols-1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
                if board[r][c]=="S":
                    board[r][c]="O"
        
        
        return board


objO=XOXO()
print("XOXO board")
print(objO.solution(board))
        

gridEn = [
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]
    
class Enclave:
    def isEnclave(self,gridEn):
        rows=len(gridEn)
        cols=len(gridEn[0])
        visited=[[False]*cols for _ in range(rows)]
        
        directions=[
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]
        q=deque() 

        for c in range(cols):
            if gridEn[0][c]==1:
                q.append((0,c))
                visited[0][c]=True
            if gridEn[rows-1][c]:
                q.append((rows-1,c))
                visited[rows-1][c]=True

        for r in range(rows):
            if gridEn[r][0]==1 and not visited[r][0]:
                q.append((r,0))
                visited[r][0]=True

            if gridEn[r][cols-1]==1 and not visited[r][cols-1]:
                q.append((r,cols-1))
                visited[r][cols-1]=True

        while q:
            pr,pc=q.popleft()
            for dr,dc in directions:
                nr=pr+dr
                nc=pc+dc

                if (0<=nr<rows and
                    0<=nc<cols and
                    gridEn[nr][nc]==1 and
                    not visited[nr][nc]):
                    q.append((nr,nc))
                    visited[nr][nc]=True

        count=0
        for r in range(rows):
            for c in range(cols):
                if gridEn[r][c]==1 and not visited[r][c]:
                    count+=1

        return count
    
enclave=Enclave()
print("enclave land")
print(enclave.isEnclave(gridEn))


                
gridd = [
    [1, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 0]
]

class DistinctIslands:
    def count(self,gridd):
        rows=len(gridd)
        cols=len(gridd[0])

        visited=[[False]*cols for _ in range(rows)]

        shapes=set()
        directions=[
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]
        def dfs(r,c,baseRow,baseCol,shape):
            visited[r][c]=True

            shape.append(
                (
                    r-baseRow,
                    c-baseCol
                )
            )

            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if(0<=nr<rows and
                   0<=nc<cols and 
                   gridd[nr][nc]==1 and not
                   visited[nr][nc]):
                    dfs(nr,nc,baseRow,baseCol,shape)    
                    
        for r in range(rows):
                for c in range(cols):
                    if gridd[r][c]==1 and not visited[r][c]:
                        shape=[]
                        dfs(r,c,r,c,shape)
                        shapes.add(tuple(shape))
        return len(shapes)

distinct=DistinctIslands()
print("distinct Islands")
print(distinct.count(gridd))


class Bipartite:
    
    def bfs(self,start,adj,color):
        q=deque()
        color[start]=0
        q.append(start)

        while q:
            node=q.popleft()

            for neighbor in adj[node]:
                if color[neighbor]==-1:
                    color[neighbor]=1-color[node]
                    q.append(neighbor)
                elif color[neighbor]==color[node]:
                    return False
                
        return True

    def isBipartite(self,adj,n):
        color=[-1]*n

        for node in range(n):
            if color[node]==-1:
                if not self.bfs(node,adj,color):
                    return False
                
        return True

bipartite=Bipartite()
print("check bipartite using BFS")
print(bipartite.isBipartite(adj,n))



class DFSBipartite:
    def dfs(self,node,adj,color):
        for neighbor in adj[node]:
            if color[neighbor]==-1:
                color[neighbor]=1-color[node]
                if not self.dfs(neighbor,adj,color):
                    return False

            elif color[neighbor]==color[node]:
                return False
            
        return True      

    

    def isBipartite(self,n,adj):
        color=[-1]*n

        for node in range(n):
            if color[node]==-1:
                color[node]=0
                if not self.dfs(node,adj,color):
                    return False
        return True
    

dfsBipartite=DFSBipartite()
print("DFS Bipartite")
print(dfsBipartite.isBipartite(n,adj))


class PathVisited:
    def dfs(self,node,adj,visited,pathVisited):
        visited[node]=True
        pathVisited[node]=True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                if self.dfs(neighbor,adj,visited,pathVisited):
                    return True
                
                
            elif pathVisited[neighbor]:
                return True
        pathVisited[node]=False
        return False

    def isVisied(self,n,adj):
        visited=[False]*n
        pathVisited=[False]*n

        for node in range(n):
            if not visited[node]:
                if self.dfs(node,adj,visited,pathVisited):
                    return True


        return False
    
isVisited=PathVisited()
print("is the graph forms a cycle")
print(isVisited.isVisied(n,adj))


graph = [
    [1],
    [2],
    [3],
    [1],
    [5],
    [],
    []
]


class safeNode:
    def dfs(self,node,graph,visited,pathVisited,check):
        visited[node]=1
        pathVisited[node]=1
        for neighbor in graph[node]:
            
            if visited[neighbor]==0:
                if self.dfs(neighbor,graph,visited,pathVisited,check):
                    return True
                
            elif pathVisited[neighbor]==1:
                return True
            
        pathVisited[node]=0
        check[node]=1
        return False
    def isSafe(self,graph):
        v=len(graph)
        visited=[0]*v
        pathVisited=[0]*v
        check=[0]*v
        for node in range(v):
            if visited[node]==0:
                self.dfs(node,graph,visited,pathVisited,check)
            
        ans=[]
        for i in range(v):

            if check[i]==1:
                ans.append(i)

        return ans
    
safeObj=safeNode()
print("if graph is safe")
print(safeObj.isSafe(graph))

topo = [
        [],
        [],
        [3],
        [1],
        [0,1],
        [0,2]
    ]

class topological:
    def dfs(self,node,visited,topo,stack):
        visited[node]=True
        for neighbor in topo[node]:
            if not visited[neighbor]:
                self.dfs(neighbor,visited,topo,stack)
        stack.append(node)

    def topoSort(self,topo):
        n=len(topo)
        visited=[False]*n
        stack=[]
        for node in range(n):            
            if not visited[node]:
                self.dfs(node,visited,topo,stack)

        return stack[::-1]
    
topologic=topological()
print("topological sort for DAG")
print(topologic.topoSort(topo))



class kahns:

    def topological(self,topo):
        n=len(topo)
        indegree=[0]*n
        q=deque()
        for node in range(n):
            for neighbor in topo[node]:
                indegree[neighbor]+=1
            
        for i in range(n):
            if indegree[i]==0:
                q.append(i)
        topos=[]
        while q:
            node=q.popleft()
            topos.append(node)
            for neighbor in topo[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    q.append(neighbor)

        return topos

kahnstopo=kahns()
print("kahns topological order using indegrees")
print(kahnstopo.topological(topo))


class kahns1:
    def topos(self,topo):
        n=len(topo)
        indegree=[0]*n
        for node in range(n):
            for neighbor in topo[node]:
                indegree[neighbor]+=1

        q=deque()
        for i in range(n):
            if indegree[i]==0:
                q.append(i)
        count=0
        while q:
            node=q.popleft()
            count+=1
            for neighbor in topo[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    q.append(neighbor)

        if count==n:
            return True
    
kahnstopo=kahns1()
print("G-23. Detect a Cycle in Directed Graph | Topological Sort | Kahn's Algorithm | BFS")
print(kahnstopo.topos(topo))


numCourses = 4

prerequisites = [
    [1,0],
    [2,0],
    [3,1],
    [3,2]
]

class classScheduling1:
    def schedule(self,numCourses,prerequisites):
        
        adj=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses 
        for course,requisite in prerequisites:
            adj[requisite].append(course)
            indegree[course]+=1
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        count=0
        while q:
            node=q.popleft()
            count+=1
            for neighbor in adj[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    q.append(neighbor)
        

        return count==numCourses

schedule=classScheduling1()
print("class scheduling")
print(schedule.schedule(numCourses,prerequisites))


class classScheduling2:
    def findOrder(self,numCourses,prerequisites):
        adj=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        for course,req in prerequisites:
            adj[req].append(course)
            indegree[course]+=1

        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        topo=[]
        while q:
            node=q.popleft()
            topo.append(node)
            for neighbors in adj[node]:
                indegree[neighbors]-=1
                if indegree[neighbors]==0:
                    q.append(neighbors)

        if len(topo)!=numCourses:
            return []
        
        return topo

class2=classScheduling2()
print("class schedulin 2")
print(class2.findOrder(numCourses,prerequisites))




class findsafenodes:

    def solution(self,topo):
        n=len(topo)
        revAdj=[[]for _ in range(n)]
        indegree=[0]*n
        for node in range(n):
            for neighbor in topo[node]:
                revAdj[neighbor].append(node)
                indegree[node]+=1

        q=deque()

        for i in range(n):
            if indegree[i]==0:
                q.append(i)
        sage=[]
        while q:

            node=q.popleft()
            sage.append(node)
            for neighbor in revAdj[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    q.append(neighbor)

        return sorted(sage)
    
sageNode=findsafenodes()
print("print sage nodes")
print(sageNode.solution(topo))


alien_dict = [
    "baa",
    "abcd",
    "abca",
    "cab",
    "cad"
]

K = 4
class alienLang:
    def solution(self,alien_dict,k):
        n=len(alien_dict)   
        adj=[[]for _ in range(k)]

        for i in range(n-1):
            s1=alien_dict[i]
            s2=alien_dict[i+1]

            length=min(len(s1),len(s2)) 
            for ptr in range(length):
                if s1[ptr]!=s2[ptr]:
                    u=ord(s1[ptr])-ord('a')
                    v=ord(s2[ptr])-ord('a')

                    adj[u].append(v)
                    break

        indegree=[0]*k
        q=deque()
        for node in range(k):
            for neighbor in adj[node]:
                indegree[neighbor]+=1

        for i in range(k):
                if indegree[i]==0:
                    q.append(i)
        stack=[]
        while q:
            node=q.popleft()
            stack.append(node)
            for neighbors in adj[node]:
                indegree[neighbors]-=1
                if indegree[neighbors]==0:
                    q.append(neighbors)

        ans=""
        for i in stack:
            ans+=chr(i+ord('a'))

            
        return ans
    
aliendict=alienLang()
print("alien dict")
print(aliendict.solution(alien_dict,K))


Nlen = 4
edges = [
    [0, 1, 5],  # Node 0 points to Node 1 with a weight/distance of 5
    [0, 2, 2],  # Node 0 points to Node 2 with a weight/distance of 2
    [2, 3, 3],  # Node 2 points to Node 3 with a weight/distance of 3
    [1, 3, 1]   # Node 1 points to Node 3 with a weight/distance of 1
]

class distanceFromNodes:
    def dfs(self,node,adj,stack,visited):
        visited[node]=True
        for neighbor,weight in adj[node]:
            if not visited[neighbor]:
                self.dfs(neighbor,adj,stack,visited)

        stack.append(node)
            

    def distance(self,edges,Nlen):
        adj=defaultdict(list)
        for u,v,wt in edges:
            adj[u].append((v,wt))

        visited=[False]*Nlen
        stack=[]
        for i in range(Nlen):
            if visited[i]==False:
                self.dfs(i,adj,stack,visited)

        dist=[float('inf')]*Nlen
        dist[0]=0

        while stack:
            node=stack.pop()
            for neighbor,weights in adj[node]:
                if dist[node]!=float('inf'):
                    if dist[node]+weights<dist[neighbor]:
                        dist[neighbor]=dist[node]+weights
        for i in range(Nlen):
                if dist[i]==float('inf'):
                    dist[i]=-1
        return dist
    
shortestdist=distanceFromNodes()
print("shortest distance from node")
print(shortestdist.distance(edges,Nlen))
                    

unitedges = [
    [0,1],
    [0,3],
    [1,2],
    [3,4],
    [4,5],
    [5,6],
    [2,6],
    [6,7],
    [7,8],
    [6,8]
]

class unitDistance:
    def solution(self,unitedges,length):
        src=0
        
        dist=[float('inf')]*length
        adj=[[]for _ in range(length)]
        for u,v in unitedges:
            adj[u].append(v)

        dist[src]=0

        q=deque()

        # for i in range(length):
        #     if dist[i]!=float('inf'):
        #         q.append(i)

        q.append(0)

        while q:
            node=q.popleft()

            for neighbor in adj[node]:
                if dist[node]+1<dist[neighbor]:
                    dist[neighbor]=dist[node]+1

                    q.append(neighbor)

        for i in range(length):
            if dist[i]==float('inf'):
                dist[i]=-1

        return dist
unit=unitDistance()
print("unit distance lengths shortest distance")
print(unit.solution(unitedges,9))


beginWord = "hit"
endWord = "cog"

wordList = [
    "hot",
    "dot",
    "dog",
    "lot",
    "log",
    "cog"
]

class wordLadder:
    def solution(self,beginWord,endWord,wordList):
        st=set(wordList)
        q=deque()
        q.append((beginWord,1))

        if beginWord in st:
            st.remove(beginWord)
        while q:
            word,step=q.popleft()
            if word ==endWord:
                return step
            for i in range(len(word)):
                for ch in range(ord('a'),ord('z')+1):
                    newWord=(
                        word[:i]
                        +chr(ch)
                        +word[i+1:]
                    )

                    if newWord in st:
                        st.remove(newWord)
                        q.append((newWord,step+1))
        return 0
            
                
wordlad=wordLadder()
print("word ladder")
print(wordlad.solution(beginWord,endWord,wordList))


class wordLadder2:
    def solution(self,beginWord,endWord,wordList):
        q=deque()
        usedOnlevel=[beginWord]
        level=1
        q.append([beginWord])
        st= set(wordList)
        ans=[]
        while q:
            path=q.popleft()

            if len(path)>level:
                level+=1    
                for word in usedOnlevel:
                    if word in st:
                        st.remove(word)
                usedOnlevel=[]

            word=path[-1]
            if word==endWord:
                if len(ans)==0:
                   ans.append(path)

                elif len(ans[0])==len(path):
                    ans.append(path)
            for i in range(len(word)):
                for ch in range(ord('a'),ord('z')+1):
                    newWord=(
                        word[:i]
                        +chr(ch)
                        +word[i+1:]
                    )
                    if newWord in st:
                        newPath=path[:]
                        newPath.append(newWord)
                        q.append(newPath)
                        usedOnlevel.append(newWord)
        return ans
            
wordlad2=wordLadder2()
print("word ladder 2 for printing the words-- brute force, so lite")
print(wordlad2.solution(beginWord,endWord,wordList))


class wordLadderdfs:
    def solution(self,beginWord,endWord, wordList):
        st=set(wordList)
        q=deque()
        mp={}
        q.append(beginWord)
        mp[beginWord]=1
        
        while q:
            word=q.popleft()
            steps=mp[word]
            if word==endWord:
                break

            if word in st:
                st.remove(word)

            for i in range(len(word)):
                for ch in range(ord('a'),ord('z')+1):
                    newWord=(
                        word[:i]
                        +chr(ch)
                        +word[i+1:]
                    )
                    if newWord in st:
                        mp[newWord]=steps+1
                        q.append(newWord)
                        st.remove(newWord)
        ans=[]
        if endWord in mp:
            seq=[endWord]
            self.dfs(
                endWord,
                beginWord,
                seq,
                mp,
                ans
            )
            return ans
        
    def dfs(
                self,
                word,
                beginWord,
                seq,
                mp,
                ans
        ):
            if word==beginWord:
                temp=seq[::-1]
                ans.append(temp)
                return
            steps=mp[word]

            for i in range(len(word)):
                for ch in range(ord('a'),ord('z')+1):
                    prevWord=(
                        word[:i]
                        +chr(ch)
                        +word[i+1:]
                    )
                    if prevWord in mp and mp[prevWord]+1==steps:
                        seq.append(prevWord)
                        self.dfs(
                            prevWord,
                            beginWord,
                            seq,
                            mp,
                            ans
                        )
                        seq.pop()

wordo=wordLadderdfs()
print("word ladder printing with dfs")
print(wordo.solution(beginWord,endWord,wordList))


dijadj = [
    [[1, 4], [2, 1]],  # Neighbors of Node 0: (Node 1, wt 4), (Node 2, wt 1)
    [],                # Neighbors of Node 1
    [[3, 2]],          # Neighbors of Node 2: (Node 3, wt 2)
    []                 # Neighbors of Node 3
]



class dijkstra:
    def solution(self,dijadj,s):
        v=len(dijadj)
        dist=[float('inf')]*v
        dist[s]=0
        pq=[(0,dist[0])]
        
        while pq:
            dis,node=heapq.heappop(pq)
            if dis>dist[node]:
                continue
            for neighbor,weight in dijadj[node]:
                if weight+dis<dist[neighbor]:
                    dist[neighbor]=weight+dis
                    heapq.heappush(pq,
                        (dist[neighbor],neighbor)
                    )

        return dist
    
dijkstra=dijkstra()
print("most awaited dijkstra")
print(dijkstra.solution(dijadj,0))



class setDijkstra:
    def solution(self,dijadj,s):
        v=len(dijadj)
        dist=[float('inf')]*v
        st=SortedSet()
        dist[s]=0
        st.add((0,s))

        while st:
            dis,node=st[0]
            st.remove((dis,node))
            for neighbor,wt in dijadj[node]:
                if dis+wt < dist[neighbor]:
                    if dist[neighbor]!=float('inf'):
                        st.discard(
                            (dist[neighbor],
                             neighbor)
                        )

                    dist[neighbor]=dis+wt

                    st.add(
                        (
                            dist[neighbor],neighbor 
                        )
                    )
        return dist

setdij=setDijkstra()
print("dijkstra using set dt")
print(setdij.solution(dijadj,0))
            
n = 5

edges = [
    [1,2,2],
    [1,4,1],
    [2,5,5],
    [4,3,3],
    [3,5,1]
]

class shortestPath:
    def Dijkstra(self,n,edges):
        adj=[[]for _ in range(n+1)]
        for u,v,wt in edges:
            adj[u].append((v,wt))
            adj[v].append((u,wt))
        dist=[float('inf')]*(n+1)
        parent=[i for i in range(n+1)]
        pq=[]
        dist[1]=0
        heapq.heappush(pq,(0,1))

        while pq:
            dis,node=heapq.heappop(pq)
            for neighbor,wt in adj[node]:
                if dis+wt<dist[neighbor]:
                    dist[neighbor]=dis+wt
                    heapq.heappush(pq,
                        (dist[neighbor],neighbor)
                    )
                    parent[neighbor]=node

        if dist[n]==float('inf'):
            return [-1]
        
        res=[]
        node=n
        while parent[node]!=node:
            res.append(node)
            node=parent[node]
        res.append(1)
        res.reverse()

        return res
    
shortestPathtoNode=shortestPath()
print("shortest path to node given")
print(shortestPathtoNode.Dijkstra(n,edges))
            

grid = [
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]
source = (0, 0)
destination = (3, 3)

class BinaryMaze:
    def maze(self,grid,source,destination):
        n=len(grid)
        m=len(grid[0])
        srcRow,srcCol=source
        desRow,desCol=destination
        dist=[[float('inf')]*m for _ in range(n)]
        q=deque()
        dist[srcRow][srcCol]=0
        q.append((0,srcRow,srcCol))
        directions=[
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]

        while q:
            dis,row,col=q.popleft()

            for nr,nc in directions:
                newRow=row+nr
                newCol=col+nc
                if srcRow==desRow and srcCol==desCol:
                    return 0

                if (0<=newRow<n and
                    0<=newCol<m and
                    grid[newRow][newCol]==1):
                    if dis+1<dist[newRow][newCol]:
                        dist[newRow][newCol]=dis+1

                        if (newRow==desRow and newCol==desCol):
                            return dis+1
                    
                        q.append(
                            (dis+1,
                            newRow,
                            newCol)
                        )
        return -1
                    
binaryMaze=BinaryMaze()
print("binary maze length between given coordinates")
print(binaryMaze.maze(grid,source,destination))

heights = [
 [1,2,2],
 [3,8,2],
 [5,3,5]
]

class MinEffort:
    def mineffort(self,heights):
        n=len(heights)
        m=len(heights[0])
        dist=[[float('inf')]*m for _ in range(n)]
        dist[0][0]=0
        pq=[]
        heapq.heappush(pq,(0,0,0))
        directions=[
            (1,0),
            (-1,0),
            (0,-1),
            (0,1)
        ]

        while pq:
            efforts,row,col=heapq.heappop(pq)
            if row==n-1 and col==m-1:
                return efforts

            for dr,dc in directions:
                nr=row+dr
                nc=col+dc

                if (0<=nr<n and 0<=nc<m):
                    newEffort=max(efforts,
                                  abs(heights[row][col]
                                      -heights[nr][nc]
                                      ))
                    if newEffort<dist[nr][nc]:
                        dist[nr][nc]=newEffort
                        heapq.heappush(pq,(newEffort,nr,nc))
        return 0

miniEffort=MinEffort()
print("minimum effort to reach last point")
print(miniEffort.mineffort(heights))

n = 4

flights = [
    [0,1,100],
    [1,2,100],
    [2,3,100],
    [0,3,500]
]

src = 0
dst = 3
k = 1
class FlightWithKstops:
    def solution(self,n,flights,src,dst,k):
        adj=[[]for _ in range(n)]
        for u,v,price in flights:
            adj[u].append((v,price))
        dist=[float('inf')]*n
        dist[src]=0
        q=deque()
        q.append((0,src,0))
        while q:
            
            stop,node,price=q.popleft()
            if stop>k:
                continue
            for neighbor,wt in adj[node]:
                newPrice=price+wt
                if (newPrice<dist[neighbor] and stop<=k):
                    dist[neighbor]=newPrice
                    q.append((  
                        stop+1,
                        neighbor,
                        newPrice)
                    )

        if dist[dst]==float('inf'):
            return [-1]
        return dist[dst]

flightObj=FlightWithKstops()
print("minimum cost of flight with k stops")
print(flightObj.solution(n,flights,src,dst,k))

arr = [2,5,7]

start = 3
end = 30
class Multiplier:
    def solution(self,arr,start,end):
        mod=100000
        dist=[float('inf')]*mod
        q=deque()
        q.append((0,start))
        dist[start]=0

        while q:
            step,node=q.popleft()
            for multiplier in arr:
                newVal=(node*multiplier)%mod
                if step+1<dist[newVal]:
                    dist[newVal]=step+1
                    if newVal==end:
                        return step+1
                    
                    q.append((step+1,newVal))
        return [-1]
    
multiplier=Multiplier()
print("Multiplier in array")
print(multiplier.solution(arr,start,end))

n = 7

roads = [
 [0,6,7],
 [0,1,2],
 [1,2,3],
 [1,3,3],
 [6,3,3],
 [3,5,1],
 [6,5,1],
 [2,5,1],
 [0,4,5],
 [4,6,2]
]
class CountPaths:
    def paths(self,roads,n):
        mod=10**9+7
        adj=[[]for _ in range(n)]
        for u,v,path in roads:
            adj[u].append((v,path))
            adj[v].append((u,path))
        dist=[float('inf')]*n
        ways=[0]*n
        ways[0]=1
        dist[0]=0
        pq=[]
        heapq.heappush(pq,(0,0))

        while pq:
            dis,node=heapq.heappop(pq)
            if dis>dist[node]:
                continue
            for neighbor,wt in adj[node]:
                newPath=dis+wt
                if newPath<dist[neighbor]:
                    dist[neighbor]=newPath
                    ways[neighbor]=ways[node]

                    heapq.heappush(pq,(newPath,neighbor)) 
                elif newPath==dist[neighbor]:
                    ways[neighbor]=(ways[neighbor]+ways[node])%mod
        return ways[n-1]%mod

pathCount=CountPaths()
print("printing all number of possible paths to destination")
print(pathCount.paths(roads,n))



belledges = [
    (0, 1, 4),
    (0, 2, 5),
    (1, 2, -2),
    (2, 3, 3)
]

class Bellman:
    def ford(self,n,belledges,source):
        dist=[float('inf')]*n
        dist[source]=0

        for _ in range(n-1):
            for u,v,w in belledges:
                if dist[u]!=float('inf') and dist[u]+w<dist[v]:
                    dist[v]=dist[u]+w

        for u,v,w in belledges:
            if dist[u]!=float('inf') and dist[u]+w<dist[v]:
                print("negative cycle found")
                return
        return dist

bellmanFord=Bellman()
print("bellman ford")
print(bellmanFord.ford(4,belledges,0))


INF=float('inf')
floydgraph = [
    [0, 4, 11],
    [INF, 0, 2],
    [3, INF, 0]
]

def floydWarshall(floydgraph):
    n=len(floydgraph)
    dist=[row[:] for row in floydgraph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])

    return dist

warshall=floydWarshall(floydgraph)
print("floyd warshall graph")
for row in warshall:
    print (row)

cityedges = [
    [0, 1, 3],
    [1, 2, 1],
    [1, 3, 4],
    [2, 3, 1]
]
class FindCity:
    def solution(self,cityedges,threshold):
        n=len(cityedges)
        dist=[[float('inf')]*n for _ in range(n)]
        for i in range(n):
            dist[i][i]=0
        for u,v,wt in cityedges:
            dist[u][v]=wt
            dist[v][u]=wt

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])

        
        cityno=-1
        minCount=float('inf')
        for city in range(n):
            count=0
            for adjCity in range(n):
                if dist[city][adjCity]<=threshold:
                    count+=1

            if count<=minCount:
                minCount=count
                cityno=city
        return cityno

findCity=FindCity()
print("finding city within distance threshold")
print(findCity.solution(cityedges,4))  

stree=[(0,1,2),
(0,2,6),
(0,3,3),
(1,3,5),
(2,3,4)]

class MinimumSpanningTree:
    def span(self,stree):
        n=len(stree)
        adj=[[]for _ in range(n)]
        for u,v,wt in stree:
            adj[u].append((wt,v))
            adj[v].append((wt,u))
        
        vis=[0]*n
        pq=[]
        heapq.heappush(pq,(0,0))
        res=0
        while pq:
            dis,node=heapq.heappop(pq)
            if vis[node]:
                continue

            vis[node]=1
            res+=dis
            for wt,neighbor in adj[node]:
                if not vis[neighbor]:
                    heapq.heappush(pq,(wt,neighbor))
        return res
    
mst=MinimumSpanningTree()
print("Minimum Spanning Tree")
print(mst.span(stree))


class DisjointSet:
    def __init__(self,n):
        self.rank=[0]*(n+1)
        self.size=[1]*(n+1)
        self.parent=[i for i in range(n+1)]


    def findPar(self,node):
        if node==self.parent[node]:
            return node
        self.parent[node]=self.findPar(self.parent[node])
        return self.parent[node]

    def unionByRank(self,u,v):
        ulp_u=self.findPar(u)
        ulp_v=self.findPar(v)
        if ulp_u==ulp_v:
            return 
        
        if self.rank[ulp_u]<self.rank[ulp_v]:
            self.parent[ulp_u]=ulp_v

        elif self.rank[ulp_v]<self.rank[ulp_u]:
            self.parent[ulp_v]=ulp_u

        else:
            self.parent[ulp_v]=ulp_u
            self.rank[ulp_v]+=1
    def unionBySize(self,u,v):
        ulp_u=self.findPar(u)
        ulp_v=self.findPar(v)

        if ulp_u==ulp_v:
            return

        if self.size[ulp_u]<self.size[ulp_v]:
            self.parent[ulp_u]=ulp_v
            self.size[ulp_v]+=self.size[ulp_u]

        else:
            self.parent[ulp_v]=ulp_u
            self.size[ulp_u]+=self.size[ulp_v]


ds=DisjointSet(7)
ds.unionBySize(1,2)
ds.unionBySize(2,3)
ds.unionBySize(4,5)

print("Disjoint set")
print(ds.findPar(3))

print(ds.findPar(3)==ds.findPar(5))


# The index of the list represents the node ID: 0, 1, 2, 3
kedges = [
    [(1, 5), (2, 6), (3, 2)],  # Node 0 connects to: 1 (wt 5), 2 (wt 6), 3 (wt 2)
    [(0, 5), (3, 3)],          # Node 1 connects to: 0 (wt 5), 3 (wt 3)
    [(0, 6), (3, 4)],          # Node 2 connects to: 0 (wt 6), 3 (wt 4)
    [(0, 2), (1, 3), (2, 4)]   # Node 3 connects to: 0 (wt 2), 1 (wt 3), 2 (wt 4)
]

class Kruskals:
    def solutions(self, kedges):
        n=len(kedges)
        edges=[]
        for node in range(n):
            for neighbor, wt in kedges[node]:
                edges.append((wt,node,neighbor))

        edges.sort()
        mstWeight=0

        ds=DisjointSet(n)
        for wt,u,v in edges:
            if ds.findPar(u)!=ds.findPar(v):
                mstWeight+=1

            ds.unionBySize(u,v)

        return mstWeight
    

kruskals=Kruskals()
print("kruskals algo")
print(kruskals.solutions(kedges))

disadj = [
 [1,1,0],
 [1,1,0],
 [0,0,1]
]
class pracDisjointSet:
    def __init__(self, v):
        self.size=[1]*v
        self.parent=[i for i in range(v)]

    def findPar(self,node):
        if node==self.parent[node]:
            return node
        self.parent[node]=self.findPar(
            self.parent[node]
        )
        return self.parent[node]
        
    def unionBySize(self,u,v):
        ulp_u=self.findPar(u)
        ulp_v=self.findPar(v)
        if ulp_u==ulp_v:
            return
        
        if self.size[ulp_u]<self.size[ulp_v]:
            self.parent[ulp_u]=ulp_v
            self.size[ulp_v]+=self.size[ulp_u]

        else:
            self.parent[ulp_v]=ulp_u
            self.size[ulp_u]+=self.size[ulp_v]


class numProvinces:
    def solution(self,disadj,v):
        ds=pracDisjointSet(v)

        for i in range(v):
            for j in range(v):
                if disadj[i][j]==1:
                    ds.unionBySize(i,j)

        count=0

        for node in range(v):
            if ds.findPar(node)==node:
                count+=1

        return count
    
numprov=numProvinces()
print("number of provinces")
print(numprov.solution(disadj,3))

        


nc = 6

connections = [
    [0,1],
    [0,2],
    [0,3],
    [1,2],
    [1,3]
]
class makeConnections:
    def solution(self,nc,connections):
        ds=pracDisjointSet(nc)
        extraEdges=0
        for u, v in connections:
            if ds.findPar(u)==ds.findPar(v):
                extraEdges+=1

            else:
                ds.unionBySize(u,v)

        connectionsNum=0
        for node in range(nc):
            if ds.findPar(node)==node:
                connectionsNum+=1

        req=connectionsNum-1

        if extraEdges>=req:
            return req
        return -1

makeCon=makeConnections()
print("make connections")
print(makeCon.solution(nc,connections))



n=3
class disjointList:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.size=[1]*n

    def findUpar(self,node):
        if node ==self.parent[node]:
            return node        
        node=self.findUpar(self.parent[node])

        return self.parent[node]
    
    def unionBySize(self,u,v):
        ulp_u=self.findUpar(u)
        ulp_v=self.findUpar(v)
        if ulp_u==ulp_v:
            return
        
        if self.size[ulp_u]<self.size[ulp_v]:
            self.parent[ulp_u]=ulp_v
            self.size[ulp_v]+=self.size[ulp_u]

        else:
            self.parent[ulp_v]=ulp_u
            self.size[ulp_u]+=self.size[ulp_v]
        
            
n=3
inputs=[
 ["John","johnsmith@mail.com","john_newyork@mail.com"],
 ["John","johnsmith@mail.com","john00@mail.com"],
 ["Mary","mary@mail.com"]
]
class MailMerging:
    def solution(self,inputs):
        n=len(inputs)
        mailsList={}
        ds=disjointList(n)
        for i in range(n):
            for j in range(1,len(inputs[i])):
                mail=inputs[i][j]
                if mail not in mailsList:
                    mailsList[mail]=i

                else:
                    ds.unionBySize(i,mailsList[mail])

        mergedMails=[[] for i in range(n)]

        for mails,node in mailsList.items():
            root=ds.findUpar(node)
            mergedMails[root].append(mails)
            
        ans=[]
        for i in range(n):
            if len(mergedMails[i])==0:
                continue
            mergedMails[i].sort()
            temp=[inputs[i][0]]
            temp.extend(mergedMails[i])
            ans.append(temp)

        return ans
    
mailmer=MailMerging()
print("finding the mails of ultimate parent")
print(mailmer.solution(inputs))




n = 4
m = 5

# The sequence of coordinate queries (Add land at these positions one by one)
operators = [
    [1, 1],  # 1st query: Creates a single standalone island
    [0, 1],  # 2nd query: Connects directly with cell (1,1) -> row 0 adjacent to row 1
    [3, 3],  # 3rd query: Creates a completely new isolated island in the corner
    [3, 4]   # 4th query: Connects with cell (3,3) -> col 4 adjacent to col 3
]
class disJointSets:
    def __init__(self,n):
        self.size=[1]*n
        self.parent=[i for i in range(n)]
    
    def findUpar(self,node):
        if node==self.parent[node]:
            return node
        
        self.parent[node]=self.findPar(self.parent[node])
        return self.parent[node]

    def unionBySize(self,u,v):
        ulp_u=self.findUpar(u)
        ulp_v=self.findUpar(v)

        if ulp_u==ulp_v:
            return
        
        if self.size[ulp_u]<self.size[ulp_v]:
            self.parent[ulp_u]=ulp_v
            self.size[ulp_v]+=self.size[ulp_u]

        else:
            self.parent[ulp_v]=ulp_u
            self.size[ulp_u]+=self.size[ulp_v]

class Islands:
    def solution(self,n,m,operators):

        ans=[]
        vis=[[0]*m for _ in range(n)]

        dr=[-1,0,1,0]
        dc=[0,1,0,-1]
        ds=disJointSets(n*m)

        count=0

        for row, col in operators:
            if vis[row][col]:
                ans.append(count)
                continue
            
            vis[row][col]=1
            count+=1
            nodeNo=row*m+col
            for k in range(4):
                nr=row+dr[k]
                nc=col+dc[k]

                if (0<=nr<n and 0<=nc<m and vis[nr][nc]):
                    adjNode= nr*m+nc

                    if (ds.findUpar(nodeNo)!=ds.findUpar(adjNode)):
                        count-=1

                        ds.unionBySize(nodeNo,adjNode)

            ans.append(count)

        return ans

isl=Islands()
print("Islands List")
print(isl.solution(n,m,operators))


grid = [
    [1, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]
    

class disJointSetIsland:
    def __init__(self,n):
        self.size=[1]*n
        self.parent=[i for i in range(n)]

    def findUpar(self,node):
        if node==self.parent[node]:
            return node
        self.parent[node]=self.findUpar(self.parent[node])
        return self.parent[node]
    
    def unionBySize(self,u,v):
        ulp_u=self.findUpar(u)
        ulp_v=self.findUpar(v)

        if ulp_u==ulp_v:
            return

        if self.size[ulp_u]<self.size[ulp_v]:
            self.parent[ulp_u]=ulp_v
            self.size[ulp_v]+=self.size[ulp_u]
        else:
            self.parent[ulp_v]=ulp_u
            self.size[ulp_u]+=self.size[ulp_v]



class LargestIsland:
    def solution(self,grid):
        n=len(grid)
        dr=[-1,0,1,0]
        dc=[0,1,0,-1]
        ds=disJointSetIsland(n*n)
        for row in range(n):
            for col in range(n):
                if grid[row][col]==0:
                    continue
                node=row*n+col
                for k in range(4):
                    nr=row+dr[k]
                    nc=col+dc[k]
                    if (0<=nr<n and 0<=nc<n and grid[nr][nc]==1):
                        adjNode=nr*n+nc
                        ds.unionBySize(node,adjNode)

        ans=0

        for row in range(n):
            for col in range(n):
                if grid[row][col]==1:
                    continue
                components=set()
                for k in range(4):
                    nr=row+dr[k]
                    nc=col+dc[k]
                    if (0<=nr<n and 0<=nc<n and grid[nr][nc]==1):
                        parent=ds.findUpar(nr*n+nc)
                        components.add(parent)
                count=1 
                for parent in components:
                    count+=ds.size[parent]
                ans=max(ans,count)

        for cell in range(n*n):
            ans=max(ans,ds.size[ds.findUpar(cell)])
        return ans

largest=LargestIsland()
print("largest island")
print(largest.solution(grid))
                    

class disJointSetStone:
    def __init__(self,n):
        self.size=[1]*n
        self.parent=[i for i in range(n)]

    def findUpar(self,node):
        if node==self.parent[node]:
            return node
        self.parent[node]=self.findUpar(self.parent[node])
        return self.parent[node]

    def unionBySize(self,u,v):
        ulp_u=self.findUpar(u)
        ulp_v=self.findUpar(v)
        if ulp_u==ulp_v:
            return
        
        if self.size[ulp_u]<self.size[ulp_v]:
            self.parent[ulp_u]=ulp_v
            self.size[ulp_v]+=self.size[ulp_u]

        else:
            self.parent[ulp_v]=ulp_u
            self.size[ulp_u]+=self.size[ulp_v]

stones = [
    [0, 0], [0, 2],
    [1, 1],
    [2, 0], [2, 2]
]
class Stones:
    def solution(self,stones):
        maxRow=0
        maxCol=0
        for r,c in stones:
            maxRow=max(maxRow,r)
            maxCol=max(maxCol,c)

        ds=disJointSetStone(maxRow+maxCol+2)

        stoneNodes={}
        for r,c in stones:
            rowNode=r
            colNode=c+maxRow+1

            stoneNodes[rowNode]=1
            stoneNodes[colNode]=1

            ds.unionBySize(rowNode,colNode)

        components=0
        for node in stoneNodes:
            if node==ds.findUpar(node):
                components+=1

        return len(stones)-components

stonesclass=Stones()
print("connected stones")
print(stonesclass.solution(stones))


V = 5
adj = [
    [1],       # Node 0 points to 1
    [2, 3],    # Node 1 points to 2 and 3
    [0],       # Node 2 points to 0
    [4],       # Node 3 points to 4
    [3]        # Node 4 points to 3
]


class Solutionss:
    def dfsk(self,node,adj,st,vis):
        vis[node]=1
        for neighbor in adj[node]:
            if not vis[neighbor]:
                self.dfsk(neighbor,adj,st,vis)
        st.append(node)

    def dfs3(self,node,adjT,vis):
            vis[node]=1
            for neighbor in adjT[node]:
                if not vis[neighbor]:
                    self.dfs3(neighbor,adjT,vis)

    def kosarajus(self,V,adj):
            vis=[0]*V
            st=[]
            for i in range(V):
                if not vis[i]:
                    self.dfsk(i,adj,st,vis)

            adjT=[[] for _ in range(V)]
            for i in range(V):
               
                    for neighbor in adj[i]:
                        adjT[neighbor].append(i)

            scc=0
            vis=[0]*V
            while st:
                node=st.pop()
                if not vis[node]:
                    scc+=1
                    self.dfs3(node,adjT,vis)
            return scc

sols=Solutionss()
print("kosarajus")
print(sols.kosarajus(V,adj))


n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]


class Tarjan:
    def __init__(self):
        self.timer=1

    def dfs(self,node,parent,adj,tin,low,vis,bridges):
        vis[node]=1
        tin[node]=self.timer
        low[node]=self.timer   
        self.timer+=1

        for nbr in adj[node]:
            if nbr==parent:
                continue
            if vis[nbr]:
                low[node]=min(low[node],tin[nbr])
            else:
                self.dfs(nbr,node,adj,tin,low,vis,bridges)
                low[node]=min(low[node],low[nbr])
            
            if low[nbr]>tin[node]:
                bridges.append((node,nbr))    

    

    def bridges(self,n,connections):
        adj=[[] for _ in range(n)]
        tin=[0]*n
        low=[0]*n
        vis=[0]*n
        bridges=[]
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)

        self.dfs(0,-1,adj,tin,low,vis,bridges)
        return bridges


tarj=Tarjan()
print("find bridges, tarjan")
print(tarj.bridges(n,connections))


V = 4
adj = [[1, 2], [0, 2, 3], [0, 1], [1]]
# Represents a graph: 
# 0 is connected to 1, 2
# 1 is connected to 0, 2, 3
# 2 is connected to 0, 1
# 3 is connected to 1


class Articulation:
    def __init__(self):
        self.timer=0

    def dfs(self,node,parent,vis,tin,low,mark,adj):
        vis[node]=1
        tin[node]=self.timer
        low[node]=self.timer
        self.timer+=1
        child=0
        for nbr in adj[node]:
            if parent==nbr:
                continue
            if not vis[nbr]:
                self.dfs(nbr,node,vis,tin,low,mark,adj)            
                low[node]=min(low[node],low[nbr])

                if low[nbr]>=tin[node] and parent!=-1:
                    mark[node]=1
                child+=1
            else:
                low[node]=min(low[node],tin[nbr])

        if parent==-1 and child>1:
            mark[node]=1           

            

    def articulation(self,V,adj):
        vis=[0]*V
        tin=[0]*V
        low=[0]*V
        mark=[0]*V
        for i in range(V):
            if not vis[i]:
                self.dfs(i,-1,vis,tin,low,mark,adj)

        ans=[]
        for i in range(V):
            if mark[i]:
                ans.append(i)

        if len(ans)==0:
                return -1
        return ans
    
art=Articulation()
print("articulation")
print(art.articulation(V,adj))

