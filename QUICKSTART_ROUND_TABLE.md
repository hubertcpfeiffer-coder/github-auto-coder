# 🚀 Quick Start - Round Table System

## In 5 Minuten zum ersten Round Table Code

### 1. Einfachster Start

```bash
# Direkt nutzen - kein Setup nötig!
python round_table_cli.py "Erstelle ein User Management Modul"
```

### 2. Interaktiv nutzen

```bash
python round_table_cli.py --interactive
```

Dann einfach beschreiben was du brauchst!

### 3. Mit Auto-Coder

```bash
python auto_coder.py "Erstelle eine REST API" --round-table --local-only
```

### 4. Demo ausprobieren

```bash
python demo_round_table.py
# Wähle Demo 1-5 oder 'all'
```

## Beispiele

### Python Modul generieren

```bash
python round_table_cli.py "Erstelle ein Logging-Modul" \
  --language python \
  --output logger.py
```

**Ergebnis:**
- ✅ `logger.py` - Fertiger Code mit Best Practices
- ✅ `logger_discussion.md` - Dokumentation der KI-Diskussion

### TypeScript Komponente

```bash
python round_table_cli.py "Entwickle eine Button Komponente" \
  --language typescript \
  --project-type web_app \
  --output Button.tsx
```

### Java API Handler

```bash
python round_table_cli.py "Baue einen REST Controller für User Management" \
  --language java \
  --project-type api \
  --output UserController.java
```

## Was bekommst du?

### 1. Konsens-Code
Optimierter Code der die Expertise von 4 KI-Modellen vereint:
- 🏛️ Grok: Architektur
- ✨ Claude: Code-Qualität
- 📚 GPT: Best Practices
- ⚡ Gemini: Performance

### 2. Diskussions-Dokumentation
Detaillierte Erklärungen warum der Code so ist wie er ist.

### 3. Empfehlungen
Nächste Schritte und Verbesserungsvorschläge.

## Ohne Installation nutzen

Das System funktioniert **sofort** ohne API-Keys:

```python
import asyncio
from round_table import RoundTable

async def main():
    rt = RoundTable()  # Kein Setup nötig!
    
    result = await rt.discuss(
        "Erstelle ein Validation Modul",
        {'language': 'python'}
    )
    
    print(result.consensus_code)

asyncio.run(main())
```

## Nächste Schritte

1. **Teste verschiedene Aufgaben**
   ```bash
   python round_table_cli.py --interactive
   ```

2. **Integriere in dein Projekt**
   ```python
   from round_table import RoundTable
   ```

3. **Lies die Dokumentation**
   - [ROUND_TABLE.md](ROUND_TABLE.md) - Vollständige Anleitung
   - [README.md](README.md) - Übersicht

## Tipps

✅ **Sei spezifisch:** "Erstelle ein User Auth Modul mit JWT" ist besser als "Auth"

✅ **Wähle die Sprache:** Nutze `--language` für bessere Ergebnisse

✅ **Speichere den Code:** Nutze `--output` um Dateien zu erstellen

✅ **Experimentiere:** Der Round Table ist schnell und kostenlos im Simulations-Modus

## Häufige Fragen

**Q: Brauche ich API-Keys?**
A: Nein! Funktioniert sofort im Simulations-Modus.

**Q: Welche Sprachen?**
A: Python, JavaScript, TypeScript, Java, Go, Rust

**Q: Ist der Code produktionsreif?**
A: Sehr guter Ausgangspunkt, aber immer reviewen!

**Q: Kann ich es in meinem Projekt nutzen?**
A: Ja! Importiere einfach `from round_table import RoundTable`

---

**Viel Erfolg! 🚀**

Bei Fragen: Siehe [ROUND_TABLE.md](ROUND_TABLE.md) für Details
