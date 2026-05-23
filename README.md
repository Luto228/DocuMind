<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-blueviolet?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/API-Gemini-orange?style=for-the-badge" alt="Gemini API">
  <img src="https://img.shields.io/badge/Made%20with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Made%20with-Love-red?style=for-the-badge&logo=heart&logoColor=white" alt="Made with love">
</p>

# DocuMind

DocuMind is a local CLI assistant for managing your personal notes. It copies files into a local `docs` folder, stores their content in SQLite, and now supports asking questions to Gemini using your saved documents.

## ✨ What is already available

### 1. `Docu add`

Use:

```bash
Docu add my_notes.txt
Docu add my_notes.txt /path/to/folder
```

What it does:
- Finds the file on your Desktop by default
- Supports a custom path
- Copies the file into the project `docs` folder
- Saves the text into the local SQLite database

### 2. `Docu ask`

Use:

```bash
Docu ask my_notes.txt "What did I write about Python?"
```

What it does:
- Reads the saved document from SQLite
- Sends the file content and your question to Gemini
- Returns a short answer based on your note

> The `ask` command uses `google.generativeai` and `python-dotenv`.

## 📦 Installation

Install the required packages:

```bash
pip install google-generativeai python-dotenv
```

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

> [!TIP]
> Keep your API key in `.env` and never commit it to Git.

## 🚀 Quick start

```bash
python main.py add example.txt
python main.py ask example.txt "What is this file about?"
```

## 🛠️ Project structure

- `main.py` — CLI entry point
- `functions/add.py` — file import logic
- `functions/ask.py` — question routing
- `core/ai_brain.py` — Gemini integration
- `db_services/db_text.py` — SQLite storage
- `docs/` — copied notes
- `test.py` — experimental Gemini test script

## 🧭 Current status

- `add` — implemented
- `ask` — implemented
- `Docu list` — planned for the next update
- `Docu delete` — planned for the next update

## 🔮 What will be added next

- `Docu list` — show which files are already added
- `Docu delete` — remove documents that are no longer needed
- Better search/output formatting for commands and answers

> [!TIP]
> In the next update, the CLI will become even more convenient for managing your document library.

## 📌 Notes

- All notes are stored locally in SQLite
- Gemini answers are generated only from saved documents
- The project is designed for personal knowledge management, not for cloud sync

## 🤝 Contribution

If you want to help improve DocuMind, feel free to open an issue or pull request.