def find_total_area_of_water_trapped_by_array(a):

    mxl = []
    mxr = []
    mx = 0

    for i in range(len(a)):
        if i == 0:
            mx = a[i]

        mxl.append(max(mx, a[i]))

    print(mxl)
    print("mxl")

    mx = 0
    for i in range(len(a)-1, -1, -1):
        if i == len(a)-1:
            mx = a[i]

        mxr.append(max(mx, a[i]))

    print(mxr)
    print("mxr")
    mxr = mxr[::-1]

    area = 0
    for i in range(len(a)):
        area = area + (min(mxl[i], mxr[i]) - a[i])

    return area

if __name__ == "__main__":
    print(find_total_area_of_water_trapped_by_array([3,0,0,2,0,4]))
