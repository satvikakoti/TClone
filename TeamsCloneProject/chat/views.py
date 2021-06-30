from django.shortcuts import render
import speech_recognition as sr
import pyttsx3


# Create your views here.


def main_view(request):
    context = {}

    return render(request, 'chat/main.html', context=context)


'''r = sr.Recognizer()


def SpeakText(command):

    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


global Name


def name():
    global Name
    with sr.Microphone() as source:
        print("Name")
        SpeakText("Name")
        audio = r.listen(source, timeout=3)
    try:
        sp = r.recognize_google(audio)
        print("You said ", sp)
        #         return sp
    except Exception as e:
        print(e)
        print("Didn't get you, can you say it again?")
        SpeakText("Didn't get you, can you say it again?")
        return name()
    Name = sp


flag = 0
while flag < 1:

    try:

        name()
        flag += 1

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")

print(Name)

# class VoiceAssistant:
#
#     r = sr.Recognizer()
#
#     def SpeakText(self, command):
#
#         # Initialize the engine
#         engine = pyttsx3.init()
#         engine.say(command)
#         engine.runAndWait()
#
#     global Name, Age, Gender, Symptom, Diagnosis, Advice, Medicine
#     Name = ""
#     Medicine = []
#     Age = ""
#     Gender = ""
#     Symptom = ""
#     Diagnosis = ""
#     Advice = ""
#
#     def name(self):
#         global Name
#         with sr.Microphone() as source:
#             print("Name")
#             self.SpeakText("Name")
#             audio = self.r.listen(source, timeout=3)
#         try:
#             sp = self.r.recognize_google(audio)
#             print("You said ", sp)
#         #         return sp
#         except Exception as e:
#             print(e)
#             print("Didn't get you, can you say it again?")
#             self.SpeakText("Didn't get you, can you say it again?")
#             return self.name()
#         Name = sp
#         print(Name)
#
#     flag = 0
#     while flag < 1:
#
#         try:
#
#             name(object)
#             flag += 1
#
#         except sr.RequestError as e:
#             print("Could not request results; {0}".format(e))
#
#         except sr.UnknownValueError:
#             print("unknown error occured")
#
#     print(Name, Age, Gender, Symptom, Diagnosis, Advice)
'''

