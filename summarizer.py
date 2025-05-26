from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text: str, mode: str = "short") -> str:
    if mode == "short":
        max_length = 60
        min_length = 20
    elif mode == "detailed":
        max_length = 120
        min_length = 40
    else:  # bullet
        max_length = 80
        min_length = 30

    if len(text) > 1024:
        text = text[:1024]

    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)

    return summary[0]["summary_text"]
