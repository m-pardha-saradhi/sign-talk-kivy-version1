from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.home_screen import HomeScreen
from screens.about_screen import AboutScreen
from screens.camera_screen import CameraScreen

    

class MyApp(App):
    def build(self):
        
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(AboutScreen(name='about'))
        sm.add_widget(CameraScreen(name='camera'))
        # sm.add_widget(LoginScreen(name='login', auth_manager=auth_manager))
        # sm.add_widget(RegistrationScreen(name='register', auth_manager=auth_manager))
        return sm


if __name__ == '__main__':
    MyApp().run()
