def transcribe_model_selection_gcs(gcs_uri, model):
    """Transcribe the given audio file asynchronously with
    the selected model."""
    from google.cloud import speech

    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri=gcs_uri)

    config = speech.RecognitionConfig(
        
        sample_rate_hertz=44100,
        language_code="en-US",
        model=model,
        audio_channel_count=2,
        
    )

    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=1000000)

    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        print("-" * 20)
        print("First alternative of result {}".format(i))
        print(u"Transcript: {}".format(alternative.transcript))
        
def main():
    transcribe_model_selection_gcs("gs://transcribe-poc-saurabh/1houraudio", "default")
    
if __name__ == "__main__":
    main()