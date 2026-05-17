<p align="center">
  <img src="https://img.shields.io/badge/Status-Premium-blueviolet?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/API-Gemini-orange?style=for-the-badge" alt="Gemini API">
  <img src="https://img.shields.io/badge/Made%20with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Made%20with-Love-red?style=for-the-badge&logo=heart&logoColor=white" alt="Made with love">
</p>

# DocuMind

DocuMind is a local CLI assistant for working with your personal text notes. It helps automatically index files, store them in a SQLite database, and quickly find the right information by meaning.

## What works so far

### 1. `add`

Command: `DocuMind add file_name.txt`

What it does:
- Finds the file on the Desktop by default
- Supports a custom file path
- Copies the file into the project `docs` folder
- Reads the entire file text and saves it to SQLite

Why it matters:
- This is the indexing stage: knowledge is loaded into the bot's memory.

> Currently only part of the `add` functionality is implemented, but the rest will definitely be added.

## Planned features

### 2. `search`

Command: `DocuMind search "what did I write about configuring alias in bashrc?"`

What it will do:
- Search not only exact words, but documents by meaning
- Use SQLite to find relevant text
- Return the relevant pieces of information from your notes

### 3. AI conversation

What it will do:
- You ask a question about your documents
- The bot finds relevant passages in the database
- It creates a prompt for the neural model using the found text
- The model answers using only the content from your files

Why it matters:
- Everything stays local and under your control
- Your notes are neatly organized and searchable
- No need to open dozens of files to find one line of text

## Why DocuMind

- Local knowledge base on SQLite
- Meaning-based search, not just keyword matching
- LLM integration for smart answers
- Focused on making personal note storage easy

## Project structure

- `main.py` — entry point
- `add.py` — `add` command
- `test.py` — tests / experimental checks

## Status

- `add` — partially implemented
- `search` — in development
- AI integration — planned

## Contacts

If you want to help with development, feel free to open pull requests and share ideas!
