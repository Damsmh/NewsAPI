import requests
from datetime import datetime, timedelta

def print_news(response):
    news_count = response['totalResults']
    if news_count >= 1:
        all_articles = response['articles']
        for article in all_articles:
            if article['source']['name'] != '[Removed]':
                print(article['source']['name'],
                    article['publishedAt'][:10],
                    article['title'],
                    article['description'],
                    article['content'],
                    article['url'], sep='\n\n')
                print('\n\n\n____________________________\n\n\n')
        
    else:
        print("Новостей по вашему запросу не было найдено!")

def main():
    key = open('apikey.ini', 'r').readline()

    
    
    from_date = datetime.now() - timedelta(days=2)
    to_date = datetime.now()

    while True:

        query = input('Введите заголовок новости: ')
        params = {'q': query, 'from': from_date, 'to': to_date, 'sortBy': 'popularity', 'language': 'en', 'page': 1, 'apiKey': key}
        response = requests.get(url='https://newsapi.org/v2/everything?', params=params)
        if response.status_code == 200:
            print_news(response.json())
        else: print(f"Ошибка {response.status_code}!")







if __name__ == "__main__":
    main()