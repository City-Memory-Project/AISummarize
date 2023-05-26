import summarize
import transcribe
import util

version = "1.0.0"

print("Version " + version)
print("Welcome to CityMemory autosummarizing script. Made by Aaron Ko.\n")

audio_name = input("Input audio file name: ")
api_key = input("Input OpenAPI key: ")
max_tokens = input("Maximum Amount of Tokens: (Set to 300 if left blank)")

if max_tokens == '':
    max_tokens = 300
else:
    max_tokens = int(max_tokens)

util.log_message("INFO", "Starting to transcribe audio..")
transcription_name = transcribe.transcribe(audio_name, api_key)

util.log_message("INFO", "Audio transcribed. Sending ChatGPT request to summarize.")
transcription_text = util.pull_text(transcription_name)
chatgpt_payload = "Please summarize this section of transcribed text: " + transcription_text
transcription_summary = summarize.request_chatgpt(chatgpt_payload, api_key, max_tokens)
transcription_summary_CN = summarize.request_chatgpt(chatgpt_payload + "in Chinese", api_key, max_tokens)

util.log_message("INFO", "ChatGPT request successful. Writing to file.")
util.write_summary_to_file(transcription_name, transcription_summary, "summary")
util.write_summary_to_file(transcription_name, transcription_summary_CN, "summaryCN")
util.log_message("INFO", "Success!")