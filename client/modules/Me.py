# -*- coding: utf-8-*-
import re

WORDS = ["YOU", "WHO", "WHAT", "HI", "HELLO"]

PRIORITY = 40

def handle(text, mic, profile):
    """
        Reports the current time based on the user's timezone.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """

    mic.say("Hi, I'm Aubrey. I currently am keeper of the house lights, but I'm always learning new tricks too. Just ask.")


def isValid(text):
    """
        Returns True if input is related to who Jasper is.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\A(who|what) are you\Z', text, re.IGNORECASE)) or bool(re.search(r'\Ayou are (who|whom|what)\Z', text, re.IGNORECASE)) or bool(re.search(r'\b(hi|hello)\b', text, re.IGNORECASE))
