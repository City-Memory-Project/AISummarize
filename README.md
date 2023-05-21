# AI Summarize

`AISummarize` is a useful python script intended to streamline the process of summarizing a piece of audio. It uses the OpenAI API to make requests to ChatGPT to transcribe and summarize an audio file.

`AISummarize` works best with audio under 15 minutes. Longer pieces of audio may not work as intended due to limitations with ChatGPT's text models. However, effectiveness depends on how much text is transcribed.

### Supported Audio File Extensions

- mp3
- mp4
- mpeg3
- mpga
- m4a
- wav
- webm

### You will need:

- A OpenAI API token. To obtain one, create a ChatGPT developer account [here](https://platform.openai.com/).
- An audio file

You may have to do some testing when deciding the maximum amount of tokens you are using (set to 300 by default.)