from os import environ

from google.cloud import translate

project_id = environ.get("PROJECT_ID", "infra-devops-experiments")
assert project_id
parent = f"projects/{project_id}"
client = translate.TranslationServiceClient()

sample_text = "if you are good at something, never do it for free"
target_language_code = "hi"

response = client.translate_text(
    contents=[sample_text],
    target_language_code=target_language_code,
    parent=parent,
)

for translation in response.translations:
    print(translation.translated_text)