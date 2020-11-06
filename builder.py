from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('whatever.kv')
'''Builder.load_string(""" 

<MyGridLayout>
	
	name:name
	pizza:pizza
	color:color

	GridLayout:
		cols:1
		size: root.width, root.height
		GridLayout:
			cols:2

			Label:
				text: "Name"
			TextInput:
				id: name
				multiline:False

			Label:
				text: "Favorite Pizza"
			TextInput:
				id: pizza
				multiline:False
				
			Label:
				text: "Favorite Color"
			TextInput:
				id: color
				multiline:False	

		Button:
			text: "Submit"
			font_size: 32
			on_press: root.press()



	""")
'''
class MyGridLayout(Widget):
	
	name = ObjectProperty(None)
	pizza = ObjectProperty(None)
	color = ObjectProperty(None)


	def press(self):
		name = self.name.text
		pizza = self.pizza.text
		color = self.color.text

		#print(f'Hello {name}, you like {pizza} pizza, and your favorite color is {color}!')
		# Print it to the screen
		#self.add_widget(Label(text=f'Hello {name}, you like {pizza} pizza, and your favorite color is {color}!'))
		print(f'Hello {name}, you like {pizza} pizza, and your favorite color is {color}!')
		# Clear the input boxes
		self.name.text = ""
		self.pizza.text = ""
		self.color.text = ""

class AwesomeApp(App):
	def build(self):
		return MyGridLayout()


if __name__ == '__main__':
	AwesomeApp().run()



