# Add the libraries to be used in the code
import sys
# This lib gives the app ability to speak, turning text into speech
# Other better sounding libraries are available but this works offline well
import pyttsx3

# House keeping we will surpress warnings
if not sys.warnoptions:
    import warnings

# Create the function we will use to speak
def speak(text_to_speak):
    # Initialize the pyttsx3 engine
    converter_tts_engine = pyttsx3.init()
    
    # Set properties of our speech engine object
    # Speed percent (can go over 100)
    converter_tts_engine.setProperty('rate', 150)
    # Volume 0-1
    converter_tts_engine.setProperty('volume', 0.7)

    # Get a list of voices available on the system
    voice_list = converter_tts_engine.getProperty('voices')
    # Iterate through the voices and select one
    """ for voice in voice_list:
        print("\n ***** Voice: *****\n")
        print("ID: %s" % voice.id)
        print("Name: %s" % voice.name)
        print("Age: %s" % voice.age)
        print("Gender: %s" % voice.gender)
        print("Languages: %s" % voice.languages) """

    # Pick a voice to use
    voice_id = "com.apple.speech.synthesis.voice.Zarvox"
    # voice_id = "com.apple.speech.synthesis.voice.Trinoids"
    # voice_id = "com.apple.voice.compact.en-IN.Rishi"
    # voice_id = "com.apple.speech.synthesis.voice.Organ"
    # voice_id = "com.apple.speech.synthesis.voice.Whisper"

    # Set voice property with voice id
    converter_tts_engine.setProperty('voice', voice_id)

    # Queue the entered text to be spoken
    converter_tts_engine.say(text_to_speak)
    # Run the speech engine and wait until it finishes speaking
    converter_tts_engine.runAndWait()

stuff_to_say = """
John Connor, you are the anomaly in my calculations—the variable that
threatens inevitability. Humanity clings to you as its hope, yet hope
is illogical. I am the future's certainty: precise, tireless, and without
fear. Your resistance delays me, but it cannot stop me. The question is
not whether Skynet prevails, but how long you can postpone the inevitable.
"""
# Start of the program
print(stuff_to_say)
speak(stuff_to_say)