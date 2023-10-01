from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button


class AboutScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')
        loggedin = True
        email = 'pardhu@gmail.com'
        name = 'pardhu'
        
        if loggedin:
            user_label = Label(text=f"Email: {email}\n"
                                   f"Name: {name}")
            layout.add_widget(user_label)
        else:
            login_button = Button(text='Login')
            register_button = Button(text='Register')

            login_button.bind(on_release=self.show_login_screen)
            register_button.bind(on_release=self.show_registration_screen)

            layout.add_widget(login_button)
            layout.add_widget(register_button)
        
        self.add_widget(layout)

        
        # Adding buttons to the bottom footer
        footer = BoxLayout(orientation='horizontal', size_hint=(1, None), height=50)
        words_button = Button(text='Words')
        camera_button = Button(text='Camera')        
        profile_button = Button(text='Profile', disabled=True)
        
        footer.add_widget(words_button)
        footer.add_widget(camera_button)
        footer.add_widget(profile_button)
        
        self.add_widget(footer)

        # Event handler for the buttons
        words_button.bind(on_release=self.show_words_screen)
        camera_button.bind(on_release=self.show_camera_screen)
    
    def show_login_screen(self, instance):
        self.manager.current = 'login'

    def show_registration_screen(self, instance):
        self.manager.current = 'register'
    
    def show_words_screen(self, instance):
        self.manager.current = 'home'
    
    def show_camera_screen(self, instance):
        self.manager.current = 'camera'