#1st trial: without queue library
import sys
input = sys.stdin.readline

NumberOfTestCases = int(input())
for i in range(NumberOfTestCases):
    NumberofDocuments, MyDocument = map(int, input().split())
    Importance = list(map(int, input().split()))
    PrintedPapers = 0
    #bigger number, more important
    while True:
        if Importance[0] == max(Importance):
            PrintedPapers += 1
            if MyDocument == 0:
                print(PrintedPapers)
                break
            else:
                del Importance[0]
        else:
            if MyDocument == 0:
                MyDocument += NumberofDocuments-PrintedPapers #keypoint '-PrintedPapers'
            Importance.append(Importance[0])
            del Importance[0]
        MyDocument -= 1