from movies.models import Director, Movie


def get_movies_by_director_last_name(*, last_name: str):
    # TODO: Task 2.2 - Create function that returns all movies by director with given last name.
    raise NotImplementedError


def get_directors_with_movie_rating_at_least(*, min_rating: float):
    # TODO: Task 2.3 - Create function that returns first and last names of directors
    # who have at least one movie with rating greater than or equal to min_rating.
    # Remember to avoid duplicates
    raise NotImplementedError


def get_movie_titles_by_director_id(*, director_id: int):
    # TODO: Task 2.4 - Create function that returns movie titles for the given director.
    # Hint: Use select_related to avoid unnecessary queries.
    raise NotImplementedError
