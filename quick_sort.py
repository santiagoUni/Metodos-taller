def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def demo():
    arr = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50, 23, 36, 18, 77, 32]
    print("Quick Sort")
    print(f"Original: {arr}")
    print(f"Ordenado: {quick_sort(arr)}\n")

if __name__ == "__main__":
    demo()
