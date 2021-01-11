# Python program to translate 
# speech to text and text to speech 
# tis use when we noice present

import speech_recognition as sr 
r = sr.Recognizer() 

# Loop infinitely for user to 
# speak 

def talk():
          
	# Exception handling to handle 
	# exceptions at the runtime 
	try: 
		
		# use the microphone as source for input. 
		with sr.Microphone() as source2: 
			
			# wait for a second to let the recognizer 
			# adjust the energy threshold based on 
			# the surrounding noise level 
			r.adjust_for_ambient_noise(source2, duration=0.5) 
			
			#listens for the user's input 
			audio2 = r.listen(source2) 
			
			# Using ggogle to recognize audio 
			MyText = r.recognize_google(audio2) 
			MyText = MyText.lower() 

			print("Did you say "+MyText) 
			return MyText 
			
	except sr.RequestError as e: 
		print("Could not request results; {0}".format(e))
		return "could not understand" 
		
	except sr.UnknownValueError: 
		print("unknown error occured")
		return "could not understand" 


# use this function it reduce back word noice
# print(talk())
talk()