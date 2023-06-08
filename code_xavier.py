# Create distances list to calculate
def list_distances(nombre_points:int) -> list:
    """Create distances list to calculate

    Args:
        nombre_points (int): Store the number of points

    Returns:
        list: List of distances
    """
    
    list_distances = [] # Store the list of distances to calculate
    cpt = 2
    tmp = ()
    tmp_inverse = ()
    
    for i in range(1,nombre_points + 1):
        for cpt in range(1,nombre_points):
            if i != cpt: # remove values when the two points are identical
                tmp = (i, cpt)
                tmp_inverse = (cpt,i) # Store the reverse list
                                      # so as not to calculate the same distance twice  
                if not list_distances.count(tmp_inverse):
                    
                    list_distances.append(tmp)
                    print(list_distances)
  
list_distances(4) # For testing