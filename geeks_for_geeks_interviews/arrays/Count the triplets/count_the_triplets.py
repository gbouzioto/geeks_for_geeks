"""
Given an array of distinct integers. The task is to count all the triplets such
that sum of two elements equals the third element.

Input:
The first line of input contains an integer T denoting the number of test cases.
Then T test cases follow. Each test case consists of two lines. First line of each test
case contains an Integer N denoting size of array and the second line contains N space
separated elements.

Output:
For each test case, print the count of all triplets, in new line.
If no such triplets can form, print "-1".

Constraints:
1 <= T <= 100
3 <= N <= 105
1 <= A[i] <= 106

Example:
Input:
2
4
1 5 3 2
3
3 2 7
Output:
2
-1

Explanation:
Testcase 1: There are 2 triplets: 1 + 2 = 3 and 3 +2 = 5
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
        array.sort()
        triplets = 0
        possible_sums = set(array)
        for i in range(num - 1):
            for j in range(i+1, num - 1):
                if array[i] + array[j] in possible_sums:
                        triplets += 1
        if triplets != 0:
            print(triplets)
        else:
            print(-1)


if __name__ == '__main__':
    main()
