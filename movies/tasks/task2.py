from movies.models import Director, Movie


def get_movies_for_director(*, director_id: int):
    # TODO: Task 2.2 - Return all movies directed by the director with given id.
    raise NotImplementedError


def get_director_by_last_name(*, last_name: str):
    # TODO: Task 2.3 - Return the director with the given last name.
    raise NotImplementedError


def count_movies_for_director(*, director_id: int):
    # TODO: Task 2.4 - Return how many movies the director has made.
    raise NotImplementedError


def get_directors_with_at_least_n_movies(*, n: int):
    # TODO: Task 2.5 - Return directors who have at least n movies.
    # Hint: Use annotate() with Count('movies').
    raise NotImplementedError


def get_top_rated_movie_for_director(*, director_id: int):
    # TODO: Task 2.6 - Return the highest rated movie for the given director (or None).
    raise NotImplementedError


def get_movies_without_director():
    # TODO: Task 2.7 - Return movies that have no director assigned.
    raise NotImplementedError
