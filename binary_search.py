

def binary_search(my_list, search_item):
    low = 0
    high = len(my_list)-1
    while low <= high:
        mid = (low+high)//2
        if search_item == my_list[mid]:
            return mid
        elif search_item > my_list[mid]:
            low = mid + 1
        elif search_item < my_list[mid]:
            high = mid - 1
    return "Not_found"


if __name__ == "__main__":
    list_items = [1, 3, 4, 6, 7, 15, 99, 100, 100, 106, 108, 200, 260]

    print(binary_search(list_items, 100))
