import sys
import shutil
from pathlib import Path

from db_services.db_text import create, save_info

PROJECT_ROOT = Path(__file__).resolve().parent.parent

def handle_add(file_name: str, custom_path = None):
    home_dir = Path.home()
    if custom_path is None:
        custom_path = "Desktop"
        file_custom_path = home_dir / custom_path
    else:
        file_custom_path = Path(custom_path)
    currently_file_name = file_name
    file_path = file_custom_path / currently_file_name
    if not file_path.is_file():
        print(f"⛔ERROR⛔ I couldn't find {currently_file_name} in {file_custom_path}")
        print("Please write the correct file name.")
        return

    print(f"✅ I found {currently_file_name} in {file_custom_path} ✅")

    DocuMind_docs_path = PROJECT_ROOT / "docs"
    DocuMind_docs_path.mkdir(parents=True, exist_ok=True)
    final_file_path = DocuMind_docs_path / currently_file_name
    shutil.copy(file_path, final_file_path)
    text_inside = final_file_path.read_text(encoding="utf-8")

    try:
        save_info(currently_file_name, text_inside)
        print(f"✅ File {currently_file_name} has been added to docs ✅")
    except Exception as e:
        print(f"⛔ERROR⛔ Something went wrong!\nError name: {e}")