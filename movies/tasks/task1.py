import datetime

from movies.models import Director, Movie


def get_director_by_id(*, director_id: int):
    # TODO: Task 1.1 - Create function that returns director by given id.
    raise NotImplementedError


def get_directors_born_on_or_after(*, date: datetime.date):
    # TODO: Task 1.2 - Create function that returns all directors born after or on given date
    # (Greater or equal)
    raise NotImplementedError


def get_top_n_movies_by_rating(*, n: int):
    # TODO: Task 1.3 - Create function that returns 'n' highest rated movies.
    # Hint: You may use python slicing
    raise NotImplementedError


def count_movies_with_rating_above(*, min_rating: float):
    # TODO: Task 1.4 - Create function that returns the total number of movies with rating greater than or equal to given min_rating.
    # Hint: Use .filter() and .count() methods.
    raise NotImplementedError


def get_movies_with_word_in_title(*, word: str):
    # TODO: Task 1.5 - Create function that returns movies containing the given word in their title (case insensitive).
    raise NotImplementedError


def get_movies_with_rating_below_excluding_year(*, max_rating: float, exclude_year: int):
    # TODO: Task 1.6 - Create function that returns movies with rating lower than max_rating
    # that were not released in exclude_year.
    raise NotImplementedError
