# GitHub Auto-Coder - Projektstruktur

## 📁 Komplette Verzeichnisstruktur

```
github-auto-coder/
├── README.md                   # Hauptdokumentation
├── QUICKSTART.md              # 5-Minuten Schnellstart
├── USAGE.md                   # Ausführliche Verwendungsanleitung
├── CONTRIBUTING.md            # Beitragsrichtlinien
├── LICENSE                    # MIT Lizenz
├── .gitignore                # Git-Ignores
│
├── requirements.txt           # Python-Dependencies
├── config.example.json        # Beispiel-Konfiguration
├── config.json               # Ihre Konfiguration (wird ignoriert)
│
├── setup.sh                  # Installationsskript
├── demo.py                   # Demo-Skript
│
├── auto_coder.py            # 🎯 HAUPTPROGRAMM (CLI)
├── github_client.py         # GitHub API Client
├── task_parser.py           # Task-Analyse
├── code_generator.py        # Code-Generierung
├── web_interface.py         # Web-UI Server
│
├── templates/               # Template-Verzeichnis
│   ├── index.html          # Web-UI Template
│   ├── python_cli/         # Python CLI Templates
│   │   └── main.py
│   ├── web_app/           # Web-App Templates
│   │   └── app.py
│   └── api/               # API Templates
│       └── main.py
│
└── tests/                  # Unit-Tests
    ├── __init__.py
    └── test_auto_coder.py
```

## 🏗️ System-Architektur

```
┌─────────────────────────────────────────────────────────────┐
│                         BENUTZER                             │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
        ┌──────────────────────────────────────┐
        │        Eingabe-Interfaces             │
        ├──────────────────────────────────────┤
        │  • CLI (auto_coder.py)               │
        │  • Web-UI (web_interface.py)         │
        │  • Python-API (GitHubAutoCoder)      │
        └──────────────────────────────────────┘
                            │
                            ▼
        ┌──────────────────────────────────────┐
        │      Task Parser (task_parser.py)     │
        ├──────────────────────────────────────┤
        │  • Sprache erkennen                   │
        │  • Projekt-Typ bestimmen              │
        │  • Dependencies ermitteln             │
        │  • Ordnerstruktur planen              │
        │  → ProjectPlan erstellen              │
        └──────────────────────────────────────┘
                            │
                            ▼
        ┌──────────────────────────────────────┐
        │  Code Generator (code_generator.py)   │
        ├──────────────────────────────────────┤
        │  • README.md generieren               │
        │  • Code-Dateien erstellen             │
        │  • Tests generieren                   │
        │  • Config-Dateien erstellen           │
        │  → Dateien-Dictionary                 │
        └──────────────────────────────────────┘
                            │
                            ▼
        ┌──────────────────────────────────────┐
        │   GitHub Client (github_client.py)    │
        ├──────────────────────────────────────┤
        │  • Repository erstellen               │
        │  • Dateien hochladen                  │
        │  • Commits erstellen                  │
        │  → GitHub Repository                  │
        └──────────────────────────────────────┘
                            │
                            ▼
        ┌──────────────────────────────────────┐
        │             ERGEBNIS                  │
        ├──────────────────────────────────────┤
        │  • Lokales Projekt-Verzeichnis       │
        │  • GitHub Repository (optional)       │
        │  • Vollständige Projektstruktur      │
        └──────────────────────────────────────┘
```

## 🔄 Datenfluss

1. **Eingabe**: "Erstelle eine Flask Web-App mit Login"
   
2. **Task Parser**:
   - Erkennt: Sprache = Python
   - Erkennt: Typ = web_app
   - Erkennt: Framework = Flask
   - Plant: Ordner (app/, templates/, static/, tests/)
   - Sammelt: Dependencies (flask, flask-cors)

3. **Code Generator**:
   - Generiert: README.md (mit Projekt-Info)
   - Generiert: requirements.txt (mit Dependencies)
   - Generiert: app/main.py (Flask-Setup)
   - Generiert: templates/index.html (HTML-Template)
   - Generiert: tests/test_main.py (Unit-Tests)
   - Generiert: .gitignore, LICENSE, CI/CD

4. **GitHub Client**:
   - Erstellt: Repository "flask-web-app-login"
   - Uploadet: Alle generierten Dateien
   - Committed: "Initial commit"

5. **Ergebnis**:
   - Lokal: ./flask-web-app-login/
   - GitHub: https://github.com/username/flask-web-app-login

## 📦 Modul-Übersicht

### auto_coder.py
**Hauptprogramm mit CLI und Orchestrierung**

Klassen:
- `GitHubAutoCoder`: Hauptklasse, koordiniert alle Komponenten

Funktionen:
- `create_project()`: Erstellt komplettes Projekt
- `interactive_mode()`: Interaktiver Modus
- `main()`: CLI Entry Point

### task_parser.py
**Intelligente Task-Analyse**

Klassen:
- `TaskParser`: Analysiert natürlichsprachliche Aufgaben
- `ProjectPlan`: Datenklasse für Projektplan

Features:
- Sprach-Erkennung (15+ Sprachen)
- Projekt-Typ-Erkennung (10+ Typen)
- Dependency-Ermittlung
- Feature-Extraktion

### code_generator.py
**Code-Generierung für alle Sprachen**

Klassen:
- `CodeGenerator`: Generiert Code-Dateien

Funktionen:
- `generate_files()`: Hauptfunktion
- `_generate_python_code()`: Python-spezifisch
- `_generate_js_code()`: JavaScript/TypeScript
- `_generate_java_code()`: Java
- `_generate_go_code()`: Go

### github_client.py
**GitHub API Integration**

Klassen:
- `GitHubClient`: Wrapper für PyGithub

Funktionen:
- `create_repository()`: Erstellt Repo
- `create_file()`: Erstellt einzelne Datei
- `create_multiple_files()`: Bulk-Upload
- `check_rate_limit()`: Rate-Limit prüfen

### web_interface.py
**Flask Web-UI**

Endpoints:
- `GET /`: Hauptseite
- `POST /api/create`: Projekt erstellen
- `GET /api/examples`: Beispiele laden
- `GET /api/health`: Health Check

## 🎯 Verwendungs-Workflows

### Workflow 1: CLI - Einfach
```bash
python auto_coder.py "Erstelle eine Flask App"
```

### Workflow 2: CLI - Erweitert
```bash
python auto_coder.py "Erstelle eine React App" \
  --repo-name my-dashboard \
  --private \
  --local-only
```

### Workflow 3: Interaktiv
```bash
python auto_coder.py --interactive
>>> Erstelle eine FastAPI
>>> my-api
>>> n
>>> n
```

### Workflow 4: Web-UI
```bash
python web_interface.py
# Browser → http://localhost:5000
# Formular ausfüllen → Submit
```

### Workflow 5: Python-API
```python
from auto_coder import GitHubAutoCoder

coder = GitHubAutoCoder()
result = coder.create_project("Erstelle ein CLI-Tool")
print(result['repo_url'])
```

## 🧪 Testing-Struktur

```
tests/
├── test_auto_coder.py      # Integration Tests
├── test_task_parser.py     # Parser Tests
├── test_code_generator.py  # Generator Tests
└── test_github_client.py   # GitHub API Tests
```

Ausführen:
```bash
pytest                    # Alle Tests
pytest tests/test_*.py   # Spezifischer Test
pytest --cov             # Mit Coverage
```

## 📊 Unterstützte Sprachen & Frameworks

| Sprache | Frameworks | Projekt-Typen |
|---------|-----------|---------------|
| Python | Flask, Django, FastAPI, Pandas | Web, API, CLI, Data Science |
| JavaScript | React, Vue, Angular, Express | Web, API, CLI |
| TypeScript | React, Angular, Express | Web, API |
| Java | Spring Boot, Maven | API, Desktop |
| Go | Gin, Echo | API, CLI, Microservices |
| Rust | Cargo | CLI, Systems |
| Ruby | Rails | Web, API |
| PHP | Laravel, Symfony | Web, API |

## 🔧 Konfiguration

```json
{
  "github_token": "ghp_...",           // GitHub Personal Access Token
  "github_username": "username",        // Ihr GitHub-Username
  "default_branch": "main",            // Default Branch
  "auto_push": true,                   // Automatisch auf GitHub pushen
  "create_readme": true,               // README erstellen
  "add_gitignore": true,              // .gitignore hinzufügen
  "default_license": "MIT",           // Standard-Lizenz
  "max_file_size": 1048576,          // Max Dateigröße (1MB)
  "templates_path": "./templates",    // Template-Pfad
  "rate_limit_delay": 1.0            // Delay zwischen API-Calls
}
```

## 🚀 Deployment

### Lokal
```bash
python auto_coder.py "..."
```

### Docker (Optional)
```dockerfile
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "web_interface.py"]
```

### Cloud (Heroku, Railway, etc.)
```bash
# Procfile
web: python web_interface.py
```

## 📈 Erweiterungen

Mögliche zukünftige Features:
- [ ] AI-gestützte Code-Generierung (GPT-4)
- [ ] Template-Management-System
- [ ] Multi-Repository-Projekte
- [ ] Deployment-Integration (Heroku, Vercel)
- [ ] Code-Qualität-Checks
- [ ] Automatische Tests
- [ ] Docker-Integration
- [ ] CI/CD-Pipeline-Generierung

## 🔗 Wichtige Links

- [GitHub API Docs](https://docs.github.com/en/rest)
- [PyGithub Docs](https://pygithub.readthedocs.io/)
- [Flask Docs](https://flask.palletsprojects.com/)
