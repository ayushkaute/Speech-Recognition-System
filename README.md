# Speech-Recognition-System

*COMPANY: CODTECH IT SOLUTIONS

*NAME: AYUSH MACHHINDRA KAUTE

*INTERN ID: CT04DF1740

*DOMAIN*: ARTIFICIAL INTELLIGENCE

*DURATION*: 4 WEEEKS

*MENTOR: NEELA SANTOSH

Description:
This script uses the speech_recognition library to convert spoken words from an audio file (harvard.wav) into text using Google's Web Speech API. The process involves loading the audio, processing it, and interpreting it into human-readable text.

1. Importing the Required Library
 
import speech_recognition as sr

This line imports the speech_recognition library and assigns it the alias sr. This library provides support for various speech recognition engines, including:
Google Web Speech API (free and popular)
Sphinx (offline)
Microsoft Bing Voice Recognition
IBM Speech to Text
And more...
By importing it as sr, we make the code cleaner and easier to read.

2. Initializing the Recognizer

recognizer = sr.Recognizer()

Here, we create an instance of the Recognizer class. This object will handle all the steps involved in recognizing speech, such as:
Adjusting for background noise
Recording the audio
Sending it to a speech recognition engine
Interpreting the results
You only need one Recognizer object in most programs.

3. Loading the Audio File

with sr.AudioFile(r"C:\Users\Ayush Kaute\.vscode\harvard.wav") as source:

sr.AudioFile() opens the .wav file so it can be used as an audio source.
The with statement ensures that the file is opened and closed safely, preventing memory leaks or file locks.
The r before the path indicates a raw string so that backslashes (\) are treated literally (e.g., \n isn't read as a newline).
At this point, source is an audio stream from the file harvard.wav.

4. Recording the Audio

audio_data = recognizer.record(source)

This line captures the audio from the source and stores it as audio_data.
recognizer.record() takes the entire content of the file.
If the file were long, you could limit it by specifying parameters like duration or offset.
The result, audio_data, is an AudioData object — a digital representation of the sound.

5. Speech Recognition Using Google Web API

text = recognizer.recognize_google(audio_data)

This sends the audio_data to the Google Web Speech API, which performs speech-to-text conversion.
This API is free to use, but requires an internet connection.
If successful, it returns the recognized spoken words as a string.
Example:
If the audio contains "hello world", this line will return "hello world".

6. Handling Exceptions

except sr.UnknownValueError:
    print("Speech was unintelligible.")
    
This catches errors where Google could not understand the speech (e.g., too noisy, unclear pronunciation, silence). It prevents the script from crashing and gives user-friendly feedback.

except sr.RequestError as e:
    print(f"Could not request results; {e}")
    
This block handles situations where:
There's no internet connection
The API is unreachable
Or the request was otherwise invalid
It prints a formatted error message with more details.

7. Output

print("Transcription:", text)

If everything works, this will print the transcribed text from your audio file.

✅ Summary
1	Loads the speech_recognition library
2	Initializes the recognizer object
3	Opens the .wav file for processing
4	Records audio data from the file
5	Sends the audio to Google’s Web Speech API
6	Handles errors if speech is unclear or internet is unavailable
7	Displays the recognized text
