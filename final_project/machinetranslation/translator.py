"""
       Language Translator
"""
import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = "2018-05-01"

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)
language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)


def  english_to_french(text_to_translate):
    """
       English -> French
    """
    translation = language_translator.translate(
    text=text_to_translate,
    model_id='en-fr').get_result()
    for k_k,v_v in translation.items():
        if k_k=='translations':
            for i_i in v_v :
                for key,value in i_i.items() :
                    if key=='translation':
                        french_text=value
    return french_text
print(english_to_french(
    'This is a translation'
    ))

def  french_to_english(text_to_translate):
    """
    French -> English
    """
    translation = language_translator.translate(
    text=text_to_translate,
    model_id='fr-en').get_result()
    for k_k,v_v in translation.items():
        if k_k=='translations':
            for i_i in v_v :
                for key,value in i_i.items() :
                    if key=='translation':
                        english_text=value
    return english_text
print(type(french_to_english('Bonjour')))
