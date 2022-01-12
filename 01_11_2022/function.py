tree = lambda size: "\n".join([" "*((size-(len(x)//2)))+x for x in ["* "*y for y in range(1,size+1)]])

for i in range(1, 20):
    print(tree(i))