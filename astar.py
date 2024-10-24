from tiles import TilesNode
from queue import PriorityQueue



def heuristic(node: TilesNode) -> int:
    """
    Evaluate the heuristic value of the current node.
    This implementation simply counts the number of misplaced tiles.

    Returns
    -------
    heuristic_value : int
        The heuristic value of the current node.
    """


    count=0
    for i in range(len(node.state)):
        for j in range(len(node.state[0])):
            count+=(node.goal_state[i][j]-node.state[i][j])

    return count
        
    #error 
   # raise NotImplementedError("Implement this function as part of the assignment.")


def AStar(root, heuristic: callable) -> TilesNode or None:  # type: ignore
    unexplored = PriorityQueue()
    counter = 0
    unexplored.put((0, counter, root))
    # HINT: PriorityQueue.put() takes a tuple as input
    # To sort the queue items, it uses the first element of each tuple
    # If the first elements are equal, it uses the second element, and so on
    # You may implement a counter to resolve ties
    explored = set()
    explored.add(root)
    g_score = {root: 0}
    f_score = {root: heuristic(root)}
    ##add fscore of current node
    # min(fn)=pop
    #if(fn==gn)
    #return path 
    #else
    #getchildren(fn)=total_children
    #for children in total_children
    # g(children),h(children),f(n)=g(children)+h(children)
    ## Add the child to the priority queue if it hasn’t been explored or if this path to the child is cheaper than any previously discovered one'''

    while not unexplored.empty():
            current_node=unexplored.get()[2]
            if(current_node.is_goal()):
                 return current_node.get_path()
            else:
                 for child in current_node.get_children():
                      if(child not in explored):
                           explored.add(child)
                           g_score[child]=g_score[current_node]+1
                           f_score[child]=heuristic(child)+g_score[child]
                           counter+=1
                           unexplored.put((f_score[child], counter, child))


    return None  # return None if no path was found


