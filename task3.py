import speech_recognition as sr
import wikipedia
import pyttsx3

engine=pyttsx3.init()
recognizer=sr.Recognizer()
with sr.Microphone() as source:
    print('Clearing background noise...Please wait')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print("wating for your message...")
    recordedaudio=recognizer.listen(source)
    print('done recording')

    try:
        print("printing your message...please wait")
        text=recognizer.recognize_google(recordedaudio,language='en-US')
        print('your message:{}',format(text))
    except Exception as ex:
        print(ex)

    #input data
    wikisearch=wikipedia.summary(text)
    engine.say(wikisearch)
    engine.runAndWait()
