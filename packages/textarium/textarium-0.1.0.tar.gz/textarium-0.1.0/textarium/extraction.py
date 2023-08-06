# -*- coding: utf-8 -*-

"""
Function for extracting information from texts.
"""

from typing import List

def extract_tokens(text: str, tokenizer) -> List[str]:
    """Extract tokens from a text

    Args:
        text (str): Any string
        tokenizer (_type_): A tokenizer object with a provided `.tokenize()` method

    Returns:
        List[str]: A list of extracted tokens
    """
    tokens = tokenizer.tokenize(text)
    return tokens
