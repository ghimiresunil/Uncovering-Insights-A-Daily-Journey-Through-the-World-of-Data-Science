from typeguard import typechecked

@typechecked
def some_function(a: int, b: float) -> bool:
    return True

if __name__ == "__main__":
    print(some_function(1, 1.2)) # -> True
    print(some_function(1.2, 1)) # -> typeguard.TypeCheckError: argument "a" (float) is not an instance of int