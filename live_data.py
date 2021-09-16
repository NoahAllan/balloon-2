# imports:
import json
import urllib
import requests


def main():
    # Fetches the JSON file from Hab Hub
    url = "https://legacy-snus.habhub.org/tracker/datanew.php?mode=1day&type=positions&format=json&max_positions=0&" \
          "position_id=86480312&vehicles=PC4L-R"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    print(data)

    data2 = data['positions']
    data3 = data2['position']
    data4 = data3[0]
    data5 = data4['data']
    # print(data4)
    try:
        vehicle = data4["vehicle"]
    except:
        vehicle = 'ERROR'
    try:
        latitude = data4["gps_lat"]
    except:
        latitude = 'ERROR'
    try:
        longitude = data4["gps_lon"]
    except:
        longitude = 'ERROR'
    try:
        altitude = data4["gps_alt"]
    except:
        altitude = 'ERROR'
    try:
        humidity = data5['humidity_external']
    except:
        humidity = 'ERROR'
    try:
        in_temperature = data5['temperature_internal']
    except:
        in_temperature = 'ERROR'
    try:
        ex_temperature = data5['temperature_external']
    except:
        ex_temperature = 'ERROR'
    try:
        satellites = data5['satellites']
    except:
        satellites = 'ERROR'
    try:
        pressure = data5['pressure_external']
    except:
        pressure = 'ERROR'
    try:
        gps_time = data4['gps_time']
    except:
        gps_time = 'ERROR'
    f = open('OBS_Data/OBS_Location_Data.txt', 'w')
    f.truncate(0)
    f.write(f'{vehicle}\n'
            f'{gps_time[11:]}\n'
            f'{latitude}\n'
            f'{longitude}\n'
            f'{altitude} m\n'
            f'{humidity}\n'
            f'{in_temperature}\n'
            f'{ex_temperature}\n'
            f'{satellites}\n'
            f'{pressure}\n')
    f.close()
    print(vehicle)
    print(gps_time[11:])
    print(latitude)
    print(longitude)
    print(altitude)
    print(humidity)
    print(in_temperature)
    print(ex_temperature)
    print(satellites)
    print(pressure)


if __name__ == '__main__':
    # x = 0
    # while True:
        main()
        # if x == 100:
        #     break
        # else:
        #     x =+ 1

