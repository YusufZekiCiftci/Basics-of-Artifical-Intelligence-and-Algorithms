

graph={
       'A':["B","C"],
       'B':["D","E"],
       'C':["F"],
       'D':[],
       'E':[],
       'F':[],
       }

visit=set()

def dfs(visit,graph,node):
    if node not in visit:
        print(node)
        visit.add(node)
        for neigh in graph[node]:
            dfs(visit,graph,neigh)
            
dfs(visit, graph, 'A')