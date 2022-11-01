#include <iostream>
using namespace std;
 
/*
    Function:
        Linear search.  
        This function will search for a target number in an unsorted array. 

    Input:  
        unsorted_array[]:  an unsorted array of integers
        array_length:  the length of the array
        target:  the number to search for

    Output:
        return value: the array index of the target number, or -1 if not found
*/
int linear_search(int unsorted_array[], int array_length, int target)
{
	// YOUR CODE GOES HERE!
}


/*
    Function:
        Binary search.  
        This function will search for a target number in a sorted array.

    Input:  
        sorted_array[]:  a sorted array of integers
        array_length:  the length of the array
        target:  the number to search for

    Output:
        return value: the array index of the target number, or -1 if not found
*/
int binary_search(int sorted_array[], int array_length, int target)
{
	// YOUR CODE GOES HERE!
}

 
// Main method.
int main()
{
    // Create an unsorted array of integers.
    int unsorted_array[] = { 11, 23, 8, 14, 30, 9, 6, 17, 22, 28, 25, 15, 7, 10, 19 };
    
    // Calculate the length of the array.
    int array_length = sizeof(unsorted_array) / sizeof(unsorted_array[0]);

    // Set a target number to find in the array.
    int target = 9;
 
    // Search for the target using the linear search function.
    int index = linear_search(unsorted_array, array_length, target);

    // Print out the results of the search.
    if (index == -1)
        cout << "Element is not found in the array\n";
    else
        cout << "Element found at array index " << index << "\n";
 

    // Create an sorted array of integers.
    int sorted_array[] = { 6, 7, 8, 9, 10, 11, 14, 15, 17, 19, 22, 23, 25, 28, 30 };

    // Calculate the length of the array.
    array_length = sizeof(sorted_array) / sizeof(sorted_array[0]);

    // Set a target number to find in the array.
    target = 19;

    // Search for the target using the linear search function.
    index = binary_search(sorted_array, array_length, target);

    // Print out the results of the search.
    if (index == -1)
        cout << "Element is not found in the array\n";
    else
        cout << "Element found at array index " << index << "\n";

    return 0;
}
