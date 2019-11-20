"""
Given an array C of size N-1 and given that there are numbers from 1 to N
with one element missing, the missing number is to be found.

Input:
The first line of input contains an integer T denoting the number of test cases.
For each test case first line contains N(size of array).
The subsequent line contains N-1 array elements.

Output:
Print the missing number in array.

Constraints:
1 ≤ T ≤ 200
1 ≤ N ≤ 107
1 ≤ C[i] ≤ 107

Example:
Input:
2
5
1 2 3 5
10
1 2 3 4 5 6 7 8 10

Output:
4
9
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
        if len(array) == 1:
            print(array[0] - 1) if array[0] > 1 else print(array[0] + 1)
            continue
        found = False
        array.sort()
        for i in range(num - 2):
            if array[i + 1] - array[i] != 1:
                print(array[i] + 1)
                found = True
                break
        if not found:
            if array[-1] < num:
                print(array[-1] + 1)
            else:
                print(array[0] - 1)


if __name__ == '__main__':
    main()
