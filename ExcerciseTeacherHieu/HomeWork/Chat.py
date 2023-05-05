# import openai
# import speech_recognition as sr
# import pyttsx3
#
# openai.api_key = "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"
#
#
# def ask_gpt(question):
#     prompt = "Question: {}\nAnswer:".format(question)
#     response = openai.Completion.create(
#         engine="davinci",
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )
#     answer = response.choices[0].text.strip()
#     return answer
#
#
# def speak(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()
#
#
# def listen():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = r.listen(source)
#     try:
#         text = r.recognize_google(audio)
#         print("You said: ", text)
#         return text
#     except:
#         print("Sorry, I couldn't understand what you said.")
#         return ""
#
#
# def main():
#     while True:
#         question = listen()
#         if question:
#             answer = ask_gpt(question)
#             print(answer)
#             speak(answer)
#             while True:
#                 response = listen()
#                 if response:
#                     break
#             print("Next question.")
#
#
#
# if __name__ == '__main__':
#     main()
