# 2024-01-06 FAIL
#     lack of fundamental idea
#     use deque
#     change M with printed_papers

# 2024-01-06
import sys
input = sys.stdin.readline
from collections import deque

Tests = int(input())
for _ in range(Tests):
    N, M = map(int, input().split())
    documents = deque(list(map(int, input().split())))
    printed_papers = 0
    while True:
        if documents[0] == max(documents):
            printed_papers += 1
            if M == 0:
                print(printed_papers)
                break
            else:
                documents.popleft()    
        else:
            if M == 0:
                M += N - printed_papers
            documents.append(documents.popleft())
        M -= 1

#1st trial: without queue library
# import sys
# input = sys.stdin.readline

# NumberOfTestCases = int(input())
# for i in range(NumberOfTestCases):
#     NumberofDocuments, MyDocument = map(int, input().split())
#     Importance = list(map(int, input().split()))
#     PrintedPapers = 0
#     #bigger number, more important
#     while True:
#         if Importance[0] == max(Importance):
#             PrintedPapers += 1
#             if MyDocument == 0:
#                 print(PrintedPapers)
#                 break
#             else:
#                 del Importance[0]
#         else:
#             if MyDocument == 0:
#                 MyDocument += NumberofDocuments-PrintedPapers #keypoint '-PrintedPapers'
#             Importance.append(Importance[0])
#             del Importance[0]
#         MyDocument -= 1
