# Ananda has changes the file 
import pandas
import bs4
import requests
import csv

URL_LINK = 'section_bangladesh_unit_page_url.csv'
CSV_LINK = 'dailySangram_international_1001_1100.csv'

def append_to_csv(row):

    global CSV_LINK

    with open(CSV_LINK, mode='a', newline='', encoding='utf-8') as unit_new_article:
            news_article_writer = csv.writer(unit_new_article, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            news_article_writer.writerow(row)

    #news_article_writer.close()    

    pass


def get_title_and_content(url):
    BASE_URL = url
    page = requests.get(BASE_URL)

    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    # < p
    #
    # class ="dateTime" > ১৩ অক্টোবর ২০২০  - ০৯:১
    #
    #     ৮ < / p >
    newsTitle = soup.find_all("h1")[0].getText()
    print(newsTitle)
    article_text = soup.find("div", {"class": "postBody"})

    article_text_time = soup.find("div", {"class": "postInfo"}).getText()
    #article_text_time = soup.find("p", {"class": "dateTime"}).getText()
    print(article_text_time)

    all_paragraphs = article_text("p")

    news_content = ""
    news_date = ""

    for paragraph in all_paragraphs:
        news_content += paragraph.getText()

    print("news: @@@@@   " + news_content)
    news_type = 'international'

    input_array = [news_type, article_text_time, newsTitle, news_content]

    append_to_csv(input_array)

    pass



with open(URL_LINK, encoding='utf-8') as unit_url_csv:
    readCSV = csv.reader(unit_url_csv)
    i = 1
    for row in readCSV:
        #if i > 2:
            #break
        try:
            print(i)
            get_title_and_content(row[0])
        except:
            print("no data ######################")
        i += 1
