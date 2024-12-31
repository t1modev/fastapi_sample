import os
import importlib
import re
from typing import Dict

locales: Dict[str, Dict] = {}

def load_locales():
    global locales
    current_dir = os.path.dirname(__file__)
    for filename in os.listdir(current_dir):
        if filename.endswith(".py") and filename not in ("__init__.py", "localization.py"):
            lang_code = filename.split(".")[0]
            module = importlib.import_module(f"app.locales.{lang_code}")
            if hasattr(module, "messages"):
                locales[lang_code] = module.messages

load_locales()

def get_text(key: str, lang: str = "en", **kwargs) -> str:
    if lang not in locales:
        lang = "en"

    messages = locales.get(lang, {})
    keys = key.split(".")
    value = messages

    for k in keys:
        value = value.get(k)
        if value is None:
            value = locales["en"]
            for fallback_key in keys:
                value = value.get(fallback_key)
                if value is None:
                    raise ValueError(f"Localization key '{key}' not found.")
            break

    if kwargs:
        try:
            value = value.format(**kwargs)
        except KeyError as e:
            raise ValueError(f"Missing argument {e} for key '{key}'.")

    return value


def get_texts(lang: str = None, key: str = None) -> dict:
   
    english_messages = locales.get("en", {})

    if lang is None:
        if key:
            return {
                locale: find_by_key_with_fallback(messages, english_messages, key)
                for locale, messages in locales.items()
            }
        return {
            locale: merge_with_fallback(messages, english_messages)
            for locale, messages in locales.items()
        }

    messages = locales.get(lang, {})
    if key:
        return {lang: find_by_key_with_fallback(messages, english_messages, key)}

    return {lang: merge_with_fallback(messages, english_messages)}


def merge_with_fallback(messages: dict, fallback: dict) -> dict:
    merged = fallback.copy()
    for key, value in messages.items():
        if isinstance(value, dict):
            merged[key] = merge_with_fallback(value, fallback.get(key, {}))
        else:
            merged[key] = value
    return merged


def find_by_key_with_fallback(messages: dict, fallback: dict, key: str) -> str:
    keys = key.split(".")
    value = messages
    fallback_value = fallback
    for k in keys:
        value = value.get(k, {})
        fallback_value = fallback_value.get(k, {})
    return value if value else fallback_value


