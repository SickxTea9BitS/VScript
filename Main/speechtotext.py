import pyttsx3
import speech_recognition as sr
import subprocess
r = sr.Recognizer ()

def speakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()



while(1):

    test_output = ''
    try:
        with sr.Microphone() as source2 :
            r.adjust_for_ambient_noise(source2,duration=0.2)
            audio2 = r.listen(source2)
            mytext = r.recognize_google(audio2)
            mytext = mytext.lower()

            print("Did you say",mytext)

            with open('test_file_1','a') as t_f1:
                t_f1.write(str(mytext+'\n'))

            test_output += mytext+'\n'

            speakText(mytext)

            if mytext == '001':
                break
    except sr.RequestError as e:
        print("could not request result; {0)".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
