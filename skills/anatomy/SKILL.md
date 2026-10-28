---
name: anatomy
description: >-
  Komenda /anatomy. Plakat "ANATOMIA" produktu: z lewej duży tytuł, z prawej
  produkt rozsunięty na warstwy jak w infografice (baton, burger, ciastko,
  tort, kanapka, kosmetyk, buty), każda warstwa podpisana. Najlepiej działa na
  jedzeniu. Generuje obrazek przez OpenAI gpt-image, a bez klucza API oddaje
  gotowy prompt do ChatGPT. Używaj, gdy użytkownik wpisze "/anatomy",
  "anatomia", "anatomia produktu", "pokaż warstwy", "z czego to jest zrobione"
  albo wrzuci zdjęcie jedzenia czy produktu z taką prośbą.
---

# /anatomy

Wynik: plakat 1536×1024 w stylu magazynowym. Lewa tercja: duży tytuł "ANATOMIA", a pod nim nazwa produktu. Dwie prawe tercje: produkt rozsunięty pionowo na 4–7 warstw, każda z cienką linią i podpisem. Ciepłe, ciemne tło.

Różnica wobec /explodedview: tam technika (części urządzenia w rzędzie), tu „z czego to jest” (składniki, warstwy materiału) z plakatowym tytułem.

## Krok 0. Sprawdź, czy da się generować
Uruchom (na macOS i Linuksie `python3` zamiast `python`):
```
python "<katalog tego skilla>/scripts/gpt_image.py" --check
```
`<katalog tego skilla>` to folder, w którym leży ten plik SKILL.md.
- `OK` → tryb obrazka (kroki 1–5).
- `TRYB PROMPTU`, brak Pythona albo brak dostępu do sieci → kroki 1–3, a potem „Tryb promptu” na dole. Powiedz użytkownikowi jednym zdaniem, czego brakuje, i odeślij do sekcji „Klucz OpenAI” w README repozytorium https://github.com/m-archM/claude-komendy-obrazkowe
- Nigdy nie proś o wklejenie klucza API do czatu.

## Krok 1. Wejście
- Zdjęcie → tryb edycji (`--input`).
- Sama nazwa → generacja z opisu.
- Obejrzyj zdjęcie, zanim napiszesz prompt.

## Krok 2. Warstwy
Wypisz 4–7 prawdziwych warstw od góry do dołu, każdą z opisem wyglądu (kolor, faktura, grubość):
- baton: polewa czekoladowa, karmel, orzechy, nugat, wafel
- burger: bułka z sezamem, sos, sałata, ser, kotlet, spód bułki
- krem: zakrętka, pompka, pojemnik, formuła, składnik aktywny

Podpisy: 1–2 słowa, po polsku i z polskimi znakami. Tytuł "ANATOMIA" (po angielsku "ANATOMY").

## Krok 3. Prompt (po angielsku, do pliku .txt)
```
Create a single wide 3:2 editorial infographic poster on a warm dark charcoal (#1d1a17) background
with soft studio light.
Left third: a large bold condensed uppercase title "{TITLE}" in off-white, and directly below it
in smaller text "{NAME}".
Right two thirds: a photorealistic {OBJECT} separated into its layers, stacked vertically from top
to bottom with even gaps between layers, each layer floating with a soft shadow, all perfectly
aligned on the same vertical axis, in this exact order from top to bottom: {LAYERS}.
Each layer has a thin off-white leader line to a short label on the right side.
Use exactly these labels, spelled exactly like this, in this order: {LABELS}
(Polish words, keep every accented letter exactly as written).
No other text, no logos added. The whole composition fills the canvas with an even margin;
nothing is cropped. Appetizing, high detail, magazine quality.
```
- `{TITLE}`: "ANATOMIA" albo "ANATOMY".
- `{NAME}`: krótka nazwa produktu.
- `{LAYERS}`: warstwy z kroku 2 z opisem wyglądu, ponumerowane.
- `{LABELS}`: te same warstwy w cudzysłowach.

## Krok 4. Generacja
```
python "<katalog tego skilla>/scripts/gpt_image.py" --prompt-file <prompt.txt> [--input <zdjęcie>] --size 1536x1024 --out "obrazki/anatomy/RRRR-MM-DD_<obiekt>.png"
```
Ścieżka `--out` jest względna wobec bieżącego folderu. Generacja trwa 1–2 minuty, daj timeout 10 minut.
Błąd sieci albo API → pokaż treść błędu (nigdy klucza) i przejdź do trybu promptu.

## Krok 5. Kontrola i oddanie
Obejrzyj wynik i sprawdź:
- czy warstwy są w dobrej kolejności i każda wygląda jak jej podpis,
- czy tytuł i podpisy nie mają literówek,
- czy jedzenie wygląda apetycznie, a kosmetyk premium,
- czy nic nie jest ucięte.

Coś nie gra → popraw jedno zdanie promptu i generuj jeszcze raz. Bez pytania najwyżej 2 poprawki, bo każda generacja kosztuje.
Oddaj ścieżkę do PNG i listę warstw.

## Tryb promptu (bez klucza API)
Oddaj użytkownikowi gotowy, wypełniony prompt z kroku 3 w bloku kodu i instrukcję:
1. Otwórz ChatGPT (albo inny generator obrazów, który przyjmuje zdjęcie).
2. Wrzuć zdjęcie produktu, jeśli je masz.
3. Wklej prompt i wyślij.
