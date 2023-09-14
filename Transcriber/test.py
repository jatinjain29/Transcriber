
# from google.cloud import speech_v1p1beta1 as speech
# print("Hello world")
# client = speech.SpeechClient()
# second_lang = ["en-IN"]
# config = {
#     "encoding": "linear16",
#     "sample_rate_hertz": 48000,
#     "audio_channel_count": 2,
#     #"enable_separate_recognition_per_channel" : true,
#     "language_code": "auto",
#     #"alternative_language_codes":second_lang
    
    
# }
# # config = speech.RecognitionConfig(
# #         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
# #         # sample_rate_hertz=16000,
# #         language_code= "auto",
# #         audio_channel_count= 2,
# #     #    alternative_language_codes=second_lang,
# #     )
# print("Hello world 2")
# audio = {"uri": "gs://translator-new/Recording.wav"}
# print(audio)

# response = client.recognize(config=config, audio=audio)
# print(response)
# print("Dedede")
# for result in response.results:
#     print("Transcript: {}".format(result.alternatives[0].transcript))





from google.cloud import speech
import requests
import json
import asyncio


    
def textToAudio(transcript):
 

 
    print("fun1 start")
    # Set the subscription key and region
    subscription_key = "22306a22c69d40d6a3184cb297b8f7c0"
    region = "eastus"

 

    # Set the endpoint URL
    url = "http://eastus.tts.speech.microsoft.com/cognitiveservices/v1"

 

    # Set the headers
    headers = {
        "Ocp-Apim-Subscription-Key": subscription_key,
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "audio-16khz-128kbitrate-mono-mp3",
        "Ocp-Apim-Subscription-Region": "eastus"
        #"User-Agent": "YOUR_RESOURCE_NAME"
    }

 

    # Set the body with the text you want to convert and the voice you want to use
    # body = """
    # <speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-IN'>
    # <voice name='Microsoft Server Speech Text to Speech Voice (en-IN, Heera, Apollo)'>
    #     {0}
    # </voice>
    # </speak>
    # """.format(transcript)

 

    # Send a POST request to the endpoint
    # response = requests.post(url, headers=headers, data=body)
    # print(response)

 

    # # Save the response content as an audio file
    # with open('output.wav', 'wb') as audio:
    #     audio.write(response.content)
        

    body = """
    <speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'>
    <voice name='Microsoft Server Speech Text to Speech Voice (en-US, Guy24KRUS)'>
        hello hey there
    </voice>
    </speak>
    """

 

    # Send a POST request to the endpoint
    response = requests.post(url, headers=headers, data=body)

 

    # Save the response content as an audio file
    with open('output.mp3', 'wb') as audio:
        audio.write(response.content)
 
    print("fun1 end")
    

def translate_text(text):
    
 
    print("fun3 start")
    # Define the endpoint
    url = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from=hi&from=en&to=en"

    headers = {
    "Ocp-Apim-Subscription-Key": "6875fe99c883446d8a4f49be039eed69",
    "Ocp-Apim-Subscription-Region": "eastus",
    "Content-type": "application/json",
    #"X-ClientTraceId": "<your-client-trace-id>"
    }
    # Define the body
    body = [{'text': text}]

 
    print(body)
    # Make the API request
    response = requests.post(url, headers=headers, json=body)
    print(response)

 
    print("here")
    # Get the response
    translations = response.json()
    #textToAudio(translations[0]['translations'][0]['text'])

 

    # Print the translated text
    print(translations[0]['translations'][0]['text'])
    
 
    print("fun3 end")

 




def SpeechToText():
    
 
    print("fun2 start")
    client = speech.SpeechClient()
    

# Replace 'your-audio-file.wav' with the path to your audio file
    audio = {"uri": "gs://translator-new/Recording.wav"}
    second_lang = ["hi-IN"]
    config = {
    "encoding": "LINEAR16",
    "audio_channel_count": 2,
    "language_code": "hi-IN", 
    #"alternative_language_codes":second_lang
    }
    
    print("fun2 start")

    response = client.recognize(config=config, audio=audio)
    out1=""
    print(response)
    print("fun2 start")

    # for result in response.results:
    #     print("Detected Language: {}".format(result.language_code))
    #     print("Transcript: {}".format(result.alternatives[0].transcript))
    #     out1+=result.alternatives[0].transcript
    
    # print("fun2 start")
    # translate_text(out1)
    
    # print("fun2 start")
    
 
    # print("fun2 end")

#SpeechToText()
textToAudio("Hello ,it seems like you are busy. Give me a call whenever you get free.Will wait for your call.")