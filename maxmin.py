# function input should be a list of rational numbers - for example: [2, 3.1, -5, 1]
def max_and_min(lst):
    initial_max = lst[0]
    for i in range(len(lst)):
        if lst[i] > lst[i-1]:
            initial_max = lst[i]
        else:
            pass
    initial_min = lst[0]
    for i in range(len(lst)):
        if lst[i] < lst[i-1]:
                initial_min = lst[i]
        else:
            pass


    return [initial_min, initial_max]

print(max_and_min([5,6,7,8,4]))