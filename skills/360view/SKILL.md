---
name: 360view
description: >-
  Komenda /360view. Pokazuje ten sam produkt z 8 stron na jednej planszy
  (siatka 4×2: przód, przód 3/4, bok, tył 3/4, tył, góra, widok dobrany do
  produktu i detal), jak karta produktu w sklepie. Działa na okularach,
  butach, zegarkach, torbach, gadżetach i autach. Generuje obrazek przez
  OpenAI gpt-image, a bez klucza API oddaje gotowy prompt do ChatGPT. Używaj,
  gdy użytkownik wpisze "/360view", "360", "widok 360", "pokaż ze wszystkich
  stron", "obróć produkt" albo wrzuci zdjęcie z taką prośbą.
---

# /360view

Wynik: plansza 1536×1024, siatka 4 kolumny × 2 rzędy, osiem jasnych kafelków na białym tle. W każdym ten sam produkt z innej strony, w tej samej skali i świetle. Pod kafelkiem mały podpis.

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
- Zdjęcie → tryb edycji (`--input`). Tu zdjęcie jest prawie konieczne: z samej nazwy model narysuje własny wariant i każdy kafelek może wyjść trochę inny.
- Sama nazwa → generacja, ale opisz produkt bardzo dokładnie (kolor, materiał, kształt, detale).
- Obejrzyj zdjęcie i spisz 2–4 detale, które muszą się powtarzać w każdym kafelku (logo na zausznikach, kolor podeszwy, kształt koperty).

## Krok 2. Kąty
Domyślnie osiem: Przód · Przód 3/4 · Bok · Tył 3/4 · Tył · Góra · {SIÓDMY} · Detal.

`{SIÓDMY}` dobierasz do produktu. Widok z dołu zwykle wygląda prawie jak widok z góry i kafelek się marnuje, więc bierzesz coś, co pokazuje nową informację:
- okulary: "Złożone" (zauszniki zamknięte)
- buty: "Podeszwa"
- torba, plecak: "Otwarta"
- laptop, słuchawki: "Złożony"
- auto: "Wnętrze"

Dół zostawiasz tylko wtedy, gdy naprawdę jest tam coś innego (np. dekiel zegarka).

Podpisy po polsku i z polskimi znakami, 1–2 słowa.

## Krok 3. Prompt (po angielsku, do pliku .txt)
```
Create a single wide 3:2 product turnaround sheet on a pure white background: a clean grid of
4 columns by 2 rows of equal light-grey (#f4f4f5) rounded tiles with even gaps.
Every tile shows the same {OBJECT}, identical in every tile in color, material, proportions and details
({KEY_DETAILS}), at the same scale and with the same soft studio lighting, centered and fully visible.
Viewing angles, left to right, top row then bottom row: {ANGLES}.
Under each tile a tiny grey sans-serif label, spelled exactly: {LABELS}
(Polish words, keep every accented letter exactly as written).
No other text, no logos added. The grid fills the canvas with an even margin; nothing is cropped.
Photorealistic e-commerce product photography, sharp, high resolution.
```
- `{OBJECT}`: konkretnie. Ze zdjęciem: "the exact {OBJECT} from the reference photo".
- `{KEY_DETAILS}`: detale z kroku 1.
- `{ANGLES}`: "front view, front three-quarter view, left side view, rear three-quarter view, back view, top view, {SEVENTH}, close-up detail of {DETAIL}", np. SEVENTH = "the glasses folded with both temples closed".
- `{LABELS}`: "Przód", "Przód 3/4", "Bok", "Tył 3/4", "Tył", "Góra", "{SIÓDMY}", "Detal".

## Krok 4. Generacja
```
python "<katalog tego skilla>/scripts/gpt_image.py" --prompt-file <prompt.txt> [--input <zdjęcie>] --size 1536x1024 --out "obrazki/360view/RRRR-MM-DD_<obiekt>.png"
```
Ścieżka `--out` jest względna wobec bieżącego folderu. Generacja trwa 1–2 minuty, daj timeout 10 minut.
Błąd sieci albo API → pokaż treść błędu (nigdy klucza) i przejdź do trybu promptu.

## Krok 5. Kontrola i oddanie
Obejrzyj wynik i sprawdź:
- czy w każdym kafelku jest NA PEWNO ten sam produkt (kolor, detale). To najczęstszy błąd,
- czy kąty się nie powtarzają,
- czy podpisy pasują do kątów i nie mają literówek.

Coś nie gra → popraw jedno zdanie promptu i generuj jeszcze raz. Bez pytania najwyżej 2 poprawki, bo każda generacja kosztuje.
Oddaj ścieżkę do PNG.

## Tryb promptu (bez klucza API)
Oddaj użytkownikowi gotowy, wypełniony prompt z kroku 3 w bloku kodu i instrukcję:
1. Otwórz ChatGPT (albo inny generator obrazów, który przyjmuje zdjęcie).
2. Wrzuć zdjęcie produktu. Tu naprawdę warto.
3. Wklej prompt i wyślij.
