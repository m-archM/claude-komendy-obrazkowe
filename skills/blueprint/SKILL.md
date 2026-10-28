---
name: blueprint
description: >-
  Komenda /blueprint. Zamienia zdjęcie (albo nazwę) auta, urządzenia, mebla,
  budynku czy gadżetu w granatowy rysunek techniczny: widok z boku, z przodu,
  z tyłu i z góry, białe linie, siatka, wymiary i tabliczka rysunku. Generuje
  obrazek przez OpenAI gpt-image, a bez klucza API oddaje gotowy prompt do
  ChatGPT. Używaj, gdy użytkownik wpisze "/blueprint", "blueprint", "rysunek
  techniczny", "zrób z tego plan", "wymiary tego" albo wrzuci zdjęcie z prośbą
  o efekt planu technicznego.
---

# /blueprint

Wynik: plansza 1536×1024, klasyczny blueprint: granatowe tło z delikatną siatką, cienkie białe linie. Cztery rzuty tego samego obiektu: bok (największy, u góry z lewej), przód, tył i góra. Linie wymiarowe z liczbami, w rogu tabliczka z nazwą.

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
- Zdjęcie → tryb edycji (`--input`), model trzyma proporcje TEGO obiektu. Tu działa to najlepiej.
- Sama nazwa → generacja z opisu.
- Obejrzyj zdjęcie, zanim napiszesz prompt.

## Krok 2. Wymiary
Podaj **prawdziwe** wymiary obiektu: długość, szerokość, wysokość, a w aucie także rozstaw osi. Znasz je → wpisz w milimetrach. Nie znasz → oszacuj rozsądnie i powiedz użytkownikowi, że to szacunek. Fan marki wyłapie zły wymiar w komentarzach.

Rzuty prostokątne model myli z perspektywą, dlatego w prompcie stoi wprost "flat orthographic, no perspective, no 3D shading".

## Krok 3. Prompt (po angielsku, do pliku .txt)
```
Create a single wide 3:2 technical engineering blueprint of {OBJECT}.
Classic blueprint style: deep blue (#123a73) paper background with a faint lighter-blue grid,
all drawing lines thin, crisp and white, like a real draftsman's drawing. Flat orthographic views,
no perspective, no 3D shading, no color fills.
Layout: top-left the large side elevation; top-right the front elevation; bottom-right the rear elevation;
bottom-left the top (plan) view. All four views at the same scale and perfectly aligned to each other.
Show key outlines and visible details: {DETAILS}.
Add white dimension lines with arrowheads and these exact numbers: {DIMENSIONS}.
Bottom-right corner: a small rectangular title block with the text "{TITLE}" and "SCALE 1:20".
No other text. The drawing fills the canvas with an even margin; nothing is cropped.
Sharp, high resolution.
```
- `{OBJECT}`: konkretnie, z modelem i rocznikiem. Ze zdjęciem: "the exact {OBJECT} from the reference photo, same proportions".
- `{DETAILS}`: 4–6 rzeczy widocznych na rzutach, np. "the sloping roofline, door line, side mirrors, headlight shape, rear spoiler".
- `{DIMENSIONS}`: np. `"4315" for the overall length on the side view, "1315" for the height on the front view`.
- `{TITLE}`: nazwa WIELKIMI literami.

## Krok 4. Generacja
```
python "<katalog tego skilla>/scripts/gpt_image.py" --prompt-file <prompt.txt> [--input <zdjęcie>] --size 1536x1024 --out "obrazki/blueprint/RRRR-MM-DD_<obiekt>.png"
```
Ścieżka `--out` jest względna wobec bieżącego folderu. Generacja trwa 1–2 minuty, daj timeout 10 minut.
Błąd sieci albo API → pokaż treść błędu (nigdy klucza) i przejdź do trybu promptu.

## Krok 5. Kontrola i oddanie
Obejrzyj wynik i sprawdź:
- czy są wszystkie 4 rzuty i czy są płaskie, bez perspektywy,
- czy liczby na liniach wymiarowych są dokładnie te z `{DIMENSIONS}`,
- czy sylwetka to TEN obiekt,
- czy nie ma zbędnego tekstu.

Coś nie gra → popraw jedno zdanie promptu i generuj jeszcze raz. Bez pytania najwyżej 2 poprawki, bo każda generacja kosztuje.
Oddaj ścieżkę do PNG i wymiary (z dopiskiem, jeśli są szacowane).

## Tryb promptu (bez klucza API)
Oddaj użytkownikowi gotowy, wypełniony prompt z kroku 3 w bloku kodu i instrukcję:
1. Otwórz ChatGPT (albo inny generator obrazów, który przyjmuje zdjęcie).
2. Wrzuć zdjęcie, jeśli je masz.
3. Wklej prompt i wyślij.
