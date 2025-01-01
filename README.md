# Bot-Asisten
Asisten virtual berbasis suara yang dapat menjalankan beberapa perintah yang diberikan oleh pengguna melalui perintah suara.

# Voice Assistant (Asisten Virtual Berbasis Suara)

This is a Python-based voice assistant that listens to voice commands in **Indonesian** and performs various tasks, such as playing music, telling the time, searching Wikipedia, and telling jokes. The assistant uses **Speech Recognition** for voice input and **Text-to-Speech** for verbal output.

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

