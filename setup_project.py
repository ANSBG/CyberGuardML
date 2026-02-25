from pathlib import Path

folders = [
    "data/raw/cicids2017",
    "data/raw/simulated",
    "data/processed",
    "notebooks",
    "src",
    "app",
    "reports",
]
for f in folders:
    Path(f).mkdir(parents=True, exist_ok=True)

print("✅ Project folders created.")