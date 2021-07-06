from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MainApp(App):
    i = 0
    def build(self):
        main_layout = BoxLayout()
        self.label = Label(text = "", size_hint = (.7, .9), pos_hint = {'center_x': 0.5, 'center_y': 0.7})
        btn = Button(text = "Click", size_hint = (.5, .1), pos_hint = {'top_x': 0.5, 'top_y': 0.5})
        btn.bind(on_press=self.on_button_press)
        main_layout.add_widget(self.label)
        main_layout.add_widget(btn)
        return main_layout

    def on_button_press(self, instance):
        self.i += 1
        self.label.text = "Clicked " + str(self.i + 1)
        
            

if __name__ == '__main__':
    app = MainApp()
    app.run()