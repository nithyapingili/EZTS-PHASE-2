def krushkals(graph):
    edge_list=[]
    for source in graph:
        for edge in graph[source]:
            weight,destn=edge
            edge_list.append((weight,source,destn))
    edge_list.sort()
    parents={}
    for vertex in graph:
        parents[vertex]=vertex
        minspantree=[]
    def find_parent(vertex):
        if parents[vertex]!=vertex:
            parents[vertex]=find_parent(parents[vertex])
        return parents[vertex]
    for edge in edge_list:
        weight,source,detn=edge
        if find_parent(source)!=find_parent(destn):
            minspantree.append(edge)
            parents[find_parent(source)]=find_parent(destn)
    print(parents)
    return minspantree

    
'''graph={
    'A':[(1,'E'),(2,'B')],
    'B':[(3,'C'),(2,'D')],
    'C':[(3,'B'),(4,'D'),(7,'F')],
    'D':[(2,'B'),(4,'C'),(2,'E')],
    'E':[(1,'A'),(2,'D'),(3,'G'),(2,'H')],
    'F':[(7,'C'),(1,'G'),(3,'I')],
    'G':[(3,'E'),(9,'H'),(2,'J'),(8,'I'),(1,'F')],
    'H':[(2,'E'),(9,'G'),(2,'J')],
    'I':[(3,'J'),(8,'G'),(3,'F')],
    'J':[(2,'G'),(2,'H'),(3,'I')]
    }'''
graph={
    'A':[(1,'B'),(3,'E')],
    'B':[(1,'A'),(2,'E'),(1,'D'),(4,'C')],
    'C':[(1,'B'),(1,'D')],
    'D':[(1,'B'),(1,'C'),(2,'E')],
    'E':[(1,'A'),(2,'B'),(2,'D')]
    }
minspantree=krushkals(graph)
print(minspantree)
         
         
    
