import os
from Read_graphs import graph
from Program import Full_exploration_starting_nodes

path1 = "../Graphs/g1.txt"
path2 = "../Graphs/g2.txt"
path3 =  "../Graphs/g3.txt"

G1 = graph(path1)
G2 = graph(path2)
G3 = graph(path3)

if not os.path.exists('../Output_folder'):
    os.makedirs('../Output_folder')
    
output_path1 ="../Output_folder/output_g1.txt"
output_path2 ="../Output_folder/output_g2.txt"
output_path3 ="../Output_folder/output_g3.txt"


Full_exploration_starting_nodes(G1, output_path1)
Full_exploration_starting_nodes(G2, output_path2)
Full_exploration_starting_nodes(G3, output_path3)