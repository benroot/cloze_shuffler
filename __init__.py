# import the main window object (mw) from aqt
# import anki.template
#
# from aqt import mw
# # import the "show info" tool from utils.py
# from aqt.utils import showInfo, qconnect
# # import the Qt GUI library
# from aqt.qt import *
#
import random
import re


def shuffle_cloze(match_object):
    if match_object.group() is not None:
        cloze_options = [item.replace("&nbsp;", " ").strip() for item in match_object.group(2).split("/")]
        # print(cloze_options)
        shuffled_options = " / ".join(random.sample(cloze_options, len(cloze_options)))
        # print(shuffled_options)
        return match_object.group(1) + shuffled_options + match_object.group(3)


def cloze_shuffler_hook(html, card, context):
    result_string = re.sub(r"(<span class=\"?cloze\"?>\[)(.*?)(\]</span>)", shuffle_cloze, html)
    return result_string


from aqt import gui_hooks

gui_hooks.card_will_show.append(cloze_shuffler_hook)
# f = open("sample-card.html")
# text = f.read()
# f.close()
# cloze_shuffler_hook(text, None, None)
