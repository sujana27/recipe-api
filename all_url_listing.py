import bs4
import requests
import csv

all_unit_link = []
main_page_links = []
abc = []

base_address = "https://dailysangram.com"
# category = "section/science-technology/outer-space"


def get_sub_links(main_page_link):
    print("mainpagelink****")
    print(main_page_link)
    global all_unit_link

    page = requests.get(main_page_link)

    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    newsArticleDivs = soup.find_all("li", {"class": "even"})
    newsArticleLiOdd = soup.find_all("li", {"class": "odd"})

    p = 0
    for newsArticle in newsArticleDivs:
        #print(newsArticle)
        print(p)
        a_tag = newsArticle.find("a")
        news_link = a_tag['href']
        #complete_url = base_address + news_link[1:]
        complete_url = news_link[0:]
        print(complete_url)
        all_unit_link.append([complete_url])
        p = p + 1

    for newsArticle in newsArticleLiOdd:
        #print(newsArticle)
        print(p)
        a_tag = newsArticle.find("a")
        news_link = a_tag['href']
        #complete_url = base_address + news_link[1:]
        complete_url = news_link[0:]
        print(complete_url)
        all_unit_link.append([complete_url])
        p = p + 1
    pass

def write_csv(list_to_be_inserted):
    with open('section_bangladesh_unit_page_url.csv', mode='w', newline='', encoding='utf-8') as unit_url_list:
        unit_url_writer = csv.writer(unit_url_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for url in list_to_be_inserted:
            #print(url)
            unit_url_writer.writerow(url)

    unit_url_list.close()

    pass



with open('section_bangladesh_main_page_url.csv', encoding='utf-8') as main_url_csv:
    readCSV = csv.reader(main_url_csv)

    for row in readCSV:
        try:
            main_page_links.append(row[0])
        except:
            print("main_page_link not found@@@@@@@@@@@@@@@@@@@@@@@")

print('+---------------------------------------------------------+')

#get_sub_links(main_page_links[5])

for main_link in main_page_links:
    try:
        get_sub_links(main_link)
    except:
        print("sub-link not found$$$$$$$$$$$$$$$$$$$$$")
    pass

write_csv(all_unit_link)

print(len(all_unit_link))


