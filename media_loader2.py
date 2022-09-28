import abc
from msilib.schema import Media

class MediaLoader(abc.ABC):
    """
    Abstract class to create a generic Media Loader.
    """
    @abc.abstractmethod
    def play(self)-> None:
        ...

    @property
    @abc.abstractclassmethod
    def ext(self) -> str:
        ...

class Wav(MediaLoader):
    pass

class Ogg(MediaLoader):

    ext = ".Ogg"
    def play(self)->None:
        print("Playing Ogg")


