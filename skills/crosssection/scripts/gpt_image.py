"""
Generowanie obrazka przez OpenAI gpt-image dla komend /xray, /explodedview, /blueprint,
/anatomy, /360view, /crosssection, /knolling.

Ze zdjeciem wejsciowym  -> images.edit   (model przerabia TWOJ produkt)
Bez zdjecia             -> images.generate (model wymysla produkt z opisu)

Klucz API (kolejnosc):
  1. zmienna srodowiskowa OPENAI_API_KEY
  2. plik .env z linia OPENAI_API_KEY=sk-... w: biezacym folderze, ~/.claude/, folderze skilla
Opcjonalnie: GPT_IMAGE_MODEL (domyslnie gpt-image-2), GPT_IMAGE_QUALITY (low|medium|high).

Uzycie:
  python gpt_image.py --check
  python gpt_image.py --prompt-file prompt.txt --out obrazki/xray/wynik.png [--input zdjecie.jpg]
                      [--size 1536x1024] [--quality high] [--model gpt-image-2]
"""
import argparse
import base64
import os
import pathlib
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_MODEL = "gpt-image-2"
DEFAULT_QUALITY = "high"
SIZES = ("1024x1024", "1536x1024", "1024x1536", "auto")


def _load_env():
    for base in (pathlib.Path.cwd(), pathlib.Path.home() / ".claude", ROOT):
        env = base / ".env"
        if not env.is_file():
            continue
        for line in env.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def _check():
    """Mowi, czy da sie generowac. Kod wyjscia 0 = tak, 2 = nie (wtedy tryb promptu)."""
    problems = []
    try:
        import openai  # noqa: F401
    except ImportError:
        problems.append("brak biblioteki openai -> pip install openai")
    if not os.environ.get("OPENAI_API_KEY"):
        problems.append("brak OPENAI_API_KEY (zmienna srodowiskowa albo plik ~/.claude/.env)")
    if problems:
        print("TRYB PROMPTU: " + "; ".join(problems))
        sys.exit(2)
    print("OK: mozna generowac")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="sprawdz klucz i biblioteke")
    ap.add_argument("--prompt")
    ap.add_argument("--prompt-file")
    ap.add_argument("--input", action="append", default=[], help="zdjecie wejsciowe (mozna kilka)")
    ap.add_argument("--out")
    ap.add_argument("--size", default="1536x1024", choices=SIZES)
    ap.add_argument("--quality", default=None, choices=("low", "medium", "high"))
    ap.add_argument("--model", default=None)
    args = ap.parse_args()

    _load_env()
    if args.check:
        _check()
        return
    if not (args.prompt or args.prompt_file) or not args.out:
        ap.error("podaj --prompt albo --prompt-file oraz --out")
    if not os.environ.get("OPENAI_API_KEY"):
        sys.exit("[blad] brak OPENAI_API_KEY. Dodaj go do ~/.claude/.env albo ustaw zmienna srodowiskowa.")
    try:
        from openai import OpenAI
    except ImportError:
        sys.exit("[blad] brak biblioteki openai. Zainstaluj: pip install openai")

    prompt = args.prompt or pathlib.Path(args.prompt_file).read_text(encoding="utf-8")
    model = args.model or os.environ.get("GPT_IMAGE_MODEL") or DEFAULT_MODEL
    quality = args.quality or os.environ.get("GPT_IMAGE_QUALITY") or DEFAULT_QUALITY
    client = OpenAI(timeout=600)

    mode = "edit" if args.input else "generate"
    print(f"[1/2] {mode}  model={model}  size={args.size}  quality={quality}  (to trwa 1-2 minuty)")
    t0 = time.time()
    common = dict(model=model, prompt=prompt, size=args.size, quality=quality)
    if args.input:
        files = [open(p, "rb") for p in args.input]
        try:
            res = client.images.edit(image=files if len(files) > 1 else files[0], **common)
        finally:
            for f in files:
                f.close()
    else:
        res = client.images.generate(**common)

    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(base64.b64decode(res.data[0].b64_json))
    # prompt obok obrazka, zeby dalo sie odtworzyc i poprawic wynik
    out.with_suffix(".prompt.txt").write_text(prompt, encoding="utf-8")
    print(f"[2/2] gotowe w {time.time() - t0:.0f} s")
    print(out.resolve())


if __name__ == "__main__":
    main()
