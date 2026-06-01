from datetime import date

import pytest

from movies.models import Model, ParentModel
from movies.tasks.task2 import (
    count_models_for_parent,
    get_models_for_parent,
    get_models_without_parent,
    get_parent_by_last_name,
    get_parents_with_at_least_n_models,
    get_top_rated_model_for_parent,
)


@pytest.fixture
def parents_three(db):
    ParentModel.objects.create(first_name='George', last_name='Lucas', birthday=date(1944, 5, 14))
    ParentModel.objects.create(first_name='Steven', last_name='Spielberg', birthday=date(1946, 12, 18))
    ParentModel.objects.create(first_name='Rian', last_name='Johnson', birthday=date(1973, 12, 17))
    return ParentModel.objects.all()


@pytest.fixture
def model_rows_with_parent(db, parents_three):
    lucas = parents_three.get(last_name='Lucas')
    spielberg = parents_three.get(last_name='Spielberg')
    johnson = parents_three.get(last_name='Johnson')
    Model.objects.create(title='Star Wars IV', release_year=1977, rating=8.6, parent=lucas)
    Model.objects.create(title='Star Wars III', release_year=2005, rating=7.6, parent=lucas)
    Model.objects.create(title='Jaws', release_year=1975, rating=8.1, parent=spielberg)
    Model.objects.create(title='Knives Out', release_year=2019, rating=7.9, parent=johnson)
    Model.objects.create(title='Orphan row', release_year=2000, rating=5.0, parent=None)
    return Model.objects.all()


@pytest.mark.django_db
def test_get_models_for_parent(parents_three, model_rows_with_parent):
    lucas = parents_three.get(last_name='Lucas')
    result = set(get_models_for_parent(parent_id=lucas.pk))
    assert result == {
        model_rows_with_parent.get(title='Star Wars IV'),
        model_rows_with_parent.get(title='Star Wars III'),
    }


@pytest.mark.django_db
def test_get_parent_by_last_name(parents_three):
    result = get_parent_by_last_name(last_name='Spielberg')
    assert result == parents_three.get(last_name='Spielberg')


@pytest.mark.django_db
def test_count_models_for_parent(parents_three, model_rows_with_parent):
    lucas = parents_three.get(last_name='Lucas')
    assert count_models_for_parent(parent_id=lucas.pk) == 2


@pytest.mark.django_db
def test_get_parents_with_at_least_n_models(parents_three, model_rows_with_parent):
    result = set(get_parents_with_at_least_n_models(n=2))
    assert result == {parents_three.get(last_name='Lucas')}


@pytest.mark.django_db
def test_get_top_rated_model_for_parent(parents_three, model_rows_with_parent):
    lucas = parents_three.get(last_name='Lucas')
    result = get_top_rated_model_for_parent(parent_id=lucas.pk)
    assert result == model_rows_with_parent.get(title='Star Wars IV')


@pytest.mark.django_db
def test_get_models_without_parent(model_rows_with_parent):
    result = set(get_models_without_parent())
    assert result == {model_rows_with_parent.get(title='Orphan row')}
