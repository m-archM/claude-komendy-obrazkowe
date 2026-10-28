---
name: crosssection
description: >-
  Komenda /crosssection. Przecina produkt na pół i pokazuje wnętrze jak
  rysunek z instrukcji: połowa obudowy zdjęta, mechanizm widoczny na swoim
  miejscu i podpisany (długopis, latarka, ekspres, wkrętarka, butelka, but,
  owoc). Generuje obrazek przez OpenAI gpt-image, a bez klucza API oddaje
  gotowy prompt do ChatGPT. Używaj, gdy użytkownik wpisze "/crosssection",
  "przekrój", "cross section", "przetnij to na pół", "co jest w środku" albo
  wrzuci zdjęcie z taką prośbą.
---

# /crosssection

Wynik: plansza 1536×1024, jasne tło. Produkt leży poziomo przez całą szerokość, przecięty wzdłuż osi: górna połowa obudowy jest wycięta, więc widać mechanizm. 4–7 elementów podpisanych cienkimi liniami u góry i u dołu.

Różnica wobec /xray: tam prześwietlenie (półprzezroczyste, czarne tło), tu fizyczne cięcie (prawdziwe materiały i kolory wnętrza). Wobec /explodedview: tam części są rozsunięte, tu stoją na swoim miejscu.

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

## Krok 2. Mechanizm
Wypisz 4–7 elementów wnętrza w kolejności od jednego końca do drugiego, **z opisem budowy** (kształt, materiał, położenie). Sama nazwa nie wystarczy, bo model nie zna budowy produktów:
- latarka: przycisk w zatyczce, stalowa sprężyna, akumulator 18650 w niebieskiej osłonie, okrągła zielona płytka sterownika, kwadratowa dioda LED na miedzianym radiatorze, srebrny odbłyśnik, szklana soczewka
- wstrzykiwacz: pokrętło dawki, sprężyna, tłok z gwintem, wkład z płynem, igła

Podpisy: 1–2 słowa, po polsku i z polskimi znakami ("Sprężyna", "Odbłyśnik").

## Krok 3. Prompt (po angielsku, do pliku .txt)
```
Create a single wide 3:2 technical cutaway illustration on a clean white background.
A photorealistic {OBJECT} lying horizontally across the full width of the canvas, cut cleanly in half
along its long axis: the upper half of the outer shell is removed, so the real internal mechanism is
visible in place, with clean flat cut edges showing the wall thickness of the shell.
Visible inside, from left to right: {INTERNALS}.
Thin dark-grey leader lines from each internal part to short labels placed above and below the object,
in small clean dark sans-serif text, spelled exactly like this, in order from left to right: {LABELS}
(Polish words, keep every accented letter exactly as written).
No other text, no logos added. Even margin around the object; nothing is cropped.
Product-manual style, soft even lighting, sharp, high resolution.
```
- `{OBJECT}`: konkretnie, z kolorem. Ze zdjęciem: "the exact {OBJECT} from the reference photo".
- `{INTERNALS}`: elementy z kroku 2 z opisem budowy, ponumerowane.
- `{LABELS}`: te same elementy w cudzysłowach.
- Obiekt wysoki (butelka, wieża) → napisz "standing vertically, cut in half from top to bottom" i daj `--size 1024x1536`.

## Krok 4. Generacja
```
python "<katalog tego skilla>/scripts/gpt_image.py" --prompt-file <prompt.txt> [--input <zdjęcie>] --size 1536x1024 --out "obrazki/crosssection/RRRR-MM-DD_<obiekt>.png"
```
Ścieżka `--out` jest względna wobec bieżącego folderu. Generacja trwa 1–2 minuty, daj timeout 10 minut.
Błąd sieci albo API → pokaż treść błędu (nigdy klucza) i przejdź do trybu promptu.

## Krok 5. Kontrola i oddanie
Obejrzyj wynik i sprawdź:
- czy obiekt jest naprawdę przecięty (widać krawędź cięcia), a nie przezroczysty,
- czy mechanizm jest wiarygodny i zgadza się z `{INTERNALS}`,
- czy każda linia prowadzi do właściwej części, a podpisy nie mają literówek.

Coś nie gra → popraw jedno zdanie promptu i generuj jeszcze raz. Bez pytania najwyżej 2 poprawki, bo każda generacja kosztuje.
Oddaj ścieżkę do PNG i listę elementów.

## Tryb promptu (bez klucza API)
Oddaj użytkownikowi gotowy, wypełniony prompt z kroku 3 w bloku kodu i instrukcję:
1. Otwórz ChatGPT (albo inny generator obrazów, który przyjmuje zdjęcie).
2. Wrzuć zdjęcie produktu, jeśli je masz.
3. Wklej prompt i wyślij.
