from button import Button


class WindowsButton(Button):
    def render(self):
        print("Render button in windows style")

    def on_click(self):
        print("Windows button says hello world")