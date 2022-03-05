import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

translator.set_service_url(url)

def englishToFrench(english_text):
    """ Translates from english to french"""
    if english_text in (None, ''):
        return None

    translated_text = translator.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()

    return translated_text['translations'][0]['translation']
    
def frenchToEnglish(french_text):
    """ Translates from english to french"""
    if french_text in (None, ''):
        return None
    translated_text = translator.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()

    return translated_text['translations'][0]['translation']

