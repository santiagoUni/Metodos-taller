def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

def demo():
    arr = [11, 12, 18, 22, 23, 25, 32, 34, 36, 45, 50, 64, 77, 88, 90]
    target = 36
    print("Binary Search")
    print(f"Arreglo: {arr}")
    print(f"Buscando: {target}")
    indice = binary_search(arr, target)
    print(f"Encontrado en índice: {indice}\n" if indice != -1 else "No encontrado\n")

if __name__ == "__main__":
    demo()
