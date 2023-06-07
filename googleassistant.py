import speech_recognition as sr
import pyttsx3
from googlesearch import search

# Inisialisasi recognizer dan engine TTS

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Silakan bicara...")
        recognizer.adjust_for_ambient_noise(source) # Menghilangkan noise dari lingkungan sekitar
        audio = recognizer.listen(source) # Mendengarkan suara dari mikrofon
        try:
            text = recognizer.recognize_google(audio, language="id-ID") #Menggunakan Google Speech Recognition API
            print("Anda mengatakan:", text)
            return text
        except sr.UnknownValueError:
            print("Maaf, tidak dapat mengenali suara Anda.")
        except sr.RequestError:
            print("Maaf, terjadi kesalahan pada koneksi ke layanan Google Speech Recognition.")
        return ""
def speak(text):
    engine.say(text)
    engine.runAndWait()
def google_search(query):
    speak("Saya mencari informasi mengenai " + query)
    results = search(query, num_results=3, lang="id", stop=3) # Menggunakan googlesearch untuk mencari
    speak("Berikut adalah beberapa hasil yang saya temukan:")
    for i, result in enumerate(results, start=1):
        speak(f"Hasil {i}: {result}")
# Contoh penggunaan
speak("Halo, saya Google Assistant. Apa yang bisa saya bantu?")
input_text = listen()
speak("Anda mengatakan: " + input_text)
google_search(input_text)