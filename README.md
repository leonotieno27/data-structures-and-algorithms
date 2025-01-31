# data-structures-and-algorithms

| **Algorithm**              | **Time Complexity**  | **Comparison**                                                                                              | **Explanation**                                              |
|----------------------------|---------------------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| **Linear Search**          | O(n)                | **Slower than Jump, Binary, Interpolation Search**                                                           | Searches every element until it finds the target.            |
| **Binary Search**          | O(log n)            | **Faster than Linear Search**                                                                                | Divides the sorted list in half repeatedly to search.        |
| **Jump Search**            | O(√n)               | **Faster than Linear Search, Slower than Binary Search**                                                      | Searches in a sorted array by jumping fixed steps.           |
| **Exponential Search**     | O(log i)            | **Faster than Linear, Jump, Comparable to Binary Search**                                                     | Useful when the target is near the beginning.                |
| **Ternary Search**         | O(log₃ n)           | **Comparable to Binary Search**                                                                              | Divides array into three parts instead of two.               |
| **Interpolation Search**   | O(log(log n))       | **Faster than Binary, Jump, and Linear Search for uniformly distributed data**                                | Estimates the position based on the key.                     |
| **Bubble Sort**            | O(n²)               | **Slower than Merge, Quick, Heap, Radix Sort**                                                                | Sorts by repeatedly swapping adjacent elements.              |
| **Selection Sort**         | O(n²)               | **Similar to Bubble Sort, Slower than Merge and Quick Sort**                                                  | Finds the minimum repeatedly and moves it to sorted portion. |
| **Insertion Sort**         | O(n²)               | **Faster than Bubble Sort for nearly sorted data, Slower than Quick and Merge Sort**                          | Builds the sorted list one item at a time.                   |
| **Merge Sort**             | O(n log n)          | **Faster than Bubble, Selection, Insertion Sort**                                                             | Divides the list in halves recursively and merges them.      |
| **Quick Sort**             | O(n log n)          | **Faster than Bubble, Selection, Insertion Sort, Comparable to Merge Sort**                                   | Sorts using a partitioning strategy.                         |
| **Heap Sort**              | O(n log n)          | **Faster than Bubble, Selection, Insertion Sort**                                                             | Uses a binary heap to sort elements.                         |
| **Radix Sort**             | O(nk)               | **Faster than Bubble, Selection Sort for large integers, but Slower than Quick Sort on small datasets**        | Sorts numbers by individual digits.                          |
| **Counting Sort**          | O(n+k)              | **Faster than Comparison-based Sorts for small range of numbers**                                              | Uses counting of elements for sorting.                       |
| **Bucket Sort**            | O(n + k)            | **Faster than Bubble, Comparable to Radix Sort for uniformly distributed inputs**                              | Divides elements into buckets and sorts them.                |
| **Dijkstra’s Algorithm**   | O((V + E) log V)    | **Faster than Bellman-Ford, but not a direct comparison to sorting**                                          | Finds shortest paths from a single source.                   |
| **Bellman-Ford Algorithm** | O(VE)               | **Slower than Dijkstra’s Algorithm**                                                                          | Finds shortest paths in a graph with negative weights.       |
| **Floyd-Warshall Algorithm** | O(V³)            | **Slower than Dijkstra’s Algorithm**                                                                          | Finds shortest paths between all pairs of vertices.          |
| **A* Search Algorithm**    | O(E) (heuristic)    | **Faster than Dijkstra for specific heuristic-based searches**                                                | Finds the shortest path in graphs using heuristics.          |
| **DFS (Depth-First Search)** | O(V + E)          | **Faster than Breadth-First Search for deep graphs**                                                          | Explores as far as possible along a branch.                  |
| **BFS (Breadth-First Search)** | O(V + E)       | **Faster for shortest unweighted paths than DFS**                                                             | Explores level by level.                                     |
| **Kruskal’s Algorithm**    | O(E log E)          | **Faster than Prim’s for sparse graphs**                                                                      | Finds the minimum spanning tree.                             |
| **Prim’s Algorithm**       | O(V²) or O(E log V) | **Comparable to Kruskal’s Algorithm**                                                                         | Finds the minimum spanning tree.                             |


| **Tree Type**        | **Applications**                               |
|-----------------------|-----------------------------------------------|
| General Trees         | File systems, Scene graphs                   |
| Binary Search Trees   | Databases, Searching, Auto-complete          |
| Heaps                 | Task scheduling, Shortest path algorithms    |
| Tries                 | Auto-complete, Dictionary lookups            |
| B-trees/B+ trees      | Database indexing                            |
| Syntax Trees          | Compilers, Programming language interpreters |
| Decision Trees        | Machine learning models                      |
| Merkle Trees          | Blockchain, Cryptography                     |
