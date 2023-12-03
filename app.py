import matplotlib.pyplot as plt
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from matplotlib.backends.backend_kivyagg import FigureCanvasKivyAgg
from sympy import lambdify, symbols, sympify


class ScientificCalculator(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # Entry widget for expression input
        self.expression_entry = TextInput(font_size=32, multiline=False, halign='right', readonly=True)
        self.layout.add_widget(self.expression_entry)

        # Buttons for digits and operators
        buttons = [
            ('7', '/'), ('8', '*'), ('9', '-'),
            ('4', '1'), ('5', '2'), ('6', '3', '+'),
            ('1', '0'), ('.', '=')
        ]

        grid_layout = BoxLayout(orientation='vertical')

        for row in buttons:
            h_layout = BoxLayout()
            for button_text in row:
                button = Button(text=button_text, font_size=24, on_press=self.on_button_press)
                h_layout.add_widget(button)
            grid_layout.add_widget(h_layout)

        self.layout.add_widget(grid_layout)

        # Button for plotting
        plot_button = Button(text="Plot", font_size=24, on_press=self.plot_graph)
        self.layout.add_widget(plot_button)

        # Create a Tkinter canvas for matplotlib
        self.canvas = FigureCanvasKivyAgg(plt.gcf())
        self.layout.add_widget(self.canvas)

        return self.layout

    def on_button_press(self, instance):
        button_text = instance.text

        if button_text == '=':
            try:
                result = sympify(self.expression_entry.text)
                self.expression_entry.text = str(result)
            except Exception as e:
                self.expression_entry.text = "Error"

        else:
            self.expression_entry.text += button_text

    def plot_graph(self, instance):
        expression = self.expression_entry.text

        if expression:
            x = symbols('x')
            try:
                func = lambdify(x, expression, 'numpy')
                x_vals = [i for i in range(-10, 11)]
                y_vals = [func(i) for i in x_vals]

                plt.figure()
                plt.plot(x_vals, y_vals)
                plt.title("Graph")
                plt.xlabel("x")
                plt.ylabel("y")

                # Update the existing canvas
                self.canvas.draw_idle()

            except Exception as e:
                self.expression_entry.text = "Error: Invalid Expression"

if __name__ == '__main__':
    ScientificCalculator().run()
