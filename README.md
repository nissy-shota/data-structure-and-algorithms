# data-structure-and-algorithms
Data Structure and Algorithms

## Bogo Sort

- In computer science, bogosort (also known as permutation sort, stupid sort, or slowsort) is a highly inefficient sorting algorithm based on the generate and test paradigm.  
- The function successively generates permutations of its input until it finds one that is sorted. It is not useful for sorting.  
- rand.shuffleでランダム生成をし続けるだけ．

## Bubble Sort
- Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
- This simple algorithm performs poorly in real world use
- 隣接する要素を順番に走査していって，所望の順番と違えば交換するアルゴリズム

## Cocktail shaker Sort
- bidirectional bubble sort
- cocktail shaker sort is an extension of bubble sort 

## Comb Sort
- Comb Sort is mainly an improvement over Bubble Sort.   
- Bubble sort always compares adjacent values. So all inversions are removed one by one. Comb Sort improves on Bubble Sort by using gap of size more than 1. The gap starts with a large value and shrinks by a factor of 1.3 in every iteration until it reaches the value 1. Thus Comb Sort removes more than one inversion counts with one swap and performs better than Bubble Sort.
- [comb sort](https://www.geeksforgeeks.org/comb-sort/)

## Selection Sort

- In computer science, selection sort is an in-place comparison sorting algorithm.  
- It has an O(n2) time complexity, which makes it inefficient on large lists, and generally performs worse than the similar insertion sort.   
- Selection sort is noted for its simplicity and has performance advantages over more complicated algorithms in certain situations, particularly where auxiliary memory is limited.
- [selection sort](https://en.wikipedia.org/wiki/Selection_sort)



# reference
I'm referring to Sakai's lecture on Udemy.
