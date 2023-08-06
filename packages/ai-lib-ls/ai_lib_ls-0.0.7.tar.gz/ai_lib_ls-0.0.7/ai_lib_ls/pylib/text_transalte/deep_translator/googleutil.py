"""
google translator API
"""
import time
from typing import List, Optional

import requests
from bs4 import BeautifulSoup

from base import BaseTranslator
from constants import BASE_URLS
from exceptions import (
    RequestError,
    TooManyRequests,
    TranslationNotFound,
)
from validate import is_empty, is_input_valid


class GoogleTranslator(BaseTranslator):
    """
    class that wraps functions, which use Google Translate under the hood to translate text(s)
    """

    def __init__(
            self,
            source: str = "auto",
            target: str = "zh-CN",
            proxies: Optional[dict] = None,
            **kwargs
    ):
        """
        @param source: source language to translate from
        @param target: target language to translate to
        """
        self.proxies = proxies
        super().__init__(
            base_url=BASE_URLS.get("GOOGLE_TRANSLATE"),
            source=source,
            target=target,
            element_tag="div",
            element_query={"class": "t0"},
            payload_key="q",  # key of text in the url
            **kwargs
        )

        self._alt_element_query = {"class": "result-container"}

    def translate(self, text: str, **kwargs) -> str:
        """
        function to translate a text
        @param text: desired text to translate
        @return: str: translated text
        """
        if is_input_valid(text):
            text = text.strip()
            if self._same_source_target() or is_empty(text):
                return text
            self._url_params["tl"] = self._target
            self._url_params["sl"] = self._source

            if self.payload_key:
                self._url_params[self.payload_key] = text

            response = requests.get(
                self._base_url, params=self._url_params, proxies=self.proxies
            )
            if response.status_code == 429:
                raise TooManyRequests()

            if response.status_code != 200:
                raise RequestError()

            soup = BeautifulSoup(response.text, "html.parser")

            element = soup.find(self._element_tag, self._element_query)

            if not element:
                element = soup.find(self._element_tag, self._alt_element_query)
                if not element:
                    raise TranslationNotFound(text)
            if element.get_text(strip=True) == text.strip():
                to_translate_alpha = "".join(ch for ch in text.strip() if ch.isalnum())
                translated_alpha = "".join(
                    ch for ch in element.get_text(strip=True) if ch.isalnum()
                )
                if (
                        to_translate_alpha
                        and translated_alpha
                        and to_translate_alpha == translated_alpha
                ):
                    self._url_params["tl"] = self._target
                    if "hl" not in self._url_params:
                        return text.strip()
                    del self._url_params["hl"]
                    return self.translate(text)

            else:
                return element.get_text(strip=True)

    def translate_file(self, path: str, **kwargs) -> str:
        """
        translate directly from file
        @param path: path to the target file
        @type path: str
        @param kwargs: additional args
        @return: str
        """
        return self._translate_file(path, **kwargs)

    def translate_batch(self, batch: List[str], **kwargs) -> List[str]:
        """
        translate a list of texts
        @param batch: list of texts you want to translate
        @return: list of translations
        """
        return self._translate_batch(batch, **kwargs)


if __name__ == "__main__":
    onetime = time.time()

    trans = GoogleTranslator()

    res = trans.translate(
            'This summer, the anesthesiology department at the Cooperman Barnabas Medical Center in Livingston, New Jersey, was in crisis. For months, the outside staffing company overseeing the department had slashed staff to what the 600-bed hospital leaders considered dangerous levels. In the first six months of 2022, hospital officials recorded 286 adverse events that resulted from chronic understaffing, according to a lawsuit. Trying to avert a catastrophe, hospital officials called a meeting on June 25 with the anesthesiology department and its chief, Joel M. Braverman. After learning that he’d attended the meeting, the staffing company that employed Braverman — North American Partners in Anesthesia — placed him on administrative leave, the lawsuit said, and directed him to leave the hospital immediately, even though he was on call and the anesthesiology department was short staffed. The next day, North American Partners in Anesthesia, also known as NAPA, fired Braverman, the lawsuit said. The nonprofit, acute care hospital then formed a new anesthesiology department of its own, hiring the clinicians who had previously worked for NAPA, and, in July, filed a lawsuit against NAPA. The company’s severe understaffing put its own profits ahead of the hospital’s patients, Cooperman Barnabas alleged, adding that the company’s “entire business structure should be scrutinized, because New Jersey laws and regulations preclude corporations from exercising clinical control over health care decisions.” NAPA’s practices have drawn complaints and generated litigation from other hospitals in recent years. This spring, for example, Renown Regional Medical Center in Reno, Nevada, broke its contract with NAPA, saying it had severely understaffed the facility and put patients at risk. Cooperman Barnabas Medical Center In late June, Cooperman Barnabas Medical Center in New Jersey formed a new anesthesiology department of its own.Cooperman Barnabas Medical Center North American Partners in Anesthesia is the nation’s largest anesthesia staffing company, employing 6,000 clinicians at 500 facilities in 21 states. The company is owned by two well-heeled private-equity firms, American Securities of New York City and Leonard Green & Partners in Los Angeles. Four of NAPA’s nine directors are private-equity executives. Private-equity firms invest in companies and aim to sell them in about five years for more than they paid. In recent years they’ve snapped up health care companies, with a particular interest in anesthesiology. But some physicians and patient advocates say the health care investments of private-equity firms and their drive to reap relatively short-term profits are inconsistent with putting patients first. Independent academic studies find that private equity’s laser focus on profits in health care operations can result in lower staffing levels at hospitals and nursing homes. A spokesperson for NAPA declined to comment on its disputes with the New Jersey and Nevada hospitals, citing ongoing litigation. In a countersuit against Cooperman Barnabas and the clinicians who went to work for the hospital, NAPA said Cooperman Barnabas “pirated” its employees and the clinicians breached their duties to the company, causing “irreparable harm to its business.” NAPA is focused on elevating the standard of patient care in the communities it serves, its spokesman said in a statement. “NAPA’s enterprise-wide culture of safety and its clinician focus has resulted in a 94 percent clinician retention rate, the industry lowest vacancy rate, a 98 percent surgeon satisfaction rate, and a 4.84/5 rating in patient satisfaction,” the spokesman added. “Reflecting its culture of safety and commitment to quality of care above all else, NAPA created the NAPA Anesthesia Patient Safety Institute, one of only 100 federally listed Patient Safety Organizations.” Michael E. Knecht, spokesman for RWJBarnabas Health, declined to comment on its dispute with NAPA, and Braverman did not return a phone call seeking comment. In a statement, however, Knecht said, “As a statewide leader in adult and pediatric surgery, the volume of patients we see daily necessitates the immediate availability of skilled anesthesiologists and certified registered nurse anesthetists to provide care. While litigation is never desirable, our actions continue to be driven by what is in the best interests of patient care.” Market power Over the past decade, private-equity firms have bought up physician practices in anesthesiology, emergency medicine and dermatology, research shows. A study of private-equity buyouts of physician practices published in JAMA Network in February 2020 found that anesthesiology practices were the focus of almost 20% of those buyouts, the highest percentage of deals involving a single specialty. Emergency medicine practices accounted for 12% of the takeovers.')
    print(res)

    twotime = time.time() - onetime

    print(twotime, onetime)

    print("translation: ", res)
