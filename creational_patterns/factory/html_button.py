from button import Button


class HtmlButton(Button):
    def render(self):
        print("Render button in HTML style")

    def on_click(self):
        print("HTML button says hello world")