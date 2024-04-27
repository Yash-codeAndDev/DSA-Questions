# LeetCode 310
"""
Problem Statement :
A tree is an undirected graph in which any two vertices are connected by exactly one path.
In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where
edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and
bi in the tree, you can choose any node of the tree as the root. When you select a node x as
the root, the result tree has height h. Among all possible rooted trees, those with minimum
height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf
"""
from collections import deque

n = 6
edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]


def findMinHeightTrees(n, edges):
    indegree = [0] * n
    adjList = [ [] for _ in range(n)]
    for x in edges:
        indegree[x[0]] += 1
        indegree[x[1]] += 1

        adjList[x[0]].append(x[1])
        adjList[x[1]].append(x[0])

    queue = deque([i for i in range(n) if indegree[i] == 1])

    nodeCount = n
    while nodeCount > 2:
        leave_count = len(queue)
        nodeCount -= leave_count

        for _ in range(leave_count):
            leaf = queue.popleft()
            for neighbour in adjList[leaf]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 1:
                    queue.append(neighbour)


    return  list(queue)

print(findMinHeightTrees(n,edges))