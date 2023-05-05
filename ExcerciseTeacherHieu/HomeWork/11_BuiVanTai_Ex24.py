# import speech_recognition as sr
# import pyttsx3
# import random
#
# r = sr.Recognizer()
# engine = pyttsx3.init()
#
# keywords = {
#     "hello": "Hello! How can I help you today?",
#     "how are you": "I'm doing well, thank you for asking. How about you?",
#     "what's the weather like": "I'm sorry, I don't have that information.",
#     "goodbye": "Goodbye, have a great day!"
# }
#
#
# def assistant():
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = r.listen(source)
#
#     try:
#         speech = r.recognize_google(audio)
#         print("You said: " + speech)
#
#         # Check if speech contains any keywords
#         for keyword, response in keywords.items():
#             if keyword in speech.lower():
#                 engine.say(response)
#                 engine.runAndWait()
#                 break
#
#     except sr.UnknownValueError:
#         print("I'm sorry, I didn't understand that.")
#     except sr.RequestError:
#         print("Sorry, speech recognition service is down.")
#
#
# while True:
#     assistant()
