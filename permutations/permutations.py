List = [1, 2, 3]

for x in List:
    for y in List:
        if y != x:
            for z in List:
                if z != y and z != x:
                    print (x , y, z)