import csv
import datetime
import matplotlib.pyplot as plt
import pandas as pd
import requests


"""переменные поиска """
mark = 'AUDI' # MERCEDES
model='Q7'  #5ER C_KLASSE
year_from = '2021'
year_to = '2022'
fuel = 'DIESEL' #GASOLINE / DIESEL
gear_type = 'ALL_WHEEL_DRIVE'


def fetch(url, params):
    headers = params["headers"]
    body = params["body"]
    return requests.post(url, headers=headers, data=body)

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
                            "x-retpath-y": "https://auto.ru/moskva/cars/audi/a4/all/?year_from=2018&year_to=2022&km_age_from=25000&power_from=220&power_to=300&owners_count_group=LESS_THAN_TWO&customs_state_group=DOESNT_MATTER&engine_group=GASOLINE&gear_type=ALL_WHEEL_DRIVE&km_age_to=50000&displacement_from=900&displacement_to=2500&geo_id=121363",
                            "cookie": "suid=88e9eb5b305ce308cb8243f1f8e27c06.c681a3704ea0c4416882a316f647954a; _csrf_token=b36220aaef759de9fc79e165da0307e8c268cda79a9c317a; autoruuid=g632ef13227jcj30884i745vca1fvbe2.bc057a6c5b9a99feb4633a062df2787d; from=direct; yuidlt=1; yandexuid=1681386771590918846; my=YwA%3D; gdpr=0; _ym_uid=1664020789321130492; yandex_login=uid-plkwlm2f; i=GpLqNOFYDQHTCcExmvuJEWuwTmS+8xU23ZL98W1RyScLAnJe2zXA+IVbWS6lJWhsKHMuqMTpiY2y518PKgryOEJJ8X4=; autoru_sid=a%3Ag632ef13227jcj30884i745vca1fvbe2.bc057a6c5b9a99feb4633a062df2787d%7C1664625586335.604800.u1m_ZbNFlFIFtJKWLqfAbw.MoNxqW6M4zg6TtpMpybsmLrgSHb-VitiF7NFkGKuwBg; Session_id=3:1664472655.5.0.1650052385383:LnANuQ:1b.1.2:1|294041356.-1.0.1:46597069|61:10007754.378315.bdIFPWWZ47mkNvfKfGLTOt9nsCE; ys=udn.czo0NjU5NzA2OTpnZzpEbWl0cnkgWWVzaW4%3D#c_chck.4076486234; mda2_beacon=1664472655318; sso_status=sso.passport.yandex.ru:synchronized; _ym_isad=2; _yasc=ZGtNhmmn3fJGry/EepgIkLmkkA2IsWKT8M8z7Bo1FQFkpyg4; autoru-visits-count=1; autoru-visits-session-unexpired=1; cycada=pQJTMU5Ws0Y3w/rQBDPdLxhLh+5eSDKQiDRfB73s7Fs=; from_lifetime=1664476584172; _ym_d=1664476584; layout-config={\"win_width\":702,\"win_height\":843}",
                            "Referer": "https://auto.ru/moskva/cars/audi/a4/all/?year_from=2018&year_to=2022&km_age_from=25000&power_from=220&power_to=300&owners_count_group=LESS_THAN_TWO&customs_state_group=DOESNT_MATTER&engine_group=GASOLINE&gear_type=ALL_WHEEL_DRIVE&km_age_to=50000&displacement_from=900&displacement_to=2500&geo_id=121363",
                            "Referrer-Policy": "no-referrer-when-downgrade"
                              },
              "body": '{\"year_from\":' + year_from +
                        ',\"year_to\":'+ year_to +
                        ',\"km_age_from\":0'+
                        ',\"km_age_to\":20000'+
                        ',\"power_from\":200'+
                        ',\"power_to\":300'+
                        ',\"displacement_from\":900'+
                        ',\"displacement_to\":6000'+
                        ',\"catalog_filter\":[{\"mark\":\"'+mark+'\",\"model\":\"'+model+'\"}]'+
                        ',\"owners_count_group\":\"LESS_THAN_TWO\"'+
                        ',\"customs_state_group\":\"DOESNT_MATTER\"'+
                        ',\"gear_type\":[\"'+gear_type+'\"]'+
                        ',\"engine_group\":[\"'+fuel+'\"]'+
                        ',\"section\":\"all\"'+
                        ',\"category\":\"cars\"'+
                        ',\"output_type\":\"list\"'+
                        ',\"geo_radius\":200'+
                        ',\"geo_id\":[121363]}',
  "method": "POST"
})

with open (f'{mark}_{model}.csv', 'w', encoding='UTF-8') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(
        (
        "Model",
        "Complectation",
        "Price",
        "VIN",
        "Milege",
        "Power",
        "Date",
        "ID"
        )
    )

auto_data = response.json()
car_price_list = []
for car in auto_data['offers']:
    #print(car['vehicle_info']['model_info']['code'],car['vehicle_info']['tech_param']['human_name'],car['price_info']['RUR'],car['documents']['vin'],car['state']['mileage'],car['owner_expenses']['transport_tax']['horse_power'],car['additional_info']['update_date'],car['id'])
    car_price_list.append(car['price_info']['RUR'])
    
    with open (f'{mark}_{model}.csv', 'a', encoding='UTF-8') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(
            (
            car['vehicle_info']['model_info']['code'],
            car['vehicle_info']['tech_param']['human_name'],
            car['price_info']['RUR'],
            car['documents']['vin'],
            car['state']['mileage'],
            car['owner_expenses']['transport_tax']['horse_power'],
            datetime.datetime.utcfromtimestamp(int(car['additional_info']['creation_date'])/1000),  #update_date
            car['id']
            )
        )

print(sorted(car_price_list))
print(min(car_price_list),max(car_price_list))

df = pd.read_csv(f'{mark}_{model}.csv', encoding='UTF-8', sep=',')
print(df["Price"].describe())


#plt.hist(car_price_list,bins=10)
#plt.show()