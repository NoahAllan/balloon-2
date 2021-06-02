import csv

csvfile = open('C:/Users/noaha/PycharmProjects/balloon-2/test-data.csv', 'r', encoding='utf-8-sig')
csv_reader = csv.reader(csvfile)

line_count = 0
for line in csv_reader:
    # if len(line) > 1:
    if line_count == 0:
        print(line)
        line_count += 1
    else:
        print(line)
