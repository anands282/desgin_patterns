from gui_factory import GUIFactory


class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()