import collections


def bfs(root, target): 
    graph = {1:[2, 9, 20],
        2:[1, 7, 3],
        3:[2, 5, 4, 6],
        4:[3],
        5:[3],
        6:[3],
        7:[2, 8],
        8:[7],
        9:[1, 10, 14],
        10:[11, 9],
        11:[12, 13, 10],
        12:[11],
        13:[11],
        14:[9, 15, 16],
        15:[14],
        16:[18, 17, 14],
        17:[16],
        18:[19, 16],
        19:[18],
        20:[1],
        }
    def reconstruct(array, v, predecessors):
        array.append(v)
        if v == root:
            return
        else:
            reconstruct(array, predecessors[v], predecessors)
        
    predecessors = {}
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    while queue: 
        vertex = queue.popleft()
        if vertex == target:
            way = []
            reconstruct(way, target, predecessors)
            way.reverse()
            return way
            # return predecessors

        for neighbour in graph[vertex]: 
            if neighbour not in visited: 
                predecessors[neighbour] = vertex
                visited.add(neighbour) 
                queue.append(neighbour) 
    
if __name__ == '__main__':
    print(bfs(5, 19))