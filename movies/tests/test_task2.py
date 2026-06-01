from datetime import date

import pytest

from movies.models import Director, Movie
from movies.tasks.task2 import (
    count_movies_for_director,
    get_director_by_last_name,
    get_directors_with_at_least_n_movies,
    get_movies_for_director,
    get_movies_without_director,
    get_top_rated_movie_for_director,
)


@pytest.fixture
def directors():
    Director.objects.create(first_name='George', last_name='Lucas', birthday=date(1944, 5, 14))
    Director.objects.create(first_name='Steven', last_name='Spielberg', birthday=date(1946, 12, 18))
    Director.objects.create(first_name='Rian', last_name='Johnson', birthday=date(1973, 12, 17))
    return Director.objects.all()


@pytest.fixture
def movies(directors):
    lucas = directors.get(last_name='Lucas')
    spielberg = directors.get(last_name='Spielberg')
    johnson = directors.get(last_name='Johnson')
    Movie.objects.create(title='Star Wars IV', release_year=1977, rating=8.6, director=lucas)
    Movie.objects.create(title='Star Wars III', release_year=2005, rating=7.6, director=lucas)
    Movie.objects.create(title='Jaws', release_year=1975, rating=8.1, director=spielberg)
    Movie.objects.create(title='Knives Out', release_year=2019, rating=7.9, director=johnson)
    Movie.objects.create(title='Orphan Film', release_year=2000, rating=5.0, director=None)
    return Movie.objects.all()


@pytest.mark.django_db
def test_get_movies_for_director(directors, movies):
    lucas = directors.get(last_name='Lucas')
    result = set(get_movies_for_director(director_id=lucas.pk))
    assert result == {
        movies.get(title='Star Wars IV'),
        movies.get(title='Star Wars III'),
    }


@pytest.mark.django_db
def test_get_director_by_last_name(directors):
    result = get_director_by_last_name(last_name='Spielberg')
    assert result == directors.get(last_name='Spielberg')


@pytest.mark.django_db
def test_count_movies_for_director(directors, movies):
    lucas = directors.get(last_name='Lucas')
    assert count_movies_for_director(director_id=lucas.pk) == 2


@pytest.mark.django_db
def test_get_directors_with_at_least_n_movies(directors, movies):
    result = set(get_directors_with_at_least_n_movies(n=2))
    assert result == {directors.get(last_name='Lucas')}


@pytest.mark.django_db
def test_get_top_rated_movie_for_director(directors, movies):
    lucas = directors.get(last_name='Lucas')
    result = get_top_rated_movie_for_director(director_id=lucas.pk)
    assert result == movies.get(title='Star Wars IV')


@pytest.mark.django_db
def test_get_movies_without_director(movies):
    result = set(get_movies_without_director())
    assert result == {movies.get(title='Orphan Film')}
