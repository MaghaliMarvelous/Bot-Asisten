# Bot-Asisten
Asisten virtual berbasis suara yang dapat menjalankan beberapa perintah yang diberikan oleh pengguna melalui perintah suara.

# Voice Assistant (Asisten Virtual Berbasis Suara)

Ini adalah asisten suara berbasis Python yang mendengarkan perintah suara dalam **Bahasa Indonesia** dan melakukan berbagai tugas, seperti memutar musik, menentukan waktu, menelusuri Wikipedia, dan menceritakan lelucon. Asisten menggunakan **Pengenalan Ucapan** untuk masukan suara dan **Teks-ke-Ucapan** untuk keluaran verbal.

## Features
- **Voice Commands**: Recognizes commands in Indonesian, such as:
  - Play music on YouTube.
  - Tell the current time.
  - Get information from Wikipedia.
  - Tell a random joke.
- **Text-to-Speech**: Provides verbal feedback to the user.
- **Hands-free**: Control your computer through voice, with no need for manual input.

## Requirements
To run this project, you'll need to install the following Python libraries:

- `speech_recognition`: For speech-to-text conversion.
- `pyttsx3`: For text-to-speech conversion.
- `pywhatkit`: For controlling YouTube (to play music).
- `wikipedia`: For searching Wikipedia articles.
- `pyjokes`: For telling jokes.

You can install all the required libraries using pip:

```bash
pip install speechrecognition pyttsx3 pywhatkit wikipedia pyjokes

