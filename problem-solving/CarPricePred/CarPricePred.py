from bs4 import BeautifulSoup
from numpy.random.mtrand import permutation
from sklearn import tree
import requests, re

x = []
y = []
n = int(input('How many pages of the site do you want to check?'))
for i in range(1,n):
    truecar = requests.get('https://www.cars.com/shopping/results/?page=%i&page_size=20&list_price_max=&makes[]=&maximum_distance=20&models[]=&stock_type=all&zip=' % (i))
    soup = BeautifulSoup(truecar.text,'html.parser')

    cars_name = soup.find_all('h2', attrs = {'class' : 'title'})
    cars_mileage = soup.find_all('div', attrs = {'class' : 'mileage'})
    cars_price = soup.find_all('span', attrs = {'class' : 'primary-price'})

    input_year = []
    input_brand = []
    temp = re.findall(r'<h2 class="title">(.*?)</h2>',str(cars_name))
    temp2 = {}
    i = 0
    for car in temp:
        car = car.split(' ')
        input_year.append(int(car[0]))
        j = temp2.keys()
        if car[1] not in j:
            temp2[car[1].lower()] = i
            i += 1
        input_brand.append(temp2[car[1].lower()])

    input_mileage = []
    temp = re.findall(r'<div class="mileage">(.*?)</div>',str(cars_mileage))
    for car in temp:
        for char in car:
                if char in " ,.mi":
                    car = car.replace(char,'')
        input_mileage.append(int(car))

    output_price = []
    temp = re.findall(r'<span class="primary-price">(.*?)</span>',str(cars_price))
    for car in temp:
        for char in car:
            if char in " ,$":
                car = car.replace(char,'')
        output_price.append(int(car))

    zipped_output = zip(input_year,input_brand,input_mileage)
    x.extend(list(zipped_output))
    y.extend(output_price)


user_req = input('Please insert YEAR BRAND MILEAGE: ')
user_req = user_req.split(' ')
user_req = [(int(user_req[0]),temp2[user_req[1].lower()],int(user_req[2]))]

clf = tree.DecisionTreeClassifier()
clf = clf.fit (x, y)
answer = clf.predict(user_req)

print('The approximate price of your car is : ', int(answer))