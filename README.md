# data-structure-and-algorithms
Data Structure and Algorithms

## Bogo Sort

- In computer science, bogosort (also known as permutation sort, stupid sort, or slowsort) is a highly inefficient sorting algorithm based on the generate and test paradigm.  
- The function successively generates permutations of its input until it finds one that is sorted. It is not useful for sorting.  
- rand.shuffleでランダム生成をし続けるだけ．
- [Bogo Sort](https://en.wikipedia.org/wiki/Bogosort)

## Bubble Sort
- Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
- This simple algorithm performs poorly in real world use
- 隣接する要素を順番に走査していって，所望の順番と違えば交換するアルゴリズム
- [Bubble Sort](https://en.wikipedia.org/wiki/Bubble_sort)

## Cocktail shaker Sort
- bidirectional bubble sort
- cocktail shaker sort is an extension of bubble sort 
- [Cocktail Sort](https://en.wikipedia.org/wiki/Cocktail_shaker_sort)

## Comb Sort
- Comb Sort is mainly an improvement over Bubble Sort.   
- Bubble sort always compares adjacent values. So all inversions are removed one by one. Comb Sort improves on Bubble Sort by using gap of size more than 1. The gap starts with a large value and shrinks by a factor of 1.3 in every iteration until it reaches the value 1. Thus Comb Sort removes more than one inversion counts with one swap and performs better than Bubble Sort.
- [Comb Sort](https://www.geeksforgeeks.org/comb-sort/)

## Selection Sort

- In computer science, selection sort is an in-place comparison sorting algorithm.  
- It has an O(n2) time complexity, which makes it inefficient on large lists, and generally performs worse than the similar insertion sort.   
- Selection sort is noted for its simplicity and has performance advantages over more complicated algorithms in certain situations, particularly where auxiliary memory is limited.
- [Selection Sort](https://en.wikipedia.org/wiki/Selection_sort)

## Gnome Sort
- The gnome sort is a sorting algorithm which is similar to insertion sort in that it works with one item at a time but gets the item to the proper place by a series of swaps, similar to a bubble sort.   
- It is conceptually simple, requiring no nested loops.   
- The average running time is O(n2) but tends towards O(n) if the list is initially almost sorted.
- [Gnome Sort](https://en.wikipedia.org/wiki/Gnome_sort)

## Insertion Sort
- Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time.   
- It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. 
- However, insertion sort provides several advantages:
  - Simple implementation
  - Efficient for (quite) small data sets, much like other quadratic sorting algorithms
  - More efficient in practice than most other simple quadratic (i.e., O(n2)) algorithms such as selection sort or bubble sort
  - In-place; i.e., only requires a constant amount O(1) of additional memory space
  - Stable; i.e., does not change the relative order of elements with equal keys
- [Insertion Sort](https://en.wikipedia.org/wiki/Insertion_sort)

## Bucket Sort
- Bucket sort, or bin sort, is a sorting algorithm that works by distributing the elements of an array into a number of buckets.  
- Each bucket is then sorted individually, either using a different sorting algorithm, or by recursively applying the bucket sorting algorithm. 
- [Bucket Sort](https://en.wikipedia.org/wiki/Bucket_sort)

# reference
I'm referring to Sakai's lecture on Udemy.
