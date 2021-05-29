# For the purpose of testing small amount of code

import csv
import datetime
import time
from pathlib import Path
from itertools import cycle

#
# def convert_from_unix_stamp(raw):
#     return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(raw) / 1000))
# #
# #
# # with open('C:/Users/noaha/PycharmProjects/balloon-2/test-data.csv', 'r', encoding='utf-8-sig') as csvfile:
# #     csv_reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
# #     for line in csv_reader:
# #         print(convert_from_unix_stamp(line[3]))
#
#
# with open('C:/Users/noaha/PycharmProjects/balloon-2/test-data.csv',  encoding='utf-8-sig') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'{", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'{row[0]} {row[1]} {row[2]} {row[3]}')
#             line_count += 1
#             bg = row[3]
#             print(datetime.datetime.fromtimestamp(float(bg)).strftime('%H:%M:%S'))

absolute_path = 'C:/Users/noaha/PycharmProjects/balloon-2/graphs/altitude.txt'
p = Path(absolute_path)
msg = 'msg 0'
message = cycle([msg, 'msg 1', 'msg 2', 'msg 3'])

while True:
    x = 1
    time.sleep(60 * x)
    with open(p, 'w') as f:
        f.write(next(message))

