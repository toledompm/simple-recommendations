def slugify(text):
    return text.lower().strip().replace(" ", "-")


def unslugify(slugified_text):
    return pretify(slugified_text.replace("-", " "))


def pretify(text):
    return text.strip().title()
