# 🤖 GitHub Auto-Coder

> **Automatisches GitHub-Programm für selbstständige Code-Generierung aus natürlichsprachlichen Aufgaben**

Ein intelligentes Automatisierungssystem, das natürlichsprachliche Programmieraufgaben entgegennimmt und automatisch vollständige GitHub-Repositories mit Code, Projektstruktur und Dokumentation erstellt.

---

## 🌟 Features

- ✅ **Natürlichsprachliche Eingabe**: Beschreiben Sie einfach, was Sie programmieren möchten
- ✅ **15+ Programmiersprachen**: Python, JavaScript, TypeScript, Java, Go, Rust, C++, C#, Ruby, PHP, Swift, Kotlin, Dart, Scala, R
- ✅ **Intelligente Projekterkennung**: Automatische Erkennung von Web-Apps, APIs, CLI-Tools, Mobile Apps, Data Science Projekten
- ✅ **Vollständige GitHub-Integration**: Erstellt automatisch Repositories, Commits und Push
- ✅ **Professioneller Code**: Best Practices, Dokumentation, Tests und README inklusive
- ✅ **Web + CLI Interface**: Benutzerfreundliche Weboberfläche und Kommandozeilen-Tool
- ✅ **Template-System**: Vorgefertigte Templates für häufige Projekttypen
- ✅ **Automatische Tests**: Generiert Unit-Tests für generierten Code

---

## 🚀 Schnellstart

### 1. Installation

```bash
# Repository klonen
git clone https://github.com/hubertcpfeiffer-coder/github-auto-coder.git
cd github-auto-coder

# Abhängigkeiten installieren
pip install -r requirements.txt

# Oder automatisches Setup-Skript verwenden
chmod +x setup.sh
./setup.sh
```

### 2. GitHub Token einrichten

1. Gehen Sie zu: https://github.com/settings/tokens
2. Klicken Sie "Generate new token (classic)"
3. Name: "Auto-Coder"
4. Wählen Sie: `repo` (alle Berechtigungen)
5. Klicken Sie "Generate token"
6. Kopieren Sie den Token

**Speichern Sie den Token:**

```bash
# Erstellen Sie eine .env Datei
echo "GITHUB_TOKEN=your_token_here" > .env
echo "GITHUB_USERNAME=your_username" >> .env
```

### 3. Erste Nutzung

#### **Kommandozeile:**

```bash
python auto_coder.py "Erstelle eine Flask REST API für ein To-Do List System"
```

#### **Web-Interface:**

```bash
python web_interface.py
# Öffnen Sie: http://localhost:5000
```

---

## 📋 Verwendungsbeispiele

### Beispiel 1: Python Flask API

```bash
python auto_coder.py "Erstelle eine Python Flask REST API mit CRUD-Operationen für eine Benutzerverwaltung"
```

**Resultat:**
- ✅ Neues GitHub Repository
- ✅ Flask-App mit Routen
- ✅ SQLAlchemy Datenbankmodelle
- ✅ API-Dokumentation
- ✅ requirements.txt
- ✅ README.md mit Anleitung

### Beispiel 2: React Frontend

```bash
python auto_coder.py "Entwickle eine React-App mit TypeScript für ein Dashboard mit Charts"
```

**Resultat:**
- ✅ React + TypeScript Setup
- ✅ Komponenten-Struktur
- ✅ Chart.js Integration
- ✅ Responsive Design
- ✅ package.json
- ✅ Deployment-Anleitung

### Beispiel 3: Data Science Projekt

```bash
python auto_coder.py "Erstelle ein Python Data Science Projekt für Sentiment-Analyse mit NLTK"
```

**Resultat:**
- ✅ Jupyter Notebooks
- ✅ Data Processing Scripts
- ✅ ML-Modell Training
- ✅ Visualisierungen
- ✅ requirements.txt
- ✅ Dokumentation

---

## 🛠️ Erweiterte Konfiguration

### Eigene Templates hinzufügen

Erstellen Sie eine Datei in `templates/custom_template.json`:

```json
{
  "name": "My Custom Template",
  "language": "python",
  "type": "web",
  "files": {
    "main.py": "# Your template code here",
    "config.py": "# Configuration template"
  }
}
```

### Mehrere Repositories auf einmal

```bash
python auto_coder.py --batch tasks.txt
```

**tasks.txt:**
```
Erstelle eine Flask API für User Management
Entwickle eine React Dashboard App
Baue ein CLI Tool für File Processing
```

---

## 📚 Dokumentation

- 📖 [**Schnellstart-Guide**](QUICKSTART.md) - Erste Schritte
- 📘 [**Verwendungsanleitung**](USAGE.md) - Detaillierte Nutzung
- 🔧 [**Installationsanleitung**](INSTALLATIONSANLEITUNG.md) - Setup-Details
- 🤝 [**Contributing**](CONTRIBUTING.md) - Entwickler-Leitfaden
- 🏗️ [**Projektstruktur**](PROJECT_STRUCTURE.md) - Code-Organisation

---

## 🎯 Unterstützte Projekttypen

| Kategorie | Beispiele |
|-----------|-----------|
| **Web Apps** | Flask, Django, Express, React, Vue, Angular |
| **APIs** | REST APIs, GraphQL, FastAPI, Spring Boot |
| **CLI Tools** | Command-line utilities, DevOps tools |
| **Mobile Apps** | React Native, Flutter, Swift |
| **Data Science** | Jupyter Notebooks, Pandas, scikit-learn |
| **Machine Learning** | TensorFlow, PyTorch, Model Training |
| **Desktop Apps** | Electron, PyQt, Tkinter |
| **Game Development** | Pygame, Unity Scripts, Godot |

---

## 🔒 Sicherheit

⚠️ **Wichtige Sicherheitshinweise:**

1. **Token-Sicherheit:**
   - Teilen Sie Ihren GitHub Token NIEMALS öffentlich
   - Verwenden Sie `.env` Dateien (sind in `.gitignore`)
   - Widerrufen Sie nicht mehr benötigte Tokens

2. **Fine-grained Tokens:**
   - Verwenden Sie Fine-grained Personal Access Tokens
   - Setzen Sie minimale Berechtigungen
   - Konfigurieren Sie Ablaufdatum (z.B. 30 Tage)

3. **Best Practices:**
   - Überprüfen Sie generierten Code vor dem Deploy
   - Verwenden Sie separate Tokens für Entwicklung/Produktion
   - Aktivieren Sie 2FA auf Ihrem GitHub-Account

Mehr Details: [GitHub_Zugriff_Optionen.md](GitHub_Zugriff_Optionen.md)

---

## 🤝 Beitragen

Wir freuen uns über Beiträge! So können Sie helfen:

1. **Fork** das Repository
2. **Clone** Ihren Fork
3. **Branch** erstellen: `git checkout -b feature/neue-funktion`
4. **Änderungen** committen: `git commit -m 'Add neue Funktion'`
5. **Push** zu GitHub: `git push origin feature/neue-funktion`
6. **Pull Request** erstellen

Siehe [CONTRIBUTING.md](CONTRIBUTING.md) für Details.

---

## 📜 Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert.

---

## 🙋 Support & Kontakt

- 🐛 **Issues**: [GitHub Issues](https://github.com/hubertcpfeiffer-coder/github-auto-coder/issues)
- 💬 **Diskussionen**: [GitHub Discussions](https://github.com/hubertcpfeiffer-coder/github-auto-coder/discussions)
- 📧 **Email**: [Ihr Email]

---

## 🌟 Roadmap

### Version 2.0 (geplant)

- [ ] AI-gestützte Code-Optimierung
- [ ] Multi-Repository Management
- [ ] Automatische Dependency Updates
- [ ] Cloud-Deployment Integration (AWS, Azure, GCP)
- [ ] Continuous Integration/Deployment Templates
- [ ] Code-Review Automatisierung
- [ ] Slack/Discord Integration
- [ ] Visual Programming Interface

---

## 📊 Statistiken

- ✅ **15+ Programmiersprachen** unterstützt
- ✅ **50+ Templates** verfügbar
- ✅ **1000+ Zeilen** generierter Code pro Projekt
- ✅ **100% Automatisierung** von Repository bis Deployment

---

## 🎓 Beispiel-Workflow

```
1. Eingabe: "Erstelle eine Flask API mit User Authentication"
           ↓
2. Task-Parser analysiert die Anfrage
           ↓
3. Code-Generator erstellt:
   - Flask App Setup
   - User Models
   - Authentication Routes
   - JWT Token System
   - Database Migration
   - Unit Tests
           ↓
4. GitHub-Client erstellt Repository
           ↓
5. Alle Dateien werden committed & gepusht
           ↓
6. ✅ Fertiges Projekt auf GitHub!
```

---

<div align="center">

**Gebaut mit ❤️ für Entwickler, die ihre Produktivität maximieren wollen**

[⭐ Star dieses Projekt](https://github.com/hubertcpfeiffer-coder/github-auto-coder) | [🐛 Report Bug](https://github.com/hubertcpfeiffer-coder/github-auto-coder/issues) | [✨ Request Feature](https://github.com/hubertcpfeiffer-coder/github-auto-coder/issues)

</div>
