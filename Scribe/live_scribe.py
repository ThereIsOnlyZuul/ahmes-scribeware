from Scribe.scribe import Scribe

#LiveScribe - a scribe for the command line

class LiveScribe(Scribe) :

	greeting = "Thanks for using Ahmes Scribeware."

	output_prompt = "What would you like the file name to be? "

	loop_prompt = "Would you like to make another worksheet? "

	def callback(self,prompt,options):
		option_prompt = "Please select one of the following options."
		stringified_options = [str(x) for x in options]
		if prompt != None:
			print(prompt)
		print(option_prompt)
		n = 0
		for o in stringified_options:
			print(str(n)+" - "+o)
			n+=1
		selection = input('Option: ')
		return stringified_options[int(selection)]

	def main_loop(self):
		print(self.greeting)
		looping = True
		while looping:
			template = self.callback(None,self.templates.keys())
			out = input(self.output_prompt)
			self.write(template,out)
			looping = self.callback(self.loop_prompt,['Yes','No']) == 'Yes'