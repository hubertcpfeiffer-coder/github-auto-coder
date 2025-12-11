# Mio-Lifepilot Developer - Projektdokumentation

## Übersicht

Der Mio-Lifepilot Developer ist ein lokaler KI-Entwickler mit einem einfachen GUI-Button. Er nutzt den Konzept eines "Runden Tisches" von verschiedenen KI-Modellen (Grok, Claude, GPT, Gemini), um den besten Code zu generieren.

## Projektstruktur

```
mio-lifepilot-developer/
├── README.md                     # Hauptdokumentation mit Anleitung und Vision
├── mio_developer.py              # Dein lokales Programm mit dem großen Button
├── daily_optimizer.py            # Täglicher Optimierer für Code-Verbesserungen
├── config.yaml.example           # Beispiel für deine API-Keys
├── requirements.txt              # Alle benötigten Pakete
├── dashboard/                    # Optional: Streamlit-Dashboard
│   └── app.py
├── .gitignore                    # Git-Ignorierregeln
└── DOCUMENTATION.md              # Diese Datei
```

## Installation

### Voraussetzungen

- Python 3.8 oder höher
- tkinter (normalerweise mit Python vorinstalliert)

Falls tkinter nicht verfügbar ist:
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# macOS (mit Homebrew)
brew install python-tk

# Windows - normalerweise vorinstalliert
```

### Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

## Verwendung

### Option 1: Desktop GUI starten

```bash
python mio_developer.py
```

Dies öffnet ein Fenster mit:
- **Eingabefeld**: Beschreibe hier, was du entwickeln möchtest
- **Großer Button**: Klicke darauf, um Code zu generieren
- **Ausgabefeld**: Hier erscheint der generierte Code

### Option 2: Streamlit Dashboard starten (optional)

```bash
streamlit run dashboard/app.py
```

Dann öffne deinen Browser auf: http://localhost:8501

Das Dashboard bietet:
- **Web-Interface**: Zugriff von überall im lokalen Netzwerk
- **Projekt-Historie**: Übersicht aller generierten Projekte
- **Erweiterte Optionen**: Framework-Auswahl, Test-Generierung, etc.
- **Runder Tisch Visualisierung**: Sehe die Diskussion der KI-Modelle

### Option 3: Täglicher Optimierer (daily_optimizer.py)

```bash
python daily_optimizer.py
```

Der tägliche Optimierer:
- **Analysiert** bestehenden Code aus deinen Repositories
- **Optimiert** Performance und Struktur durch den Runden Tisch
- **Generiert** verbesserte Versionen mit Erklärungen
- **Integriert** später echte KI-APIs für automatische Optimierung
- **Pusht** Verbesserungen automatisch zu GitHub (in Entwicklung)

Beispiel-Verwendung:
```python
# Der Optimierer analysiert z.B. Betalifepilot-Code und schlägt vor:
# - Modularer strukturieren
# - List-Comprehensions statt Schleifen
# - Neue Features: Biorhythmus, Provisionsverhandlung, q.ANT
```

### Beispiel-Anfragen

1. "Erstelle ein Modul für Provisionsverhandlungen"
2. "Entwickle eine Klasse für Kundenverwaltung"
3. "Baue ein Datenanalyse-Tool für Verkaufszahlen"
4. "Implementiere einen API-Client für REST-Services"

## Aktuelle Features (Demo-Version)

- ✅ Einfaches Desktop GUI mit großem Button
- ✅ Streamlit-Dashboard für Web-Zugriff
- ✅ Täglicher Optimierer (daily_optimizer.py)
- ✅ Eingabe von Programmierwünschen
- ✅ Simulation des "Runden Tisches" (Demo)
- ✅ Code-Generierung mit Erklärung
- ✅ Schöne Ausgabe mit Formatierung
- ✅ Biorhythmus-Berechnung und Provisionsverhandlung (Beispiele)

## Geplante Erweiterungen

### Phase 1: API-Integration
- [ ] Echte OpenAI (GPT) Integration
- [ ] Anthropic (Claude) Integration
- [ ] Google (Gemini) Integration
- [ ] xAI (Grok) Integration

### Phase 2: Code-Qualität
- [ ] Automatische Code-Reviews
- [ ] Syntax-Validierung
- [ ] Best-Practice-Checks
- [ ] Automatische Tests generieren

### Phase 3: GitHub-Integration
- [ ] Automatisches Erstellen von Repositories
- [ ] Code-Commits und Push
- [ ] Pull-Request-Erstellung
- [ ] Issue-Tracking

### Phase 4: Streamlit-Dashboard
- [x] Web-basiertes Interface
- [x] Projekt-Historie (Basis)
- [ ] Code-Vergleiche
- [ ] Statistiken und Analytics

## Konfiguration

### API-Keys einrichten

1. Kopiere `config.yaml.example` zu `config.yaml`:
   ```bash
   cp config.yaml.example config.yaml
   ```

2. Trage deine API-Keys in `config.yaml` ein:
   ```yaml
   api_keys:
     openai: "sk-..."
     anthropic: "sk-ant-..."
     google: "..."
     xai: "..."
   ```

3. Optional: GitHub-Konfiguration für Auto-Push:
   ```yaml
   github:
     token: "ghp_..."
     username: "dein_username"
   ```

## Architektur

### Runder Tisch Konzept

Der "Runde Tisch" simuliert eine Diskussion zwischen verschiedenen KI-Modellen:

1. **Grok**: Fokus auf Architektur und Design
2. **Claude**: Fokus auf Code-Qualität und Wartbarkeit
3. **GPT**: Fokus auf Best Practices und Dokumentation
4. **Gemini**: Fokus auf Performance und Skalierbarkeit

Jedes Modell gibt seine Empfehlung ab, und der finale Code ist ein Konsens aller Modelle.

### Code-Generierung Flow

```
User Input
    ↓
Task Analysis
    ↓
Round Table Discussion
    ├── Grok → Architecture
    ├── Claude → Quality
    ├── GPT → Practices
    └── Gemini → Performance
    ↓
Consensus Building
    ↓
Code Generation
    ↓
Output Formatting
    ↓
User Display
```

## Entwicklung

### Struktur erweitern

Die Anwendung ist modular aufgebaut:

- `MioDeveloperGUI`: Haupt-GUI-Klasse
- `generate_code()`: Button-Handler
- `simulate_round_table()`: Demo-Logik (später mit echten APIs ersetzen)
- `_to_class_name()`: Hilfsfunktion

### Eigene Erweiterungen hinzufügen

1. Neue KI-Modelle hinzufügen
2. Zusätzliche Code-Templates erstellen
3. Export-Funktionen implementieren
4. History-Feature einbauen

## Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'tkinter'"

**Lösung**:
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# macOS
brew install python-tk
```

### Problem: "GUI öffnet sich nicht"

**Lösung**:
- Stelle sicher, dass du in einer Desktop-Umgebung arbeitest
- Auf Servern ohne GUI verwende alternativ die Web-Version (geplant)

### Problem: "API-Keys funktionieren nicht"

**Lösung**:
- Überprüfe, dass `.env` Datei existiert
- Überprüfe, dass die Keys korrekt formatiert sind
- Überprüfe, dass die Keys gültig und aktiv sind

## Lizenz

Siehe LICENSE Datei im Hauptverzeichnis.

## Support

Bei Fragen oder Problemen:
- Erstelle ein Issue im GitHub Repository
- Kontaktiere das Entwicklerteam
- Siehe CONTRIBUTING.md für Entwickler-Richtlinien

---

**Version**: 1.0.0 (Demo)  
**Letzte Aktualisierung**: Dezember 2024
