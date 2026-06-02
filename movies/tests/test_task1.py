from datetime import date

import pytest

from movies.models import Director, Movie
from movies.tasks.task1 import (
    count_movies_with_rating_above,
    get_director_by_id,
    get_directors_born_on_or_after,
    get_movies_with_rating_below_excluding_year,
    get_movies_with_word_in_title,
    get_top_n_movies_by_rating,
)


@pytest.fixture
def directors(db):
    Director.objects.create(first_name='George', last_name='Lucas', birthday=date(1944, 5, 14))
    Director.objects.create(first_name='Steven', last_name='Spielberg', birthday=date(1946, 12, 18))
    Director.objects.create(first_name='Rian', last_name='Johnson', birthday=date(1973, 12, 17))
    Director.objects.create(first_name='Taika', last_name='Waititi', birthday=date(1975, 8, 16))
    Director.objects.create(first_name='Christopher', last_name='Nolan', birthday=date(1970, 7, 30))
    return Director.objects.all()


@pytest.fixture
def movies(db):
    Movie.objects.create(title='Star Wars: Episode IV - A New Hope', release_year=1977, rating=8.6)
    Movie.objects.create(title='Star Wars: Episode III - Revenge of the Sith', release_year=2005, rating=7.6)
    Movie.objects.create(title='Star Wars: Episode VIII - The Last Jedi', release_year=2017, rating=6.9)
    Movie.objects.create(title='American Graffiti', release_year=1973, rating=7.4)
    Movie.objects.create(title='Jaws', release_year=1975, rating=8.1)
    Movie.objects.create(title='Knives Out', release_year=2019, rating=7.9)
    Movie.objects.create(title='Thor: Ragnarok', release_year=2017, rating=7.9)
    Movie.objects.create(title='Inception', release_year=2010, rating=8.8)
    return Movie.objects.all()


@pytest.mark.django_db
def test_get_director_by_id(directors):
    result = get_director_by_id(director_id=directors[0].pk)
    assert result == directors[0]


@pytest.mark.django_db
def test_get_directors_born_on_or_after_gt(directors):
    result = get_directors_born_on_or_after(date=date(1970, 1, 1))
    assert set(result) == {
        directors.get(last_name='Nolan'),
        directors.get(last_name='Johnson'),
        directors.get(last_name='Waititi'),
    }


@pytest.mark.django_db
def test_get_directors_born_on_or_after_gte(directors):
    result = get_directors_born_on_or_after(date=date(1970, 7, 30))
    assert set(result) == {
        directors.get(last_name='Nolan'),
        directors.get(last_name='Johnson'),
        directors.get(last_name='Waititi'),
    }


@pytest.mark.django_db
def test_get_top_n_movies_by_rating(movies):
    result = list(get_top_n_movies_by_rating(n=3))
    assert result == [
        movies.get(title='Inception'),
        movies.get(title='Star Wars: Episode IV - A New Hope'),
        movies.get(title='Jaws'),
    ]


@pytest.mark.django_db
def test_count_movies_with_rating_above(movies):
    result = count_movies_with_rating_above(min_rating=8.0)
    assert result == 3


@pytest.mark.django_db
def test_get_movies_with_word_in_title(movies):
    result = get_movies_with_word_in_title(word='Star Wars')
    assert set(result) == {
        movies.get(title='Star Wars: Episode IV - A New Hope'),
        movies.get(title='Star Wars: Episode III - Revenge of the Sith'),
        movies.get(title='Star Wars: Episode VIII - The Last Jedi'),
    }


@pytest.mark.django_db
def test_get_movies_with_word_in_title_case_insensitive(movies):
    result = get_movies_with_word_in_title(word='star wars')
    assert set(result) == {
        movies.get(title='Star Wars: Episode IV - A New Hope'),
        movies.get(title='Star Wars: Episode III - Revenge of the Sith'),
        movies.get(title='Star Wars: Episode VIII - The Last Jedi'),
    }


@pytest.mark.django_db
def test_get_movies_with_rating_below_excluding_year(movies):
    result = get_movies_with_rating_below_excluding_year(max_rating=8.0, exclude_year=2017)
    assert set(result) == {
        movies.get(title='Star Wars: Episode III - Revenge of the Sith'),
        movies.get(title='American Graffiti'),
        movies.get(title='Knives Out'),
    }
