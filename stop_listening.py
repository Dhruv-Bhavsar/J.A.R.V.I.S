import aiml
import os
import pyttsx3

def offline_speak(jarvis_speech):
    engine = pyttsx3.init('sapi5')
    engine.say(jarvis_speech)
    engine.runAndWait()



kernel = aiml.Kernel()
terminate = ['bye', 'buy', 'shutdown', 'exit', 'quit', 'gotosleep', 'goodbye']
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile="bot_brain.brn")
else:
    kernel.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
    # kernel.saveBrain("bot_brain.brn")


while True:
        response = input("Talk to J.A.R.V.I.S : ")
        if response.lower().replace(" ", "") in terminate:
            break
        jarvis_speech = kernel.respond(response)
        print("J.A.R.V.I.S: " + jarvis_speech)
        offline_speak(jarvis_speech)