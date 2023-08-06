# -*- coding: utf-8 -*-

"""
Text cleaning and preprocessing functions.
"""

import string
import re
from typing import List
from textarium.extraction import extract_tokens

def remove_extra_spaces(text: str) -> str:
    """Removes extra spaces from a string

    Args:
        text (str): Any string

    Returns:
        str: A string without extra spaces (maximum 1 space between two words)

    Examples:
        >>> remove_extra_spaces("  This line    has extra   spaces   .  ")
        "This line has extra spaces."
    """
    text_wo_extra_spaces = " ".join(text.split())

    return text_wo_extra_spaces.strip()

def remove_charset(text: str, charset: string) -> str:
    """Removes provided chars from a string

    Args:
        text (str): Any string
        charset (str): A string of chars which should be removed

    Returns:
        str: A string without provided chars
    """
    text_wo_charset = text.translate(
        str.maketrans(charset, " " * len(charset))
    )
    text_wo_charset = remove_extra_spaces(text_wo_charset)

    return text_wo_charset

def remove_html(text: str) -> str:
    """Removes HTML-tags and other special symbols from a string

    Args:
        text (str): Any string

    Returns:
        str: A string without HTML-tags
    """
    re_pattern = re.compile("<.*?>+")
    text = re_pattern.sub(r" ", text)
    text = text.replace("&nbsp", " ")
    text = text.replace("&lt", " ")
    text = text.replace("&gt", " ")
    text_wo_html_tags = remove_extra_spaces(text)
    return text_wo_html_tags

def remove_urls(text: str):
    """Removes URLs from a string

    Args:
        text (str): Any string

    Returns:
        str: A string without any URLs
    """
    url_pattern = re.compile(r"http\S+")
    text_wo_urls = url_pattern.sub(r"", text)
    text_wo_urls = remove_extra_spaces(text_wo_urls)
    return text_wo_urls

def remove_tokens(text: str, tokenizer, tokens_to_exclude: List) -> str:
    """Remove any particular words from a string (e.g. stopwords)

    Args:
        text (str): Any string
        tokenizer (Tokenizer): A tokenizer object with a provided `.tokenize()` method
        tokens_to_exclude (List): A list of tokens to exclude from a string

    Returns:
        str: A string without excluded tokens
    """
    tokens = extract_tokens(text, tokenizer)
    cleaned_tokens = [w for w in tokens if not w in tokens_to_exclude]
    return " ".join(cleaned_tokens)
