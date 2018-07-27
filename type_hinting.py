def hello_world(name: str) -> None:
    """ Type hinting allows us to specify the type of arguments we expect,
        as well as the type of the return value
        See https://docs.python.org/3/library/typing.html
        Note that the API may be unstable (see link above)
    """
    print(f"Hello {name}")

if __name__ == "__main__":
    hello_world("Dylan")
