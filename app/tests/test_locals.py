import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from app.locales.localization import get_text, get_texts, find_by_key_with_fallback

text_en = get_text(key="header.second_text", lang="en", variable="value")
print(text_en)

text_uk = get_text("header.second_text", lang="uk", variable="значення")
print(text_uk)

full_texts = get_texts(lang="uk")
print(full_texts)

