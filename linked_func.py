import re
import string
from typing import List
from string import punctuation

import nltk
from unidecode import unidecode
from nltk import tokenize

from organize import token_data


class remove_trash():

    def __init__(self, list_stopword: List[str]):
        self.stopword = list_stopword

    def start_clean(self, data):
        return self.__remove_stopwords(data)

    def __remove_stopwords(self, data):
        list_clean_data: List[str] = []
        list_separete_sentence: List[str] = token_data(data)

        for word in list_separete_sentence:
            not_accent = unidecode(word)
            if not_accent not in self.stopword:
                list_clean_data.append(word)

        phrase_complete = ' '.join(list_clean_data)
        return self.__remove_user(phrase_complete)

    def __remove_user(self, data):
        pattern = re.compile(r'@\w+: |@\w+|@\w+ ')
        data_without_user = pattern.sub(r'', str(data))
        return self.__remove_URL(data_without_user)

    def __remove_URL(self, data):
        url = re.compile(r'https?://\S+|www\.\S+|https+|tco?')
        data = url.sub(r'', data)
        return self.__remove_emoji(data)

    def __remove_emoji(self, data):
        emoji_pattern = re.compile("["
                                   u"\U0001F600-\U0001F64F"  # emoticons
                                   u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                   u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                   u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                   u"\U00002500-\U00002BEF"  # chinese char
                                   u"\U00002702-\U000027B0"
                                   u"\U00002702-\U000027B0"
                                   u"\U000024C2-\U0001F251"
                                   u"\U0001f926-\U0001f937"
                                   u"\U00010000-\U0010ffff"
                                   u"\u2640-\u2642"
                                   u"\u2600-\u2B55"
                                   u"\u200d"
                                   u"\u23cf"
                                   u"\u23e9"
                                   u"\u231a"
                                   u"\ufe0f"  # dingbats
                                   u"\u3030"
                                   "]+", flags=re.UNICODE)

        data_without_emoji = emoji_pattern.sub(r'', str(data))
        return self.__remove_punct(data_without_emoji)

    def __remove_punct(self, data):
        table = str.maketrans('', '', string.punctuation)
        data = data.translate(table)
        return self.__remove_hashtag(data)

    def __remove_hashtag(self, data):
        pattern = re.compile(r'#\w+')
        data_without_hashtag = pattern.sub(r'', str(data))
        data = data_without_hashtag
        return data
