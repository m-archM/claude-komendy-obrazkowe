---
name: explodedview
description: >-
  Komenda /explodedview. Rozkłada produkt (telefon, słuchawki, buty, pilot,
  zegarek) na części ustawione w jednym rzędzie, od obudowy do środka, każda
  z krótkim podpisem, na jasnym tle. Generuje obrazek przez OpenAI gpt-image,
  a bez klucza API oddaje gotowy prompt do ChatGPT. Używaj, gdy użytkownik
  wpisze "/explodedview", "exploded view", "rozłóż to na części", "pokaż,
  z czego to się składa", "rozbierz produkt" albo wrzuci zdjęcie z taką prośbą.
---

# /explodedview

Wynik: plansza 1536×1024, jasne tło. Produkt rozłożony na 5–8 warstw w jednym rzędzie od lewej do prawej, od najbardziej zewnętrznej (szybka, obudowa) do najgłębszej. Pod każdą częścią krótki podpis. Na brzegach cały produkt: z lewej przód, z prawej tył albo bok.

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
- Sama nazwa → generacja z opisu. Opisz kolor, materiał, kształt.
- Obejrzyj zdjęcie, zanim napiszesz prompt.

## Krok 2. Lista części
Wypisz 5–8 prawdziwych warstw TEGO produktu w kolejności od zewnątrz. Każda część z opisem wyglądu, a nie samą nazwą, bo model nie zna budowy produktów:
- telefon: szkło ochronne, panel OLED, ramka z antenami, płyta główna z układami, bateria w kształcie L, moduł aparatów, tylny panel
- słuchawki: poduszka, maskownica przetwornika, przetwornik 40 mm, płytka z mikrofonami, bateria, muszla, pałąk
- but: sznurówki, cholewka, wkładka, pianka śródpodeszwy, podeszwa z bieżnikiem

Podpisy: 1–2 słowa, po polsku i z polskimi znakami ("Całość", "Płytka", "Pałąk"). gpt-image pisze je poprawnie, a bez ogonków wyglądają amatorsko. Użytkownik chce angielskie → daj angielskie.

## Krok 3. Prompt (po angielsku, do pliku .txt)
```
Create a single wide 3:2 technical product illustration on a clean light-grey (#f2f3f5) background.
Photorealistic exploded view of {OBJECT}: the product taken apart into its real internal layers,
arranged in one straight horizontal row from left to right, evenly spaced, all at the same scale,
each part shown front-facing and floating slightly with a soft shadow beneath it.
At the far left: the complete assembled {OBJECT} seen from the front. At the far right: the complete
{OBJECT} seen from the back. Between them, in this exact order: {PARTS}.
Under each part a thin leader line and a short label in small clean black sans-serif text.
Use exactly these labels, spelled exactly like this, left to right: {LABELS}
(Polish words, keep every accented letter exactly as written).
No other text, no title, no logos added. The row fills the full width of the canvas with even margins;
nothing is cropped. Sharp, high resolution, Apple-style product photography, editorial quality.
```
- `{OBJECT}`: konkretnie, z kolorem i modelem. Ze zdjęciem: "the exact {OBJECT} from the reference photo, same color and details".
- `{PARTS}`: części z kroku 2, ponumerowane (1)…(n), każda z opisem wyglądu.
- `{LABELS}`: podpisy w cudzysłowach, w tej samej kolejności co na planszy, razem z obiema całościami na brzegach.

## Krok 4. Generacja
```
python "<katalog tego skilla>/scripts/gpt_image.py" --prompt-file <prompt.txt> [--input <zdjęcie>] --size 1536x1024 --out "obrazki/explodedview/RRRR-MM-DD_<obiekt>.png"
```
Ścieżka `--out` jest względna wobec bieżącego folderu. Generacja trwa 1–2 minuty, daj timeout 10 minut.
Błąd sieci albo API → pokaż treść błędu (nigdy klucza) i przejdź do trybu promptu.

## Krok 5. Kontrola i oddanie
Obejrzyj wynik i sprawdź:
- czy części stoją w jednym rzędzie, w tej samej skali, i nic nie jest ucięte,
- czy każda część wygląda jak jej podpis (bateria jak bateria, a nie druga płytka),
- czy podpisy nie mają literówek,
- czy produkt na brzegach to TEN produkt.

Coś nie gra → popraw jedno zdanie promptu i generuj jeszcze raz. Bez pytania najwyżej 2 poprawki, bo każda generacja kosztuje.
Oddaj ścieżkę do PNG i listę części.

## Tryb promptu (bez klucza API)
Oddaj użytkownikowi gotowy, wypełniony prompt z kroku 3 w bloku kodu i instrukcję:
1. Otwórz ChatGPT (albo inny generator obrazów, który przyjmuje zdjęcie).
2. Wrzuć zdjęcie produktu, jeśli je masz.
3. Wklej prompt i wyślij.
