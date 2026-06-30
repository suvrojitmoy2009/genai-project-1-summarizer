import os
import PyPDF2
from openai import OpenAI
from openai import RateLimitError, APIError
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MAX_CHARS_GPT4O_MINI = 700000

def extract_text_from_pdf(filepath):
    """
    Extracts all text from a PDF file given its filepath.
    """
    try:
        with open(filepath, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        return f"Error: Could not read PDF - {e}"

def summarize_text(text, model="gpt-4o-mini"):
    """
    Takes a piece of text and returns a 2-sentence summary using OpenAI's API.
    """
    if len(text) > MAX_CHARS_GPT4O_MINI:
        return f"Error: Input text is too large ({len(text)} characters). Max allowed is {MAX_CHARS_GPT4O_MINI}."
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": f"Summarize this in 2 sentences: {text}"}
            ]
        )
        return response.choices[0].message.content
    except RateLimitError:
        return "Error: Rate limit exceeded. Try again in a moment, or reduce input size."
    except APIError as e:
        if "Request too large" in str(e):
            return "Error: API issue - Request too large. Please reduce the input text size."
        return f"Error: API issue - {e}"
    except Exception as e:
        return f"Error: Unexpected issue - {e}"

def answer_question(text, question, model="gpt-4o-mini"):
    """
    Takes a piece of text and a question, returns an answer based only on that text.
    """
    if len(text) > MAX_CHARS_GPT4O_MINI:
        return f"Error: Input text is too large ({len(text)} characters). Max allowed is {MAX_CHARS_GPT4O_MINI}."
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": f"Based only on the following text, answer the question. If the answer isn't in the text, say so.\n\nText: {text}\n\nQuestion: {question}"}
            ]
        )
        return response.choices[0].message.content
    except RateLimitError:
        return "Error: Rate limit exceeded. Try again in a moment, or reduce input size."
    except APIError as e:
        return f"Error: API issue - {e}"
    except Exception as e:
        return f"Error: Unexpected issue - {e}"