#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
#Input Format
#The first line contains n . The second line contains an array A[]  of  integers each separated by a space.

if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))
    arr.sort()
    print(arr[-2])


