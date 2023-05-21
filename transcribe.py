import os
import openai

def transcribe(audio_file, api_key) -> str:
    openai.api_key = api_key

    audio_file= open(audio_file, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    lsttrans = dict(transcript)
    text = lsttrans['text']

    if not os.path.exists("transcript.txt"):
        fil = open("transcript.txt", "w")
        fil.write(text)
        fil.close()
        return "transcript.txt"
    else:
        i = 0
        while True:
            i += 1
            if os.path.exists("transcript" + str(i) + ".txt"):
                continue
            else:
                fil = open("transcript" + str(i) + ".txt", "w")
                fil.write(text)
                fil.close()
                return "transcript" + str(i) + ".txt"