---
name: knolling
description: >-
  Komenda /knolling. Zdjęcie z góry (flat lay): produkt w środku, a wokół
  niego, równo i pod kątem prostym, jego akcesoria, części albo zawartość
  (buty z przypinkami, aparat z obiektywami, plecak z zawartością, zestaw do
  kawy). Generuje obrazek przez OpenAI gpt-image, a bez klucza API oddaje
  gotowy prompt do ChatGPT. Używaj, gdy użytkownik wpisze "/knolling",
  "knolling", "flat lay", "rozłóż równo", "ułożenie z góry", "pokaż zestaw"
  albo wrzuci zdjęcie z taką prośbą.
---

# /knolling

Wynik: kwadrat 1024×1024, widok idealnie z góry. Produkt w centrum, wokół 8–16 przedmiotów ułożonych w siatce: równolegle, pod kątem prostym, w równych odstępach. Jednolite tło w kolorze dobranym do produktu. Bez podpisów.

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
- Zdjęcie → tryb edycji (`--input`), model trzyma wygląd TEGO produktu.
- Sama nazwa → generacja z opisu.
- Obejrzyj zdjęcie, zanim napiszesz prompt.

## Krok 2. Co leży wokół
Wypisz 8–16 przedmiotów, które naturalnie idą z produktem, każdy z kolorem i wielkością:
- klapki piankowe: 10–12 przypinek w różnych kształtach, sznurek, metka, zapasowy pasek
- aparat: 3 obiektywy, karty pamięci, bateria, pasek, dekielki
- plecak: laptop, ładowarka, słuchawki, notes, długopisy, bidon, klucze

Tło: jeden kolor dopasowany do produktu (kontrast albo ton w ton), np. "soft lilac" przy limonkowych butach.

## Krok 3. Prompt (po angielsku, do pliku .txt)
```
Create a square knolling flat-lay photograph shot from exactly directly above (perfect 90-degree
top-down view, no perspective) on a seamless solid {BACKGROUND} background.
In the center: {OBJECT}. Around it, neatly arranged in a precise grid, all items parallel or at
exact right angles to each other and to the frame, with equal spacing between every item and
nothing overlapping: {ITEMS}.
Symmetrical, balanced composition with an even margin; every item fully visible, nothing cropped.
Soft even shadowless studio light, true colors, crisp detail. No text, no labels, no logos added.
Photorealistic, high resolution, editorial quality.
```
- `{BACKGROUND}`: kolor z kroku 2.
- `{OBJECT}`: produkt. Ze zdjęciem: "the exact {OBJECT} from the reference photo, same color and details".
- `{ITEMS}`: przedmioty z kroku 2, każdy z kolorem i wielkością.

## Krok 4. Generacja
```
python "<katalog tego skilla>/scripts/gpt_image.py" --prompt-file <prompt.txt> [--input <zdjęcie>] --size 1024x1024 --out "obrazki/knolling/RRRR-MM-DD_<obiekt>.png"
```
Ścieżka `--out` jest względna wobec bieżącego folderu. Generacja trwa 1–2 minuty, daj timeout 10 minut.
Błąd sieci albo API → pokaż treść błędu (nigdy klucza) i przejdź do trybu promptu.

## Krok 5. Kontrola i oddanie
Obejrzyj wynik i sprawdź:
- czy widok jest naprawdę z góry, bez perspektywy i bez cieni padających w bok,
- czy przedmioty leżą równo, pod kątem prostym, i nic na siebie nie zachodzi,
- czy produkt w środku to TEN produkt.

Coś nie gra → popraw jedno zdanie promptu i generuj jeszcze raz. Bez pytania najwyżej 2 poprawki, bo każda generacja kosztuje.
Oddaj ścieżkę do PNG.

## Tryb promptu (bez klucza API)
Oddaj użytkownikowi gotowy, wypełniony prompt z kroku 3 w bloku kodu i instrukcję:
1. Otwórz ChatGPT (albo inny generator obrazów, który przyjmuje zdjęcie).
2. Wrzuć zdjęcie produktu, jeśli je masz.
3. Wklej prompt i wyślij.
