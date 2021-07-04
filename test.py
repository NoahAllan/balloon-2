# For the purpose of testing small amount of code

# Imports
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import json
import matplotlib.pyplot as plt
from matplotlib import style

f = open('C:/Users/noaha/PycharmProjects/balloon-2/Test_Data.json', 'r')
data = json.load(f)
# print(data)

data2 = data['positions']
data3 = data2['position']
data4 = data3[0]
data5 = data4['data']


latitude = data4["gps_lat"]
longitude = data4["gps_lon"]
altitude = data4["gps_alt"]
humidity = data5['humidity_external']
in_temperature = data5['temperature_internal']
ex_temperature = data5['temperature_external']
satellites = data5['satellites']
pressure = data5['pressure_external']
gps_time = data4['gps_time']



style.use('seaborn')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

xs = []
ys = []  #[7,5,3,-1,0,2,7,13,31,19,15,9,17,43,48,48,50,48,51,72,78,78,78,78,78,78,78,79,79,79,79,80,80,80,80,78,79,79,79,78,79,79,79,79,79,78,78,78,78,77,77,77,76,76,76,75,76,74,73,73,73,73,72,74,74,73,74,11,8,8,14,16,15,10,5,5,8,10,11,9,12,12,14,12,11,12,11,11,9,9,4,9,14,15,15,28,26,18,10,15,14,3,-1,10,17,13,61,59,64,10,12,14,12,10,9,10,9,11,13,14,16,16,15,16,17,17,16,16,15,16,15,15,15,15,14,13,11,12,12,8,8,7,8,-5,-4,-2,-1,2,3,1,1,-1,-1,-2,-1,-2,-1,-1,-2,-2,-1,-3,-3,-2,-2,-2,-1,0,1,2,4,5,6,6,5,6,7,7,6,8,11,10,8,7,10,9,8,6,3,2,5,4,4,3,3,3,3,4,6,7,5,6,6,7,7,7,5,6,9,14,17,17,13,10,5,2,2,5,3,4,5,6,7,6,5,15,12,8,7,7,9,12,15,14,15,15,13,12,11,43,68,69,70,73,73,73,73,73,72,12,16,19,21,22,16,13,11,12,13,15,13,12,13,15,15,16,16,15,16,17,18,16,18,17,16,19,18,17,17,17,14,15,16,16,16,14,13,15,16,16,15,16,17,21,23,23,23,25,25,23,18,15,18,19,16,14,13,9,5,1,0,3,6,9,9,3,2,2,0,0,4,6,10,13,13,15,14,12,10,11,8,9,14,16,13,16,18,21,22,18,13,5,3,7,9,7,6,7,4,3,6,6,9,13,14,15,14,15,15,13,11,10,11,14,16,15,15,13,10,9,7,7,8,10,12,13,13,14,15,16,12,12,13,14,13,13,13,13,12,11,12,12,12,12,13,13,13,13,13,12,12,11,13,13,13,11,12,13,15,17,12,14,0,4,9,10,9,11,13,15,12,12,11,11,12,13,12,10,11,13,13,13,13,12,12,13,15,16,18,19,21,26,27,25,18,11,5,-1,-4,-4,-6,5,3,3,8,6,6,4,2,0,0,-4,0,3,6,8,10,10,10,9,8,8,6,8,9,9,10,9,7,10,12,13,14,11,11,11,13,14,16,15,13,11,9,8,6,3,1,2,4,4,6,6,6,7,6,5,5,5,6,8,10,11,11,10,11,10,8,29,28,25,22,18,15,14,18,19,19,20,20,18,17,16,14,17,17,18,16,17,17,18,19,20,17,16,15,15,16,18,17,16,16,16,16,15,15,17,19,19,19,17,17,16,16,13,11,11,10,12,11,11,11,11,12,12,12,12,12,15,15,16,15,12,11,9,10,10,12,14,14,13,14,14,14,13,13,13,13,14,14,13,12,11,11,11,9,11,15,16,15,15,16,16,15,15,13,14,14,15,14,12,10,10,16,14,14,16,12,9,15,14,13,13,13,12,12,13,15,17,18,20,19,19,17,10,11,12,12,14,16,20,21,21,19,18,17,17,19,21,21,19,19,19,20,21,20,21,20,24,24,10,11,12,10,9
#
xs1 = []
for i in range(len(data['positions']['position'])):
    data4 = data3[i]
    data5 = data4['data']
    # alt = data4['gps_alt']
    x, y = data4['gps_time'], data5['temperature_internal']
    xs.append(x)
    ys.append(float(y))
    xs1.append(x[11:])

# for i in range(len(xs)):
#     xs[i] = xs[i][11:]
ax1.plot(xs, ys)
ax = plt.gca()
ax.tick_params(axis='x', labelrotation=60)
ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))


plt.setp(ax1.get_xticklabels(), visible=True)

plt.show()





# Stating which site will be scraped
# site = "https://spacenear.us/tracker/datanew.php?mode=1day&type=positions&format=json&vehicles=St_Osc"
#
# # Installing and opening the web driver
# driver = webdriver.Chrome(ChromeDriverManager().install())
#
# # Finding the site to be scraped
# driver.get(site)
# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")
#
# # print(soup)
# print(soup.select('position'))
# # returns JSON object as
# # a dictionary
# # data = json.load(soup)
# #
# # # Iterating through the json
# # # list
# # for i in data['position']:
# #     print(i)

