# import os
# import django
# root_dir = django.__path__[0]
# for root, dirs, files in os.walk(root_dir):
#     print(root, len(dirs), len(files))

import os
from time import perf_counter

import os
import random
# folder = 'some_data'
# # os.mkdir(folder)
# letters = [chr(code) for code in range(ord('a'), ord('z') + 1)]
# for _ in range(10 ** 3):
#     f_name = ''.join(random.sample(letters, random.randint(5, 10)))
#     f_content = bytes(random.randint(0, 255) for _ in range(random.randrange(10 ** 5)))
#
#     with open(os.path.join(folder, f'{f_name}.bin'), 'wb') as f:
#         f.write(f_content)

folder = 'some_data'
start = perf_counter()
size_threshold = 15 * 2 ** 10
small_files = [item for item in os.listdir(folder) if os.stat(os.path.join(folder, item)).st_size < size_threshold]

print(len(small_files), perf_counter() - start)

start = perf_counter()
small_files_2 = [item.name for item in os.scandir(folder) if item.stat().st_size < size_threshold]


print(len(small_files_2), perf_counter() - start)
print(small_files == small_files_2)