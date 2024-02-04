from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class Calculator(App):
    def build(self):
        self.expression = ''
        layout = GridLayout(cols=1)

        # Текстовое поле для отображения выражения
        self.text_input = TextInput(text='', multiline=False)
        layout.add_widget(self.text_input)

        buttons_layout = GridLayout(cols=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        for label in buttons:
            button = Button(text=label, on_press=self.on_button_click)
            buttons_layout.add_widget(button)

        layout.add_widget(buttons_layout)

        return layout

    def on_button_click(self, instance):
        if instance.text == '=':
            try:
                result = str(eval(self.expression))
                self.text_input.text = result
                self.expression = result
            except Exception as e:
                self.text_input.text = 'Error'
                self.expression = ''
        elif instance.text == 'C':
            self.text_input.text = ''
            self.expression = ''
        else:
            self.expression += instance.text
            self.text_input.text = self.expression


if __name__ == '__main__':
    Calculator().run()