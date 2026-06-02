import datetime

from movies.models import Director, Movie


def get_director_by_id(*, director_id: int):
    # TODO: Task 1.1 - Return director by given id.
    raise NotImplementedError


def get_directors_born_on_or_after(*, date: datetime.date):
    # TODO: Task 1.2 - Return all directors born on or after the given date.
    raise NotImplementedError


def get_top_n_movies_by_rating(*, n: int):
    # TODO: Task 1.3 - Return n highest rated movies.
    raise NotImplementedError


def count_movies_with_rating_above(*, min_rating: float):
    # TODO: Task 1.4 - Return count of movies with rating >= min_rating.
    raise NotImplementedError


def get_movies_with_word_in_title(*, word: str):
    # TODO: Task 1.5 - Return movies whose title contains word (case insensitive).
    raise NotImplementedError


def get_movies_with_rating_below_excluding_year(*, max_rating: float, exclude_year: int):
    # TODO: Task 1.6 - Return movies with rating < max_rating and release_year != exclude_year.
    raise NotImplementedError
