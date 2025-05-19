def translate_to_pidgin(text, tone="default"):
    translations = {
        "default": {
            "You should save more.": "Try dey save small-small.",
            "Great job keeping your expenses low.": "You try wella!",
            "You're spending too much on transport.": "You dey chop transport money like gala!"
        }
    }
    return translations.get(tone, {}).get(text, text)
