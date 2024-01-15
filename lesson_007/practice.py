import zipfile
from pprint import pprint
from random import randint

# zip_file_name = 'voyna-i-mir.zip'
#
# zfile = zipfile.ZipFile(zip_file_name, 'r')
# # zfile.printdir()
# for filename in zfile.namelist():
#     # print(filename)
#     zfile.extract(filename)

class Chatterer:
    analize_count = 4
    def __init__(self, zip_file_name):
        self.zip_file_name = zip_file_name
        self.stat = {}

    def unzip(self):
         zfile = zipfile.ZipFile(self.zip_file_name, 'r')
         for filename in zfile.namelist():
             zfile.extract(filename)
         return filename

    def collect(self, filename):
        sequence = ' ' * self.analize_count
        with open(filename, 'r', encoding='cp1251') as file:
            for line in file:
                line = line[:-1]
                # print(line)
                for char in line:
                    if sequence in self.stat:
                        if char in self.stat[sequence]:
                            self.stat[sequence][char] += 1
                        else:
                            self.stat[sequence][char] = 1
                    else:
                        self.stat[sequence] = {char: 1}
                    sequence = sequence[1:] + char


# filename = 'voyna-i-mir.txt'
# stat = {}
# stat = {'а':{'т': 500, 'х': 5, }, '':{'о': 100, 'у': 50, }}

# analize_count = 4
# sequence = ' ' * analize_count
# with open(filename, 'r', encoding='cp1251') as file:
#     for line in file:
#         line = line[:-1]
#         # print(line)
#         for char in line:
#             if sequence in stat:
#                 if char in stat[sequence]:
#                     stat[sequence][char] += 1
#                 else:
#                     stat[sequence][char] = 1
#             else:
#                 stat[sequence] = {char: 1}
#             sequence = sequence[1:] + char
#
# pprint(stat)
# pprint(len(stat))

totals = {}
stat_for_generate = {}
for sequence, char_stat in stat.items():
    totals[sequence] = 0
    stat_for_generate[sequence] = []
    for char, count in char_stat.items():
        totals[sequence] += count
        stat_for_generate[sequence].append([count, char])
    stat_for_generate[sequence].sort(reverse=True)

# pprint(totals)
# pprint(stat_for_generate)

N = 1000
printed = 0

sequence = ' ' * analize_count
spaces_printed = 0
while printed < N:
    char_stat = stat_for_generate[sequence]
    total = totals[sequence]
    dice = randint(1, total)
    pos = 0
    for count, char in char_stat:
        pos += count
        if dice <= pos:
            break
    print(char, end='')
    if char == ' ':
        spaces_printed += 1
        if spaces_printed >= 10:
            print()
            spaces_printed = 0
    printed += 1
    sequence = sequence[1:] + char
