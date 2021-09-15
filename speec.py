import speech_recognition as sr
recog = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak :")
    huh = recog.listen(source)
    try:
        text = recog.recognize_google(huh)
        print("You said : {}".format(text))
    except:
        print("Sorry try again")
