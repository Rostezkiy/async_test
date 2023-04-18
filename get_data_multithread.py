import requests
import time
from concurrent.futures import ProcessPoolExecutor


def fetch_url_data(page_url):
    try:
        response = requests.get(page_url)
    except Exception as e:
        print(e, " - error while fetching url: ", page_url)
    else:
        return response.content


def get_all_url_data(url_list):
    with ProcessPoolExecutor() as executor:
        response = executor.map(fetch_url_data, url_list)
    return response


if __name__ == '__main__':
    url = "https://www.google.com/"
    for amount in [1, 10, 50, 100, 500]:
        start_time = time.time()
        responses = get_all_url_data([url] * amount)
        print('Collected ', amount, ' results for ', time.time() - start_time, ' seconds')
