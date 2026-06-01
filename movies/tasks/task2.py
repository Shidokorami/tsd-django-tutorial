from movies.models import Model, ParentModel


def get_models_for_parent(*, parent_id: int):
    # TODO: Task 2.2 - Return all Model rows linked to the ParentModel with given id.
    raise NotImplementedError


def get_parent_by_last_name(*, last_name: str):
    # TODO: Task 2.3 - Return the ParentModel with the given last_name.
    raise NotImplementedError


def count_models_for_parent(*, parent_id: int):
    # TODO: Task 2.4 - Return how many Model rows belong to the ParentModel.
    raise NotImplementedError


def get_parents_with_at_least_n_models(*, n: int):
    # TODO: Task 2.5 - Return ParentModel rows with at least n related Model rows.
    # Hint: Use annotate() with Count('models').
    raise NotImplementedError


def get_top_rated_model_for_parent(*, parent_id: int):
    # TODO: Task 2.6 - Return the highest-rated Model for the ParentModel (or None).
    raise NotImplementedError


def get_models_without_parent():
    # TODO: Task 2.7 - Return Model rows with no ParentModel assigned.
    raise NotImplementedError
