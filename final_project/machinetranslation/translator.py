''' Python Watson Translator for French to English and English to French'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION_LT = '2018-05-01'
authenticator = IAMAuthenticator(apikey)
lt = LanguageTranslatorV3(version=VERSION_LT,authenticator=authenticator)
lt.set_service_url(url)

def english_to_french(english_text):
    ''' Function for translating english to french, input is english text '''
    translation = lt.translate(text=english_text,model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    ''' Function for translating french to english, input is french text '''
    translation = lt.translate(text=french_text,model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
