# The Captain's Room : https://www.hackerrank.com/challenges/py-the-captains-room/problem

k = int(input())
room_list = list(map(int, input().split()))

room_set = set(room_list)

print(sum(room_set), sum(room_list))
captain_room = (sum(room_set) * k - sum(room_list)) // (k - 1)
print(captain_room)



# Alternate solution:
from collections import Counter

k = int(input())
room_list = list(map(int, input().split()))

# Count occurrences of each room number
room_counts = Counter(room_list)

# The Captain's room is the one that appears only once
for room, count in room_counts.items():
    if count == 1:
        print(room)
        break


