# This is the brain of Smart File Organizer
# It reads the rules from rules.yml and moves files into the right folders

from pathlib import Path
import yaml
import shutil
import logging

def load_rules(config_path: str) -> dict:
    """Opens the rules.yml file and returns the rules as a dictionary."""
    with open(config_path, "r") as f:
        rules = yaml.safe_load(f)
    return rules["folders"]
    
def get_destination(filename: str, rules: dict) -> str:
    """Look at a file's extension and return which folder it belongs to."""
    suffix = Path(filename).suffix.lower()
    for folder_name, extensions in rules.items():
        if suffix in extensions:
            return folder_name
    return "Others"

    def organize_folder(folder_path: str, config_path: str, dry_run: bool = False):
        """Go through every file in the folder and move it to the right subfolder."""

        rules = load_rules(config_path)
        folder = Path(folder_path)

        for file in folder.iterdir():
            if file.is_file():
                destination_name = get_destination(file.name, rules)
                destination_folder = folder / destination_name
                destination_folder.mkdir(exist_ok=True)

                if dry_run:
                    print(f"[DRY RUN] Would move: {file.name} -> {destination_name}/")
                    else:
                        shutil.move(str(file), str(destination_folder / file.name))
                        print(f"Moved: {file.name} -> {destination_name}/")