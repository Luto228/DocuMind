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
        print(f"⛔ERROR⛔ \n i cannt find {currently_file_name} file in {file_custom_path}")
        print(f"Please write correct name")
        return
    print(f"✅i found {currently_file_name} file in {file_custom_path}✅")
    DocuMind_docs_path = PROJECT_ROOT / "docs"
    DocuMind_docs_path.mkdir(parents=True, exist_ok=True)
    final_file_path = DocuMind_docs_path / currently_file_name
    shutil.copy(file_path, final_file_path)
    text_inside = final_file_path.read_text(encoding="utf-8")
    try:
        save_info(currently_file_name, text_inside)
        print(f"✅file {currently_file_name} file has been created in docs✅")
    except Exception as e:
        print(f"Sorry! Something went wrong! \n errors name: {e}")
