# Requirements Document

AURA (Autonomous Unit & Resource Arbitrator) to aplikacja desktopowa umożliwiająca komunikację z systemem orkiestracji agentów AI poprzez interfejs czatu. System składa się z Orkiestratora zarządzającego zespołem wyspecjalizowanych agentów (Researcher, Coder, Designer), którzy współpracują przy wykonywaniu złożonych zadań użytkownika. Aplikacja wykorzystuje lokalne modele LLM (Ollama) oraz pamięć wektorową do przechowywania wiedzy długoterminowej.

## Table of Contents

- [Requirements Document](#requirements-document)
  - [Table of Contents](#table-of-contents)
  - [Requirement 1](#requirement-1)
  - [Requirement 2](#requirement-2)
  - [Requirement 3](#requirement-3)
  - [Requirement 4](#requirement-4)
  - [Requirement 5](#requirement-5)
  - [Requirement 6](#requirement-6)
  - [Requirement 7](#requirement-7)
  - [Requirement 8](#requirement-8)
  - [Requirement 9](#requirement-9)
  - [Requirement 10](#requirement-10)
  - [Requirement 11](#requirement-11)
  - [Requirement 12](#requirement-12)

### **Requirement 1**

- _User Story:_

      Jako użytkownik, chcę mieć graficzny interfejs desktopowy z czatem, aby móc komunikować się z systemem AURA w intuicyjny sposób.

- _Acceptance Criteria:_

      1. WHEN użytkownik uruchamia aplikację THEN system SHALL wyświetlić okno desktopowe z interfejsem czatu
      2. WHEN użytkownik wpisuje polecenie w pole tekstowe THEN system SHALL wyświetlić wiadomość w oknie czatu
      3. WHEN użytkownik naciśnie Enter lub przycisk "Wykonaj Zadanie" THEN system SHALL rozpocząć przetwarzanie polecenia
      4. WHEN system przetwarza zadanie THEN aplikacja SHALL wyświetlać komunikaty o postępie w czasie rzeczywistym
      5. WHEN zadanie zostanie zakończone THEN system SHALL wyświetlić końcowy wynik w oknie czatu

### **Requirement 2**

- _User Story:_

      Jako użytkownik, chcę aby Orkiestrator analizował moje polecenia i delegował zadania do odpowiednich agentów, aby złożone problemy były rozwiązywane systematycznie.

- _Acceptance Criteria:_

      1. WHEN użytkownik poda złożone zadanie THEN Orkiestrator SHALL przeanalizować je i rozbić na mniejsze kroki
      2. WHEN Orkiestrator identyfikuje kroki zadania THEN system SHALL przypisać każdy krok do odpowiedniego agenta (Researcher, Coder, Designer)
      3. WHEN agent zakończy swoje zadanie THEN wynik SHALL być przekazany z powrotem do Orkiestratora
      4. WHEN wszystkie kroki zostaną wykonane THEN Orkiestrator SHALL zsyntezować końcową odpowiedź
      5. IF zadanie wymaga informacji z internetu THEN system SHALL delegować je do agenta Researcher

### **Requirement 3**

- _User Story:_

      Jako użytkownik, chcę aby agent Researcher mógł wyszukiwać i pobierać informacje z internetu, aby system miał dostęp do aktualnych danych.

- _Acceptance Criteria:_

      1. WHEN Researcher otrzyma zadanie wyszukiwania THEN agent SHALL użyć narzędzi wyszukiwania internetowego
      2. WHEN Researcher znajdzie relevantne strony THEN system SHALL pobrać i przetworzyć ich zawartość
      3. WHEN zawartość zostanie pobrana THEN system SHALL oczyścić tekst z niepotrzebnych elementów HTML
      4. WHEN tekst przekracza limit kontekstu THEN system SHALL ograniczyć go do maksymalnie 8000 znaków
      5. WHEN Researcher zakończy wyszukiwanie THEN wyniki SHALL być przekazane do Orkiestratora

### **Requirement 4**

- _User Story:_

      Jako użytkownik, chcę aby agent Coder mógł tworzyć, modyfikować i zarządzać plikami kodu, aby system mógł implementować rozwiązania programistyczne.

- _Acceptance Criteria:_

      1. WHEN Coder otrzyma zadanie programistyczne THEN agent SHALL móc tworzyć nowe pliki
      2. WHEN Coder pracuje z plikami THEN system SHALL umożliwić odczyt, zapis i listowanie plików
      3. WHEN Coder potrzebuje wykonać polecenia systemowe THEN agent SHALL mieć dostęp do terminala
      4. WHEN Coder tworzy kod THEN system SHALL zapisać go w odpowiedniej strukturze katalogów
      5. IF operacja na plikach nie powiedzie się THEN system SHALL zwrócić informację o błędzie

### **Requirement 5**

- _User Story:_

      Jako użytkownik, chcę aby system posiadał pamięć długoterminową, aby mógł wykorzystywać wcześniej zdobytą wiedzę w przyszłych zadaniach.

- _Acceptance Criteria:_

      1. WHEN system przetworzy ważne informacje THEN dane SHALL być zapisane w bazie wektorowej
      2. WHEN agent potrzebuje informacji z przeszłości THEN system SHALL przeszukać pamięć długoterminową
      3. WHEN system wyszukuje w pamięci THEN wyniki SHALL być posortowane według relevancji
      4. WHEN pamięć zostanie zaktualizowana THEN system SHALL potwierdzić zapisanie danych
      5. WHEN aplikacja zostanie uruchomiona ponownie THEN pamięć długoterminowa SHALL być zachowana

### **Requirement 6**

- _User Story:_

      Jako użytkownik, chcę aby system wykorzystywał lokalne modele LLM przez Ollama, aby zachować prywatność i kontrolę nad danymi.

- _Acceptance Criteria:_

      1. WHEN system się uruchamia THEN aplikacja SHALL połączyć się z serwerem Ollama
      2. WHEN Orkiestrator potrzebuje analizy THEN system SHALL użyć modelu rogue-v1-brain
      3. WHEN agenci wykonują zadania THEN system SHALL użyć modelu rogue-v1-agent
      4. IF połączenie z Ollama nie powiedzie się THEN system SHALL wyświetlić komunikat o błędzie
      5. WHEN model przetwarza zapytanie THEN system SHALL obsłużyć odpowiedź asynchronicznie

### **Requirement 7**

- _User Story:_

      Jako użytkownik, chcę aby aplikacja działała bezpiecznie, aby nie narazić mojego systemu na szkody.

- _Acceptance Criteria:_

      1. WHEN agent Coder wykonuje operacje na plikach THEN system SHALL ograniczyć dostęp do bezpiecznych katalogów
      2. WHEN agent wykonuje polecenia terminala THEN system SHALL walidować polecenia pod kątem bezpieczeństwa
      3. WHEN system wykryje potencjalnie niebezpieczną operację THEN aplikacja SHALL poprosić o potwierdzenie użytkownika
      4. WHEN występuje błąd bezpieczeństwa THEN system SHALL zatrzymać wykonywanie zadania
      5. IF użytkownik nie potwierdzi ryzykownej operacji THEN system SHALL anulować zadanie

### **Requirement 8**

- _User Story:_

      Jako użytkownik, chcę aby aplikacja działała wydajnie, aby nie przeciążać mojego komputera.

- _Acceptance Criteria:_

      1. WHEN aplikacja przetwarza zadania THEN GUI SHALL pozostać responsywny
      2. WHEN system wykonuje długotrwałe operacje THEN przetwarzanie SHALL odbywać się w osobnych wątkach
      3. WHEN agent pobiera dane z internetu THEN system SHALL ograniczyć rozmiar pobieranych treści
      4. WHEN pamięć kontekstu się zapełnia THEN system SHALL automatycznie zarządzać jej rozmiarem
      5. WHEN użytkownik zamknie aplikację THEN wszystkie procesy SHALL zostać prawidłowo zakończone

### **Requirement 9**

- _User Story:_

      Jako użytkownik, chcę aby system wykorzystywał określone biblioteki Python, aby zapewnić kompatybilność i funkcjonalność zgodną z projektem.

- _Acceptance Criteria:_

      1. WHEN system się inicjalizuje THEN aplikacja SHALL używać CrewAI jako framework do orkiestracji agentów
      2. WHEN GUI jest tworzone THEN system SHALL wykorzystać PyQt6 do interfejsu desktopowego
      3. WHEN agent Researcher wyszukuje informacje THEN system SHALL używać playwright do zaawansowanego przeglądania stron
      4. WHEN system potrzebuje prostszego wyszukiwania THEN aplikacja SHALL wykorzystać duckduckgo-search
      5. WHEN system parsuje HTML THEN aplikacja SHALL używać BeautifulSoup4
      6. WHEN system łączy się z Ollama THEN aplikacja SHALL wykorzystać langchain-community i langchain-ollama
      7. WHEN system zarządza pamięcią wektorową THEN aplikacja SHALL używać ChromaDB
      8. WHEN system potrzebuje zmiennych środowiskowych THEN aplikacja SHALL wykorzystać python-dotenv

### **Requirement 10**

- _User Story:_

      Jako użytkownik, chcę aby aplikacja obsługiwała narzędzia z serwerów MCP (Model Context Protocol), aby rozszerzyć możliwości agentów o dodatkowe funkcjonalności.

- _Acceptance Criteria:_

      1. WHEN system się uruchamia THEN aplikacja SHALL automatycznie wykryć i połączyć się z dostępnymi serwerami MCP
      2. WHEN serwer MCP jest dostępny THEN system SHALL załadować jego narzędzia i udostępnić je agentom
      3. WHEN agent potrzebuje użyć narzędzia MCP THEN system SHALL wykonać wywołanie do odpowiedniego serwera
      4. WHEN narzędzie MCP zwróci wynik THEN system SHALL przetworzyć odpowiedź i przekazać ją agentowi
      5. IF serwer MCP nie jest dostępny THEN system SHALL kontynuować pracę z dostępnymi narzędziami lokalnymi

### **Requirement 11**

- _User Story:_

      Jako użytkownik, chcę aby aplikacja była modułowa i łatwa w nawigacji, aby móc łatwo rozbudowywać i modyfikować system.

- _Acceptance Criteria:_

      1. WHEN deweloper przegląda kod THEN struktura projektu SHALL być logicznie podzielona na moduły
      2. WHEN deweloper chce dodać nowego agenta THEN system SHALL umożliwić łatwe dodanie przez utworzenie nowego modułu
      3. WHEN deweloper chce dodać nowe narzędzie THEN system SHALL pozwolić na dodanie go w dedykowanym module narzędzi
      4. WHEN deweloper modyfikuje funkcjonalność THEN zmiany SHALL być izolowane w odpowiednich modułach
      5. WHEN system się uruchamia THEN moduły SHALL być automatycznie wykrywane i ładowane

### **Requirement 12**

- _User Story:_

      Jako użytkownik, chcę mieć centralny plik konfiguracyjny, aby łatwo zarządzać wszystkimi ustawieniami aplikacji w jednym miejscu.

- _Acceptance Criteria:_

      1. WHEN aplikacja się uruchamia THEN system SHALL wczytać wszystkie ustawienia z centralnego pliku konfiguracyjnego
      2. WHEN użytkownik zmieni ustawienie w pliku konfiguracyjnym THEN zmiana SHALL być automatycznie zastosowana w całej aplikacji
      3. WHEN moduł potrzebuje parametru konfiguracyjnego THEN system SHALL automatycznie dostarczyć wartość z centralnej konfiguracji
      4. WHEN dodawany jest nowy moduł THEN jego ustawienia SHALL być dodane do centralnego pliku konfiguracyjnego
      5. IF plik konfiguracyjny nie istnieje THEN system SHALL utworzyć domyślny plik z podstawowymi ustawieniami
