#include <iostream>
using namespace std;

int main() {
    int* arr = new int[5];  
    arr[0] = 1;
    cout << arr[0] << endl;  
    delete[] arr;            
    return 0;
}