"""Top-level package for Deep Translator"""
import sys
import os

runFileUrl = os.path.dirname(sys.path[0])
print(f'runFileUrl= {runFileUrl}')

sys.path.append('/Users/apple/Qsync/gitNew/PythonProjects/PythonLib/ai_lib_ls/pylib/text_transalte/deep_translator')

from googleutil import GoogleTranslator
from deepl import DeeplTranslator
from detection import batch_detection, single_detection

from libre import LibreTranslator
from linguee import LingueeTranslator
from microsoft import MicrosoftTranslator
from mymemory import MyMemoryTranslator
from papago import PapagoTranslator
from pons import PonsTranslator
from qcri import QcriTranslator
from yandex import YandexTranslator

__author__ = """Nidhal Baccouri"""
__email__ = "nidhalbacc@gmail.com"
__version__ = "1.8.0"

__all__ = [
    "GoogleTranslator",
    "PonsTranslator",
    "LingueeTranslator",
    "MyMemoryTranslator",
    "YandexTranslator",
    "MicrosoftTranslator",
    "QcriTranslator",
    "DeeplTranslator",
    "LibreTranslator",
    "PapagoTranslator",
    "single_detection",
    "batch_detection",
]
