from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


# Designate Our .kv design file 
Builder.load_file('fun.kv')


class MyGridLayout(Widget):
	pass
	

	
class AwesomeApp(App):
	def build(self):
		return MyGridLayout()


if __name__ == '__main__':
	AwesomeApp().run()



