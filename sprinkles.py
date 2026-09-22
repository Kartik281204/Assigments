def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("**Adds sprinkles✨✨✨✨****")
        func(*args, **kwargs)
    return wrapper


def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("**Adds fudge🫕🍫🫕🍫**")
        func(*args, **kwargs)
    return wrapper


@add_fudge
@add_sprinkles
def get_icecream(flavour):
    print(f"Here is {flavour} icecream 🍨🍨🍨🍨")


get_icecream("Vanilla")
