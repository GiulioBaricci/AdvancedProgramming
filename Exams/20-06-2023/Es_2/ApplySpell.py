from FullStack import FullStack
from EmptyStack import EmptyStack
from Stack import Stack
from Smeagol import Smeagol
from Gollum import Gollum

def wrapper(className, method):
    def wrapped(self, *args, **kwargs):
        dictionary[className](self)
        result = method(self, *args, **kwargs)
        dictionary[className](self)
        return result
    return wrapped


class ApplySpell(type):
    def __new__(meta, classname, bases, classDict):
        newClassDict = {}
        for attributeName, attribute in classDict.items():
            if callable(attribute) and attributeName != "__init__":
                attribute = wrapper(classname, attribute)
            newClassDict[attributeName] = attribute
        return type.__new__(meta, classname, bases, newClassDict)
    def __call__(cls, *args, **kwargs):
        return type.__call__(cls, *args, **kwargs)


def changeStack(self):
    if self.__top__ == self.__size__:
        self.__class__ = FullStack
    elif self.__top__ == 0:
        self.__class__ = EmptyStack
    else:
        self.__class__ = Stack
    return self

def changeSmeagol(self):
    if self.hasTheOneRing:
        self.__class__ = Gollum
    else:
        self.__class__ = Smeagol
    return self

dictionary = {
    "Stack": changeStack,
    "EmptyStack": changeStack,
    "FullStack": changeStack,
    "Smeagol": changeSmeagol,
    "Gollum": changeSmeagol
}

Stack = ApplySpell(Stack.__name__, Stack.__bases__, dict(Stack.__dict__))
EmptyStack = ApplySpell(EmptyStack.__name__, EmptyStack.__bases__, dict(EmptyStack.__dict__))
FullStack = ApplySpell(FullStack.__name__, FullStack.__bases__, dict(FullStack.__dict__))
Smeagol = ApplySpell(Smeagol.__name__, Smeagol.__bases__, dict(Smeagol.__dict__))
Gollum = ApplySpell(Gollum.__name__, Gollum.__bases__, dict(Gollum.__dict__))