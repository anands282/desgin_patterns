from abc import ABC, abstractmethod
from button import Button

class Dialog(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

