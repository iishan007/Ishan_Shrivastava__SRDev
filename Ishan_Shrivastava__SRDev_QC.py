import requests
from bs4 import BeautifulSoup
import time
import sys, getopt
import json

keywords = ''
counts = ''

myopts, args = getopt.getopt(sys.argv[1:],"k:c:")

for k,c in myopts:
    if k == '-k':
        keywords=c
    elif k == '-c':
        counts=c
    else:
        print ("Usage: %s -k Keywords -c Count" % sys.argv[0])

counts = int(counts)
USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}


def fetch_results(search_term, number_results):
    assert isinstance(search_term, str), 'Search term must be a string'
    assert isinstance(number_results, int), 'Number of results must be an integer'
    search_term_clean = search_term.replace(' ', '+')
    google_url = 'https://www.google.com/search?q={}&num={}'.format(search_term_clean, number_results)
    response = requests.get(google_url, headers=USER_AGENT)
    response.raise_for_status()

    return search_term, response.text
	
def parse_results(html, keyword):
    soup = BeautifulSoup(html, 'html.parser')
 
    found_results = []
    rank = 1
    result_block = soup.find_all('div', attrs={'class': 'g'})
    for result in result_block:
 
        link = result.find('a', href=True)
        title = result.find('h3')
        description = result.find('span', attrs={'class': 'st'})
        if link and title:
            link = link['href']
            title = title.get_text()
            if description:
                description = description.get_text()
            if link != '#':
                found_results.append({'keyword': keyword, 'rank': rank, 'title': title, 'description': description,'link':link})
                rank += 1
    return found_results

def scrape_google(search_term, number_results):
    try:
        keyword, html = fetch_results(search_term, number_results)
        results = parse_results(html, keyword)
        return results
    except AssertionError:
        raise Exception("Incorrect arguments parsed to function")
    except requests.HTTPError:
        raise Exception("You appear to have been blocked by Google")
    except requests.RequestException:
        raise Exception("Appears to be an issue with your connection")
 
 
# if __name__ == '__main__':
    # keywords = ['python', 'google scraping']
    # data = []
    # for keyword in keywords:
        # try:
            # results = scrape_google(keyword, 100)
            # for result in results:
                # data.append(result)
        # except Exception as e:
            # print(e)
        # finally:
            # time.sleep(10)
    # print(data)
	

data = []
results = scrape_google(keywords,counts)
for result in results:
    print ('Rank: ',result['rank'],'Title: ',result['title'])
    print ('Desc: ',result['description'], 'Link:',result['link'])
