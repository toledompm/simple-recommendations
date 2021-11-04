def slugify(text: str) -> str:
    return text.lower().strip().replace(" ", "-")


def unslugify(slugified_text: str) -> str:
    return pretify(slugified_text.replace("-", " "))


def pretify(text: str) -> str:
    return text.strip().title()
