def subsets(array):
    if array == []:
        return [array]
    sets = [array]
    for i in range(0, len(array)):
        tmp_subsets = subsets(array[:i] + array[i+1:])
        for subset in tmp_subsets:
            if subset not in sets:
                sets.append(subset)
    return sets

x = [1,2,3,4]

x = subsets(x)
print x
print "\nLenght:", len(x)
