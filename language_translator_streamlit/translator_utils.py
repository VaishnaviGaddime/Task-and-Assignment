from deep_translator import GoogleTranslator


LANGUAGES = {
    "Auto Detect": "auto",
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Bengali": "bn",
    "Punjabi": "pa",
    "Urdu": "ur",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Arabic": "ar",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese Simplified": "zh-CN",
    "Russian": "ru"
}


def translate_text(text: str, source_language: str, target_language: str) -> str:
    """
    Translate text from source language to target language.

    Args:
        text: Input text to translate.
        source_language: Source language code, for example "en" or "auto".
        target_language: Target language code, for example "hi".

    Returns:
        Translated text.
    """
    if not text or not text.strip():
        raise ValueError("Please enter some text to translate.")

    if source_language == target_language:
        return text

    translated = GoogleTranslator(
        source=source_language,
        target=target_language
    ).translate(text)

    return translated


def get_language_code(language_name: str) -> str:
    """
    Convert language display name into language code.
    """
    return LANGUAGES.get(language_name, "en")
