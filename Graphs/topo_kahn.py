# topological soting using kahns algorith 
from collections import deque

graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}

indegree = [0] * len(graph)
ans = []

# count indegree
for i in graph:
  for j in graph[i]:
    indegree[j] +=1 

# push it in a queue
dq = deque()

for i in range(len(indegree)):
  if indegree[i] == 0:
    dq.append(i)

#BFS 
while dq:
  node = dq.popleft()
  ans.append(node)

  #check for neigh

  for neigh in graph[node]:
    indegree[neigh]-=1
    if indegree[neigh] == 0:
      dq.append(neigh)

for i in range(len(ans)):
    print(ans[i])