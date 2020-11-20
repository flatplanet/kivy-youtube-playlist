from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
#from kivy.uix.image import Image

# Designate Our .kv design file 
Builder.load_file('images.kv')

class MyLayout(Widget):
	pass

class AwesomeApp(App):
	def build(self):
		Window.clearcolor = (1,1,1,1)
		return MyLayout()

if __name__ == '__main__':
	AwesomeApp().run()



