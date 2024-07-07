from creational_patterns.factory.button import Button
from html_button import HtmlButton
from windows_button import WindowsButton
from dialog import Dialog

class WindowsDialog(Dialog):
    def create_button(self) -> Button:
        return WindowsButton()


class WebDialog(Dialog):
    def create_button(self) -> Button:
        return HtmlButton()