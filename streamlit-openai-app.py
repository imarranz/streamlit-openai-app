import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

# list engines
engines = openai.Engine.list()
# print(engines)
# print the first engine's id
# print(engines.data[0].id)

# Generación de Textos
# --------------------

prompt = "Python class. A brief definition"
temperature = 0.9
max_tokens = 150

# create a completion
kwargs = {
    "engine": "text-davinci-003",
    "prompt": prompt,
    "temperature": temperature,
    "max_tokens": max_tokens,
    "n": 1, #How many completions to generate for each prompt
    "top_p": 1,  # default
    "frequency_penalty": 0,  # default,
    "presence_penalty": 0,  # default
}


completion = openai.Completion.create(**kwargs)

# print the completion (choices depends of n)

print("-----------------------")
print(completion.choices[0].text) 
#print("-----------------------")
#print(completion.choices[1].text) 

# Generación de Imágenes
# ----------------------

#image_resp = openai.Image.create(
    #prompt = "Genetic Algorithms Applied to Translational Strategy in NASH. Learning from Mouse Models", n=1, size="512x512")

#image_url = image_resp['data'][0]['url']
#print(image_url)
