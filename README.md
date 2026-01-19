# Scoundrel - Projekt

Cyfrowa adaptacja jednoosobowej gry karcianej typu roguelike o nazwie **Scoundrel**. Projekt został stworzony jako zaliczenie przedmiotu *Wstęp do programowania* na I roku Informatyki Praktycznej.

Gra łączy w sobie elementy strategii i losowości, gdzie celem gracza jest przetrwanie w lochu pełnym potworów, używając jedynie standardowej talii kart (z pewnymi modyfikacjami).

## 🛠️ Technologie i Narzędzia

Projekt został zrealizowany przy użyciu:
* **Język:** Python 3.14.2
* **Silnik:** pygame-ce 2.5.6 (Community Edition)
* **Grafika:** LibreSprite 1.1

---

## 🎮 Zasady Gry

Oryginalna gra została zaprojektowana przez Zacha Gage'a i Kurta Biega. Poniżej znajduje się opis zasad zaimplementowanych w tej cyfrowej wersji.

### Cel Gry
Twoim zadaniem jest przejście przez całą talię (Loch/Dungeon) lub zdobycie jak najwyższego wyniku, zanim Twoje życie spadnie do 0. Zaczynasz z **20 punktami życia (HP)**.

### Karty w Tali
Z talii usunięte są Jokery oraz czerwone figury i Asy. Pozostałe karty pełnią następujące funkcje:

* **Potwory (♣️ Trefl i ♠️ Pik):** Zadają obrażenia równe swojej wartości.
    * Figury: Walet (J) = 11, Dama (Q) = 12, Król (K) = 13, As (A) = 14.
* **Bronie (♦️ Karo):** Służą do walki z potworami. Wartość karty to siła ataku.
* **Mikstury (♥️ Kier):** Leczą bohatera o wartość karty. Maksymalne życie to 20 HP.

### Przebieg Rozgrywki

1.  **Pokój (The Room):** W każdej turze na ekranie pojawiają się 4 karty.
2.  **Decyzja:**
    * **Ucieczka:** Możesz ominąć cały pokój. Wszystkie 4 karty wracają na spód talii. **Uwaga:** Nie możesz uciec z dwóch pokoi z rzędu!.
    * **Wejście:** Jeśli nie uciekasz, musisz wejść w interakcję z **3 z 4 kart**. Czwarta karta zostaje na stole i przechodzi do następnej tury.

### Interakcje

* **Zbieranie Broni (♦️):** Podniesienie broni automatycznie ją ekwipuje. Jeśli masz już broń, stara zostaje wyrzucona (wraz z zabitymi nią potworami).
* **Picie Mikstury (♥️):** Leczy Cię o wskazaną wartość. Możesz wypić tylko **jedną** miksturę na turę (druga przepada, jeśli ją klikniesz).
* **Walka z Potworem (♣️/♠️):**
    * **Gołe ręce:** Otrzymujesz obrażenia równe pełnej sile potwora.
    * **Użycie Broni:** Obrażenia = Siła Potwora - Siła Broni. (Jeśli wynik jest ujemny, nie otrzymujesz obrażeń).

### ⚠️ Ważna zasada: Tępienie Ostrza
Kluczowa mechanika gry. Kiedy użyjesz broni na potworze, ta broń zapamiętuje siłę tego potwora.
* Możesz zaatakować tą samą bronią kolejnego potwora tylko wtedy, gdy jest on **słabszy lub równy** ostatniemu zabitemu potworowi.
* Przykład: Jeśli bronią o sile 5 zabijesz Damę (12), następny potwór zabity tą bronią musi mieć siłę 12 lub mniej. Jeśli potem zabijesz 6-tkę, kolejny cel musi mieć siłę 6 lub mniej.
* Jeśli potwór jest silniejszy niż ostatni zabity – musisz walczyć gołymi rękami (ale nie tracisz broni).

### Punktacja
Gra kończy się, gdy skończy się talia lub zginiesz.
* **Wygrana (przejście lochu):** Twój wynik to pozostałe **punkty życia + pozostałe mikstury**.
* **Przegrana (śmierć):** Od Twojego życia (ujemnego) odejmuje się sumę siły wszystkich potworów, które zostały w talii.

---
*Orginalnie gra stworzona przez Zach Gage oraz Kurt Bieg (2011).*

---

**Gdańsk, 2025**
**Miłosz Ostrowski, 1 rok informatyki praktycznej, studia I stopnia na Uniwersytecie Gdańskim**