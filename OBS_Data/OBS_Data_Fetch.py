import csv

Index = 'NO DATA'
Latitude = 'NO DATA'
Longitude = 'NO DATA'
Altitude = 'NO DATA'
Time = 'NO DATA'
Temperature = 'NO DATA'
Pressure = 'NO DATA'
Humidity = 'NO DATA'
CarbonDioxideLevels = 'NO DATA'
CarbonMonoxideLevels = 'NO DATA'
Ozone = 'NO DATA'
NitrousOxideLevels = 'NO DATA'
OxygenLevels = 'NO DATA'
DustLevels = 'NO DATA'
LightLevels = 'NO DATA'
UVLightLevels = 'NO DATA'

csvfile = open('C:/Users/noaha/PycharmProjects/balloon-2/test-data.csv', 'r', encoding='utf-8-sig')
csv_reader = csv.reader(csvfile)

line_count = 0
for line in csv_reader:
    if line_count == 0:
        line_count += 1
    else:
        if len(line) > 1:
            pass
lines = int(csv_reader.line_num)

line_count_1 = 0
y = True
while y is True:
    if line_count_1 != lines:
        line_count_1 += 1
    else:
        try:
            Index = line[0]
            Latitude = line[1]
            Longitude = line[2]
            Altitude = line[3]
            Time = line[4]
            Temperature = line[5]
            Pressure = line[6]
            Humidity = line[7]
            CarbonDioxideLevels = line[8]
            CarbonMonoxideLevels = line[9]
            Ozone = line[10]
            NitrousOxideLevels = line[11]
            OxygenLevels = line[12]
            DustLevels = line[13]
            LightLevels = line[14]
            UVLightLevels = line[15]
        except Exception as e:
            print('Error: %s' % str(e))

        y = False

f = open('OBS_Location_Data.txt', 'w')
f.truncate(0)
f.write(f'{Latitude}, {Longitude}\n'
        f'{Altitude} ft')
f.close()
