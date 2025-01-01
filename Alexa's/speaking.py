import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Gunakan suara perempuan (jika mau pake)


def talk(text):
    ## Aktifkan bagian ini kalau mau pake menggunakan suara bot
    ## engine.say(text)
    ## engine.runAndWait()
    pass  

def take_command():
    """Mendengarkan perintah dari pengguna."""
    try:
        with sr.Microphone() as source:
            print("Mendengarkan...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='id-ID')  # Bahasa Indonesia
            print(f"Anda berkata: {command}")
            return command.lower()
    except Exception as e:
        print(f"Error: {e}")
        return None

def run_assistant():
    """Logika untuk menjalankan asisten."""
    command = take_command()
    if command:
        
        if 'terima kasih' in command or 'makasih' in command:
            print("Sama-sama, semoga hari Anda menyenankan!")
            return  # Berhenti dari loop
        elif 'putar' in command:
            song = command.replace('putar', '').strip()
            print(f"Memutar lagu: {song}")
            ## talk(f"Memutar lagu {song}")
            pywhatkit.playonyt(song)
        elif 'waktu' in command:  # "Waktu" untuk jam
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(f"Sekarang jam: {time}")
            ## talk(f"Sekarang jam {time}")
        elif 'apa itu' in command:  # "Apa itu" untuk mencari di Wikipedia
            query = command.replace('apa itu', '').strip()
            try:
                info = wikipedia.summary(query, sentences=1, auto_suggest=False)
                print(f"{query.capitalize()}: {info}")
                ## talk(info)
            except wikipedia.exceptions.DisambiguationError:
                error_message = f"Terlalu banyak hasil untuk '{query}'. Spesifikkan pencarian Anda."
                print(error_message)
                ## talk(error_message)
            except wikipedia.exceptions.PageError:
                error_message = f"Tidak ada hasil untuk '{query}'."
                print(error_message)
                ## talk(error_message)
        elif 'siapa' in command:  # "Siapa" untuk mencari informasi tentang seseorang di Wikipedia
            person = command.replace('siapa', '').strip()
            try:
                info = wikipedia.summary(person, sentences=2, auto_suggest=False)
                print(f"Informasi tentang {person.capitalize()}: {info}")
                ## talk(info)
            except wikipedia.exceptions.DisambiguationError:
                error_message = f"Terlalu banyak hasil untuk '{person}'. Spesifikkan pencarian Anda."
                print(error_message)
                ## talk(error_message)
            except wikipedia.exceptions.PageError:
                error_message = f"Tidak ada informasi tentang '{person}'."
                print(error_message)
                ## talk(error_message)
        elif 'joke' in command:  # Cerita lucu
            joke = pyjokes.get_joke()
            print(f"Cerita lucu: {joke}")
            ## talk(joke)
        else:
            error_message = "Saya tidak mengerti perintah Anda. Coba lagi."
            print(error_message)
            ## talk(error_message)

# Jalankan asisten
while True:
    run_assistant()
