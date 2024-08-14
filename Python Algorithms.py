# Sorting Algorithms

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Searching Algorithms

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Graph Traversal Algorithms

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            queue.extend(graph[vertex] - visited)
    
    return order

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    order = [start]
    
    for neighbor in graph[start] - visited:
        order.extend(dfs(graph, neighbor, visited))
    
    return order

# Usage Examples

if __name__ == "__main__":
    # Sorting examples
    array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", array)
    print("Bubble Sorted:", bubble_sort(array.copy()))
    print("Quick Sorted:", quick_sort(array.copy()))

    # Searching examples
    sorted_array = quick_sort(array.copy())
    target = 22
    print(f"Binary Search for {target}:", binary_search(sorted_array, target))
    print(f"Linear Search for {target}:", linear_search(array, target))

    # Graph traversal examples
    graph = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'E'}
    }
    print("BFS:", bfs(graph, 'A'))
    print("DFS:", dfs(graph, 'A'))
