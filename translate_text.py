from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from gtts import gTTS
import os

asr = pipeline("automatic-speech-recognition", model="openai/whisper-small")

model_name = "facebook/nllb-200-distilled-600M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

languages = {
    "Telugu": ("tel_Telu", "te"),
    "Hindi": ("hin_Deva", "hi"),
    "Tamil": ("tam_Taml", "ta"),
    "French": ("fra_Latn", "fr"),
    "English": ("eng_Latn", "en"),
    "Japanese": ("jpn_Jpan", "ja"),
    "Korean": ("kor_Hang", "ko")

}

def translate_audio(target_language):

    if not os.path.exists("speech.wav"):
        raise FileNotFoundError("speech.wav not found. Please record or upload audio.")

    nllb_code, gtts_code = languages[target_language]

    result = asr("speech.wav")
    recognized_text = result["text"]

    inputs = tokenizer(recognized_text, return_tensors="pt")

    translated_tokens = model.generate(
        **inputs,
        forced_bos_token_id=tokenizer.convert_tokens_to_ids(nllb_code)
    )

    translated_text = tokenizer.batch_decode(
        translated_tokens,
        skip_special_tokens=True
    )[0]

    tts = gTTS(text=translated_text, lang=gtts_code)
    tts.save("translated_audio.wav")

    return recognized_text, translated_text