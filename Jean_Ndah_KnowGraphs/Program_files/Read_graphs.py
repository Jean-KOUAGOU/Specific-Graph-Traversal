
def graph(filename):
    assert isinstance(filename, str), "The input should be a string"
    f=open(filename, "r")
    g1 = f.read()
    f.close()
    # Here we take a precaution in case the number of nodes is 0 and is not even specified
    if g1.split("\n")[0] == "":
        number_of_nodes = 0
    else:
        number_of_nodes = int(g1.split("\n")[0])  # get the first number in the file which is the number of nodes
    g1 = g1.split("\n")[1:]
    g = {}
    for i in range(len(g1)):
        if g1[i] != "":
            key, value = g1[i].split("->")
            key = int(key)
            value = int(value)
            if key in g.keys():
                g[key].append(value)
            else:
                g[key] = [value]   
    return number_of_nodes, g
