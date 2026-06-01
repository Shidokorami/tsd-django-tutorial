import datetime

from movies.models import Model, ParentModel


def get_parent_by_id(*, parent_id: int):
    # TODO: Task 1.1 - Return ParentModel by given id.
    raise NotImplementedError


def get_parents_born_on_or_after(*, date: datetime.date):
    # TODO: Task 1.2 - Return all ParentModel rows with birthday on or after the given date.
    raise NotImplementedError


def get_top_n_models_by_rating(*, n: int):
    # TODO: Task 1.3 - Return n Model rows with the highest rating.
    raise NotImplementedError


def count_models_with_rating_above(*, min_rating: float):
    # TODO: Task 1.4 - Return count of Model rows with rating >= min_rating.
    raise NotImplementedError


def get_models_with_word_in_title(*, word: str):
    # TODO: Task 1.5 - Return Model rows whose title contains word (case insensitive).
    raise NotImplementedError


def get_models_with_rating_below_excluding_year(*, max_rating: float, exclude_year: int):
    # TODO: Task 1.6 - Return Model rows with rating < max_rating and release_year != exclude_year.
    raise NotImplementedError
