"""
Given an unsorted array A of size N of non-negative integers, find a continuous
sub-array which adds to a given number S.

Input:
The first line of input contains an integer T denoting the number of test cases.
Then T test cases follow. Each test case consists of two lines.
The first line of each test case is N and S, where N is the size of array and S is the sum.
The second line of each test case contains N space separated integers denoting the array elements.

Output:
For each testcase, in a new line, print the starting and ending positions(1 indexing)
of first such occuring subarray from the left if sum equals to subarray, else print -1.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= Ai <= 1010

Example:
Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
Output:
2 4
1 5

Explanation :
Testcase1: sum of elements from 2nd position to 4th position is 12
Testcase2: sum of elements from 1st position to 5th position is 15
"""
import sys
from collections import deque


def is_subarray(current_sum, d_sum, indexes):
    if current_sum == d_sum:
        if len(indexes) == 1:
            print("{} {}".format(indexes[0] + 1, indexes[0] + 1))
        else:
            print("{} {}".format(indexes[0] + 1, indexes[-1] + 1))
        return True
    return False


def main():
    test_cases = []
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        with open(input_file) as f:
            lines = f.readlines()[1:]
            for i in range(0, len(lines), 2):
                num, d_sum = map(int, lines[i].split())
                array = list(map(int, lines[i+1].split()))
                test_cases.append((num, d_sum, array))
    else:
        test_cases_num = int(input())
        for i in range(test_cases_num):
            num, d_sum = map(int, input().split())
            array = list(map(int, input().split()))
            test_cases.append((num, d_sum, array))

    for test_case in test_cases:
        indexes = deque()
        current_sum = 0
        found = False
        num, d_sum, array = test_case
        for i in range(num):
            indexes.append(i)
            current_sum += array[i]
            found = is_subarray(current_sum, d_sum, indexes)
            if found:
                break
            if current_sum > d_sum:
                while indexes:
                    index = indexes.popleft()
                    current_sum -= array[index]
                    found = is_subarray(current_sum, d_sum, indexes)
                    if found or current_sum < d_sum:
                        break
                if found:
                    break
        if not found:
            print(-1)


if __name__ == '__main__':
    main()
