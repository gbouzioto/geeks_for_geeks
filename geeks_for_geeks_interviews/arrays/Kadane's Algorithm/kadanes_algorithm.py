"""
Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

Input:
The first line of input contains an integer T denoting the number of test cases.
The description of T test cases follows. The first line of each test case contains
a single integer N denoting the size of array. The second line contains N space-separated
integers A1, A2, ..., AN denoting the elements of the array.

Output:
Print the maximum sum of the contiguous sub-array in a separate line for each test case.

Constraints:
1 ≤ T ≤ 110
1 ≤ N ≤ 106
-107 ≤ A[i] <= 107

Example:
Input
2
5
1 2 3 -2 5
4
-1 -2 -3 -4
Output
9
-1

Explanation:
Testcase 1: Max subarray sum is 9 of elements (1, 2, 3, -2, 5) which is a contiguous subarray.
"""

import sys


def main():
    test_cases = []
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        with open(input_file) as f:
            lines = f.readlines()[1:]
            for i in range(0, len(lines), 2):
                num = int(lines[i])
                array = list(map(int, lines[i+1].split()))
                test_cases.append((num, array))
    else:
        test_cases_num = int(input())
        for i in range(test_cases_num):
            num = int(input())
            array = list(map(int, input().split()))
            test_cases.append((num, array))

    for test_case in test_cases:
        num, array = test_case
        max_so_far = 0
        max_ending_here = 0
        min_negative = -100000
        for i in range(num):
            max_ending_here += array[i]
            if min_negative <= array[i] < 0:
                min_negative = array[i]
            if max_ending_here < 0:
                max_ending_here = 0
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
        print(max_so_far) if max_so_far != 0 else print(min_negative)


if __name__ == '__main__':
    main()
