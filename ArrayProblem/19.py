def subarrayWithSum(arr, x):
    st = 0
    curr_sum = 0

    for end in range(len(arr)):
        curr_sum += arr[end]

        while curr_sum > x:
            curr_sum -= arr[st]
            st += 1

        if curr_sum == x:
            return st,end

    return None


arr = [1,2,3,7,5]
tar = 12

print(subarrayWithSum(arr, tar))
