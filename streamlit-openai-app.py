
# https://platform.openai.com/docs/introduction

# Standard Libraries
import logging

# Streamlit Library and Components
import streamlit as st
import streamlit.components.v1 as components

# OpenAI
import openai


# Logger Configuration
logging.basicConfig(format = "\n%(asctime)s\n%(message)s", 
                    level = logging.INFO, 
                    force = True)


f = open("about.txt", "r")
st.set_page_config(
     page_title = "Open AI",
     page_icon = ":robot_face:",
     layout = "centered",
     initial_sidebar_state = "auto",
     menu_items = {
         'Get Help': 'https://github.com/imarranz/streamlit-openai-app',
         'Report a bug': 'https://github.com/imarranz/streamlit-openai-app',
         'About': f.read()
     }
)                                    
f.close()

font_css = """
<style>
button[data-baseweb="tab"] {
    font-size: 22px;
}
</style>
"""
st.write(font_css, unsafe_allow_html = True)


openai.api_key = st.secrets["OPENAI_API_KEY"]

# list engines
# engines = openai.Engine.list()
# print(engines)
# print the first engine's id
# print(engines.data[0].id)


st.markdown("## Open AI")
st.markdown("**Generative Pre.trained Transformer 3 (GPT-3) is a new language model created by [OpenAI](https://openai.com) that is able to generate written text**")


tab1, tab2, tab3, tab4 = st.tabs(['davinci', 'dall-e', 'ChatGPT', 'Resources'])

with tab1:

    with st.form("playground"):

        col1, col2, col3 = st.columns([1,1,1], gap = "medium")
        
        with col1:

            PROMPT_ = st.text_input(label = "Write a tagline for a ...")
            
            TEMPERATURE_ = st.slider(label = "Temperature", 
                                    min_value = 0.0, max_value = 1.0, value = 0.9, step = 0.1, help = "Control randomness: Lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive. Source: OpenAI Playground.")
        with col2:
        
            MAXTOKENS_ = st.slider(label = "Maximum number of tokens", 
                                min_value = 100, max_value = 4000, value = 250, step = 50,
                                help = "The maximum number of tokens to generate. Requests can use up to 2,048 or 4,000 tokens shared between prompt and completion. The exact limit varies by model. One token is roughly 4 characters for normal English text. Source: OpenAI Playground.")

            TOPP_ = st.slider(label = "Top P",
                            min_value = 0.0, max_value = 1.0, value = 1.0, step = 0.1,
                            help = "Controls diversity via nucleus sampling: 0.5 means half of all likelihood-weighted options are considered. Source: OpenAI Playground.")
        
        with col3:
        
            FREQUENCYPENALTY_ = st.slider(label = "Frequency penalty",
                                        min_value = 0.00, max_value = 2.00, value = 0.0, step = 0.01,
                                        help = "How much to penalize new tokens based on their existing frequency in the text so far. Decreases the model's likelihood to repeat the same line verbatim. Source: OpenAI Playground.")
            PRESENCEPENALTY_ = st.slider(label = "Presence penalty",
                                        min_value = 0.00, max_value = 2.00, value = 0.0, step = 0.01,
                                        help = "How much to penalize new tokens based on whether they appear in the text so far. Increases the model's likelihood to talk about new topics. Source: OpenAI Playground.")
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            # TEXT GENERATION
            kwargs = {
                "engine": "text-davinci-003",
                "prompt": PROMPT_,
                "temperature": TEMPERATURE_,
                "max_tokens": MAXTOKENS_,
                "n": 1, #How many completions to generate for each prompt
                "top_p": TOPP_,  # default
                "frequency_penalty": FREQUENCYPENALTY_,  # default,
                "presence_penalty": PRESENCEPENALTY_,}  # default}
            
            completion = openai.Completion.create(**kwargs)
            st.info(f"""**Configuration**:  
                    **engine**: text-davinci-003  
                    **prompt**: {PROMPT_}  
                    **temperature**: {TEMPERATURE_}  
                    **maximum number of tokens**: {MAXTOKENS_}  
                    **top P**: {TOPP_}  
                    **frequency penalty** {FREQUENCYPENALTY_}  
                    **presence penalty**: {PRESENCEPENALTY_}""")
            st.success(completion.choices[0].text) 

with tab2:
    
    with st.form('image'):
        
        col1, col2 = st.columns([1,1], gap = "medium")
        
        with col1:
            
            
            PROMPT_ = st.text_input(label = "Write a tagline for a ...")
        with col2:
            
            SIZE_ = st.selectbox(label = "Size", 
                                 options = ('256x256', '512x512', '1024x1024'))
        
        submitted = st.form_submit_button("Submit")
        
        with st.expander(label = "Prompt examples", expanded = False):
            
            st.info("Examples from [mpost.io](https://mpost.io/top-50-text-to-image-prompts-for-ai-art-generators-midjourney-and-dall-e/)")
            
            st.success("earth reviving after human extinction, a new beginning, nature taking over buildings, animal kingdom, harmony, peace, earth balanced --version 3 --s 1250 --uplight --ar 4:3 --no text, blur")
            
            st.success("earth after human extinction, a new beginning, nature taking back the planet, harmony, peace, earth balanced --version 3 --s 42000 --uplight --ar 4:3 --no text, blur, people, humans, pollution")
            
            st.success("2 medieval warriors ::0.4 travelling on a cliff to a background castle , view of a coast line landscape , English coastline, Irish coastline, scottish coastline, perspective, folklore, King Arthur, Lord of the Rings, Game of Thrones. Photographic, Photography, photorealistic, concept art, Artstation trending , cinematic lighting, cinematic composition, rule of thirds , ultra-detailed, dusk sky , low contrast, natural lighting, fog, realistic, light fogged, detailed, atmosphere hyperrealistic , volumetric light, ultra photoreal, | 35mm| , Matte painting, movie concept art, hyper-detailed, insanely detailed, corona render, octane render, 8k, --ar 3:1 --no blur")
            
        
        if submitted:
            kwargs = {
                "prompt": PROMPT_,
                "n": 1,
                "size": SIZE_}
            image_resp = openai.Image.create(**kwargs)
            image_url = image_resp['data'][0]['url']
            st.image(image_url)
            
            
        #prompt = "Genetic Algorithms Applied to Translational Strategy in NASH. Learning from Mouse Models", n=1, size="512x512")
    
    # Generación de Imágenes
    # ----------------------

    #image_resp = openai.Image.create(
        #prompt = "Genetic Algorithms Applied to Translational Strategy in NASH. Learning from Mouse Models", n=1, size="512x512")

    #image_url = image_resp['data'][0]['url']
    #print(image_url)


    # https://towardsdatascience.com/gpt-3-parameters-and-prompt-design-1a595dc5b405

with tab3:
    # https://platform.openai.com/docs/guides/chat
    with st.form('chat'):
        col1, col2 = st.columns([1,1], gap = "medium")
            
        with col1:

            CONTENT_ = st.text_input(label = "Write a tagline for a ...")
                
        submitted = st.form_submit_button("Submit")
        if submitted:
            # TEXT GENERATION
            kwargs = {
                "model": "gpt-3.5-turbo",
                "n": 1,
                "stop": None,
                "messages": [{"role": "user", "content": CONTENT_}]
                }  # default}
            
            completion = openai.ChatCompletion.create(**kwargs, )
            st.info(f"""**Configuration**:  
                    **model**: gpt-3.5-turbo  
                    **content**: {CONTENT_}  
                    **more information**: https://platform.openai.com/docs/guides/chat""")
            
            st.success(completion.choices[0].message['content']) 
            
with tab4:
    
    st.markdown("## Resources")
    
    st.markdown("Welcome to our resource section, where you will find a collection of links to various websites and online tools that I have found helpful for various purposes. I will continue to update this section regularly, so be sure to check back often for new additions.")
    
    st.markdown("[openai](https://platform.openai.com/docs/introduction)")
    st.markdown("[Text Completion](https://platform.openai.com/docs/guides/completion)")
    st.markdown("[Chat Completion](https://platform.openai.com/docs/guides/chat)")
    st.markdown("[Image Generation](https://platform.openai.com/docs/guides/images)")
    st.markdown("[Fine-tuning](https://platform.openai.com/docs/guides/fine-tuning)")
