from bs4 import BeautifulSoup
import requests, re


carname = input('Please enter the name of the car you want:')
truecar = requests.get('https://www.cars.com/shopping/results/?stock_type=all&makes[]=%s' % (carname))
soup = BeautifulSoup(truecar.text,'html.parser')

cars_name = soup.find_all('h2', attrs = {'class' : 'title'})
cars_price = soup.find_all('span', attrs = {'class' : 'primary-price'})
cars_mileage = soup.find_all('div', attrs = {'class' : 'mileage'})

output_name = re.findall(r'<h2 class="title">(.*?)</h2>',str(cars_name))
output_price = re.findall(r'<span class="primary-price">(.*?)</span>',str(cars_price))
output_mileage = re.findall(r'<div class="mileage">(.*?)</div>',str(cars_mileage))
zipped_output = zip(output_name,output_price,output_mileage)
output = list(zipped_output)
print ('Car Name  Car Price  Car Mileage')
for i in range(0,20):
    this_car = output[i]
    print(this_car[0],this_car[1],this_car[2])
