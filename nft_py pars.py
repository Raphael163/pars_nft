import requests
from bs4 import BeautifulSoup
def get_data():
    headers = {'User-Agent':
                   "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "}
    # main
    url = 'https://coinmarketcap.com/nft/upcoming/'
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, "html.parser")
    data = soup.find("div", class_="table")

    # main scripts
    name = data.find("div", class_="sc-15yqupo-0 cqAZPF")
    name_info = name.find("span").text
    crypt_info = name.find("span", class_="lsid7u-0 kciUBo").text
    description = data.find("div", class_="sc-15yqupo-0 cqAZPF").text

    # social Links
    result_social = []
    social_info = data.find("div", class_="sc-15yqupo-1 gEtvIk")
    for link in social_info.find_all('a'):
        result_social.append(link.get('href'))

    # time starts in
    result_time = []
    time_info = data.find("div", class_="sc-15yqupo-2 dhMNvT")
    time = time_info.find('p')
    for link in time_info.find_all('p'):
        result_time.append(link.text)

    # Sale Info
    result_price = []
    prece_info = data.find("div", class_="sc-1ay2tc4-0 dRIGnz")
    price = prece_info.find('span').text
    for link in prece_info.find_all('span'):
        result_price.append(link.text)

    print(f'Name - {name_info}\nDescription - {description}\n'
         f'Crypt - {crypt_info}\nPrice Sale Info - {result_price}\nTime Starts in - {str(result_time)}\nSocial Links - {result_social}')


def main():
    get_data()


if __name__ == '__main__':
    main()
