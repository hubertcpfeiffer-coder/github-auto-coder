# GitHub Auto-Coder - Verwendungsanleitung

## 🚀 Schnellstart

### 1. Installation

```bash
# Repository klonen
git clone https://github.com/IHR-USERNAME/github-auto-coder.git
cd github-auto-coder

# Installation durchführen
chmod +x setup.sh
./setup.sh
```

### 2. GitHub Token einrichten

**Schritt-für-Schritt:**

1. Gehe zu GitHub: https://github.com/settings/tokens
2. Klicke auf **"Generate new token"** → **"Generate new token (classic)"**
3. Token-Details:
   - **Note**: `GitHub Auto-Coder` (oder einen Namen deiner Wahl)
   - **Expiration**: Wähle eine Ablaufzeit (empfohlen: 90 Tage)
   - **Scopes**: Wähle folgende Berechtigungen:
     - ✅ **repo** (alle Unteroptionen werden automatisch aktiviert)
       - repo:status
       - repo_deployment
       - public_repo
       - repo:invite
       - security_events
4. Scrolle nach unten und klicke **"Generate token"**
5. **WICHTIG**: Kopiere den Token sofort (er wird nur einmal angezeigt!)
6. Öffne `config.json` und füge den Token ein:

```json
{
  "github_token": "ghp_IhrTokenHier123456789...",
  "github_username": "IhrGitHubUsername"
}
```

### 3. Erste Verwendung

**Kommandozeile:**
```bash
python auto_coder.py "Erstelle eine Python Flask Webapplikation"
```

**Interaktiver Modus:**
```bash
python auto_coder.py --interactive
```

**Web-Interface:**
```bash
python web_interface.py
# Öffne http://localhost:5000 im Browser
```

## 💡 Verwendungsbeispiele

### Beispiel 1: Web-Applikation

```bash
python auto_coder.py "Erstelle eine Flask Web-App mit Login-System und SQLite-Datenbank"
```

**Ergebnis:**
- ✅ Repository: `flask-web-app-login-system`
- 📁 Ordnerstruktur: `app/`, `templates/`, `static/`, `tests/`
- 🐍 Python Code mit Flask, SQLAlchemy
- 📝 README.md, requirements.txt, .gitignore
- 🚀 Automatisch auf GitHub gepusht

### Beispiel 2: React Frontend

```bash
python auto_coder.py "Erstelle ein React Dashboard mit Charts" --repo-name my-dashboard
```

**Ergebnis:**
- ✅ Repository: `my-dashboard` (eigener Name)
- ⚛️ React-Komponenten
- 📦 package.json mit Dependencies
- 🎨 Modernes Dashboard-Layout

### Beispiel 3: REST API

```bash
python auto_coder.py "Erstelle eine FastAPI REST API mit Authentifizierung" --private
```

**Ergebnis:**
- 🔒 Privates Repository
- 🚀 FastAPI-Setup
- 🔐 JWT-Authentifizierung
- 📊 Swagger-Dokumentation

### Beispiel 4: Nur lokal (kein GitHub)

```bash
python auto_coder.py "Erstelle ein Python CLI-Tool für Datei-Backup" --local-only
```

**Ergebnis:**
- 📁 Nur lokale Dateien (kein GitHub-Push)
- ✅ Vollständige Projektstruktur

### Beispiel 5: Data Science Projekt

```bash
python auto_coder.py "Erstelle ein Jupyter Notebook Projekt für Verkaufsdaten-Analyse"
```

**Ergebnis:**
- 📓 Jupyter Notebooks
- 🐼 Pandas, NumPy, Matplotlib
- 📊 Beispiel-Notebooks für Datenanalyse

## 🎯 Unterstützte Projekttypen

| Typ | Schlüsselwörter | Beispiel |
|-----|----------------|----------|
| **Web App** | webapp, web app, website, dashboard | "Erstelle eine Django Blog-Website" |
| **REST API** | api, rest, graphql, backend | "Erstelle eine Express REST API" |
| **CLI Tool** | cli, command line, terminal | "Erstelle ein Python CLI für Datei-Konvertierung" |
| **Library** | library, package, modul | "Erstelle eine Python-Library für JSON-Validierung" |
| **Bot** | bot, chatbot, discord, telegram | "Erstelle einen Discord-Bot" |
| **Data Science** | data, analyse, jupyter, ml | "Erstelle ein ML-Projekt mit TensorFlow" |
| **Mobile App** | mobile, app, react native | "Erstelle eine React Native Todo-App" |
| **Desktop App** | desktop, gui, electron | "Erstelle eine Electron Desktop-App" |

## 🔧 Kommandozeilen-Optionen

```bash
python auto_coder.py [AUFGABE] [OPTIONEN]

Optionen:
  -r, --repo-name NAME     Spezifischer Repository-Name
  -l, --local-only         Nur lokal generieren (kein GitHub)
  -p, --private            Privates Repository erstellen
  -c, --config PATH        Pfad zur Config-Datei (Standard: config.json)
  -i, --interactive        Interaktiver Modus
  -h, --help              Hilfe anzeigen
```

## 🌐 Web-Interface

Das Web-Interface bietet eine benutzerfreundliche grafische Oberfläche:

```bash
python web_interface.py
```

Dann öffne im Browser: http://localhost:5000

**Features:**
- 📝 Formular für Projektbeschreibung
- 💡 Vorgefertigte Beispiele zum Anklicken
- 🎨 Moderne, responsive UI
- ✅ Echtzeit-Feedback

## 🔍 Erweiterte Verwendung

### Interaktiver Modus

Im interaktiven Modus kannst du mehrere Projekte nacheinander erstellen:

```bash
python auto_coder.py --interactive

>>> Erstelle eine Flask API
Repository-Name (Enter für automatisch): 
>>> my-api
Privates Repository? (j/n, Standard: n): 
>>> n
Nur lokal generieren? (j/n, Standard: n): 
>>> n

[Projekt wird erstellt...]

Bereit für die nächste Aufgabe!

>>> Erstelle eine React App
...
```

### Python-API verwenden

Du kannst den Auto-Coder auch in deinen eigenen Python-Skripten verwenden:

```python
from auto_coder import GitHubAutoCoder

# Initialisieren
coder = GitHubAutoCoder(config_path='config.json')

# Projekt erstellen
result = coder.create_project(
    task_description="Erstelle eine FastAPI mit PostgreSQL",
    repo_name="my-fastapi-project",
    local_only=False,
    private=True
)

# Ergebnis anzeigen
print(f"Repository URL: {result['repo_url']}")
print(f"Lokaler Pfad: {result['local_path']}")
print(f"Dateien: {len(result['files'])}")
```

### Konfiguration anpassen

Bearbeite `config.json` für erweiterte Einstellungen:

```json
{
  "github_token": "ghp_...",
  "github_username": "username",
  "default_branch": "main",
  "auto_push": true,
  "create_readme": true,
  "add_gitignore": true,
  "default_license": "MIT",
  "max_file_size": 1048576,
  "templates_path": "./templates",
  "rate_limit_delay": 1.0
}
```

## 🐛 Fehlerbehebung

### Problem: "Authentication failed"

**Lösung:**
- Überprüfe deinen GitHub Token in `config.json`
- Stelle sicher, dass der Token `repo`-Berechtigungen hat
- Prüfe, ob der Token nicht abgelaufen ist

### Problem: "Repository already exists"

**Lösung 1** - Anderen Namen verwenden:
```bash
python auto_coder.py "Erstelle eine Flask App" --repo-name meine-neue-app
```

**Lösung 2** - Existierendes Repo löschen (Vorsicht!):
```python
from github_client import GitHubClient
client = GitHubClient()
client.delete_repository('repo-name')
```

### Problem: "Rate limit exceeded"

**Lösung:**
- Warte eine Stunde (GitHub API Limit: 5000 Requests/Stunde)
- Oder erhöhe `rate_limit_delay` in config.json auf 2.0

### Problem: "Config file not found"

**Lösung:**
```bash
cp config.example.json config.json
# Dann Token in config.json einfügen
```

## 📊 Rate Limits

GitHub API hat folgende Limits:

- ✅ **Authentifiziert**: 5000 Requests/Stunde
- ❌ **Nicht authentifiziert**: 60 Requests/Stunde

Der Auto-Coder zeigt dir nach jedem Projekt die verbleibenden Requests an.

## 🔒 Sicherheit

**Wichtige Sicherheitshinweise:**

1. ⚠️ **Token nie committen**: Füge `config.json` zu `.gitignore` hinzu
2. 🔐 **Token-Berechtigungen**: Nutze minimal notwendige Berechtigungen
3. 🕐 **Token-Ablauf**: Setze ein Ablaufdatum (z.B. 90 Tage)
4. 🔄 **Token erneuern**: Erneuere regelmäßig deinen Token

## 💡 Tipps & Tricks

### Tipp 1: Präzise Beschreibungen

**Gut:**
```bash
"Erstelle eine Flask-Webapplikation mit Login-System, SQLite-Datenbank und Admin-Dashboard"
```

**Weniger gut:**
```bash
"Erstelle eine Web-App"
```

### Tipp 2: Technologie spezifizieren

Erwähne spezifische Technologien:
- "mit Flask" statt nur "Python"
- "mit React" statt nur "JavaScript"
- "mit PostgreSQL" statt nur "Datenbank"

### Tipp 3: Features auflisten

```bash
"Erstelle eine Node.js API mit:
- Express Framework
- JWT Authentifizierung
- MongoDB Datenbank
- Rate Limiting
- Swagger Dokumentation"
```

## 🎓 Lernressourcen

- [GitHub API Dokumentation](https://docs.github.com/en/rest)
- [PyGithub Library](https://pygithub.readthedocs.io/)
- [Flask Dokumentation](https://flask.palletsprojects.com/)

## 🆘 Support

Bei Problemen:
1. Prüfe die Logs in der Konsole
2. Überprüfe deine config.json
3. Teste mit `--local-only` für lokale Fehlersuche
4. Erstelle ein Issue auf GitHub

## 📝 Lizenz

MIT License - Siehe LICENSE Datei für Details
