import os import json import shutil

Paths

data_dir = os.path.join(os.path.dirname(file), 'data') crypto_main = os.path.join(data_dir, 'accounts_crypto.json') auto_crypto = os.path.join(data_dir, 'accounts_crypto_autogen.json')

youtube_main = os.path.join(data_dir, 'accounts_youtube.json') auto_youtube = os.path.join(data_dir, 'accounts_youtube_autogen.json')

Backup function

def backup(path): if os.path.exists(path): shutil.copy(path, path + '.bak') print(f"Backed up {path} -> {path}.bak")

Merge lists, dedupe by key

def merge_accounts(main_list, auto_list, key='username'): existing = {acc[key]: acc for acc in main_list} for acc in auto_list: if acc[key] not in existing: existing[acc[key]] = acc # preserve order: first existing then new merged = list(existing.values()) return merged

Load JSON helper

def load_json(path): if os.path.exists(path): with open(path, 'r') as f: return json.load(f) return []

def save_json(path, data): with open(path, 'w') as f: json.dump(data, f, indent=4, ensure_ascii=False) print(f"Saved {len(data)} accounts to {path}")

Process crypto accounts

auto_list = load_json(auto_crypto) if not auto_list: print(f"No autogen crypto file found at {auto_crypto}") else: main_list = load_json(crypto_main) backup(crypto_main) merged = merge_accounts(main_list, auto_list, key='username') save_json(crypto_main, merged)

Process YouTube accounts

auto_list_y = load_json(auto_youtube) if not auto_list_y: print(f"No autogen YouTube file found at {auto_youtube}") else: main_list_y = load_json(youtube_main) backup(youtube_main) merged_y = merge_accounts(main_list_y, auto_list_y, key='name') save_json(youtube_main, merged_y)

print("Auto-fix completed: accounts added to bot.")

