import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list of nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        # Define frontier as a queue. Implemented as a list and an index of
        # the head, where the tail is the last item. 
        # This enables the full list to act as the order of BFS traversal
        frontier = [start]
        frontier_head = 0
        # Define a dictionary mapping nodes to their parent, for backtracking
        prev_node = {start: None}
        while len(frontier) - frontier_head > 0: # while some node unexplored
            # Pop the next item from the queue
            curr_node = frontier[frontier_head]
            frontier_head += 1
            if curr_node == end: # Return the shortest path
                path = [end] # build path in reverse from the end
                while prev_node[path[-1]] is not None:
                    path.append(prev_node[path[-1]])
                return path[::-1] # Reverse the path for return
            for next_node in self.graph.adj[curr_node]: # Explore neighbours
                if next_node not in frontier: # Nodes in frontier are explored
                    frontier.append(next_node)
                    prev_node[next_node] = curr_node
        # If this loop terminates, end is None or we failed to reach the end
        if end is None: # Return nodes by traversal order
            return frontier
        return None # Failed to find end
