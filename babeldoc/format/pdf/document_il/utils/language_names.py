"""Human-readable language names for LLM prompts (PDFidelity).

BabelDOC prompts used the raw ``lang_out`` code ("translate into hi"). Some codes
are ambiguous for the model and produced untranslated or English "translations".
"""

LANGUAGE_DISPLAY_NAMES = {
    "en": "English",
    "es": "Spanish",
    "pt": "Portuguese",
    "pt-br": "Brazilian Portuguese",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "id": "Indonesian",
    "zh": "Simplified Chinese",
    "zh-cn": "Simplified Chinese",
    "zh-tw": "Traditional Chinese (Taiwan)",
    "zh-hk": "Traditional Chinese (Hong Kong)",
    "ja": "Japanese",
    "ko": "Korean",
    "ko-kr": "Korean",
    "ar": "Modern Standard Arabic",
    "hi": "Hindi (Devanagari script)",
    "bn": "Bengali (Bangla script)",
    "ru": "Russian",
    "tr": "Turkish",
    "vi": "Vietnamese",
}


def language_display_name(code: str | None) -> str:
    """Return e.g. "Hindi (Devanagari script) (hi)"; unknown codes are returned as is."""
    if not code:
        return ""
    name = LANGUAGE_DISPLAY_NAMES.get(code.lower())
    return f"{name} ({code})" if name else code
