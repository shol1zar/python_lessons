some_list = range(1, 1000, 7)
add = list(map(lambda x, y: x + y, some_list, some_list))
itr = iter(add)
i = 0
while i < 143:
    print(next(itr))
    i += 1
