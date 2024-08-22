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
from collections import defaultdict

#
#
# def group_anagrams(strs: list[str]):
#     result = defaultdict(list)
#     for string in strs:
#         key = ''.join(sorted(string))
#         result[key].append(string)
#     return f'anagrams: {list(result.values())}'
#
#
# print(group_anagrams(['str1', 'str2', 'str3', 'trs1', 'trs2', 'trs3']))
# def group_anagrams(strs: list[str]):
#     result = defaultdict(set)  # Use a set to avoid duplicates
#     for string in strs:
#         key = ''.join(sorted(string))
#         result[key].add(string)  # Add to the set to ensure uniqueness
#     # Convert sets back to lists for final output
#     return f'anagrams: {list(map(list, result.values()))}'
#
# print(group_anagrams(['str1', 'str2', 'str3', 'trs1', 'trs2', 'trs3', 'str1','tea','tea','eat ']))

# from django.db import transaction
#
# batch_size = 1000  # Adjust the batch size according to your database capacity
#
# users = User.objects.all()
#
# while users.exists():
#     with transaction.atomic():  # Ensure that each batch is treated as a single transaction
#         batch = users[:batch_size]
#         batch_ids = batch.values_list('id', flat=True)
#         User.objects.filter(id__in=batch_ids).delete()

car_objs = [
    'chevrolet nexia',
    'chevrolet onix',
    'BMW M5 cs',
    'BMW M5 c',
    'BMW M5',
    'BMW XM', 'Audi A4', 'Audi Q5', 'Audi Q7', 'Mercedes-Benz C-Class', 'Mercedes-Benz E-Class',
    'Mercedes-Benz S-Class', 'Lexus RX', 'Lexus NX', 'Toyota Camry', 'Toyota Corolla',
    'Honda Civic', 'Honda Accord', 'Honda CR-V', 'Ford Mustang', 'Ford F-150',
    'Chevrolet Malibu', 'Chevrolet Tahoe', 'Tesla Model S', 'Tesla Model 3', 'Tesla Model X',
    'Porsche 911', 'Porsche Cayenne', 'Porsche Macan', 'Jeep Wrangler', 'Jeep Grand Cherokee',
    'Dodge Charger', 'Dodge Challenger', 'BMW 3 Series', 'BMW 5 Series', 'BMW 7 Series',
    'BMW X3', 'BMW X5', 'BMW X7', 'Nissan Altima', 'Nissan Maxima', 'Nissan Rogue',
    'Mazda CX-5', 'Mazda 6', 'Mazda 3', 'Hyundai Elantra', 'Hyundai Sonata', 'Hyundai Tucson',
    'Kia Sorento', 'Kia Sportage', 'Kia Optima', 'Subaru Outback', 'Subaru Forester',
    'Volkswagen Passat', 'Volkswagen Jetta', 'Volkswagen Golf', 'Mitsubishi Outlander',
    'Mitsubishi Eclipse Cross', 'Jaguar F-Type', 'Jaguar XE', 'Land Rover Range Rover',
    'Land Rover Discovery', 'Alfa Romeo Giulia', 'Alfa Romeo Stelvio', 'Ferrari 488',
    'Lamborghini Huracan', 'Lamborghini Aventador', 'Maserati Ghibli', 'Maserati Levante'
]


def find_by_prefix(prefix, top_n):
    result = sorted((car for car in car_objs if car.startswith(prefix)), key=len)
    return result[:top_n]


print(find_by_prefix('BMW', 3))
