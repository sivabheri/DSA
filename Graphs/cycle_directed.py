# Cycle Detection in a Directed graph - Not DAG

''' 
# we maintain a visited array and path array

so when the element is not visited we mark     visited[ node] = path[node] =  1

again we perfrom    dfs  on its neighbour if neighbour is not visited:

if neighbour is visited  Then there may be a chance of having cycle :

                       so,     if visited [ neigbour ]  and  path[neigbour] == path [ node ] -> Then There is a Cycle 
                                 so we return True


'''
class Solution:
    def dfsCheck(self, node, adj, vis, pathVis):
        vis[node] = 1
        pathVis[node] = 1

        # Traverse for adjacent nodes
        for neighbor in adj[node]:
            # When the node is not visited
            if not vis[neighbor]:
                if self.dfsCheck(neighbor, adj, vis, pathVis):
                    return True
            # If the node has been previously visited
            # but it has to be visited on the same path
            elif pathVis[neighbor]:
                return True

        pathVis[node] = 0  # Backtrack
        return False

    def isCyclic(self, V, adj):
        vis = [0] * V  # Visited array
        pathVis = [0] * V  # Path visited array

        for i in range(V):
            if not vis[i]:  # If the node is not visited
                if self.dfsCheck(i, adj, vis, pathVis):
                    return True
        return False

# Example usage
if __name__ == "__main__":
    # V = 11, E = 11
    adj = [[] for _ in range(11)]
    adj[1].append(2)
    adj[2].append(3)
    adj[3].append(4)
    adj[3].append(7)
    adj[4].append(5)
    adj[5].append(6)
    adj[7].append(5)
    adj[8].append(9)
    adj[9].append(10)
    adj[10].append(8)

    V = 11
    solution = Solution()
    ans = solution.isCyclic(V, adj)
    print("Cycle Exist ? ",end= ' ')
    if ans:
        print("True")
    else:
        print("False")