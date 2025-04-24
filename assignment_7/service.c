#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

double mean(int arr[], int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    return (double)sum / n;
}

double median(int arr[], int n) {
    qsort(arr, n, sizeof(int), compare);
    if (n % 2 == 0)
        return (arr[n/2 - 1] + arr[n/2]) / 2.0;
    else
        return arr[n/2];
}

void mode(int arr[], int n, int result[], int *mode_count) {
    int max_count = 0;
    *mode_count = 0;
    for (int i = 0; i < n; i++) {
        int count = 1;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] == arr[i]) count++;
        }
        if (count > max_count) {
            max_count = count;
            result[0] = arr[i];
            *mode_count = 1;
        } else if (count == max_count) {
            int found = 0;
            for (int k = 0; k < *mode_count; k++) {
                if (result[k] == arr[i]) {
                    found = 1;
                    break;
                }
            }
            if (!found) {
                result[*mode_count] = arr[i];
                (*mode_count)++;
            }
        }
    }
}

int main() {
    int arr[] = {1, 2, 2, 3, 4};
    int n = sizeof(arr)/sizeof(arr[0]);

    printf("Mean: %.2f\n", mean(arr, n));
    printf("Median: %.2f\n", median(arr, n));

    int mode_result[100];
    int mode_count;
    mode(arr, n, mode_result, &mode_count);
    printf("Mode: ");
    for (int i = 0; i < mode_count; i++) {
        printf("%d ", mode_result[i]);
    }
    printf("\n");
    return 0;
}
