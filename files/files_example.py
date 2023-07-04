# with open(".\db.txt") as file:
#     pass
#     # print(file.readlines())
#     # print("************************")
#     # print(file.readline())
#     # print("************************")
#     # print(file.read())
#     # print("************************")
#
#
# with open(".\db.txt", 'r+w') as file:
#     text_from_file = file.read()
#     lines = text_from_file.split('\n')
#     print(lines)
#     for line in lines:
#         item = line.split(' ')
#         # print(item)
#         print(f"{item[0].split(':')[0]} = {item[0].split(':')[1]}")
#         print(f"{item[1].split(':')[0]} = {item[1].split(':')[1]}")
#         print(f"{item[2].split(':')[0]} = {item[2].split(':')[1]}")

#
# with open("new_file.txt", 'w') as file:
#     file.write("cba")
#
#
# class ContextManager:
#     def __enter__(self):
#         print("Enter to 'with' construction")
#
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Exit from 'with' construction")
#
# # manager = ContextManager()
# with ContextManager() as manager:
#     print("Before exception")
#     raise Exception()
#     print("After exception")

numbers = [1,2,3]
#
# with open("numbers.txt", 'w') as file:
#      file.write(str(numbers))
#
#
# with open("numbers.txt", 'r') as file:
#      n = list(file.read())
#      print(n)
#      print(type(n))

import pickle
with open("numbers.txt", 'w+b') as file:
     write_data = pickle.dumps(numbers)
     file.write(write_data)

with open("numbers.txt", 'r+b') as file:
     result = file.readline()
     # print(result)
     data_from_file = pickle.loads(result)
     print(data_from_file)
     print(type(data_from_file))