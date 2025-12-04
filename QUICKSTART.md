# 🚀 Schnellstart-Anleitung

## In 5 Minuten loslegen!

### Schritt 1: Installation (2 Minuten)

```bash
# Klonen
git clone https://github.com/IHR-USERNAME/github-auto-coder.git
cd github-auto-coder

# Installieren
./setup.sh
```

### Schritt 2: GitHub Token (2 Minuten)

1. Gehe zu: https://github.com/settings/tokens/new
2. Name: `Auto-Coder`
3. Berechtigung: ✅ repo
4. Klicke "Generate token"
5. Kopiere den Token

Öffne `config.json`:
```json
{
  "github_token": "DEIN_TOKEN_HIER",
  "github_username": "DEIN_USERNAME"
}
```

### Schritt 3: Erstes Projekt erstellen (1 Minute)

```bash
python auto_coder.py "Erstelle eine Flask Web-App mit Login-System"
```

**Fertig!** 🎉

Dein Projekt ist auf GitHub: https://github.com/DEIN-USERNAME/PROJEKT-NAME

---

## Weitere Beispiele

**Python CLI-Tool:**
```bash
python auto_coder.py "Erstelle ein Python CLI-Tool für Datei-Backup"
```

**React Dashboard:**
```bash
python auto_coder.py "Erstelle ein React Dashboard mit Charts"
```

**FastAPI:**
```bash
python auto_coder.py "Erstelle eine FastAPI REST API mit Datenbank"
```

**Interaktiv:**
```bash
python auto_coder.py --interactive
```

**Web-Interface:**
```bash
python web_interface.py
# Öffne: http://localhost:5000
```

---

## Hilfe

```bash
python auto_coder.py --help
```

Mehr Infos: [USAGE.md](USAGE.md)
