import sys

N = int(input())

list = []

for i in range (1, N + 1):
    town, people = map(int,input().split())
    list.append((town, people))

list = sorted(list, key=lambda x: x[0])

person = sum(people for town, people in list)
median = (person + 1) // 2

total = 0
for town,people in list:
    total += people
    if total >= median:
        print(town)
        break