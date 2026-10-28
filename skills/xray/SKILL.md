---
name: xray
description: >-
  Komenda /xray. Zamienia zdjęcie (albo nazwę) przedmiotu, zabawki, jedzenia
  czy auta w poziomy tryptyk: oryginał, pełne zdjęcie rentgenowskie i zbliżenie
  RTG najciekawszego detalu. Urządzenia i maszyny dostają prawdziwe wnętrze,
  zabawki i maskotki wymyślony szkielet. Generuje obrazek przez OpenAI
  gpt-image, a bez klucza API oddaje gotowy prompt do ChatGPT. Używaj, gdy
  użytkownik wpisze "/xray", "xray", "x-ray", "rentgen", "zrób RTG tego",
  "prześwietl to" albo wrzuci zdjęcie z prośbą o efekt rentgena.
---

# /xray

Wynik: jedna plansza 1536×1024 z trzema panelami na ciemnym tle.

| Panel | Zawartość |
|---|---|
| 1 | Oryginał: przedmiot jak na zdjęciu, na czystym ciemnym tle studyjnym |
| 2 | Ten sam przedmiot, ta sama poza i kadr, jako zdjęcie rentgenowskie |
| 3 | Zbliżenie RTG jednego detalu, tego najciekawszego w środku |

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
- Zdjęcie od użytkownika → tryb edycji (`--input`). To lepsza opcja, bo model trzyma kształt TEGO produktu.
- Sama nazwa ("/xray PS5") → generacja z opisu.
- Obejrzyj zdjęcie, zanim napiszesz prompt.

## Krok 2. Zdecyduj, co jest w środku
Od tego zależy efekt. Ustal przed napisaniem promptu:
- **Urządzenie, maszyna, auto** → prawdziwe wnętrze: silnik, rama, przewody, śruby, płytki, baterie. Wymień 4–6 konkretnych elementów dla TEGO obiektu.
- **Zabawka, maskotka, postać** → wymyślony szkielet, jakby była żywym stworzeniem: czaszka w proporcjach postaci, kręgosłup, żebra, kości uszu albo ogona. Panel 3 to zwykle czaszka.
- **Jedzenie, napój** → warstwy, pęcherzyki powietrza, kawałki składników w środku.
- **Ubranie, buty** → szwy, wkładki, podeszwa, metalowe elementy (nity, zamki). Metal świeci najmocniej.

Detal z panelu 3 opisz **z budową**, nie samą nazwą. Model nie zna specyfikacji: "V6 engine" potrafi dać silnik rzędowy z czterema tłokami, a "V-shaped block, two angled banks of three cylinders, six pistons, not inline" daje prawdziwe V6. Liczby, układ i kierunek widoku podawaj wprost.

## Krok 3. Prompt (po angielsku, do pliku .txt)
```
Create a single wide 3:2 image: a clean horizontal triptych of three equal rounded-corner panels
on a near-black (#0b0d10) background. The three panels fill almost the entire canvas height and width,
with only a thin even margin around and between them (no empty bands above or below).
No text, no labels, no logos added. In panels 1 and 2 the whole object is fully visible, centered
and as large as the panel allows, never cropped at the edges.

Panel 1 (left): the exact {OBJECT} from the reference photo, same shape, color, proportions and details,
placed on a dark studio backdrop with soft top light. Photorealistic product photo.

Panel 2 (center): the same {OBJECT} in the same pose and framing, rendered as a real hospital
X-ray film radiograph (not a 3D glass render, not a wireframe): deep black background,
translucent glowing blue-white silhouette of the outer shell, dense parts brighter.
Visible inside: {INTERNALS}. Fine film grain, realistic radiograph look.

Panel 3 (right): close-up X-ray of {DETAIL}, filling the panel, same radiograph style, high detail,
bright bone-white or metal-white structures against black.

Consistent lighting and scale across panels. Sharp, high resolution, editorial quality.
```
- `{OBJECT}`: konkretnie, z kolorem i modelem.
- `{INTERNALS}`: 4–6 elementów z kroku 2.
- `{DETAIL}`: jeden detal z budową.
- Bez zdjęcia zamień "from the reference photo" na pełny opis wyglądu.
- Obiekt szeroki (auto, sofa) wychodzi w wąskim panelu mały. Dopisz "shown from the front three-quarter angle so it fits the tall panel".

## Krok 4. Generacja
```
python "<katalog tego skilla>/scripts/gpt_image.py" --prompt-file <prompt.txt> [--input <zdjęcie>] --size 1536x1024 --out "obrazki/xray/RRRR-MM-DD_<obiekt>.png"
```
Ścieżka `--out` jest względna wobec bieżącego folderu. Generacja trwa 1–2 minuty, daj timeout 10 minut.
Błąd sieci albo API → pokaż treść błędu (nigdy klucza) i przejdź do trybu promptu.

## Krok 5. Kontrola i oddanie
Obejrzyj wynik i sprawdź:
- czy panel 1 to TEN produkt, a nie podobny,
- czy panel 2 ma tę samą pozę co panel 1,
- czy wnętrze pasuje do obiektu (auto ma silnik, a nie szkielet),
- czy model nie dopisał tekstu.

Coś nie gra → popraw jedno zdanie promptu i generuj jeszcze raz. Bez pytania najwyżej 2 poprawki, bo każda generacja kosztuje.
Oddaj ścieżkę do PNG i powiedz krótko, co jest w panelach.

## Tryb promptu (bez klucza API)
Oddaj użytkownikowi gotowy, wypełniony prompt z kroku 3 w bloku kodu i instrukcję:
1. Otwórz ChatGPT (albo inny generator obrazów, który przyjmuje zdjęcie).
2. Wrzuć zdjęcie produktu, jeśli je masz.
3. Wklej prompt i wyślij.
