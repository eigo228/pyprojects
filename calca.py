from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.clock import Clock

Window.size = (270, 585)

class Container(BoxLayout):
	formula = "0"
	button7 = ObjectProperty()
	button8 = ObjectProperty()
	button9 = ObjectProperty()

	button4 = ObjectProperty()
	button5 = ObjectProperty()
	button6 = ObjectProperty()

	button1 = ObjectProperty()
	button2 = ObjectProperty()
	button3 = ObjectProperty() 

	button0 = ObjectProperty()
	button_dot = ObjectProperty()
	button_slash = ObjectProperty()
	button_bs = ObjectProperty()
	button_star = ObjectProperty()

	button_minus = ObjectProperty()
	button_plus = ObjectProperty()
	button_res = ObjectProperty()

	lebel = ObjectProperty()

	def update_label(self):
		self.lebel.text = self.formula
		
	def add_numb(self, instance):
		if self.formula == "0":
			self.formula = ""

		self.formula += str(instance.text)
		self.update_label()
		
	def add_oper(self, instance):
		if self.lebel.text.endswith("+"):
			if str(instance.text) == "+":
				self.formula = self.formula[:-1]
				self.update_label
			else:
				self.formula = self.formula[:-1]
				self.update_label()
				self.formula += str(instance.text)
				self.update_label()
			
		if self.lebel.text.endswith("-"):
			if str(instance.text) == "-":
				self.formula = self.formula[:-1]
				self.update_label()
			else:
				self.formula = self.formula[:-1]
				self.update_label()
				self.formula += str(instance.text)
				self.update_label()

			
		if self.lebel.text.endswith("*"):
			if str(instance.text) == "*":
				self.formula = self.formula[:-1]
			else:
				self.formula = self.formula[:-1]
				self.update_label()
				self.formula += str(instance.text)
				
		if self.lebel.text.endswith("/"):
			if str(instance.text) == "/":
				self.formula = self.formula[:-1]
			else:
				self.formula = self.formula[:-1]
				self.update_label()
				self.formula += str(instance.text)
				
		if self.lebel.text.endswith("."):
			if str(instance.text) == ".":
				self.formula = self.formula[:-1]
			else:
				self.formula = self.formula[:-1]
				self.update_label()
				self.formula += str(instance.text)
			
			
			
		else:
			self.formula += str(instance.text)

		self.update_label()
				
	def backspace(self, instance):
		if self.formula == "0":
			pass
		else:
			self.formula = self.formula[:-1]
			self.update_label()
	
	def clear(self):
		self.formula = "0"
		self.update_label()

	def button_stat(self, instance):
		if self.button_bs.state == "down":
			self.clear()

	def on_state(self, instance):
		if self.button_bs.state == "down":
			Clock.schedule_once(self.button_stat, 0.7)

			
	def result(self, instance):

		try:
			self.lebel.text = str(eval(self.lebel.text))
		except SyntaxError:
			self.lebel.text = "Error."
		self.formula = "0"

	
	

class CalcApp(App):


	def build(self):
			return Container()

		
		
		
if __name__=="__main__":
	CalcApp().run()