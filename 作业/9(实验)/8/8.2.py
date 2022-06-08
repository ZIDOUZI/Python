import requests
from bs4 import BeautifulSoup


def get_content(url):
    r = requests.request("get", url)
    r.encoding = r.apparent_encoding
    return r.text


def get_data(html_text):
    bf = BeautifulSoup(html_text, "html.parser")
    data = []
    for day in bf.find("ul", class_="t clearfix").find_all("li"):
        date = day.find("h1").get_text()
        weather = day.find("p", class_="wea").get_text()
        temp = day.find("p", class_="tem")
        highest = temp.find("span").get_text() + "℃"
        lowest = temp.find("i").get_text()
        data.append({"date": date, "weather": weather, "highest": highest, "lowest": lowest})
    return data


def write_data(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("日期\t\t\t天气\t\t\t最高温度\t最低温度\n")
        for day in data:
            if len(day["weather"]) >= 5:
                fill = "\t"
            elif len(day["weather"]) >= 3:
                fill = "\t\t"
            else:
                fill = "\t\t\t"
            f.write(day["date"] + "\t" + day["weather"] + fill + day["highest"] + "\t" + day["lowest"] + "\n")


if __name__ == '__main__':
    # noinspection HttpUrlsUsage
    write_data(get_data(get_content("http://www.weather.com.cn/weather/101010100.shtml")), "8-2.txt")
