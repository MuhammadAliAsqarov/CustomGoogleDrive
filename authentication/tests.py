# def isValid(s: str) -> bool:
#     stack = ['']
#     mapping = {")": "(", "}": "{", "]": "["}
#     for char in s:
#         if char in mapping.values():
#             stack.append(char)
#         elif char in mapping.keys():
#             if not stack or mapping[char] != stack.pop():
#                 return False
#     return True
from collections import defaultdict

from itypes import List


# def romanToInt(s: str) -> int:
#     translations = {
#         "I": 1,
#         "V": 5,
#         "X": 10,
#         "L": 50,
#         "C": 100,
#         "D": 500,
#         "M": 1000
#     }
#     number = 0
#     s = s.replace("IV", "IIII").replace("IX", "VIIII")
#     s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
#     s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
#     for char in s:
#         number += translations[char]
#     return number
#
#
# print(romanToInt('XC'))
# class CustomList:
#     def __init__(self, initial_list=None):
#         self.data = initial_list if initial_list is not None else []
#
#     def insert(self, index, value):
#         # Ensure the index is within the bounds of the list
#         if index < 0:
#             index = max(len(self.data) + index, 0)
#         elif index > len(self.data):
#             index = len(self.data)
#
#         # Shift elements to the right to make space for the new element
#         self.data = self.data[:index] + [value] + self.data[index:]
#
#     def __str__(self):
#         return str(self.data)
#
# # Usage example:
# my_list = CustomList([1, 2, 3, 4, 5])
# print("Original list:", my_list)
#
# my_list.insert(2, 99)  # Insert 99 at index 2
# print("After insertion at index 2:", my_list)
#
# my_list.insert(0, 77)  # Insert 77 at the beginning
# print("After insertion at index 0:", my_list)
#
# my_list.insert(-1, 88)  # Insert 88 at the second last position
# print("After insertion at index -1:", my_list)
#
# my_list.insert(10, 100)  # Insert 100 at an index greater than the list size
# print("After insertion at index 10:", my_list)

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    ans = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        ans[key].append(s)
    print(ans.values())


groupAnagrams(['aste', 'stea', 'eat', 'tea','ice'])





























