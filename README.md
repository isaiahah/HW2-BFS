# Assignment 2
Breadth-first search
![BuildStatus](https://github.com/isaiahah/HW2-BFS/workflows/HW2-BFS/badge.svg?event=push)

# Algorithm Overview
Breadth-first search explores the nodes of a graph in order of increasing distance from the start node. It maintains this ordering by placing the discovered neighbours of each explored node into a queue, then selecting the next node by dequeing (returning the oldest discovered node added to the queue).

My algorithm uses the `frontier` array as both the list of all discovered nodes (in order of exploration) and the queue of unexplored nodes. Items toward the start were added oldest and items at the end were added most recently. The `frontier_head` variable stores the index of the array of the oldest unexplored item, so all items before it are explored and all items after it are discovered and unexplored.

The `prev_node` dictionary maps each node to the node which discovered it. This is used for reconstructing paths, as we can backtrack from the end node along the path of discovery to the start node.

The algorithm initializes the start node as discovered and unexplored by adding it at the start of `frontier` and setting `frontier_head` to 0. Then, as long as some node is discovered and unexplored (`frontier_head` is less than the length of `frontier`), it dequeues from the frontier by setting `curr_node` to the item in `frontier` at index `frontier_head` then incrementing `frontier_head`. If that node is the target node, it generates the path from the start node to the end node using `prev_node` and returns that path. Otherwise, it enqueues all neighbours of `curr_node` which were not already discovered or explored (already in the frontier) and records their previous node as `curr_node` in `prev_node`. When the loop finishes, it either returns `None` if a end node was given (to signify no path from the start to end node could be found) or returns the frontier as the list of nodes in exploration order (as the user requested a BFS traversal).
