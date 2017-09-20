import requests


main_url = 'http://www.ivi.ru/mobileapi/'


def get_categories():
    url = '{}/{}'.format(main_url, 'categories')
    resp = requests.get(url)
    return resp.json()


def get_countries_with_content(**kwargs):
    url = '{}/{}/{}'.format(main_url, 'videos', 'countries')
    params = {k: v for k, v in kwargs}
    resp = requests.get(url, params=params)
    return resp.json()


def get_top_movies():
    url = '{}/{}/'.format(main_url, 'videos')
#    params = {k: v for k, v in kwargs}
    resp = requests.get(url)
    return resp.json()


def show_categories():
    categories = get_categories()
    for category in categories:
        print('\n{} {}:'.format(category['id'], category['title']))
        print(', '.join('{} {}'.format(genre['id'], genre['title'])
            for genre in category['genres']))


def show_countries_with_content():
    countries = get_countries_with_content()
    print('\n' + ', '.join(countries[id] for id in countries))


def show_top_movies():
    movies = get_top_movies()
    print('\n' + '\n'.join(movie['title'] for movie in movies))


if __name__ == '__main__':
    while True:
        print('\nIvi.ru API client')
        print('1. Categories and genres')
        print('2. Countries with content')
        print('3. Top 20 movies')
        print('0. Exit')
        try:
            n = int(input('> '))
            if n == 0:
                break
            elif n == 1:
                show_categories()
            elif n == 2:
                show_countries_with_content()
            elif n == 3:
                show_top_movies()
        except:
            pass
