import speech_recognition as s
r=s.Recognizer()
with s.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("speak Anything:")
    audio=r.listen(source)

    try:
        text=r.recognize_google(audio)
        print("you said:",text)
    except:
        print("sorry i cant understant your voice....")




    
