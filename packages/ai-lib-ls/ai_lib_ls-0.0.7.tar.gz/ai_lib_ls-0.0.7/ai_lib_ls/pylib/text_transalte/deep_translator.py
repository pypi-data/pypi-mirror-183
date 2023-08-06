# -*- coding: utf-8 -*-
import sys
import os

from ai_lib_ls.pylib.text_transalte.deep_translator import GoogleTranslator


class DeepTranslator:

    def __init__(self):
        pass

    def start_translate(self, str):
        translated = GoogleTranslator(source='auto', target='de').translate(
            str)  # output -> Weiter so, du bist großartig

        return translated


if __name__ == '__main__':
    trans = GoogleTranslator(source="auto", target="zh-CN")
    res = trans.translate("good")
    print("translation: ", res)
    # deepTrans = DeepTranslator()
    # deepTrans.start_translate("keep it up, you are awesome")
