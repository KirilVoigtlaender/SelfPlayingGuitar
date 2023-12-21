import speech_recognition as sr

def record_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something to choose a file:")
        audio = recognizer.listen(source)
    return recognizer.recognize_google(audio)
    
def play_file(file_path):
    print("You said" + file_path)
    
if __name__=="__main__":
  choosen_file = record_audio()
  play_file(choosen_file)
  
