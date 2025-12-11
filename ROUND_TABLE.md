# 🤖 Round Table - Multi-AI Kollaborations-System

## Übersicht

Das **Round Table** System ist ein innovativer Ansatz zur Code-Generierung, bei dem mehrere KI-Modelle zusammenarbeiten, um optimalen Code zu erstellen. Jedes Modell bringt seine eigene Expertise ein:

- **🏛️ Grok (xAI)**: Architektur & Design
- **✨ Claude (Anthropic)**: Code-Qualität & Wartbarkeit
- **📚 GPT (OpenAI)**: Best Practices & Dokumentation
- **⚡ Gemini (Google)**: Performance & Skalierbarkeit

## Features

- ✅ Multi-AI Kollaboration für besseren Code
- ✅ Konsens-basierte Code-Generierung
- ✅ Unterstützung für mehrere Programmiersprachen
- ✅ Detaillierte Diskussions-Dokumentation
- ✅ CLI und programmatische API
- ✅ Simulations-Modus (ohne API-Keys)
- ✅ Integration in GitHub Auto-Coder

## Schnellstart

### 1. Als Standalone Tool

```bash
# Direkte Verwendung
python round_table_cli.py "Erstelle ein User Management Modul"

# Mit Sprach-Auswahl
python round_table_cli.py "Entwickle eine API für Produktverwaltung" --language python

# TypeScript Code generieren
python round_table_cli.py "Baue eine React Login Komponente" --language typescript

# Interaktiver Modus
python round_table_cli.py --interactive
```

### 2. Integration mit Auto-Coder

```bash
# Mit Round Table
python auto_coder.py "Erstelle eine Flask API" --round-table

# Interaktiv mit Round Table Option
python auto_coder.py --interactive
# Dann: Wähle "j" bei "Runden Tisch nutzen?"
```

### 3. Programmatische Verwendung

```python
import asyncio
from round_table import RoundTable

async def main():
    # Initialisiere Round Table
    round_table = RoundTable()
    
    # Starte Diskussion
    result = await round_table.discuss(
        task="Erstelle ein Authentication Modul",
        context={
            'language': 'python',
            'project_type': 'api'
        }
    )
    
    # Zeige Ergebnis
    print(result.consensus_code)
    print(result.final_recommendation)

asyncio.run(main())
```

## Modi

### Simulations-Modus (Standard)

Wenn keine API-Keys konfiguriert sind, läuft der Round Table im Simulations-Modus:

- ✅ Funktioniert ohne API-Keys
- ✅ Demonstriert das Konzept
- ✅ Generiert qualitativ hochwertigen Code
- ✅ Zeigt Diskussions-Prozess

### Echter API-Modus (Geplant)

Mit konfigurierten API-Keys nutzt der Round Table echte KI-Modelle:

```yaml
# config.yaml
api_keys:
  openai: "sk-..."
  anthropic: "sk-ant-..."
  google: "..."
  xai: "..."
```

## Ausgabe-Beispiel

```
======================================================================
🤖 RUNDER TISCH ERGEBNIS
======================================================================

📋 Aufgabe: Erstelle ein User Management Modul
⏰ Zeitstempel: 2024-12-11 15:30:45

======================================================================
💡 DISKUSSIONS-ZUSAMMENFASSUNG
======================================================================

GROK (Architektur & Design):
  Ich empfehle einen objektorientierten Ansatz mit klaren Schnittstellen...

CLAUDE (Code-Qualität & Wartbarkeit):
  Fokus auf Wartbarkeit: Verwende Type Hints, Docstrings...

GPT (Best Practices & Dokumentation):
  Nutze bewährte Design Patterns, dokumentiere gründlich...

GEMINI (Performance & Skalierbarkeit):
  Denke an Skalierbarkeit: Nutze async/await für I/O-Operationen...

======================================================================
📝 GENERIERTER KONSENS-CODE
======================================================================

[Vollständiger, optimierter Code hier...]

======================================================================
📝 FINALE EMPFEHLUNG

Der Konsens-Code vereint die Expertise aller 4 KI-Modelle:

✅ Architektur (Grok): Objektorientierter Ansatz mit klaren Schnittstellen
✅ Qualität (Claude): Type Hints, Docstrings und SOLID-Prinzipien  
✅ Best Practices (GPT): Design Patterns und umfassende Dokumentation
✅ Performance (Gemini): Async/await und Caching-Strategien

📊 Durchschnittliches Vertrauen: 88%
======================================================================
```

## CLI Optionen

```bash
python round_table_cli.py --help

Optionen:
  -l, --language {python,javascript,typescript,java,go,rust}
                        Programmiersprache für den generierten Code
  -t, --project-type {web_app,api,cli,library,module}
                        Art des Projekts
  -o, --output FILE     Ausgabedatei für den generierten Code
  -i, --interactive     Interaktiver Modus
```

## Unterstützte Sprachen

- 🐍 Python
- 📜 JavaScript
- 📘 TypeScript
- ☕ Java
- 🐹 Go
- 🦀 Rust

## Workflow

```
Benutzer-Eingabe
    ↓
Task-Analyse
    ↓
Runder Tisch Diskussion
    ├── Grok → Architektur-Empfehlung
    ├── Claude → Qualitäts-Analyse
    ├── GPT → Best-Practice-Review
    └── Gemini → Performance-Optimierung
    ↓
Konsens-Bildung
    ↓
Code-Generierung
    ↓
Formatierte Ausgabe
    ├── Konsens-Code
    ├── Diskussions-Protokoll
    └── Finale Empfehlung
```

## Integration in eigene Projekte

```python
from round_table import RoundTable, AIModel, RoundTableResult

# Einfache Integration
async def generate_with_round_table(task: str):
    rt = RoundTable()
    result = await rt.discuss(task)
    return result.consensus_code

# Erweiterte Nutzung
async def advanced_usage():
    rt = RoundTable(config={'api_keys': {...}})
    
    result = await rt.discuss(
        task="Komplexe Aufgabe",
        context={
            'language': 'python',
            'project_type': 'api',
            'dependencies': ['fastapi', 'sqlalchemy']
        }
    )
    
    # Zugriff auf einzelne Antworten
    for response in result.individual_responses:
        print(f"{response.model.value}: {response.recommendation}")
    
    # Formatierte Ausgabe
    formatted = rt.format_result(result)
    print(formatted)
```

## Vorteile des Round Table

### Für Entwickler
- 📈 Höhere Code-Qualität durch Multi-AI Review
- 🎯 Verschiedene Perspektiven auf Probleme
- 📚 Lernen von Best Practices aller Modelle
- ⚡ Schnellere Entwicklung komplexer Features

### Für Teams
- 🤝 Konsistenter Code-Stil
- 📖 Automatische Dokumentation
- 🔍 Eingebaute Code-Reviews
- 🎓 Wissenstransfer durch Empfehlungen

### Für Projekte
- 🏗️ Solide Architektur von Anfang an
- 🔧 Wartbarer und erweiterbarer Code
- ⚡ Performance-optimiert
- 📊 Skalierbar designed

## Beispiele

### Python API Modul

```bash
python round_table_cli.py "Erstelle ein FastAPI Modul für User Authentication" \
  --language python \
  --project-type api \
  --output auth_module.py
```

### TypeScript React Komponente

```bash
python round_table_cli.py "Entwickle eine wiederverwendbare Button Komponente" \
  --language typescript \
  --project-type web_app \
  --output Button.tsx
```

### Go Microservice

```bash
python round_table_cli.py "Baue einen REST API Handler für Produktverwaltung" \
  --language go \
  --project-type api \
  --output handlers.go
```

## Nächste Schritte

1. **Teste den Round Table**:
   ```bash
   python round_table_cli.py --interactive
   ```

2. **Integriere in dein Projekt**:
   ```python
   from round_table import RoundTable
   ```

3. **Konfiguriere API-Keys** (optional):
   Kopiere `config.yaml.example` zu `config.yaml`

4. **Erweitere und Anpasse**:
   Der Code ist modular und leicht erweiterbar

## FAQ

**Q: Funktioniert es ohne API-Keys?**  
A: Ja! Der Simulations-Modus generiert hochwertigen Code ohne APIs.

**Q: Welche Sprachen werden unterstützt?**  
A: Python, JavaScript, TypeScript, Java, Go, Rust und mehr geplant.

**Q: Kann ich eigene Modelle hinzufügen?**  
A: Ja, der Code ist modular und erweiterbar.

**Q: Ist der generierte Code produktionsreif?**  
A: Er ist ein sehr guter Ausgangspunkt, sollte aber reviewt und getestet werden.

## Lizenz

MIT License - siehe LICENSE Datei

## Support

- 🐛 Issues: GitHub Issues
- 💬 Diskussionen: GitHub Discussions
- 📖 Dokumentation: Diese README

---

**Gebaut mit ❤️ für besseren Code durch KI-Kollaboration**
