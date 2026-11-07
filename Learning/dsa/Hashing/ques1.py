# Given list x having n numbers of element which can have 10**8 elements
# Given list y having m numbers of element which can go upto 10**8 elements
# Check frequency of element in y present in x

def freq_meth1(x,y):
    len_y = len(y)
    len_x = len(x)
    freq_dict = {}
    for i in range(0,len_y):
        count = 0
        for j in range(0,len_x):
            if y[i] == x[j]:
                count+=1
        freq_dict[y[i]] = count
    print(freq_dict)

def freq_meth2(x,y):
    hash_map_x = {}
    hash_map_xy = {}
    x_len = len(x)
    y_len = len(y)
    for i in range(0,x_len):
        hash_map_x[x[i]] = hash_map_x.get(x[i],0)+1
    for j in range(0,y_len):
        hash_map_xy[y[j]] = hash_map_x.get(y[j],0)
    print(f"Prestored value -> {hash_map_x}")
    print(f"Result -> {hash_map_xy}")

def freq_meth3(x,y):
    hash_list = [0]*11
    hash_map = {}
    for i in x:
        hash_list[i]+=1
    print(f"Prestored hash list -> {hash_list}")
    for j in y:
        hash_map[j] = hash_list[j]
    print(f"Result -> {hash_map}")

def dict_hash_meth4(x,y):
    hash_dict = {}
    for i in x:
        if i in hash_dict:
            hash_dict[i] += 1
        else:
            hash_dict[i] = 1
    print(hash_dict)
    hash_dict_y = {}
    for j in y:
        if j in hash_dict.keys():
            hash_dict_y[j] = hash_dict[j]
        else:
            hash_dict_y[j] = 0
    print(hash_dict_y)




if __name__ == "__main__":
    x = [1,3,6,2,7,3,6,1,8,7,7,7]
    y = [6,7,8,9,10]
    #freq_meth1(x,y)
    #freq_meth2(x, y)
    # freq_meth3(x, y)
    dict_hash_meth4(x,y)
