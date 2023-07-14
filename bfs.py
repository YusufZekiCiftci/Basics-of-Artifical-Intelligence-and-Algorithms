
graph ={'A':['B','C'],
         'B':['D','E'],
         'C':['F'],
         'D':[],
         'E':[],
         'F':[],
         }

visit=[]
mass=[]

def bfs(visit,graph,node):
    visit.append(node)
    mass.append(node)
    
    while mass :
        s=mass.pop(0)
        print(s,end="*")
        
        for neigh in graph[s]:
            if neigh not in visit:
                mass.append(neigh)
                

bfs(visit,graph,'A')