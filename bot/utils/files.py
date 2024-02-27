from pathlib import Path
from tomllib import load


BOT_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = BOT_DIR.parent
LOGS_DIR = ROOT_DIR / "logs"
BOT_CONFIG = ROOT_DIR / "config.toml"

with open(BOT_CONFIG, 'rb') as f:
    config = load(f)


if __name__ == "__main__":
    print(config)