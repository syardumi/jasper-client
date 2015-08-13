# -*- coding: utf-8-*-
import re

WORDS = ["YOU", "WHO"]


def handle(text, mic, profile):
    """
        Reports the current time based on the user's timezone.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """

    mic.say("I'm Aubrey. I currently am keeper of the house lights, but I'm always learning new tricks too. Just ask.")


def isValid(text):
    """
        Returns True if input is related to who Jasper is.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\byou\b', text, re.IGNORECASE)) and any(word in text.upper() for word in ["WHO", "WHAT"])
