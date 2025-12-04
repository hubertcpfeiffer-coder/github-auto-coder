# Contributing to GitHub Auto-Coder

Vielen Dank für dein Interesse, zu GitHub Auto-Coder beizutragen! 🎉

## 🚀 Wie kann ich beitragen?

Es gibt viele Möglichkeiten, wie du helfen kannst:

- 🐛 **Bug Reports**: Gefundene Fehler melden
- 💡 **Feature Requests**: Neue Funktionen vorschlagen
- 📝 **Dokumentation**: Dokumentation verbessern
- 💻 **Code**: Bugfixes und neue Features implementieren
- 🌍 **Übersetzungen**: Weitere Sprachen hinzufügen

## 📋 Entwicklungs-Setup

### 1. Repository forken

Klicke auf "Fork" oben rechts auf der GitHub-Seite.

### 2. Repository klonen

```bash
git clone https://github.com/DEIN-USERNAME/github-auto-coder.git
cd github-auto-coder
```

### 3. Development-Umgebung einrichten

```bash
# Virtual Environment erstellen
python3 -m venv venv
source venv/bin/activate

# Dependencies installieren
pip install -r requirements.txt

# Dev-Dependencies installieren
pip install pytest pytest-cov black flake8 mypy
```

### 4. Branch erstellen

```bash
git checkout -b feature/meine-neue-funktion
```

## 🧪 Testing

Stelle sicher, dass alle Tests erfolgreich durchlaufen:

```bash
# Alle Tests ausführen
pytest

# Tests mit Coverage
pytest --cov=. --cov-report=html
```

## 📏 Code-Style

Wir verwenden:
- **Black** für Code-Formatierung
- **Flake8** für Linting
- **MyPy** für Type-Checking

```bash
# Code formatieren
black .

# Linting
flake8 .

# Type-Checking
mypy .
```

## 🎯 Pull Request Prozess

### 1. Änderungen committen

```bash
git add .
git commit -m "feat: Add support for Go projects"
```

**Commit Message Format:**
- `feat:` Neue Funktion
- `fix:` Bugfix
- `docs:` Dokumentation
- `style:` Formatierung
- `refactor:` Code-Refactoring
- `test:` Tests hinzufügen
- `chore:` Wartung

### 2. Branch pushen

```bash
git push origin feature/meine-neue-funktion
```

### 3. Pull Request erstellen

1. Gehe zu deinem Fork auf GitHub
2. Klicke "Compare & pull request"
3. Fülle die PR-Beschreibung aus
4. Verlinke relevante Issues

## 🐛 Bug Reports

Gute Bug Reports enthalten:

1. **Beschreibung**: Was ist das Problem?
2. **Schritte zum Reproduzieren**: Wie kann man den Bug nachstellen?
3. **Erwartetes Verhalten**: Was sollte passieren?
4. **Tatsächliches Verhalten**: Was passiert stattdessen?
5. **Umgebung**: OS, Python-Version, relevante Logs

## 💡 Feature Requests

Gute Feature Requests enthalten:

1. **Problem**: Welches Problem wird gelöst?
2. **Lösung**: Wie soll die Funktion aussehen?
3. **Alternativen**: Welche Alternativen wurden erwogen?
4. **Zusätzlicher Kontext**: Screenshots, Beispiele, etc.

## 📚 Dokumentation verbessern

- README.md aktualisieren
- USAGE.md erweitern
- Code-Kommentare hinzufügen
- Beispiele hinzufügen

## 🌍 Übersetzungen

Wir würden uns über Übersetzungen freuen!

1. Kopiere README.md zu README.{SPRACHE}.md
2. Übersetze den Inhalt
3. Erstelle einen Pull Request

## 📜 Code of Conduct

Sei respektvoll und freundlich zu allen Contributors!

## 🎉 Danke!

Vielen Dank für deinen Beitrag zu GitHub Auto-Coder! 🚀
