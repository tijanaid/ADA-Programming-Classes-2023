"""Demonstrates details of writing Python functions: annotations, default args, kwargs.
"""


#%%
# Setup / Data
song = 'Here Comes the Sun'
year = 1969

john = 'John Lennon'
paul = 'Paul McCartney'
george = 'George Harrison'
ringo = 'Ringo Starr'
the_beatles = [john, paul, george, ringo]


#%%
# def demonstrate_annotations(title, year):
def demonstrate_annotations(title: str, year: int) -> str:
    """Demonstrates how to use annotations of
    function parameters/arguments (<arg>: <type>) and of function return type (def f(...) -> <type>:).
    - print the function parameters/arguments
    - print the value of the __annotations__ attribute of this function
    - print the name and the docstring of this function
    - return a formatted string (including function parameters/arguments)
    """

    print(title + ',', year)
    print(demonstrate_annotations.__annotations__)
    print(demonstrate_annotations.__name__ + '\n\n', demonstrate_annotations.__doc__)
    return f'{demonstrate_annotations.__name__}("{title}", {year})'


#%%
# Test demonstrate_annotations(title, year)
print(demonstrate_annotations(song, year))


#%%
# def show_song(title, author='George Harrison', year: int = 1969):
def show_song(title, author='George Harrison', year=1969):

    """Demonstrates default arguments/parameters.
    - print locals()
    - print the function arguments/parameters in one line
    """

    print(locals())
    print(f'"{title}", by {author}, {year}')


#%%
# Test show_song(title, author='George Harrison', year=1969)
show_song(song)


#%%
def use_flexible_arg_list(band: str, *members):
    """Demonstrates flexible number of arguments/parameters.
    - print the band name and the list of band members in one line
    """

    print(type(members))
    print(f'{band}:', ', '.join([m for m in members]))


#%%
# Test use_flexible_arg_list(band: str, *members)
use_flexible_arg_list('The Beatles', *the_beatles)
use_flexible_arg_list('The Beatles')


#%%
def use_all_categories_of_args(band, *members, is_active=True, **details):
    """Demonstrates positional args, flexible args, keyword args, and kwargs (flexible keyword args).
    - print all arguments/parameters, including the keyword arguments/parameters, in one line
    """

    print(type(details))
    print()

    b = f'{band}: ' if members and details else f'{band}'
    m = ', '.join([m for m in members]) + ';' if members else ';'
    a = 'active;' if is_active else 'not active;'
    d = ', '.join([str(k) + ': ' + str(v) for k, v in details.items()]) if details else ''
    print(b + m, a, d)


#%%
# Test use_all_categories_of_args(band, *members, is_active=True, **details)
use_all_categories_of_args('The Beatles', is_active=False, start=1962, end=1970)
use_all_categories_of_args('The Beatles', *the_beatles, is_active=False, start=1962, end=1970)


