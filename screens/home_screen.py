from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
import joblib

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_layout = BoxLayout(orientation='vertical', spacing=dp(10))

        # Create a label for the title
        title_label = Label(
            text="Words Available for Translation",
            font_size=24,
            size_hint=(1, None),
            height=dp(60),
            color=(0.2, 0.4, 0.8, 1),  # Customize the text color
        )
        
        # list of words (labels)
        label_encoder = joblib.load('label_encoder.joblib')
        word_list =  label_encoder.classes_  # ['Accident', 'Come', 'Doctor', 'Help', 'Hot', 'Lose', 'Pain', 'Thief']
        word_scrollview = ScrollView(size_hint=(1, 1))
        word_layout = GridLayout(cols=1, spacing=dp(10), size_hint_y=None)
        
        for word in word_list:
            word_label = Label(
                text=word,
                font_size=18,
                size_hint_y=None,
                height=dp(40),
                color=(0.4, 0.4, 0.4, 1),  # Customize the text color
                # background_color=(0.9, 0.9, 0.9, 1),  # Customize the background color
                padding=(dp(10), dp(5)),  # Add padding around each word
            )
            word_layout.add_widget(word_label)
        
        word_scrollview.add_widget(word_layout)

        # Add widgets to the main layout
        main_layout.add_widget(title_label)
        main_layout.add_widget(word_scrollview)
        
        # for word in word_list:
        #     label = Label(text=word, size_hint_y=None, height=40)
        #     layout.add_widget(label)
        
        self.add_widget(main_layout)

        
        # Adding buttons to the bottom footer
        footer = BoxLayout(orientation='horizontal', size_hint=(1, None), height=50)
        words_button = Button(text='Words', disabled=True)
        camera_button = Button(text='Camera')
        profile_button = Button(text='Profile')
        
        footer.add_widget(words_button)
        footer.add_widget(camera_button)
        footer.add_widget(profile_button)
        
        self.add_widget(footer)

        # Event handler for the Profile button
        profile_button.bind(on_release=self.show_about_screen)
        camera_button.bind(on_release=self.camera_screen)
    
    def show_about_screen(self, instance):
        self.manager.current = 'about'  # Switch to the About screen
    
    def camera_screen(self, instance):
        self.manager.current = 'camera'