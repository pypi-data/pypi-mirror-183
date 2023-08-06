from google.cloud import translate
from os_translator.modules import translator_boilerplate as bp


###########################################################################
# this module aim is to translate text.
###########################################################################

def translate_text(service_account_json_path,
                   project_id,
                   text,
                   language_initials_dest,
                   language_initials_src='en-US',
                   html_or_normal_text='normal_text'
                   ):
    """Will translate a text to a given language.

    Parameters:
        service_account_json_path: the path to your google translate api json key. Download from your firebase's project's settings
        project_id: your project id (fetch from your api console project's name: https://console.cloud.google.com/?_ga=2.55756075.1423406147.1582784765-1154152733.1582784765)
        text: the text to translate
        language_initials_dest: the initials of the language you want to translate to
        language_initials_src: the source language
        html_or_normal_text: toggle to html if you want to set text with html tag (like <p>what's the deal here?</p>. Leave blank for normal text

    NOTICE:
        If there are substrings you don't want to translate, write KEEP before them. Example: "The boy looks KEEPWord"
    """

    # Instantiates the client
    translate_client = translate.TranslationServiceClient.from_service_account_json(service_account_json_path)

    # translate the sentence
    return bp.translate_sentence(translate_client,
                                 project_id,
                                 language_initials_src,
                                 language_initials_dest,
                                 text,
                                 html_or_normal_text=html_or_normal_text)


def translate_lines_with_same_context(service_account_json_path,
                                      project_id,
                                      text,
                                      language_initials_dest,
                                      language_initials_src='en-US'
                                      ):
    """Will translate a same context text, broken to lines, into a given language.
    Call this function usually from a screenshot caption or other text of more than one line with the same context. Like:
    "Use this\nif you want to help\nthe environment"

    NOTICE: the program separates new lines using <u> so make sure you aren't using the <u> tag.

    Parameters:
        service_account_json_path: the path to your google translate api json key. Download from your firebase's project's settings
        project_id: your project id (fetch from your api console project's name: https://console.cloud.google.com/?_ga=2.55756075.1423406147.1582784765-1154152733.1582784765)
        text: the text to translate
        language_initials_dest: the initials of the language you want to translate to
        language_initials_src: the source language

    NOTICE:
        If there are substrings you don't want to translate, write KEEP before them. Example: "The boy looks KEEPWord"
    """

    # Instantiates the client
    translate_client = translate.TranslationServiceClient.from_service_account_json(service_account_json_path)

    # translate the sentence
    return bp.translate_lines_with_same_context(translate_client,
                                                project_id,
                                                language_initials_src,
                                                language_initials_dest,
                                                text)
