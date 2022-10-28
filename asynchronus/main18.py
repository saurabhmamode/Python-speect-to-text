from os import environ

from google.cloud import translate

project_id = environ.get("PROJECT_ID", "infra-devops-experiments")
assert project_id
parent = f"projects/{project_id}"
client = translate.TranslationServiceClient()


def detect_language(text):
    response = client.detect_language(parent=parent, content=text)

    for languages in response.languages:
        confidence = languages.confidence
        language_code = languages.language_code
        print(
            f"Confidence: {confidence:6.1%}",
            f"Language: {language_code}",
            text,
            sep=" | ",
        )


sentences = (
    "Hola Mundo!",
    "Hallo Welt!",
    "Bonjour le Monde !",
)
for sentence in sentences:
    detect_language(sentence)
    