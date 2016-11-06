import json
import random
from threading import Timer

#Load the conversation from the JSON file
with open('responses.json') as data_file:    
    responses = json.load(data_file)
	
#Load the questions and responses
your_messages = responses['your_messages']
your_messages_lower = [x.lower() for x in your_messages]
his_responses = responses['his_responses']


def show_typing(your_message):
	#Shows 'Typing' message and the executes the recursion.
	print "Typing....."
	Timer(random.randint(3, 5) * 1.0, communicate, [your_message]).start()

#The primary recursive function
def communicate(your_message):
	#Here we're trying get the prompt, aka response to the user's message.
	if your_message is not "":
		#The message that the user enters will be searched in 'your messages' property in the JSON derived dict.
		if your_message in your_messages_lower:
			#We'll find the id of the message entered and will use it to retrieve the corresponding response
			location_index = your_messages_lower.index(your_message)
			prompt = his_responses[location_index]
		else:		
			prompt = responses['error_response']
	else:
		prompt = responses['welcome_response']
		
	#Once we have the prompt, we'll show it, and use it to draw in another user message.
	your_message = raw_input("Reply : " + prompt + "\n-----------------\nYou : ")
	#If the user enter's exit, we'll stop, else, we'll recursively continue to responsd.
	if your_message != "exit":
		Timer(random.randint(1, 3) * 1.0, show_typing, [your_message]).start()
	
	
communicate("")

