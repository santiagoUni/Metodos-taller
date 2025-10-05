def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def demo():
    arr = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50, 23, 36, 18, 77, 32]
    print("Merge Sort")
    print(f"Original: {arr}")
    print(f"Ordenado: {merge_sort(arr)}\n")

if __name__ == "__main__":
    demo()
