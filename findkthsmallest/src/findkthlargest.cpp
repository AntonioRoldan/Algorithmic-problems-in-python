#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

void swap(int i, int j) {
    int temp = i; i = j; j = temp;
}

int partition(int array[], int left, int right, int pivot){
    int i = left, j = right;
    while (i <= j) { //We are iterating back and forth simultaneously throughout the array 
        while (array[i] < pivot) //For as long as our forward traversal is less than the pivot 
            i++;
        while (array[j] > pivot) //For as long as our backwards traversal is greater than the pivot 
            j--;
        if (i <= j) { //Variables are swapped to satisfy the fundamental condition of the quicksort algorithm 
            swap(array[i], array[j]);
            i++;
            j--;
        }
    };
    //We made sure that all elements smaller than the pivot are found on the left and those greater than the pivot are on the right 
    return i;
}

int quickselect(int array[], int left, int right, int k){
    k -= 1; //Value readjustment to ensure that we will get the right output 
    while(1){
        srand(time(NULL)); //C++ idiom to generate random elements 
        if (left == right){ 
            return array[left];
        } 
        int pivotIndex = left + rand() % (right - left + 1);
        int pivot = array[pivotIndex];
        pivotIndex = partition(array, left, right, pivot);
        if (k == pivotIndex){ //In our base case we have already found the kth smallest element thanks to the condition 
            return array[k]; //that there are k - 1 elements before the pivot that are smaller 
        } else if (k < pivotIndex){ //We constantly swing between right and left as we assign random pivots on the left  
            right = pivotIndex - 1;
        } else{ //or the right side of our array 
            left = pivotIndex + 1;
        } //Until our pivot is equal to the number we are looking for 
    }
}

int main(){
    int array[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int N = sizeof(array)/sizeof(array[0]);
    std::cout<<quickselect(array, 0, N - 1, 2)<<std::endl;
}
