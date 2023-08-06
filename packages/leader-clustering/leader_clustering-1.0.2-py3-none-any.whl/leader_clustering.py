def create_clusters(scalars_list:list, distance:float, sort=False):
    assert len(scalars_list)>0, "input list is empty"
    assert len(scalars_list)<=1000000, "found more than 1 Million elements in input list"
    assert distance>=0.0, "distance threshold cannot be negative"

    if sort:
        scalars_list = sorted(scalars_list)

    leaders = []
    clusters = []

    for element in scalars_list:
        cluster_found = False

        for idx in range(len(leaders)):
            if abs(leaders[idx]-element)<=distance:
                clusters[idx].append(element)
                cluster_found = True
                break

        if not cluster_found:
            leaders.append(element)
            clusters.append([element])
    
    num_clusters = len(leaders)
    
    return num_clusters, leaders, clusters
