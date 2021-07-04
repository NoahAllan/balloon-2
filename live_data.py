# imports:
import json
import urllib
import requests


def main():
    # Fetches the JSON file from Hab Hub
    url = "https://spacenear.us/tracker/datanew.php?mode=1day&type=positions&format=json&vehicles=St_Osc"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    print(data)

    data2 = data['positions']
    data3 = data2['position']
    data4 = data3[0]
    data5 = data4['data']
    print(data4)

    latitude = data4["gps_lat"]
    longitude = data4["gps_lon"]
    altitude = data4["gps_alt"]
    humidity = data5['humidity_external']
    in_temperature = data5['temperature_internal']
    ex_temperature = data5['temperature_external']
    satellites = data5['satellites']
    pressure = data5['pressure_external']
    gps_time = data4['gps_time']
    f = open('OBS_Data/OBS_Location_Data.txt', 'w')
    f.truncate(0)
    f.write(f'{gps_time[11:]}\n'
            f'{latitude}\n'
            f'{longitude}\n'
            f'{altitude} m\n'
            f'{humidity}\n'
            f'{in_temperature}\n'
            f'{ex_temperature}\n'
            f'{satellites}\n'
            f'{pressure}\n')
    f.close()


if __name__ == '__main__':
    main()

