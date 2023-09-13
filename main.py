from kivy.app import App
from kivy.uix.label import  Label
class HelloKivy(App):
    def build(self):
        self.icon = "123.png"
        self.title = "Hello Vuong"
        return Label (text = "Chao ")
if __name__ == "__main__":
    app = HelloKivy()
    app.run()