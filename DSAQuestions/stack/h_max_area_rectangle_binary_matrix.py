from g_maximum_area_histogram import find_maximum_area_histogram


def find_max_area_rectangle_binary_matrix(a_list):
    mx = find_maximum_area_histogram(a_list[0])
    v = a_list[0]
    for i in range(1, len(a_list)):
        for j in range(len(a_list[i])):
            if a_list[i][j] == 0:
                v[j] = 0
            else:
                v[j] = (a_list[i][j] + v[j])
        # print(v)
        mx = max(mx, find_maximum_area_histogram(v))

    return mx


a = [
    [0, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0]
]
print(find_max_area_rectangle_binary_matrix(a))
