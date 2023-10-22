import pyttsx3
import speech_recognition as sr
import datetime

r = sr.Recognizer()

def speakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

test_output = ''

while True:
    try:
        with sr.Microphone() as source:
            print("started")
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
            mytext = r.recognize_google(audio).lower()

            print("Did you say:", mytext)

            test_output += mytext + '\n'

            speakText(mytext)

            if mytext == '001':
                
                current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                file_name = f"output_{current_time}.txt"
                with open(file_name, 'w') as t_f2:
                    t_f2.write(test_output)
                print(f"All recognized text saved to {file_name}")
                break

    except sr.RequestError as e:
        print("Could not request result; {0}".format(e))

    except sr.UnknownValueError:
        print("Unknown error occurred")