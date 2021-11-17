// SORTING FUNCTIONS DERIVED FROM DR. HALTERMAN'S POWERPOINTS AND GEEKSFORGEEK.COM

//  Name: Andrew Hansbury
//  Assignment number: 5
//  Assignment: Sorting Algorithms
//  File name: stuff.cpp
//  Date last modified: November 11, 2021
//  Honor statement: I have neither given nor received any unauthorized help on this assignment.

#include <vector>
#include <iostream>
#include "stopwatch.cpp"
#include <stdio.h>

template <typename T>
void selection_sort(std::vector<T> &v)
{
    int n = v.size();

    for (int i = 0; i < n - 1; i++)
    {

        int small = i;

        for (int j = i + 1; j < n; j++)
            if (v[j] < v[small])
                small = j; // Found a smaller value // Swap elements at position iter and small, if a smaller value was found if (i != small)
        if (i != small)
            std::swap(v[i], v[small]);
        // break;
    }
}

template <typename T>
void exhange_sort(std::vector<T> &vec)
{
    int n = vec.size();
    int k = 0;
    bool sorted = false;
    while (k < n - 1 && !sorted)
    {
        sorted = true;
        for (int i = 0; i < n - k - 1; i++)
        {
            if (vec[i] > vec[i + 1])
            {
                std::swap(vec[i], vec[i + 1]);
                sorted = false;
            }
        }
        // break;
        k++;
    }
}

void insertionSort(std::vector<int> &arr)
{
    int n = arr.size();
    int i, key, j;
    for (i = 1; i < n; i++)
    {
        key = arr[i];
        j = i - 1;

        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

int partition(std::vector<int> &arr, int low, int high)
{
    int pivot = arr[high]; // pivot
    int i = (low - 1);     // Index of smaller element

    for (int j = low; j <= high - 1; j++)
    {
        // If current element is smaller than or
        // equal to pivot
        if (arr[j] <= pivot)
        {
            i++; // increment index of smaller element
            std::swap(arr[i], arr[j]);
        }
    }
    std::swap(arr[i + 1], arr[high]);
    return (i + 1);
}

void quickSort(std::vector<int> &arr, int low, int high)
{
    if (low < high)
    {
        /* pi is partitioning index, arr[p] is now
           at right place */
        int pi = partition(arr, low, high);

        // Separately sort elements before
        // partition and after partition
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// NEXT TWO FUNCTIONS NEEDED FOR HEAPSORT
void heapify(std::vector<int> &arr, int n, int i)
{
    int largest = i;   // Initialize largest as root
    int l = 2 * i + 1; // left = 2*i + 1
    int r = 2 * i + 2; // right = 2*i + 2

    // If left child is larger than root
    if (l < n && arr[l] > arr[largest])
        largest = l;

    // If right child is larger than largest so far
    if (r < n && arr[r] > arr[largest])
        largest = r;

    // If largest is not root
    if (largest != i)
    {
        std::swap(arr[i], arr[largest]);

        // Recursively heapify the affected sub-tree
        heapify(arr, n, largest);
    }
}

void heapSort(std::vector<int> &arr)
{
    int n = arr.size();
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    for (int i = n - 1; i > 0; i--)
    {
        std::swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}

void print_vec(std::vector<int> vec)
{
    for (int i = 0; i < vec.size(); i++)
    {
        std::cout << vec[i] << " ";
    }
    std::cout << std::endl;
}

std::vector<int> populate_vector(std::vector<int> &vec, int size)
{
    vec.clear();
    print_vec(vec);
    srand(time(NULL));
    int x;
    for (int i = 0; i < size; i++)
    {
        x = rand() % 1000 + 1;
        vec.push_back(x);
    }

    return vec;
}

int main()
{
    Stopwatch timer;
    Stopwatch total_timer;

    std::vector<int> vec_10;

    total_timer.start();

    // 10 Elements
    //
    //
    //
    std::cout << "\n--------------10 Elements--------------\n";
    populate_vector(vec_10, 10);
    timer.start();
    selection_sort(vec_10);
    std::cout << "Selection Sort (10 Elements): " << timer.elapsed() << " seconds";
    timer.reset();

    populate_vector(vec_10, 10);
    timer.start();
    insertionSort(vec_10);
    std::cout << "Insertion Sort (10 Elements): " << timer.elapsed() << " seconds";
    timer.reset();

    populate_vector(vec_10, 10);
    timer.start();
    exhange_sort(vec_10);
    std::cout << "Exchange Sort (10 Elements): " << timer.elapsed() << " seconds";
    timer.reset();

    populate_vector(vec_10, 10);
    timer.start();
    heapSort(vec_10);
    std::cout << "HeapSort (10 Elements): " << timer.elapsed() << " seconds";
    timer.reset();

    populate_vector(vec_10, 10);
    timer.start();
    quickSort(vec_10, 0, vec_10.size());
    std::cout << "QuickSort (10 Elements): " << timer.elapsed() << " seconds";
    timer.reset();

    std::cout << std::endl;

    // 100 Elements
    //
    //
    //
    //
    std::cout << "\n--------------100 Elements--------------\n";
    populate_vector(vec_10, 100);
    timer.start();
    selection_sort(vec_10);
    std::cout << "Selection Sort (100 Elements): " << timer.elapsed() << " seconds";
    timer.reset();

    populate_vector(vec_10, 100);
    timer.start();
    insertionSort(vec_10);
    std::cout << "Insertion Sort (100 Elements): " << timer.elapsed() << " seconds";
    timer.reset();

    populate_vector(vec_10, 100);
    timer.start();
    exhange_sort(vec_10);
    std::cout << "Exchange Sort (100 Elements): " << timer.elapsed() << " seconds";
    timer.reset();

    populate_vector(vec_10, 100);
    timer.start();
    heapSort(vec_10);
    std::cout << "HeapSort (100 Elements): " << timer.elapsed() << " seconds";
    timer.reset();

    populate_vector(vec_10, 100);
    timer.start();
    quickSort(vec_10, 0, vec_10.size());
    std::cout << "QuickSort (100 Elements): " << timer.elapsed() << " seconds";
    timer.reset();

    std::cout << std::endl;

    // 1000 Elements
    //
    //
    //
    //
    std::cout << "\n--------------1000 Elements--------------\n";
    populate_vector(vec_10, 1000);
    timer.start();
    selection_sort(vec_10);
    std::cout << "Selection Sort (1000 Elements): " << timer.elapsed() << " seconds";
    timer.reset();

    populate_vector(vec_10, 1000);
    timer.start();
    insertionSort(vec_10);
    std::cout << "Insertion Sort (1000 Elements): " << timer.elapsed() << " seconds";
    timer.reset();

    populate_vector(vec_10, 1000);
    timer.start();
    exhange_sort(vec_10);
    std::cout << "Exchange Sort (1000 Elements): " << timer.elapsed() << " seconds";
    timer.reset();

    populate_vector(vec_10, 1000);
    timer.start();
    heapSort(vec_10);
    std::cout << "HeapSort (1000 Elements): " << timer.elapsed() << " seconds";
    timer.reset();

    populate_vector(vec_10, 1000);
    timer.start();
    quickSort(vec_10, 0, vec_10.size());
    std::cout << "QuickSort (1000 Elements): " << timer.elapsed() << " seconds";
    timer.reset();

    std::cout << std::endl;

    // 10000 Elements
    //
    //
    //
    //
    std::cout << "\n--------------10000 Elements--------------\n";
    populate_vector(vec_10, 10000);
    timer.start();
    selection_sort(vec_10);
    std::cout << "Selection Sort (10000 Elements): " << timer.elapsed() << " seconds";
    timer.reset();

    populate_vector(vec_10, 10000);
    timer.start();
    insertionSort(vec_10);
    std::cout << "Insertion Sort (10000 Elements): " << timer.elapsed() << " seconds";
    timer.reset();

    populate_vector(vec_10, 10000);
    timer.start();
    exhange_sort(vec_10);
    std::cout << "Exchange Sort (10000 Elements): " << timer.elapsed() << " seconds";
    timer.reset();

    populate_vector(vec_10, 10000);
    timer.start();
    heapSort(vec_10);
    std::cout << "HeapSort (10000 Elements): " << timer.elapsed() << " seconds";
    timer.reset();

    populate_vector(vec_10, 10000);
    timer.start();
    quickSort(vec_10, 0, vec_10.size());
    std::cout << "QuickSort (10000 Elements): " << timer.elapsed() << " seconds";
    timer.reset();

    std::cout << std::endl;

    // 100000 Elements
    //
    //
    //
    //
    std::cout << "\n--------------100000 Elements--------------\n";
    populate_vector(vec_10, 100000);
    timer.start();
    selection_sort(vec_10);
    std::cout << "Selection Sort (100000 Elements): " << timer.elapsed() << " seconds";
    timer.reset();

    populate_vector(vec_10, 100000);
    timer.start();
    insertionSort(vec_10);
    std::cout << "Insertion Sort (100000 Elements): " << timer.elapsed() << " seconds";
    timer.reset();

    populate_vector(vec_10, 100000);
    timer.start();
    exhange_sort(vec_10);
    std::cout << "Exchange Sort (100000 Elements): " << timer.elapsed() << " seconds";
    timer.reset();

    populate_vector(vec_10, 100000);
    timer.start();
    heapSort(vec_10);
    std::cout << "HeapSort (100000 Elements): " << timer.elapsed() << " seconds";
    timer.reset();

    populate_vector(vec_10, 10000);
    timer.start();
    quickSort(vec_10, 0, vec_10.size());
    std::cout << "QuickSort (100000 Elements): " << timer.elapsed() << " seconds";
    timer.reset();

    std::cout << std::endl;
}
