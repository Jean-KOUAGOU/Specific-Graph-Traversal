
import numpy as np

def update_reachable_nodes_from(G, reachable_nodes):
    """
    -Input: A list of nodes and a tuple where the first element is an integer, the number of nodes of the graph and
     the second element is the graph itself
    -Algorithm: Finds all rechable nodes from the list of nodes including the list itself
    -Output: Returns a list composed of all reachable nodes in the graph from the given list

    """
    # We initialize a list called Previously_reached_nodes as the input list of nodes
    Previously_reached_nodes = reachable_nodes[:]
    while True: #We repeat the following instructions until the stopping condition is satisfied, that is, until all nodes
        #in Previously_reached_nodes don't have any successor
        Current_reachable_nodes = reachable_nodes[:] # In the loop, we update Current_reachable nodes as reachable nodes
        New_nodes_to_reach = [] #And the list of new nodes to reach is empty at the beginning of each step

        for node in Previously_reached_nodes: # We go through all the nodes in Previously_reached_nodes and find their successors
            #then add them to New_nodes_to_reach and to reachable_nodes
            if node in G[1].keys():
                New_nodes_to_reach.extend(G[1][node])
                reachable_nodes.extend(G[1][node]) 
        reachable_nodes = list(set(reachable_nodes)) # Here we use the function "set" to avoid repetitions of nodes in the list
        New_nodes_to_reach = list(set(New_nodes_to_reach)-set(Current_reachable_nodes)) # Here we remove nodes in New_nodes_to_reach
        # that are already present in Current_reachable_nodes
        Previously_reached_nodes = New_nodes_to_reach[:]   # We update Previously_reached_nodes to be New_nodes_to_reach
        if all([node not in G[1].keys() for node in Previously_reached_nodes]): # Stopping if all nodes in Previously_reached_nodes don't have successor
            break #Stopping keyword
    return reachable_nodes # We return the list of updated reachable nodes


def Full_exploration_starting_nodes(G, output_file_name):
    """
    -Input: A graph and a string. 
    The graph is a dictionary where the keys are nodes and values are lists of nodes directly connected to the key in the
    #direction key-->value
    -Algorithm: Finds a minimum set of starting nodes from which we can explore the whole graph
    -Output: Returns None but creates a txt file containing the nodes found, listed one per line

    """
    # First we check if the input is valid
    assert isinstance(G[1], dict) and isinstance(G[0], int) and isinstance(output_file_name, str), "Wrong input type"
    Size_of_the_graph = G[0] #Number of nodes of the graph
    # Analysis of extreme cases for example if the graph is empty or does not have any edge
    if Size_of_the_graph > 0 and G[1] == {}: # Here no edges but there are nodes
        Key_starting_nodes = list(range(Size_of_the_graph))
    elif Size_of_the_graph == 0: # Here the graph is empty and we should expect the output to be empty as well
        Key_starting_nodes = []
    else:
        #Since the key starting nodes we want to find should necessarily contain all the nodes that do not have an incoming edge, then
        # we initialize the key starting nodes list to contain all those nodes
        #set(np.sum(list(G[1].values()), axis = 0)) below is the set of all nodes having an incoming edge
        Key_starting_nodes = list(set(range(Size_of_the_graph))-set(np.sum(list(G[1].values()), axis = 0)))[:]
        # In the following we take all the nodes in the set of key starting nodes as currently reachable nodes
        current_reachable_nodes = Key_starting_nodes[:] 
        #Now we update current reachable nodes by adding all those nodes in the graph that can be reached starting from
        # the above list, that is, current_reachable_nodes
        current_reachable_nodes = update_reachable_nodes_from(G, current_reachable_nodes)
        # In the following, we go through the nodes of the graph and for those that are not in current_reachable_nodes, we find all 
        #other nodes that can be reached starting from them, then add all of them (the initial nodes and those found) in current_reachables_nodes 
        for node in G[1].keys(): 
            if node not in current_reachable_nodes: # We check wether the node is or not in current reachable nodes
                Key_starting_nodes.append(node)
                current_reachable_nodes.extend(update_reachable_nodes_from(G, [node])) #We update current_reachable_nodes
            if len(current_reachable_nodes) == Size_of_the_graph: #If all the nodes of the graph are seen, then we stop
                break
    #In the following, we create a txt file containing the nodes found, one node per line 
    filewriter = open(output_file_name, "w")
    for node in Key_starting_nodes:
        filewriter.write(str(node) + "\n")
    filewriter.close()
    return None
