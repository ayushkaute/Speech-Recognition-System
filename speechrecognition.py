import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Load your audio file
with sr.AudioFile(r"C:\Users\Ayush Kaute\.vscode\harvard.wav") as source:
    audio_data = recognizer.record(source)
    try:
        # Recognize using Google Web Speech API
        text = recognizer.recognize_google(audio_data)
        print("Transcription:", text)
    except sr.UnknownValueError:
        print("Speech was unintelligible.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
