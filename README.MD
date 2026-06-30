# AI Document Summarizer & Q&A

A Generative AI web app that lets you upload a PDF and either summarize it or ask specific questions about its content — powered by OpenAI's GPT-4o-mini.

## What it does
- Upload any PDF document
- Get a concise 2-sentence summary
- Ask specific questions and get answers grounded strictly in the document (no hallucination)

## Tech stack
- Python 3.13
- OpenAI API (gpt-4o-mini)
- Streamlit (UI)
- PyPDF2 (PDF text extraction)
- python-dotenv (secret management)

## How to run locally

1. Clone the repo
2. Create a virtual environment and activate it
3. Install dependencies
4. Add your OpenAI API key to a `.env` file
5. Run the app

\```bash
git clone https://github.com/suvrojitmoy2009/genai-project-1-summarizer.git
cd genai-project-1-summarizer
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
echo OPENAI_API_KEY=your-key-here > .env
streamlit run app.py
\```

## Key engineering decisions
- Used `gpt-4o-mini` for cost efficiency (~$0.00003 per request)
- Input validation before API calls to prevent unnecessary charges
- Grounded Q&A — model is explicitly instructed to only use provided context, preventing hallucination
- Specific error handling for rate limits, oversized inputs, and unexpected failures
- Secrets managed via `.env` file, never committed to version control

## What I learned
- OpenAI API — prompting, tokens, context windows, cost awareness
- Grounding techniques to prevent hallucination
- Error handling patterns for production-ready AI apps
- PDF text extraction with PyPDF2
- Building interactive AI apps with Streamlit