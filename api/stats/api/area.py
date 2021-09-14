# -*- coding: utf-8 -*- 
# @Author : Eurkon
# @Date : 2021/9/7 10:55

import requests
import threading
from bs4 import BeautifulSoup


class Area():
    def __init__(self):
        self.url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/'
        self.county_href = ''
        self.city_href = ''
        self.town_href = ''
        self.province = []

    def get_data(self):
        province_response = requests.get(self.url)
        province_soup = BeautifulSoup(province_response.text, 'html.parser')
        province_list = province_soup.select('tr.provincetr > td > a')
        threads = []
        for province_item in province_list:
            print(province_item.get_text().encode("iso-8859-1").decode('gbk'))
            t1 = threading.Thread(target=self.area_thread, args=(1, province_item),
                                  name=province_item.get_text().encode("iso-8859-1").decode('gbk'))
            threads.append(t1)
        for t in threads:
            t.start()

    def area_thread(self, num, province_item):
        city = self.get_city(province_item)
        print('city===' + city)
        self.province.append({'name': province_item.get_text().encode("iso-8859-1").decode('gbk'), 'child': city})

    def get_city(self, province_item):
        city = []
        self.city_href = province_item['href']
        city_response = requests.get(self.url + self.city_href)
        city_soup = BeautifulSoup(city_response.text, 'html.parser')
        city_list = city_soup.select('tr.citytr')
        for city_item in city_list:
            print(city_item.select('td')[1].get_text().encode("iso-8859-1").decode('gbk'))
            if len(city_item.select('td')[0].select('a')) > 0:
                county = self.get_county(city_item)
                city.append(
                    {'name': city_item.select('td')[1].get_text().encode("iso-8859-1").decode('gbk'),
                     'code': city_item.select('td')[0].get_text().encode("iso-8859-1").decode('gbk'),
                     'child': county})
        return city

    def get_county(self, city_item):
        county = []
        self.county_href = city_item.select('td')[0].select('a')[0]['href']
        county_response = requests.get(self.url + self.county_href)
        county_soup = BeautifulSoup(county_response.text,
                                    'html.parser')
        county_list = county_soup.select('tr.countytr')
        for county_item in county_list:
            print(county_item.select('td')[1].get_text().encode("iso-8859-1").decode('gbk'))
            if len(county_item.select('td')[0].select('a')) > 0:
                town = self.get_town(county_item)
                county.append(
                    {'name': county_item.select('td')[1].get_text().encode("iso-8859-1").decode('gbk'),
                     'code': county_item.select('td')[0].get_text().encode("iso-8859-1").decode('gbk'),
                     'child': town})
        return county

    def get_town(self, county_item):
        town = []
        self.town_href = county_item.select('td')[0].select('a')[0]['href']
        town_response = requests.get(self.url + self.county_href[0:2] + '/' + self.town_href)
        town_soup = BeautifulSoup(town_response.text,
                                  'html.parser')
        town_list = town_soup.select('tr.towntr')
        for town_item in town_list:
            print(town_item.select('td')[1].get_text().encode("iso-8859-1").decode('gbk'))
            if len(town_item.select('td')[0].select('a')) > 0:
                village = self.get_village(town_item)
                town.append(
                    {'name': town_item.select('td')[1].get_text().encode("iso-8859-1").decode('gbk'),
                     'code': town_item.select('td')[0].get_text().encode("iso-8859-1").decode('gbk'),
                     'child': village})
        return town

    def get_village(self, town_item):
        village = []
        village_href = town_item.select('td')[0].select('a')[0]['href']
        village_response = requests.get(
            self.url + self.county_href[0:2] + '/' + self.town_href[0:2] + '/' + village_href)
        village_soup = BeautifulSoup(
            village_response.text,
            'html.parser')
        village_list = village_soup.select('tr.villagetr')
        for village_item in village_list:
            print(village_item.select('td')[2].get_text().encode("iso-8859-1").decode('gbk'))
            village.append({'name': village_item.select('td')[2].get_text().encode("iso-8859-1").decode('gbk'),
                            'code': village_item.select('td')[0].get_text().encode("iso-8859-1").decode('gbk')})
        return village


if __name__ == '__main__':
    area = Area()
    with open('F:/province.json', 'a') as f:
        f.write(str(area.get_data()))
