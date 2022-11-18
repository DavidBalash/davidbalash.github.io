
public class Search
{
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
    public int linear_search(int unsorted_array[], int array_length, int target)
    {
        // YOUR CODE GOES HERE!
        return -1;
    }
   

    /*
        Function:
            Binary search (iterative).  
            This function will search for a target number in a sorted array.

        Input:  
            sorted_array[]:  a sorted array of integers
            array_length:  the length of the array
            target:  the number to search for

        Output:
            return value: the array index of the target number, or -1 if not found
    */
    public int binary_search(int sorted_array[], int array_length, int target)
    {
        // YOUR CODE GOES HERE!
        return -1;
    }


    /*
        Function:
            Binary search (recursive).  
            This function will search for a target number in a sorted array.

        Input:  
            sorted_array[]:  a sorted array of integers
            array_length:  the length of the array
            target:  the number to search for

        Output:
            return value: the array index of the target number, or -1 if not found
    */
    public int binary_search_recursive(int sorted_array[], int left, int right, int target)
    {
        // YOUR CODE GOES HERE!
        return -1;
    }

    // Main method.
    public static void main(String args[])
    {
        Search search = new Search();

        // Create an unsorted array of integers.
        int unsorted_array[] = { 11, 23, 8, 14, 30, 9, 6, 17, 22, 28, 25, 15, 7, 10, 19 };

        // Set a target number to find in the array.
        int target = 9;
    
        // Search for the target using the linear search function.
        int index = search.linear_search(unsorted_array, unsorted_array.length, target);

        // Print out the results of the search.
        if (index == -1)
            System.out.println("Element is not found in the array");
        else
            System.out.println("Element found at array index " + index);
    

        // Create an sorted array of integers.
        int sorted_array[] = { 6, 7, 8, 9, 10, 11, 14, 15, 17, 19, 22, 23, 25, 28, 30 };

        // Set a target number to find in the array.
        target = 19;

        // Search for the target using the linear search function.
        index = search.binary_search(sorted_array, sorted_array.length, target);

        // Print out the results of the search.
        if (index == -1)
            System.out.println("Element is not found in the array");
        else
            System.out.println("Element found at array index " + index);

        // Search for the target using the linear search function.
        index = search.binary_search_recursive(sorted_array, 0, sorted_array.length, target);

        // Print out the results of the search.
        if (index == -1)
            System.out.println("Element is not found in the array");
        else
            System.out.println("Element found at array index " + index);    
    }
}