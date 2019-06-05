#### Valid code for leetcode but very UGLY - so to revise ####

def monotonic_array(arr):
    arr_sort = None;
    
    if len(arr) <= 1:
        return True;
    if arr[0] < arr[1]:
        arr_sort = sorted(arr);
    elif arr[0] == arr[1]:
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr_sort = sorted(arr);
                break;
            elif arr[i] > arr[i + 1]:
                arr_sort = sorted(arr, reverse = True);
            else:
                continue;
        if arr_sort is None:
            arr_sort = arr;
    else:
        arr_sort = sorted(arr, reverse = True);
    return(all([arr_sort[i] == arr[i] for i in range(len(arr))]));
