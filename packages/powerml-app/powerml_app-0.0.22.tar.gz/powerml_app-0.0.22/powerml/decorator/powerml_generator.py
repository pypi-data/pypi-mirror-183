import functools
from typing import TypedDict


class ModelData(TypedDict):
    model_input: str
    model_output: str


def powerml_generator(func):
    @functools.wraps(func)
    def wrapper():
        result: list[ModelData] = func()
        # Type checking
        if type(result) != list:
            raise Exception(
                f"Return Value of {func.__name__} is improperly formatted. It should be a list of dictionaries with keys 'model_input' and 'model_output'")
        for return_value in result:
            if not ('model_input' in return_value or 'model_output' in return_value):
                raise Exception(
                    f"Return Value of {func.__name__} is improperly formatted. It should be a list of dictionaries with keys 'model_input' and 'model_output'")
        return result
    wrapper.is_generator_function = True
    return wrapper
