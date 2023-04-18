def sample_loop(list):
    for i in list:
        if i % 2 == 0:
            return i


list = [19, 33, 4, 2, 5, 6, 7, 8, 9]
print(list)
print(sample_loop(list))

