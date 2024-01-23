from vosk import Model, KaldiRecognizer
from roku import Roku
import pyaudio
import json
from threading import Thread
from utils.index import load, parse_command

model = Model("./Modals/vosk-model-small-en-us-0.15")
rec = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(
    format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4000
)
stream.start_stream()
commands = []
awaited_responses = []
prefix = "candy"
rokus = Roku.discover()
roku = Roku(rokus[0])
def handle_command(information):
    if information == None:
        return
    command, run_function, name_function, name_description = information
    commands.append((run_function, name_function))
    print(f"Loaded command '{name_description()}': {command}")


load("./commands", handle_command)
def executeCommand(textInput):
    textResult = parse_command(textInput, prefix)
    if textResult == None:
        return
    for command_tuple in commands:
        run_function, name_function = command_tuple
        if name_function(textResult):
            context = {"roku": roku, "args": name_function(textResult).groups(), "awaited_responses": awaited_responses}
            return run_function(context)


while True:
    
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        results = rec.Result()
        results = json.loads(results)
        textResult = results["text"].strip()
        if textResult == "":
            continue
        # if len(awaited_responses) > 0: 
        #     run_function,  = awaited_responses[0]

        if prefix in textResult:
            Thread(target=executeCommand, args=(textResult,)).start()