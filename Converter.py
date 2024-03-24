from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen


class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main_screen"))
        sm.add_widget(MassScreen(name="mass_screen"))
        sm.add_widget(DlinaScreen(name="dlina_screen"))
        sm.add_widget(ObemScreen(name="obem_screen"))
        sm.add_widget(SqrScreen(name="sqr_screen"))

        return sm


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_layout = BoxLayout(orientation="vertical")
        hlayout1 = BoxLayout()
        hlayout2 = BoxLayout()
        btn1 = Button(text="Масса", on_press=self.go_mass_screen)
        btn2 = Button(text="Длина", on_press=self.go_dlina_screen)
        btn3 = Button(text="Объём", on_press=self.go_obem_screen)
        btn4 = Button(text="Площадь", on_press=self.go_sqr_screen)
        hlayout1.add_widget(btn1)
        hlayout1.add_widget(btn2)
        hlayout2.add_widget(btn3)
        hlayout2.add_widget(btn4)

        main_layout.add_widget(hlayout1)
        main_layout.add_widget(hlayout2)

        self.add_widget(main_layout)

    def go_mass_screen(self, *args):
        self.manager.transition.direction = "left"
        self.manager.current = "mass_screen"

    def go_dlina_screen(self, *args):
        self.manager.transition.direction = "left"
        self.manager.current = "dlina_screen"

    def go_obem_screen(self, *args):
        self.manager.transition.direction = "left"
        self.manager.current = "obem_screen"

    def go_sqr_screen(self, *args):
        self.manager.transition.direction = "left"
        self.manager.current = "sqr_screen"


class MassScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.mass_list = {"lbs": 0.453592, "oz": 0.0283495, "мг": 0.000001, "мкг": 0.000000001, "г": 0.001, "кг": 1.0,
                          "т": 1000}
        self.reverse_mass = {"lbs": 2.20462, "oz": 35.274, "мг": 1000000.0, "мкг": 1000000000.0, "г": 1000, "кг": 1.0,
                             "т": 0.001}
        self.btn_text1 = ""
        self.btn_text2 = ""
        self.instance1 = None
        self.instance2 = None

        main_layout = BoxLayout(orientation="vertical")

        h_layout1 = BoxLayout()
        for i in list(self.mass_list):
            btn = Button(text=i, on_press=self.first_button)
            h_layout1.add_widget(btn)
        main_layout.add_widget(h_layout1)

        self.txt1 = TextInput(halign="right", multiline=False, font_size=50)
        main_layout.add_widget(self.txt1)

        h_layout2 = BoxLayout()
        for i in list(self.reverse_mass):
            btn = Button(text=i, on_press=self.second_button)
            h_layout2.add_widget(btn)
        main_layout.add_widget(h_layout2)

        self.txt2 = TextInput(halign="right", multiline=False, font_size=50, readonly=True, background_color="grey")
        main_layout.add_widget(self.txt2)

        main_btn = Button(text="Подсчитать", on_press=self.calculate)
        main_layout.add_widget(main_btn)

        btn = Button(text="Назад", on_press=self.go_back)
        main_layout.add_widget(btn)
        self.add_widget(main_layout)

    def first_button(self, instance):
        self.btn_text1 = instance.text
        instance.background_color = 'red'
        if self.instance1 != None:
            if self.instance1 == instance:
                instance.background_color = 'red'
            else:
                self.instance1.background_color = 1, 1, 1, 1
        self.instance1 = instance
        return self.btn_text1

    def second_button(self, instance):
        self.btn_text2 = instance.text
        instance.background_color = 'red'
        if self.instance2 != None:
            if self.instance2 == instance:
                instance.background_color = 'red'
            else:
                self.instance2.background_color = 1, 1, 1, 1
        self.instance2 = instance
        return self.btn_text2

    def calculate(self, instance):
        text = self.txt1.text
        if text == "":
            return
        else:
            text = float(text)
            keys_1 = list(self.mass_list.keys()).index(self.btn_text1)
            values_1 = list(self.mass_list.values())
            key1 = values_1[keys_1]
            keys_2 = list(self.reverse_mass.keys()).index(self.btn_text2)
            values_2 = list(self.reverse_mass.values())
            key2 = values_2[keys_2]
            kgs = key1 * text
            result = kgs * key2
            result = str(result)
            for i in result:
                if i == ".":
                    j = result.index(i)
                    result1 = result[j:1000]
                    b = 0
                    for x in result1:
                        if x == 0:
                            b += 1
                            if b > 10:
                                result = float(result)
                                round(result, 1)

            self.txt2.text = str(result)

    def go_back(self, *args):
        self.manager.transition.direction = "right"
        self.manager.current = "main_screen"


class DlinaScreen(MassScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.mass_list = {"mm": 0.001, "sm": 0.01, "m": 1.0, "km": 1000.0, "ярд": 0.9144, "миля": 1609.344,
                          "мор. миля": 1852.0}
        self.reverse_mass = {"mm": 1000.0, "sm": 100.0, "m": 1.0, "km": 0.001, "ярд": 1.09361329834,
                             "миля": 0.00062137119, "мор. миля": 0.0005399568}
        self.btn_text1 = ""
        self.btn_text2 = ""
        self.instance1 = None
        self.instance2 = None

        main_layout = BoxLayout(orientation="vertical")

        h_layout1 = BoxLayout()
        for i in list(self.mass_list):
            btn = Button(text=i, on_press=self.first_button)
            h_layout1.add_widget(btn)
        main_layout.add_widget(h_layout1)

        self.txt1 = TextInput(halign="right", multiline=False, font_size=50)
        main_layout.add_widget(self.txt1)

        h_layout2 = BoxLayout()
        for i in list(self.reverse_mass):
            btn = Button(text=i, on_press=self.second_button)
            h_layout2.add_widget(btn)
        main_layout.add_widget(h_layout2)

        self.txt2 = TextInput(halign="right", multiline=False, font_size=50, readonly=True, background_color="grey")
        main_layout.add_widget(self.txt2)

        main_btn = Button(text="Подсчитать", on_press=self.calculate)
        main_layout.add_widget(main_btn)

        btn = Button(text="Назад", on_press=self.go_back)
        main_layout.add_widget(btn)
        self.add_widget(main_layout)


class ObemScreen(MassScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.mass_list = {"mm3": 0.000000001, "sm3": 0.000001, "m3": 1.0, "km3": 1000000000.0, "литры": 0.001,
                          "милилитры": 0.000001, "микролитр": 0.000000001}
        self.reverse_mass = {"mm3": 1000000000.0, "sm3": 1000000.0, "m3": 1.0, "km3": 0.000000001, "литры": 1000.0,
                             "милилитры": 1000000.0, "микролитры": 1000000000.0}
        self.btn_text1 = ""
        self.btn_text2 = ""
        self.instance1 = None
        self.instance2 = None

        main_layout = BoxLayout(orientation="vertical")

        h_layout1 = BoxLayout()
        for i in list(self.mass_list):
            btn = Button(text=i, on_press=self.first_button)
            h_layout1.add_widget(btn)
        main_layout.add_widget(h_layout1)

        self.txt1 = TextInput(halign="right", multiline=False, font_size=50)
        main_layout.add_widget(self.txt1)

        h_layout2 = BoxLayout()
        for i in list(self.reverse_mass):
            btn = Button(text=i, on_press=self.second_button)
            h_layout2.add_widget(btn)
        main_layout.add_widget(h_layout2)

        self.txt2 = TextInput(halign="right", multiline=False, font_size=50, readonly=True, background_color="grey")
        main_layout.add_widget(self.txt2)

        main_btn = Button(text="Подсчитать", on_press=self.calculate)
        main_layout.add_widget(main_btn)

        btn = Button(text="Назад", on_press=self.go_back)
        main_layout.add_widget(btn)
        self.add_widget(main_layout)


class SqrScreen(MassScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.mass_list = {"mm2": 0.000001, "sm2": 0.0001, "dm2": 0.01, "m2": 1.0, "km2": 11000000.0, "гектар": 10000.0,
                          "акр": 4046.86}
        self.reverse_mass = {"mm2": 1000000.0, "sm2": 10000.0, "dm2": 100.0, "m2": 1.0, "km2": 0.000001,
                             "гектар": 0.0001, "акр": 0.00024710516}

        main_layout = BoxLayout(orientation="vertical")

        h_layout1 = BoxLayout()
        for i in list(self.mass_list):
            btn = Button(text=i, on_press=self.first_button)
            h_layout1.add_widget(btn)
        main_layout.add_widget(h_layout1)

        self.txt1 = TextInput(halign="right", multiline=False, font_size=50)
        main_layout.add_widget(self.txt1)

        h_layout2 = BoxLayout()
        for i in list(self.reverse_mass):
            btn = Button(text=i, on_press=self.second_button)
            h_layout2.add_widget(btn)
        main_layout.add_widget(h_layout2)

        self.txt2 = TextInput(halign="right", multiline=False, font_size=50, readonly=True, background_color="grey")
        main_layout.add_widget(self.txt2)

        main_btn = Button(text="Подсчитать", on_press=self.calculate)
        main_layout.add_widget(main_btn)

        btn = Button(text="Назад", on_press=self.go_back)
        main_layout.add_widget(btn)
        self.add_widget(main_layout)


MainApp().run()
