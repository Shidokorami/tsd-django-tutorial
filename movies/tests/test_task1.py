from datetime import date

import pytest

from movies.models import Model, ParentModel
from movies.tasks.task1 import (
    count_models_with_rating_above,
    get_models_with_rating_below_excluding_year,
    get_models_with_word_in_title,
    get_parent_by_id,
    get_parents_born_on_or_after,
    get_top_n_models_by_rating,
)


@pytest.fixture
def parents(db):
    ParentModel.objects.create(first_name='George', last_name='Lucas', birthday=date(1944, 5, 14))
    ParentModel.objects.create(first_name='Steven', last_name='Spielberg', birthday=date(1946, 12, 18))
    ParentModel.objects.create(first_name='Rian', last_name='Johnson', birthday=date(1973, 12, 17))
    ParentModel.objects.create(first_name='Taika', last_name='Waititi', birthday=date(1975, 8, 16))
    ParentModel.objects.create(first_name='Christopher', last_name='Nolan', birthday=date(1970, 7, 30))
    return ParentModel.objects.all()


@pytest.fixture
def model_rows(db):
    Model.objects.create(title='Star Wars: Episode IV - A New Hope', release_year=1977, rating=8.6)
    Model.objects.create(title='Star Wars: Episode III - Revenge of the Sith', release_year=2005, rating=7.6)
    Model.objects.create(title='Star Wars: Episode VIII - The Last Jedi', release_year=2017, rating=6.9)
    Model.objects.create(title='American Graffiti', release_year=1973, rating=7.4)
    Model.objects.create(title='Jaws', release_year=1975, rating=8.1)
    Model.objects.create(title='Knives Out', release_year=2019, rating=7.9)
    Model.objects.create(title='Thor: Ragnarok', release_year=2017, rating=7.9)
    Model.objects.create(title='Inception', release_year=2010, rating=8.8)
    return Model.objects.all()


@pytest.mark.django_db
def test_get_parent_by_id(parents):
    result = get_parent_by_id(parent_id=parents[0].pk)
    assert result == parents[0]


@pytest.mark.django_db
def test_get_parents_born_on_or_after_gt(parents):
    result = get_parents_born_on_or_after(date=date(1970, 1, 1))
    assert set(result) == {
        parents.get(last_name='Nolan'),
        parents.get(last_name='Johnson'),
        parents.get(last_name='Waititi'),
    }


@pytest.mark.django_db
def test_get_parents_born_on_or_after_gte(parents):
    result = get_parents_born_on_or_after(date=date(1970, 7, 30))
    assert set(result) == {
        parents.get(last_name='Nolan'),
        parents.get(last_name='Johnson'),
        parents.get(last_name='Waititi'),
    }


@pytest.mark.django_db
def test_get_top_n_models_by_rating(model_rows):
    result = list(get_top_n_models_by_rating(n=3))
    assert result == [
        model_rows.get(title='Inception'),
        model_rows.get(title='Star Wars: Episode IV - A New Hope'),
        model_rows.get(title='Jaws'),
    ]


@pytest.mark.django_db
def test_count_models_with_rating_above(model_rows):
    result = count_models_with_rating_above(min_rating=8.0)
    assert result == 3


@pytest.mark.django_db
def test_get_models_with_word_in_title(model_rows):
    result = get_models_with_word_in_title(word='Star Wars')
    assert set(result) == {
        model_rows.get(title='Star Wars: Episode IV - A New Hope'),
        model_rows.get(title='Star Wars: Episode III - Revenge of the Sith'),
        model_rows.get(title='Star Wars: Episode VIII - The Last Jedi'),
    }


@pytest.mark.django_db
def test_get_models_with_word_in_title_case_insensitive(model_rows):
    result = get_models_with_word_in_title(word='star wars')
    assert set(result) == {
        model_rows.get(title='Star Wars: Episode IV - A New Hope'),
        model_rows.get(title='Star Wars: Episode III - Revenge of the Sith'),
        model_rows.get(title='Star Wars: Episode VIII - The Last Jedi'),
    }


@pytest.mark.django_db
def test_get_models_with_rating_below_excluding_year(model_rows):
    result = get_models_with_rating_below_excluding_year(max_rating=8.0, exclude_year=2017)
    assert set(result) == {
        model_rows.get(title='Star Wars: Episode III - Revenge of the Sith'),
        model_rows.get(title='American Graffiti'),
        model_rows.get(title='Knives Out'),
    }
