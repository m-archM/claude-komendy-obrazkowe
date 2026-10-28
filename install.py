"""
Instalator 7 komend obrazkowych dla Claude Code.

Kopiuje skille z folderu skills/ do ~/.claude/skills/ i sprawdza, czy da sie generowac obrazki
(biblioteka openai + klucz OPENAI_API_KEY). Niczego nie wysyla do sieci.

Uzycie:
  python install.py                 # instalacja do ~/.claude/skills/
  python install.py --target <dir>  # instalacja do innego folderu skilli (np. projektu: .claude/skills)
"""
import argparse
import os
import pathlib
import shutil
import sys
import time

REPO = pathlib.Path(__file__).resolve().parent
SKILLS = ["xray", "explodedview", "blueprint", "anatomy", "360view", "crosssection", "knolling"]


def _key_found():
    if os.environ.get("OPENAI_API_KEY"):
        return "zmienna srodowiskowa OPENAI_API_KEY"
    for base in (pathlib.Path.cwd(), pathlib.Path.home() / ".claude"):
        env = base / ".env"
        if env.is_file() and any(
            line.strip().startswith("OPENAI_API_KEY=") and len(line.split("=", 1)[1].strip()) > 10
            for line in env.read_text(encoding="utf-8").splitlines()
        ):
            return str(env)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", default=str(pathlib.Path.home() / ".claude" / "skills"))
    args = ap.parse_args()

    target = pathlib.Path(args.target).expanduser()
    target.mkdir(parents=True, exist_ok=True)
    # kopie zapasowe poza folderem skilli, zeby Claude nie wczytal starych wersji jako duplikatow
    backup_root = target.parent / "skills-backup" / time.strftime("%Y%m%d-%H%M%S")

    print(f"Instaluje do: {target}")
    for name in SKILLS:
        src = REPO / "skills" / name
        dst = target / name
        if dst.exists():
            backup_root.mkdir(parents=True, exist_ok=True)
            shutil.move(str(dst), str(backup_root / name))
            print(f"  {name}: stara wersja przeniesiona do {backup_root / name}")
        shutil.copytree(src, dst)
        print(f"  /{name}  OK")

    print()
    try:
        import openai  # noqa: F401
        lib = True
    except ImportError:
        lib = False
    key = _key_found()

    if lib and key:
        print(f"Generowanie obrazkow: GOTOWE (klucz: {key}).")
    else:
        print("Generowanie obrazkow: jeszcze nie. Komendy dzialaja w TRYBIE PROMPTU (oddaja prompt do ChatGPT).")
        if not lib:
            print("  - brak biblioteki openai -> pip install openai")
        if not key:
            print("  - brak klucza -> utworz plik ~/.claude/.env z linia OPENAI_API_KEY=sk-... (klucz z platform.openai.com)")
    print("\nUruchom Claude Code od nowa i wpisz na przyklad /xray")
    return 0


if __name__ == "__main__":
    sys.exit(main())
