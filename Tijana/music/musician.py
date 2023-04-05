"""Domain classes and functions related to the concept of musician
"""


#%%
# Setup / Data

from util import utility
from music.enums import Vocals, Instrument
import json

from testdata.musicians import *


#%%
class Musician:
    """The class describing the concept of musician.
    It is assumed that a musician is sufficiently described by their
    name and whether they are a solo musician or a member of a band.

    This class illustrates some important concepts of Python classes:
    - self
    - __init__()
    - __str__()
    - __eq__(self, other) is the equivalent of Java equals() and should be overridden in classes
    - __dict__ attribute of all objects
    - data fields (instance variables)
    - methods - calling them by self.<method>(...) from the same class where they are defined
    """

    def __init__(self, name, is_band_member=True):
        self.name = name
        self.is_band_member = is_band_member
        # self.__n = 'lll'                                    # 'private' field
        # self._m = 'mmm'
        # # self.__immutable_property = 'I am immutable'

    def __str__(self):
        b = '(band member)' if self.is_band_member else '(solo musician)'
        return f'{self.name} {b}'

    def __eq__(self, other):
        i = isinstance(other, Musician)
        n = self.name == other.name if i else False
        bm = self.is_band_member == other.is_band_member if i else False
        return i and n and bm

    # Properties: 'private' fields/attributes:
    #   @property
    #   def <attr>(self):
    #       """ The docstring for <attr> must go here."""
    #       return self.__<attr>
    #   @<attr>.setter
    #   def <attr>(self, <attr>):
    #       self.__<attr> = <attr> if ... else ...
    #   @<attr>.deleter
    #   def <attr>(self, <attr>):
    #       del self.__<attr>

    # Properties allow programmers to create methods that behave like attributes.
    # With properties, one can change how they compute the target attribute whenever they need to do so.
    # A more detailed explanation: https://realpython.com/python-property/.
    # In general, avoid turning attributes that don’t require extra processing into properties.
    # Using properties in those situations can make the code unnecessarily verbose, confusing and slower
    # than code based on regular attributes.

    # Make name a property (after setting up __init__(), __str__(), __eq__(), methods,...)

    # Run setters and getters in the debugger

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name if isinstance(name, str) else 'unknown'

    # Add an immutable property (no setter for it)
    # @property
    # def immutable_property(self):
    # return self.__immutable_property

    def play(self, song_title, *args, **kwargs):
        """Assumes that song_title, *args (expressions of gratitude) and kwargs.values() (messages) are strings.
        Prints song_title, rhythm counts, expressions of gratitude and messages. A call example:
            <musician>.play(song_title, *['Thank you!', 'You're wonderful!], love='We love you!')
        Convention: if rhythm count is provided, it is passed as rhythm_count='...' and is the first kwarg.
        """

        n = self.name
        s = f'"{song_title}"'
        r = kwargs['rhythm_count'] if 'rhythm_count' in kwargs.keys() else ''
        g = ' '.join([a for a in args]) if args else ''
        m = ' '.join([v for v in list(kwargs.values())[1:]]) if list(kwargs.values())[1:] else ''

        return f'{n} playing {s}: {r} ...playing... {g} {m}'

    def play_song(self, song_title, *args, **kwargs):
        """Demonstrates calling another method from the same class (self.<method>(...) as a mandatory syntax).
        """

        return self.play(song_title, *args, **kwargs)

    # Alternative constructor
    @classmethod
    def from_str(cls, musician_string):
        """Inverted __str__() method.
        Assumes that musician_string is in the format generated by __str__().
        """

        # b = '(band member)' if self.is_band_member else '(solo musician)'
        # return f'{self.name} {b}'
        n = musician_string.split(' (')[0]
        bm = True if musician_string.split(' (')[1].startswith('b') else False
        return cls(n, bm)


#%%
# Print objects
george = Musician('George Harrison', True)
print(george)


#%%
# Run setters and getters in the debugger
george.name = 'George Harrison'
print(george.name)


#%%
# Compare objects
print(george == Musician('George Harrison', True))


#%%
# Access data fields/attributes (instance variables),
# including 'private' ones (<object>._Musician__n), 'protected' ones (<object>._Musician__m) and
# immutable ones (<object>.immutable_property)

# print(george._Musician__n)
# print(george._m)
# print(paul.immutable_property)


#%%
# Add new data fields (instance variables)
#   1. <object>.<new_attr> = <value>
#   2. <object>.__setattr__('<new_attr>', <value>)      # counterpart: <object>.__getattribute__('<attr>')
#   3. setattr(<object>, '<new_attr>', <value>))        # counterpart: getattr(<object>, '<attr>')


#%%
# Calling methods
# george.play('Don\'t Bother Me', 'Thank you!', 'Thanks!', rhythm_count='One, two, three, four!', great='Great!')
george.play_song('Don\'t Bother Me', 'Thank you!', 'Thanks!', rhythm_count='One, two, three, four!', great='Great!')


#%%
# Demonstrate object data fields and methods (possibly in Python console)
# for some built-in classes (boolean, int, object,...)
# - True + 1
# - True.__int__()
# - (1).__class__.__name__
# - (1).__class__
# - o.__dir__()
# - o.__dir__
# - o.__dict__

print(False + 1)
print(True.__int__())
print((1).__class__)
print((1).__class__.__name__)
print((1).__dir__())
print(object.__dict__)
print()

print(dir(1))
print(object.__str__(george))


#%%
# Demonstrate object data fields and methods for Musician objects
print(george.__dict__)


#%%
# Demonstrate @classmethod (from_str())
george_harrison = Musician.from_str(str(george))
print(george_harrison)
print(george == george_harrison)


#%%
class MusicianEncoder(json.JSONEncoder):
    """JSON encoder for Musician objects (cls= parameter in json.dumps()).
    """

    def default(self, musician):
        # recommendation: always use double quotes with JSON

        pass
        # can simply return musician_py_to_json(musician), to avoid code duplication


#%%
def musician_py_to_json(musician):
    """JSON encoder for Musician objects (default= parameter in json.dumps()).
    """

    # recommendation: always use double quotes with JSON


#%%
def musician_json_to_py(musician_json):
    """JSON decoder for Musician objects (object_hook= parameter in json.loads()).
    """


#%%
class Singer(Musician):
    """The class describing the concept of singer.
    It is assumed that a singer is sufficiently described as a Musician,
    with the addition of whether they are a lead or a background singer.

    Useful link (related to inheritance in Python):
    https://stackoverflow.com/questions/3394835/use-of-args-and-kwargs/3394902#3394902 (calling super() in constructors)
    """

    # # Version 1 - no multiple inheritance
    # def __init__(self, name, vocals, is_band_member=True):
    #     super().__init__(name, is_band_member)
    #     self.vocals = vocals if isinstance(vocals, Vocals) else None

    # Version 2 - with multiple inheritance
    def __init__(self, vocals=Vocals.LEAD_VOCALS, **kwargs):
        super().__init__(**kwargs)
        self.vocals = vocals if isinstance(vocals, Vocals) else None

    def __str__(self):
        v = f', {self.vocals.value}' if isinstance(self.vocals, Vocals) else ''
        return super().__str__() + v

    def __eq__(self, other):
        pass
        # Recommended if inheritance is involved
        # (https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes):
        # if type(other) is type(self):
        #     return self.__dict__ == other.__dict__
        # return False

        return self.__dict__ == other.__dict__ if isinstance(other, Singer) else False

    def play(self, song_title, *args, **kwargs):
        """Overrides the play() method from superclass.
        In addition to printing song_title, expressions of gratitude and messages,
        it also prints an additional message in the end.
        A call example:
            <singer>.play(song_title, *['Thank you!', 'You're wonderful!], love='We love you!')
        """

        return super().play(song_title, *args, **kwargs) + '\nYeah!'

    def what_do_you_do(self):
        """Just a simple method to describe the concept of singer.
        """

        return f'I am {self.name} and I sing songs.'


#%%
class Songwriter(Musician):
    """The class describing the concept of songwriter.
    It is assumed that a songwriter is sufficiently described as a musician
    who writes songs and plays an instrument.
    """

    # Version 1 - no multiple inheritance

    # def __init__(self, name, instrument, is_band_member=True):
    #     super().__init__(name, is_band_member)
    #     self.instrument = instrument if isinstance(instrument, Instrument) else None

    # Version 2 - with multiple inheritance
    def __init__(self, instrument=Instrument.RHYTHM_GUITAR, **kwargs):
        super().__init__(**kwargs)
        self.instrument = instrument if isinstance(instrument, Instrument) else None

    def __str__(self):
        v = f', {self.instrument.value}' if isinstance(self.instrument, Instrument) else ''
        return super().__str__() + v

    def __eq__(self, other):
        pass
        # Recommended if inheritance is involved
        # (https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes):
        # if type(other) is type(self):
        #     return self.__dict__ == other.__dict__
        # return False

        return self.__dict__ == other.__dict__ if isinstance(other, Songwriter) else False

    def what_do_you_do(self):
        """Just a simple method to describe the concept of songwriter.
        """

        return f'I am {self.name} and I write songs.'


#%%
# Demonstrate inheritance
# object class (like the Object class in Java; all classes inherit from object
#   try, e.g., list.__mro__ in the console)
#   object class defines object.__eq__(self, other) etc.
#   object.__ne__(self, other), the inverse of object.__eq__(self, other),
#   is provided by Python automatically once object.__eq__(self, other) is implemented

#%%
# Demonstrate inheritance
# Version 1 - no multiple inheritance
george = Singer(name='George Harrison', vocals=Vocals.LEAD_VOCALS)
print(george)
print(Singer.__mro__)
print(george == Singer(name='George Harrison', vocals=Vocals.LEAD_VOCALS))
print()
john = Songwriter(name='John Lennon', instrument=Instrument.RHYTHM_GUITAR)
print(john)
print(john == Songwriter(name='John Lennon', instrument=Instrument.RHYTHM_GUITAR))
print(john.what_do_you_do())

#%%
# Demonstrate method overriding
print(george.play('While My Guitar Gently Weeps'))


#%%
class SingerSongwriter(Singer, Songwriter):
    """The class describing the concept of singer-songwriter.
    It is assumed that a singer-songwriter is sufficiently described as a Singer who is simultaneously a Songwriter.

    Useful links :
    https://stackoverflow.com/a/50465583/1899061 (designing classes (i.e. their __init__() methods) for multiple inh.)
    https://stackoverflow.com/a/533675/1899061 (mixins explained, and what good they are in multiple inheritance)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __str__(self):
        return super().__str__()

    def __eq__(self, other):
        pass
        # Recommended if inheritance is involved
        # (https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes):
        # if type(other) is type(self):
        #     return self.__dict__ == other.__dict__
        # return False

        return self.__dict__ == other.__dict__ if isinstance(other, SingerSongwriter) else False

    def tell(self):
        """What if multiple inheritance requires calling a method with same method name
        from different paths (i.e., from different base classes)?
        E.g., class C(A, B) and both A and B implement a method with the same name m() in their own ways).
        In that case, call A's version like A.m(self), and B's version like B.m(self).
        """
        print(Singer.what_do_you_do(self))
        print(Songwriter.what_do_you_do(self))


#%%
# Demonstrate multiple inheritance and MRO.
# Make sure to read this first: https://stackoverflow.com/a/50465583/1899061 (especially Scenario 3).


#%%
# Demonstrate inheritance
# Version 2 - with multiple inheritance

print(SingerSongwriter.__mro__)
print()
bob = SingerSongwriter(name='Bob Dylan', vocals=Vocals.LEAD_VOCALS,
                       instrument=Instrument.RHYTHM_GUITAR, is_band_member=False)
print(bob)
print()
print(bob == SingerSongwriter(name='Bob Dylan', vocals=Vocals.LEAD_VOCALS,
                              instrument=Instrument.RHYTHM_GUITAR, is_band_member=False))
print()

bob.tell()

#%%
# Demonstrate JSON encoding/decoding of simple data types.
# Refer to https://docs.python.org/3.3/library/json.html#encoders-and-decoders for details.

#%%
# Demonstrate JSON encoding/decoding of Musician objects

# Using the json_tricks module from the json-tricks external package (https://github.com/mverleg/pyjson_tricks).
# From the package documentation:
# The JSON string resulting from applying the json_tricks.dumps() function stores the module and class name.
# The class must be importable from the same module when decoding (and should not have changed).
# If it isn't, you have to manually provide a dictionary to cls_lookup_map when loading
# in which the class name can be looked up. Note that if the class is imported, then globals() is such a dictionary
# (so try loads(json, cls_lookup_map=glboals())).
# Also note that if the class is defined in the 'top' script (that you're calling directly),
# then this isn't a module and the import part cannot be extracted. Only the class name will be stored;
# it can then only be deserialized in the same script, or if you provide cls_lookup_map.
# That's why the following warning appears when serializing Band objects in this script:
# UserWarning: class <class '__main__.Musician'> seems to have been defined in the main file;
# unfortunately this means that it's module/import path is unknown,
# so you might have to provide cls_lookup_map when decoding.

#%%
# Single object
from json_tricks import loads, dumps
george_json = dumps(george, indent=4)
print(george_json)
print(george == loads(george_json))


#%%
# List of objects
from json_tricks import loads, dumps
the_beatles = [johnLennon, paulMcCartney, georgeHarrison, ringoStarr]
the_beatles_json = dumps(the_beatles, indent=4)
print(the_beatles_json)
print(the_beatles == loads(the_beatles_json))
