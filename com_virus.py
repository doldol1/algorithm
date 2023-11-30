n=int(input())
net_n=int(input())

networks=list()
for i in range(net_n):
    networks.append(list(map(int, input().split(' '))))

# n=7
# net_n=6
# networks=[(1,2),
#           (2,3),
#           (1,5),
#           (5,2),
#           (5,6),
#           (4,7)]


route=list()

def graph_search(piv, networks, route):
    route.append(piv)

    for i in networks:
        if (piv==i[0]) and (i[1] not in route):
            graph_search(i[1], networks, route)
        elif (piv==i[1]) and (i[0] not in route):
            graph_search(i[0], networks, route)
        else:
            pass
    
    return route
        
route =graph_search(1, networks, route)

print(len(route)-1)