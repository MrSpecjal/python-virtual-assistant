import speech_recognition as sr
import pyttsx3


def textToSpeach(audio):
    print(audio)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    for voice in voices:
        # If MS Hazel voice is exist set as default
        if voice.id == 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0':
            engine.setProperty('voice',
                               'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0')

    engine.runAndWait()
    engine.say(audio)
    engine.runAndWait()


def recognizeSpeach():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # Just for debug
        print('Ready ...')

        r.listen(source)
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        # Just for debug
        print('You said: ' + command + '\n')

    # Loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        textToSpeach('Sorry, I can\'t understand you.')
        command = recognizeSpeach()

    return command


def assistant(command):
    if 'command' in command:
        textToSpeach('You said command')


while True:
    assistant(recognizeSpeach())