import bs4
import requests
import csv 


base_address = "https://dailysangram.com"
# category = "literature/the-arts"
category = "section/international"

section_bangladesh_category = ["", "accident", "environment", "emigration", "capital", "politics",
                               "obituary", "parliament", "national", "country", "court", "crime"]
all_url = []
i = 1

#for page_index in section_bangladesh_category:
for page_index in [i for i in range(1001, 1100)]:
    i = i + 1
    if i == 1:
        complete_url = base_address+'/'+category
        print(complete_url)
    else:
        complete_url = base_address+'/'+category+'/'+str(page_index)
        print(complete_url)

    all_url.append([complete_url])

    pass

with open('section_bangladesh_main_page_url.csv', mode='w', newline='', encoding='utf-8') as main_url_list:
    main_url_writer = csv.writer(main_url_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for url in all_url:
        print(url)
        main_url_writer.writerow(url)

main_url_list.close()