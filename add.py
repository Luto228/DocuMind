import sys
import shutil
from pathlib import Path

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
    DocuMind_docs_path = Path("./docs")
    DocuMind_docs_path.mkdir(exist_ok = True)
    final_file_path = DocuMind_docs_path / currently_file_name
    shutil.copy(file_path, final_file_path)
    print(f"✅file {currently_file_name} file has been created in docs✅")

def distributor_handle(words):
    lwords = len(words)
    if lwords < 1 or lwords >= 3:
        print("\n--- Project DocuMind ---")
        print("Usage: Docu add <file_name> OR <file_name> <file_path>")
        print("\nSetup: alias Docu='/your_path/main.py' in .bashrc")
        sys.exit(1)
    elif lwords == 1:
        handle_add(words[0])
    elif lwords == 2:
        handle_add(words[0], words[1])