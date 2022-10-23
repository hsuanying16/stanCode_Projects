"""
File: extension.py
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names' + year + '.html'
        ##################
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)
        items = soup.find_all('tbody')
        total_boy = 0
        total_girl = 0
        for item in items:
            all_trs = item.find_all('tr')
            for tr in all_trs:
                number_boy = tr.find_all('td')[2].text
                number_girl = tr.find_all('td')[4].text
                ans_boy = ''
                ans_girl = ''
                for i in range(len(number_boy)):
                    ch = number_boy[i]
                    if ch == ',':
                        ans_boy += ''
                    else:
                        ans_boy += ch
                total_boy += int(ans_boy)
                for i in range(len(number_girl)):
                    ch = number_boy[i]
                    if ch == ',':
                        ans_girl += ''
                    else:
                        ans_girl += ch
                total_girl += int(ans_girl)
            print(total_boy)
            print(total_girl)
        ##################


if __name__ == '__main__':
    main()
