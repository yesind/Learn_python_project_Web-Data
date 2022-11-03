import csv
import datetime
import json
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import requests
import webapp.settings


"""переменные поиска """

#mark = 'AUDI' # MERCEDES
#model='A8'  #5ER C_KLASSE
#year_from = '2019'
#year_to = '2022'
fuel = 'GASOLINE' #GASOLINE / DIESEL
gear_type = 'ALL_WHEEL_DRIVE'


def fetch(url, params):
    headers = params["headers"]
    body = params["body"]
    return requests.post(url, headers=headers, data=body)

def response_function (mark,model,year_from,year_to,page):
    body = {"year_from":year_from,
         "year_to":year_to,
        #"km_age_from":0,
        #"km_age_to":200000,
        #"power_from":100,
        #"power_to":300,
        #"displacement_from":900,
        #"displacement_to":6000,
         "catalog_filter":[{"mark":mark,"model":model}],
         "owners_count_group":"LESS_THAN_TWO",
         "customs_state_group":"DOESNT_MATTER",
        "gear_type":[gear_type],
        #"engine_group":[fuel],
         "section":"all",
         "category":"cars",
         "output_type":"list",
         "page":str(page),
         "geo_radius":200,
         "geo_id":[121363]}
    response = fetch("https://auto.ru/-/ajax/desktop/listing/", {
                    "headers": {
                                "accept": "*/*",
                                "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                                "content-type": "application/json",
                                "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
                                "sec-ch-ua-mobile": "?0",
                                "sec-ch-ua-platform": "\"macOS\"",
                                "sec-fetch-dest": "empty",
                                "sec-fetch-mode": "same-origin",
                                "sec-fetch-site": "same-origin",
                                "x-client-app-version": "166.0.10087591",
                                "x-client-date": "1664476616232",
                                "x-csrf-token": "b36220aaef759de9fc79e165da0307e8c268cda79a9c317a",
                                "x-page-request-id": "8e4acf5436f70d7530b91245c85901af",
                                "x-requested-with": "XMLHttpRequest",
                                "x-retpath-y": webapp.settings.REFERER,
                                "cookie": webapp.settings.COOKIE,
                                "Referer": webapp.settings.REFERER,
                                "Referrer-Policy": "no-referrer-when-downgrade"
                                },
                "body": json.dumps(body),
    }).json()

    return response 

def create_csv(mark,model,year_from,year_to):
    auto_data = response_function(mark,model,year_from,year_to,0)
    #print(auto_data)
    cars_list  = [["Model","Full name","Price","VIN","Complectation","Milege","Power","Date","ID"]]
    total_lists = int(auto_data['pagination']['total_page_count'])
    print(total_lists)

    for list in range(total_lists+1):
        auto_data = response_function(mark,model,year_from,year_to,list)
        for car in auto_data['offers']:
        #print(car['vehicle_info']['model_info']['code'],car['vehicle_info']['tech_param']['human_name'],car['price_info']['RUR'],car['documents']['vin'],car['state']['mileage'],car['owner_expenses']['transport_tax']['horse_power'],car['additional_info']['update_date'],car['id'])
            try:
                complectation = car['vehicle_info']['complectation']['name']
            except KeyError:
                complectation = '----------'
            cars_list.append([
                    car['vehicle_info']['model_info']['code'],
                    car['vehicle_info']['tech_param']['human_name'],
                    car['price_info']['RUR'],
                    car['documents']['vin'],
                    complectation,
                    car['state']['mileage'],
                    car['owner_expenses']['transport_tax']['horse_power'],
                    datetime.datetime.now() - datetime.datetime.utcfromtimestamp(int(car['additional_info']['creation_date'])/1000),  #update_date
                    car['id']
            ])
            
    with open (f'{mark}_{model}.csv', 'w', encoding='UTF-8') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(cars_list)
    link_csv = f'{mark}_{model}.csv'
    return link_csv

#print(sorted(car_price_list))
#print(min(car_price_list),max(car_price_list))
def plot(mark,model,year_from,year_to):

    
    create_csv(mark,model,year_from,year_to)
    plt.switch_backend('Agg')
    df = pd.read_csv(f'{mark}_{model}.csv', encoding='UTF-8', sep=',')
    print(df.Price)
    fig, axs = plt.subplots(1,1)

    axs.hist(df.Price/1000000, bins=10, color = '0.8', linewidth = 8) ###

    axs.set_title(f'Распределение цены {mark} {model}')
    axs.set_ylabel('Количество автомобилей, шт.')
    axs.set_xlabel('Цена автомобиля, млн.руб.')
    axs.grid(which='major', color = '0.5', linestyle = ':')
    axs.ticklabel_format(style="plain", axis="both")
    axs.yaxis.set_major_locator(ticker.MultipleLocator(2))
    
    plt.savefig(f'webapp/static/images/<{mark}_{model}.jpg', dpi = 100)
    link_plot= f'webapp/static/images/{mark}_{model}.jpg'
    return link_plot

if __name__ == "__main__":
    plot()