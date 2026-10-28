# 7 komend obrazkowych do Claude

Wpisujesz `/xray`, wrzucasz zdjęcie produktu i dostajesz zdjęcie rentgenowskie. Tak samo z sześcioma innymi efektami.

| Komenda | Co robi |
|---|---|
| `/xray` | prześwietla produkt jak na RTG; zabawkom dorysowuje szkielet |
| `/explodedview` | rozkłada produkt na części w jednym rzędzie, z podpisami |
| `/blueprint` | robi granatowy rysunek techniczny z wymiarami |
| `/anatomy` | plakat „ANATOMIA” z produktem rozsuniętym na warstwy |
| `/360view` | ten sam produkt z 8 stron na jednej planszy |
| `/crosssection` | przecina produkt na pół i podpisuje, co jest w środku |
| `/knolling` | układa produkt i akcesoria z góry, równo pod kątem prostym |

## Jak zainstalować

Otwórz Claude Code i wklej:

```
Zainstaluj mi komendy z https://github.com/m-archM/claude-komendy-obrazkowe
```

Claude zrobi resztę sam. Na koniec powie, czy możesz od razu generować obrazki, czy musisz jeszcze dodać klucz OpenAI.

W zwykłym czacie na claude.ai też to działa, tylko inaczej. Wklej link i napisz na przykład `/xray` plus nazwę produktu. Claude przeczyta instrukcję z repo i da ci gotowy prompt do wklejenia w ChatGPT razem ze zdjęciem.

## Klucz OpenAI (tylko jeśli chcesz gotowe obrazki)

Bez klucza każda komenda daje ci gotowy prompt do ChatGPT. Z kluczem Claude Code sam generuje obrazek i zapisuje go w folderze `obrazki/`.

1. Weź klucz z platform.openai.com, w zakładce API keys.
2. Utwórz plik `.env` w folderze `.claude` w swoim katalogu domowym (Windows: `C:\Users\<twoja nazwa>\.claude\.env`, macOS i Linux: `~/.claude/.env`).
3. Wpisz w nim jedną linię:
   ```
   OPENAI_API_KEY=sk-twoj-klucz
   ```

Klucza nie wklejaj do czatu. Skrypt sam znajdzie go w tym pliku.

Każdy obrazek to jedno płatne wywołanie API OpenAI, liczone według ich cennika. Jedna grafika powstaje w 1–2 minuty. Chcesz taniej, dopisz w `.env` linię `GPT_IMAGE_QUALITY=medium`.

## Żeby wyszło dobrze

Wrzucaj zdjęcie produktu. Bez niego AI wymyśla produkt po swojemu, a w `/360view` każdy kafelek może wyjść trochę inny.

Mów, co jest w środku. AI nie zna specyfikacji twojego produktu. Kiedy napisałem „silnik V6”, narysowało silnik z czterema tłokami w rzędzie. Dopiero opis budowy dał prawdziwe V6. Claude robi to za ciebie, ale jak znasz budowę lepiej, dopisz ją przy komendzie.

Podpisy na grafikach są domyślnie po polsku. Chcesz po angielsku, napisz to przy komendzie.

Zrobił @i.am_mikolaj. Jak coś nie działa, napisz na DM.

---

## Instrukcja dla Claude'a

Ta sekcja jest dla Claude'a, któremu użytkownik wkleił link do tego repo.

### Claude Code (masz terminal)

1. Sklonuj repo do folderu tymczasowego:
   ```
   git clone --depth 1 https://github.com/m-archM/claude-komendy-obrazkowe.git <folder tymczasowy>/claude-komendy-obrazkowe
   ```
   Brak gita → pobierz `https://github.com/m-archM/claude-komendy-obrazkowe/archive/refs/heads/main.zip` i rozpakuj.
2. Uruchom instalator (na macOS i Linuksie `python3`):
   ```
   python <folder tymczasowy>/claude-komendy-obrazkowe/install.py
   ```
   Instalator kopiuje 7 folderów z `skills/` do `~/.claude/skills/`. Jeśli użytkownik miał już skill o tej samej nazwie, stara wersja trafia do `~/.claude/skills-backup/`. Użytkownik chce komendy tylko w bieżącym projekcie → dodaj `--target .claude/skills`.
3. Instalator zgłosi brak biblioteki `openai` → zapytaj użytkownika, czy ją zainstalować, i uruchom `pip install openai`.
4. Instalator zgłosi brak klucza → wytłumacz użytkownikowi sekcję „Klucz OpenAI” powyżej. Nigdy nie proś o wklejenie klucza do czatu i nie zapisuj go za użytkownika z treści rozmowy.
5. Powiedz użytkownikowi, żeby uruchomił Claude Code od nowa, i podaj listę komend z tabeli na górze. Folder tymczasowy możesz usunąć.

### Czat bez terminala (claude.ai i podobne)

Nie da się tu zainstalować skilli. Kiedy użytkownik wpisze komendę z tabeli, przeczytaj jej instrukcję:

```
https://raw.githubusercontent.com/m-archM/claude-komendy-obrazkowe/main/skills/<komenda>/SKILL.md
```

Wykonaj kroki 1–3 z tej instrukcji (wejście, ustalenie zawartości, prompt) i oddaj wynik w trybie promptu, opisanym na końcu pliku.
