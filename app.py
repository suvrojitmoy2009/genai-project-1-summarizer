import streamlit as st
import tempfile
import os
from utils import extract_text_from_pdf, summarize_text, answer_question

st.title("AI Document Summarizer & Q&A")
st.write("Upload a PDF document, then choose to summarize it or ask a specific question about it.")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file is not None:
    # Save uploaded file temporarily so we can read it
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    # Extract text from PDF
    with st.spinner("Extracting text from PDF..."):
        text = extract_text_from_pdf(tmp_path)

    # Clean up temp file
    os.unlink(tmp_path)

    if text.startswith("Error"):
        st.error(text)
    else:
        st.success("PDF loaded successfully!")

        # Choose mode
        mode = st.radio("What would you like to do?", ["Summarize", "Ask a Question"])

        if mode == "Summarize":
            if st.button("Generate Summary"):
                with st.spinner("Summarizing..."):
                    summary = summarize_text(text)
                st.subheader("Summary")
                st.write(summary)

        elif mode == "Ask a Question":
            question = st.text_input("Enter your question about the document:")
            if st.button("Get Answer"):
                if question.strip() == "":
                    st.warning("Please enter a question first.")
                else:
                    with st.spinner("Finding answer..."):
                        answer = answer_question(text, question)
                    st.subheader("Answer")
                    st.write(answer)