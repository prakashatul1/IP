from maximum_area_histogram import find_maximum_area_histogram


def find_max_area_rectangle_binary_matrix(a):
    mx = find_maximum_area_histogram(a[0])
    v = a[0]
    for i in range(1, len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 0:
                v[j] = 0
            else:
                v[j] = (a[i][j] + v[j])
        # print(v)
        mx = max(mx, find_maximum_area_histogram(v))


        # mx = max(mx, find_maximum_area_histogram([x + y if x > 1 else 0 for x, y in zip(a[i], a[i - 1])]))

    return mx


a = [
    [0, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0]
]
print(find_max_area_rectangle_binary_matrix(a))
