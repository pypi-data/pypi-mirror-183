# coding=utf-8
import sys
from google.cloud import translate

# just the boiler plate of the sentence translator
play_initials_bank = ['en-GB', 'af', 'am', 'ar', 'hy-AM', 'az-AZ', 'bn-BD', 'eu-ES', 'be', 'bg', 'my-MM', 'ca', 'zh-HK', 'zh-CN', 'zh-TW', 'hr', 'cs-CZ', 'da-DK', 'nl-NL', 'en-AU', 'en-IN', 'en-SG',
                      'en-ZA', 'en-CA', 'en-US', 'et', 'fil', 'fi-FI', 'fr-FR', 'fr-CA', 'gl-ES', 'ka-GE', 'de-DE', 'el-GR', 'hi-IN', 'hu-HU', 'is-IS', 'id', 'it-IT', 'ja-JP', 'kn-IN', 'km-KH',
                      'ko-KR', 'ky-KG', 'lo-LA', 'lv', 'lt', 'mk-MK', 'ms', 'ml-IN', 'mr-IN', 'mn-MN', 'ne-NP', 'no-NO', 'fa', 'pl-PL', 'pt-BR',
                      'pt-PT', 'ro', 'ro', 'ru-RU', 'sr', 'si-LK', 'sk', 'sl', 'es-419', 'es-ES', 'es-US', 'sw', 'sv-SE', 'ta-IN', 'te-IN', 'th', 'tr-TR', 'uk', 'vi', 'zu']


# the actual conversion of a text
def translate_sentence(translate_client,
                       project_id,
                       language_src,
                       language_dest,
                       text,
                       html_or_normal_text='normal_text'):
    # translate
    parent = f'projects/{project_id}'
    text_type = "plain" if html_or_normal_text == 'normal_text' else 'html'
    try:
        response = translate_client.translate_text(
            parent=parent,
            contents=[text],
            mime_type=f'text/{text_type}',
            source_language_code=language_src,
            target_language_code=language_dest)

        ans = ""
        for translation in response.translations:
            ans += format(translation.translated_text)
        return ans
    except Exception as e:
        return e


# the actual conversion of a text
def translate_lines_with_same_context(translate_client,
                                      project_id,
                                      language_src,
                                      language_dest,
                                      text):
    # substitute <u> and </u> instead of \n
    manipulated = text
    new_line_count = manipulated.count('\n')
    if new_line_count == 1:
        manipulated = manipulated.replace('\n', '<u>')
        manipulated += '</u>'
    else:
        manipulated = manipulated.replace('\n', '</u><u>')
        manipulated = manipulated.replace('</u><u>', '<u>', 1)
        manipulated += '</u>'
    ans = translate_sentence(translate_client, project_id, language_src, language_dest, manipulated, html_or_normal_text='html')
    splat_start = '</u>'
    splat_end = '<u>'

    # roll back the \n
    outer_lines = ans.split(splat_start)
    line_legal = True
    for outer_line in outer_lines:
        if splat_end not in outer_line:
            line_legal = False
    if outer_lines[-1] == '' or outer_lines[0] == '' or not line_legal:
        outer_lines = ans.split(splat_end)
        temp = splat_end
        splat_end = splat_start
        splat_start = temp

    ans_new2 = list(map(lambda x: x.replace(splat_end, ''), outer_lines))
    as_new_3 = '\n'.join(ans_new2)
    return as_new_3.replace('&#39;', '\'').replace('&amp;', '&')

    # translate
    parent = f'projects/{project_id}'
    text_type = "plain" if html_or_normal_text == 'normal_text' else 'html'
    try:
        response = translate_client.translate_text(
            parent=parent,
            contents=[text],
            mime_type=f'text/{text_type}',
            source_language_code=language_src,
            target_language_code=language_dest)

        ans = ""
        for translation in response.translations:
            ans += format(translation.translated_text)
        return ans
    except Exception as e:
        return e


# will convert play initials to translate initials
def play_for_translate(play_initials):
    translate_initials = play_initials
    if '-' in play_initials:
        translate_initials = play_initials[:play_initials.index('-')]
    return translate_initials


# will return the indexes of all of the matching substrings in a string
def find_all_substrings(string, word):
    all_positions = []
    next_pos = -1
    while True:
        next_pos = string.find(word, next_pos + 1)
        if next_pos < 0:
            break
        all_positions.append(next_pos)
    return all_positions
