import time

import requests
from bs4 import BeautifulSoup

def get_book_info(url: str):
    book_request = requests.get(url)
    book_soup = BeautifulSoup(book_request.text, "html.parser")
    reviews = book_soup.find('div', attrs={'data-testid': 'book-factoids__reviews'}).select_one('div')

    volume_wrapper = book_soup.find('div', attrs={'data-testid': 'book-volume__wrapper'})
    volume = volume_wrapper.find_next('p')
    year = volume.find_next('p')
    age_rating = year.find_next('p')

    review_section = book_soup.find('section', attrs={'data-testid': 'comment-system__wrapper'})
    tags = review_section.select('article div div div p')
    book_attributes = dict()
    book_attributes['reviews_count'] = reviews.text
    book_attributes['pages_count'] = volume.text
    book_attributes['year'] = year.text
    book_attributes['age'] = age_rating.text

    reviews = []
    for tag in tags:
        reviews.append(tag.text)
    book_attributes['text_reviews'] = reviews
    return book_attributes


def get_books(limit: int):
    url = 'https://www.litres.ru/genre/programmirovanie-5272/?page={}'
    for page in range(1, limit):
        formatted_url = url.format(page)
        response = requests.get(formatted_url)
        soup = BeautifulSoup(response.text, "html.parser")
        for tag in soup.find_all('div', attrs={'data-testid': 'art__wrapper'}):
            object = dict()
            book_name = tag.find_next('p')
            book_author = tag.find_next('a', attrs={'data-testid': 'art__authorName'})
            book_link = tag.find_next('a', attrs={'data-testid': 'art__title'})
            book_rating = tag.find_next('div', attrs={'data-testid': 'art__ratingAvg'})
            book_rating_count = tag.find_next('div', attrs={'data-testid': 'art__ratingCount'})
            book_price = tag.find_next('strong', attrs={'data-testid': 'art_price--value'})

            link = 'https://www.litres.ru' + book_link['href']
            book_attr = get_book_info(link)
            object['name'] = book_name.text
            object['author'] = book_author.text
            object['link'] = link
            object['rating'] = book_rating.text
            object['rating_count'] = book_rating_count.text

            object['reviews_count'] = book_attr['reviews_count']
            object['pages_count'] = book_attr['pages_count']
            object['price'] = book_price.text
            object['text_reviews'] = book_attr['text_reviews']
            object['age'] = book_attr['age']
            object['year'] = book_attr['year']
            print(object)
            time.sleep(3)
            break

# name: название книги
# author: автор
# link: ссылка на книгу
# rating: рейтинг по 5-балльной шкале
# rating_count: количество оценок
# review_count: количество отзывов
# pages_count: объем (число страниц)
# price: цена
# text_reviews: тексты отзывов: список строк
# age: возрастное ограничение
# year: год написания

get_books(2)