from datetime import date

import pytest

from movies.models import Director, Movie
from movies.tasks.task2 import (
    get_movies_by_director_last_name,
    get_directors_with_movie_rating_at_least,
    get_movie_titles_by_director_id,
)


@pytest.fixture
def directors(db):
    return {
        'lucas': Director.objects.create(first_name='George', last_name='Lucas', birthday=date(1944, 5, 14)),
        'spielberg': Director.objects.create(first_name='Steven', last_name='Spielberg', birthday=date(1946, 12, 18)),
        'johnson': Director.objects.create(first_name='Rian', last_name='Johnson', birthday=date(1973, 12, 17)),
        'waititi': Director.objects.create(first_name='Taika', last_name='Waititi', birthday=date(1975, 8, 16)),
        'nolan': Director.objects.create(first_name='Christopher', last_name='Nolan', birthday=date(1970, 7, 30)),
    }


@pytest.fixture
def movies(db, directors):
    return {
        'a_new_hope': Movie.objects.create(
            title='Star Wars: Episode IV - A New Hope',
            release_year=1977,
            rating=8.6,
            director=directors['lucas'],
        ),
        'revenge_of_the_sith': Movie.objects.create(
            title='Star Wars: Episode III - Revenge of the Sith',
            release_year=2005,
            rating=7.6,
            director=directors['lucas'],
        ),
        'the_last_jedi': Movie.objects.create(
            title='Star Wars: Episode VIII - The Last Jedi',
            release_year=2017,
            rating=6.9,
            director=directors['johnson'],
        ),
        'american_graffiti': Movie.objects.create(
            title='American Graffiti',
            release_year=1973,
            rating=7.4,
            director=directors['lucas'],
        ),
        'jaws': Movie.objects.create(
            title='Jaws',
            release_year=1975,
            rating=8.1,
            director=directors['spielberg'],
        ),
        'knives_out': Movie.objects.create(
            title='Knives Out',
            release_year=2019,
            rating=7.9,
            director=directors['johnson'],
        ),
        'thor_ragnarok': Movie.objects.create(
            title='Thor: Ragnarok',
            release_year=2017,
            rating=7.9,
            director=directors['waititi'],
        ),
        'inception': Movie.objects.create(
            title='Inception',
            release_year=2010,
            rating=8.8,
            director=directors['nolan'],
        ),
    }


@pytest.mark.django_db
def test_get_movies_by_director_last_name(movies):
    result = get_movies_by_director_last_name(last_name='Lucas')
    assert set(result) == {
        movies['a_new_hope'],
        movies['revenge_of_the_sith'],
        movies['american_graffiti'],
    }


@pytest.mark.django_db
def test_get_directors_with_movie_rating_at_least(movies):
    result = get_directors_with_movie_rating_at_least(min_rating=8.0)
    assert set(result) == {
        ('George', 'Lucas'),
        ('Steven', 'Spielberg'),
        ('Christopher', 'Nolan'),
    }


@pytest.mark.django_db
def test_get_directors_with_movie_rating_at_least_distinct(movies):
    # Lucas has 3 movies >= 7.0 — without distinct() you would get duplicate director rows.
    result = list(get_directors_with_movie_rating_at_least(min_rating=7.0))
    assert len(result) == 5
    assert len(set(result)) == 5


@pytest.mark.django_db
def test_get_movie_titles_by_director_id(movies, directors):
    result = set(get_movie_titles_by_director_id(director_id=directors['lucas'].pk))
    assert result == {
        'Star Wars: Episode IV - A New Hope',
        'Star Wars: Episode III - Revenge of the Sith',
        'American Graffiti',
    }


@pytest.mark.django_db
def test_get_movie_titles_by_director_id_query_count(directors, django_assert_num_queries):
    with django_assert_num_queries(1):
        list(get_movie_titles_by_director_id(director_id=directors['lucas'].pk))
