#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

void swap(int i, int j) {
    int temp = i; i = j; j = temp;
}

int partition(int array[], int left, int right, int pivot){
    int i = left, j = right;
    while (i <= j) {
        while (array[i] < pivot)
            i++;
        while (array[j] > pivot)
            j--;
        if (i <= j) {
            swap(array[i], array[j]);
            i++;
            j--;
        }
    };
    return i;
}

int quickselect(int array[], int left, int right, int k){
    k -= 1;
    while(1){
        srand(time(NULL));
        if (left == right){ //We return the only element there is if the array contains only one element
            return array[left];
        }
        int pivotIndex = left + rand() % (right - left + 1);
        int pivot = array[pivotIndex];
        pivotIndex = partition(array, left, right, pivot);
        if (k == pivotIndex){
            return array[k];
        } else if (k < pivotIndex){
            right = pivotIndex - 1;
        } else{
            left = pivotIndex + 1;
        }
    }
}

int main(){
    int array[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int N = sizeof(array)/sizeof(array[0]);
    std::cout<<quickselect(array, 0, N - 1, 2)<<std::endl;
}
