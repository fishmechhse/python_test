import time
import csv
import requests
import re
from bs4 import BeautifulSoup, PageElement


def get_book_info(url: str):
    book_request = requests.get(url)
    book_soup = BeautifulSoup(book_request.text, "html.parser")

    # Получение характеристики книги
    book_wrapper = book_soup.find('div', attrs={'data-testid': 'book-characteristics__wrapper'})
    price = book_soup.find('strong', attrs={'data-testid': 'book-sale-block__discount--art--price'})
    real_price = extract_price(prepare_text(price))
    tags = book_wrapper.find_all('div', recursive=False)

    book_attributes = dict({
        'age': '',
        'pages_count': '',
        'year': '',
    })
    fields = {
        'Возрастное ограничение': 'age',
        'Объем': 'pages_count',
        'Дата написания': 'year',
    }
    for tag in tags:
        pair_values = tag.text.strip().split(':')
        if len(pair_values) != 2:
            continue
        if pair_values[0] in fields:
            field_name = fields[pair_values[0]]
            book_attributes[field_name] = pair_values[1].strip()

    review_section = book_soup.find('section', attrs={'data-testid': 'comment-system__wrapper'})
    tags = review_section.select('article div div div p')

    reviews_count = book_soup.find('div', attrs={'data-testid': 'book-factoids__reviews'}).select_one('div')
    book_attributes['reviews_count'] = prepare_text(reviews_count)

    book_attributes['age'] = book_attributes['age'].strip().replace('+', '')
    reviews = []
    for tag in tags:
        reviews.append(tag.text)

    book_attributes['text_reviews'] = reviews
    book_attributes['price'] = real_price

    return book_attributes


def extract_pages_count(pages_count: str):
    extracted_pages_count = re.findall(r'\d+', pages_count)
    if len(extracted_pages_count) != 1:
        return pages_count
    return extracted_pages_count[0]


def extract_price(price: str):
    chars_to_remove = [' ', ' ', '₽']
    res = price.translate({ord(x): '' for x in chars_to_remove})
    res = res.replace(',', '.')
    try:
        res = float(res)
    except ValueError:
        print("value not float")
    return res


def prepare_rating_count(rating_count: PageElement):
    if rating_count is None:
        return 0
    return rating_count.text


def extract_year(year: str):
    extracted_year = re.findall(r'\d+', year)
    if len(extracted_year) != 1:
        return year
    return extracted_year[0]


def prepare_rating(rating: PageElement):
    if rating is None:
        return 0
    return float(rating.text.replace(',', '.'))


def prepare_text(author: PageElement):
    if author is None:
        return ""
    return author.text.strip()


def get_books(start: int, end: int):
    file = open(f'book_dataset_{start}_{end}.csv', 'w', newline='\n')
    fieldnames = ["rating", "rating_count", "age",
                  "year", "review_count", "pages_count", "price", "name", "author", "link", "text_reviews"]
    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
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

    writer.writeheader()
    url = 'https://www.litres.ru/genre/programmirovanie-5272/?page={}'
    for page in range(start, end + 1):
        # page = 18
        print(f"-----------------------------------------------")
        print(f"--------------print page {page}----------------")
        print(f"-----------------------------------------------")
        formatted_url = url.format(page)
        response = requests.get(formatted_url)
        soup = BeautifulSoup(response.text, "html.parser")
        time.sleep(1)
        for tag in soup.find_all('div', attrs={'data-testid': 'art__wrapper'}):
            try:
                object = dict()
                book_name = tag.find_next('p')
                book_author = tag.find_next('a', attrs={'data-testid': 'art__authorName'})
                book_link = tag.find_next('a', attrs={'data-testid': 'art__title'})
                book_rating = tag.find_next('div', attrs={'data-testid': 'art__ratingAvg'})
                # book_price = tag.find_next('strong', attrs={'data-testid': 'art_price--value'})
                rating_count = tag.find('div', attrs={'data-testid': 'art__ratingCount'})

                link = 'https://www.litres.ru' + book_link['href']

                book_attr = get_book_info(link)

                object['name'] = prepare_text(book_name)
                object['author'] = prepare_text(book_author)
                object['link'] = link
                object['rating'] = prepare_rating(book_rating)
                object['rating_count'] = prepare_rating_count(rating_count)

                object['review_count'] = book_attr['reviews_count']
                object['pages_count'] = book_attr['pages_count']
                object['price'] = book_attr['price']
                object['text_reviews'] = book_attr['text_reviews']
                object['age'] = book_attr['age']
                object['year'] = extract_year(book_attr['year'])
                print(object)
                writer.writerow(object)
            except Exception as e:
                print(e)

        # break
    file.close()


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

get_books(31, 40)
