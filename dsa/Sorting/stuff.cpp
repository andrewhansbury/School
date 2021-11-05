#include <vector>
#include <iostream>


template <typename T>
void selection_sort(std::vector<T>& v) {
    int n = v.size();

    for (int i = 0; i < n - 1; i++) {

        int small = i;

        for (int j = i + 1; j < n; j++)
            if (v[j] < v[small])
                small = j; // Found a smaller value // Swap elements at position iter and small, if a smaller value was found if (i != small)
        if (i != small)
            std::swap(v[i], v[small]);
        break;            
    }
}

template <typename T>
void exhange_sort(std::vector<T>& vec){
    int n = vec.size();
    int k = 0;
    bool sorted = false;
    while(k < n -1 && !sorted){
        sorted = true;
        for (int i=0; i<n-k-1; i++){
            if (vec[i] > vec[i + 1]) {
                std::swap(vec[i], vec[i+1]);
                sorted = false;
            }
        }
        break;
        k++;
    }

}



int main(){
    std::vector<int> vec = {7,2,3,1,5,4};
    //selection_sort(vec);

    exhange_sort(vec);
    for (int i = 0; i<vec.size(); i++){
        std::cout<<vec[i];
    }
}
