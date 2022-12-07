from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

Window.size = (600, 700)
Window.clearcolor = (255 / 255, 100 / 255, 1 / 255, 1)
Window.title = 'Черчение онлайн'
cB = {'Б': 6, 'Ы': 7, 'Ж': 8, 'Е': 5, 'с': 4, '1': 3,
      'В': 6, 'Х': 7, 'Ф': 8, 'Г': 5,
      'И': 6, 'М': 7, 'Ш': 8, 'З': 5,
      'Й': 6, 'Д': 7, 'Щ': 8, 'С': 5,
      'К': 6, 'А': 7, 'Ъ': 8, 'а': 5,
      'Л': 6, 'ж': 7, 'Ю': 8, 'б': 5,
      'Н': 6, 'т': 7, 'в': 5,
      'О': 6, 'ф': 7, 'г': 5,
      'П': 6, 'ш': 7, 'д': 5,
      'Р': 6, 'щ': 7, 'е': 5,
      'Т': 6, 'з': 5,
      'У': 6, 'к': 5,
      'Ц': 6, 'л': 5,
      'Ч': 6, 'н': 5,
      'Ь': 6, 'и': 5,
      'Э': 6, 'й': 5,
      'Я': 6, 'о': 5,
      ' ': 6, 'п': 5,
      'м': 6, 'р': 5,
      'ъ': 6, 'у': 5,
      'ы': 6, 'х': 5,
      'ю': 6, 'ч': 5,
      '4': 6, 'ц': 5,
      'ь': 5,
      'э': 5,
      'я': 5,
      '2': 5,
      '3': 5,
      '5': 5,
      '6': 5,
      '7': 5,
      '8': 5,
      '9': 5,
      '0': 5,
      }


class MyApp(App):
    def __init__(self):
        super().__init__()
        self.btn = Label(text='Кнопка')
        self.btn2 = Button(text='Кнопка 2', font_size=30, background_color='red')
        self.solution = TextInput(hint_text='введите что-то', multiline=False)
        self.solution.bind(text=self.on_text)

    def on_text(self, *args):
        a = self.solution.text
        l = 0
        for i in range(len(a)):
            l += cB[a[i]]

        l += 2 * (len(a) - a.count(' ') - len(a.split()))
        self.btn.text = str(float(l)) + 'мм'

    def build(self):
        but = BoxLayout(orientation='vertical')
        but.add_widget(self.solution)
        but.add_widget(self.btn)

        return but


if __name__ == '__main__':
    MyApp().run()