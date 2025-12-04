# GitHub Auto-Coder - Vollständige Installationsanleitung

## 📋 Inhaltsverzeichnis

1. Voraussetzungen
2. GitHub Personal Access Token erstellen
3. Repository auf GitHub hochladen
4. Lokale Installation
5. Konfiguration
6. Erste Nutzung
7. Beispiele
8. Fehlerbehebung

---

## 1. Voraussetzungen

Bevor Sie beginnen, stellen Sie sicher, dass Sie folgendes haben:

- **GitHub-Account**: Ein aktiver GitHub-Account
- **Python 3.8+**: Installiert auf Ihrem System
- **Git**: Installiert für Repository-Verwaltung
- **Texteditor**: VS Code, Sublime Text, oder ähnliches

**Python-Installation prüfen:**
```bash
python --version
# oder
python3 --version
```

Sollte mindestens Python 3.8.0 oder höher anzeigen.

---

## 2. GitHub Personal Access Token erstellen

Der Token ermöglicht dem Programm, automatisch auf Ihr GitHub-Konto zuzugreifen.

### Schritt-für-Schritt Anleitung:

**Schritt 1:** Gehen Sie zu GitHub Settings
- Öffnen Sie [https://github.com](https://github.com)
- Klicken Sie oben rechts auf Ihr Profilbild
- Wählen Sie **Settings** (Einstellungen)

**Schritt 2:** Developer Settings öffnen
- Scrollen Sie in der linken Seitenleiste ganz nach unten
- Klicken Sie auf **Developer settings**

**Schritt 3:** Personal Access Token erstellen
- Klicken Sie auf **Personal access tokens**
- Wählen Sie **Tokens (classic)**
- Klicken Sie auf **Generate new token**
- Wählen Sie **Generate new token (classic)**

**Schritt 4:** Token konfigurieren
- **Note**: Geben Sie einen Namen ein, z.B. "Auto-Coder System"
- **Expiration**: Wählen Sie die Gültigkeitsdauer (empfohlen: 90 days oder No expiration)
- **Scopes**: Wählen Sie folgende Berechtigungen:
  - ✅ **repo** (alle Unterpunkte)
  - ✅ **workflow**
  - ✅ **admin:org** → **read:org**
  - ✅ **user** → **read:user**
  - ✅ **user** → **user:email**

**Schritt 5:** Token generieren und speichern
- Klicken Sie auf **Generate token** (grüner Button unten)
- **WICHTIG**: Kopieren Sie den Token SOFORT und speichern Sie ihn sicher!
- Der Token wird NUR EINMAL angezeigt!
- Format: `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

**⚠️ WICHTIG:** Behandeln Sie diesen Token wie ein Passwort! Teilen Sie ihn niemals öffentlich!

---

## 3. Repository auf GitHub hochladen

### Option A: Neues Repository erstellen (Empfohlen)

**Schritt 1:** Neues Repository auf GitHub erstellen
- Gehen Sie zu [https://github.com/new](https://github.com/new)
- **Repository name**: `github-auto-coder`
- **Description**: "Automatisches System zur Erstellung von GitHub-Projekten"
- **Visibility**: Public oder Private (Ihre Wahl)
- ❌ **NICHT** "Initialize with README" anklicken
- Klicken Sie auf **Create repository**

**Schritt 2:** Lokales Projekt initialisieren
```bash
# Navigieren Sie zum Projektordner (wo alle erstellten Dateien liegen)
cd /pfad/zum/github-auto-coder

# Git initialisieren
git init

# Alle Dateien hinzufügen
git add .

# Ersten Commit erstellen
git commit -m "Initial commit: GitHub Auto-Coder System"

# Remote Repository verbinden (ersetzen Sie USERNAME mit Ihrem GitHub-Nutzernamen)
git remote add origin https://github.com/USERNAME/github-auto-coder.git

# Auf GitHub hochladen
git branch -M main
git push -u origin main
```

**Schritt 3:** Überprüfung
- Öffnen Sie `https://github.com/USERNAME/github-auto-coder`
- Sie sollten alle Dateien sehen können

### Option B: Fork eines bestehenden Repositories

Falls Sie das Projekt von einem anderen Repository forken möchten:

```bash
# Repository klonen
git clone https://github.com/ORIGINAL-OWNER/github-auto-coder.git
cd github-auto-coder

# Ihren eigenen Fork als Remote hinzufügen
git remote set-url origin https://github.com/IHR-USERNAME/github-auto-coder.git
git push -u origin main
```

---

## 4. Lokale Installation

Jetzt installieren Sie das System auf Ihrem Computer, um es zu nutzen.

**Schritt 1:** Repository klonen (falls noch nicht geschehen)
```bash
# Navigieren Sie zu Ihrem gewünschten Arbeitsverzeichnis
cd ~/Projekte

# Repository klonen (ersetzen Sie USERNAME)
git clone https://github.com/USERNAME/github-auto-coder.git

# In das Verzeichnis wechseln
cd github-auto-coder
```

**Schritt 2:** Virtuelle Umgebung erstellen (empfohlen)
```bash
# Virtuelle Umgebung erstellen
python -m venv venv

# Aktivieren
# Für Linux/Mac:
source venv/bin/activate

# Für Windows:
venv\Scripts\activate
```

Sie sollten jetzt `(venv)` vor Ihrer Kommandozeile sehen.

**Schritt 3:** Dependencies installieren
```bash
# Alle erforderlichen Pakete installieren
pip install -r requirements.txt
```

Dies installiert:
- PyGithub (GitHub API)
- Flask (Web-Interface)
- python-dotenv (Umgebungsvariablen)
- requests (HTTP-Anfragen)

**Schritt 4:** Installation verifizieren
```bash
# Prüfen ob Installation erfolgreich war
pip list | grep -E "PyGithub|Flask|python-dotenv|requests"
```

Sollte alle vier Pakete anzeigen.

---

## 5. Konfiguration

**Schritt 1:** Umgebungsvariablen-Datei erstellen
```bash
# .env-Datei erstellen
cp .env.example .env

# Oder manuell erstellen:
touch .env
```

**Schritt 2:** .env-Datei bearbeiten
Öffnen Sie `.env` mit einem Texteditor:

```bash
nano .env
# oder
code .env  # VS Code
```

**Schritt 3:** Token eintragen
Fügen Sie folgende Zeile ein (ersetzen Sie den Token):

```
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
GITHUB_USERNAME=IhrGitHubUsername
```

Beispiel:
```
GITHUB_TOKEN=ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t
GITHUB_USERNAME=hubertcpfeiffer-coder
```

**Schritt 4:** Datei speichern und schließen
- In `nano`: Drücken Sie `Ctrl+X`, dann `Y`, dann `Enter`
- In anderen Editoren: Normal speichern und schließen

**Schritt 5:** Berechtigungen setzen (wichtig für Sicherheit!)
```bash
# Nur Sie können die Datei lesen
chmod 600 .env
```

**⚠️ SICHERHEITSHINWEIS:**
- Die `.env`-Datei ist bereits in `.gitignore` eingetragen
- Sie wird NICHT auf GitHub hochgeladen
- Teilen Sie diese Datei niemals!

---

## 6. Erste Nutzung

### Methode 1: Kommandozeilen-Interface (CLI)

**Einfachste Nutzung:**
```bash
python auto_coder.py "Erstelle eine Python Flask Web-App mit Login-System"
```

**Mit allen Optionen:**
```bash
python auto_coder.py \
  --task "Erstelle eine REST API mit Python FastAPI" \
  --repo-name "my-fastapi-project" \
  --description "Eine schnelle REST API für Produktverwaltung" \
  --private
```

**Parameter erklärt:**
- `--task`: Die Aufgabenbeschreibung (was soll erstellt werden)
- `--repo-name`: Name des GitHub-Repositories (optional, wird automatisch generiert)
- `--description`: Beschreibung des Projekts (optional)
- `--private`: Repository privat machen (optional, standard ist public)

**Interaktiver Modus:**
```bash
python auto_coder.py
```

Dann werden Sie Schritt für Schritt gefragt:
1. Was soll erstellt werden?
2. Repository-Name?
3. Beschreibung?
4. Public oder Private?

### Methode 2: Web-Interface

**Schritt 1:** Web-Server starten
```bash
python web_app.py
```

**Schritt 2:** Browser öffnen
- Öffnen Sie [http://localhost:5000](http://localhost:5000)

**Schritt 3:** Formular ausfüllen
- **Task Description**: Beschreiben Sie Ihr Projekt
- **Repository Name**: (optional) Gewünschter Name
- **Description**: (optional) Projekt-Beschreibung
- **Privacy**: Public/Private auswählen

**Schritt 4:** "Generate Project" klicken
- Das System analysiert Ihre Aufgabe
- Erstellt den Code
- Legt das Repository an
- Zeigt den Link zum neuen Repository

---

## 7. Praktische Beispiele

### Beispiel 1: Einfache Website
```bash
python auto_coder.py "Erstelle eine HTML/CSS/JS Portfolio-Website"
```

**Was passiert:**
- Erstellt Repository: `portfolio-website`
- Generiert: `index.html`, `style.css`, `script.js`
- Fügt README.md hinzu
- Committed und pusht alles

### Beispiel 2: Python Data Science Projekt
```bash
python auto_coder.py \
  --task "Erstelle ein Data Science Projekt für Aktienkurs-Analyse mit Pandas und Matplotlib" \
  --repo-name "stock-analysis" \
  --description "Analysiere und visualisiere Aktienkurse"
```

**Was wird erstellt:**
- `main.py` (Haupt-Analyse-Skript)
- `requirements.txt` (pandas, matplotlib, numpy, yfinance)
- `data/` Ordner für Daten
- `notebooks/` für Jupyter Notebooks
- `README.md` mit Installationsanleitung

### Beispiel 3: REST API
```bash
python auto_coder.py "Erstelle eine REST API mit Express.js für ein Todo-System"
```

**Was wird erstellt:**
- `server.js` (Express.js Server)
- `routes/` (API-Routen)
- `models/` (Datenmodelle)
- `package.json` (Dependencies)
- `.env.example` (Umgebungsvariablen-Template)
- `README.md` (API-Dokumentation)

### Beispiel 4: Machine Learning Projekt
```bash
python auto_coder.py \
  --task "Erstelle ein ML-Projekt für Bild-Klassifikation mit TensorFlow" \
  --private
```

**Was wird erstellt:**
- `train.py` (Training-Skript)
- `predict.py` (Vorhersage-Skript)
- `models/` (Modell-Verzeichnis)
- `data/` (Daten-Verzeichnis)
- `requirements.txt` (tensorflow, numpy, pillow)
- `README.md` (Anleitung)

### Beispiel 5: Full-Stack Anwendung
```bash
python auto_coder.py "Erstelle eine Full-Stack App mit React Frontend und Django Backend für ein Blog-System"
```

**Was wird erstellt:**
- `frontend/` (React App)
- `backend/` (Django Projekt)
- `docker-compose.yml` (Container-Orchestrierung)
- Separate README für Frontend und Backend
- `.gitignore` für beide Teile

---

## 8. Fehlerbehebung

### Problem: "Authentication failed"

**Ursache:** Token ist ungültig oder nicht korrekt eingetragen

**Lösung:**
```bash
# .env-Datei prüfen
cat .env

# Sicherstellen, dass keine Leerzeichen vorhanden sind:
# ✅ RICHTIG: GITHUB_TOKEN=ghp_xxx...
# ❌ FALSCH:  GITHUB_TOKEN = ghp_xxx...
# ❌ FALSCH:  GITHUB_TOKEN=ghp_xxx... (mit Leerzeichen am Ende)

# Neuen Token erstellen falls nötig
```

### Problem: "Repository already exists"

**Ursache:** Ein Repository mit diesem Namen existiert bereits

**Lösung:**
```bash
# Anderen Namen verwenden
python auto_coder.py \
  --task "Ihre Aufgabe" \
  --repo-name "anderer-name-v2"

# Oder altes Repository löschen:
# 1. Gehen Sie zu github.com/USERNAME/REPO-NAME
# 2. Settings → Scroll nach unten → Delete repository
```

### Problem: "Module not found: PyGithub"

**Ursache:** Dependencies nicht installiert

**Lösung:**
```bash
# Prüfen ob virtuelle Umgebung aktiv ist
# Sollte (venv) vor der Kommandozeile zeigen

# Falls nicht, aktivieren:
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Dependencies neu installieren
pip install -r requirements.txt
```

### Problem: "Permission denied"

**Ursache:** Token hat nicht die richtigen Berechtigungen

**Lösung:**
1. Gehen Sie zu GitHub Settings → Developer settings → Personal access tokens
2. Klicken Sie auf den Token
3. Stellen Sie sicher, dass folgende Scopes aktiviert sind:
   - ✅ repo (alle)
   - ✅ workflow
4. Falls nicht: Löschen Sie den alten Token und erstellen Sie einen neuen mit den richtigen Berechtigungen

### Problem: "Rate limit exceeded"

**Ursache:** Zu viele API-Anfragen in kurzer Zeit

**Lösung:**
```bash
# Warten Sie 60 Minuten
# Oder prüfen Sie Ihr aktuelles Limit:

curl -H "Authorization: token ghp_xxx..." https://api.github.com/rate_limit
```

GitHub erlaubt 5000 Anfragen pro Stunde für authentifizierte Nutzer.

### Problem: Web-Interface startet nicht

**Ursache:** Port 5000 bereits belegt

**Lösung:**
```bash
# Anderen Port verwenden
python web_app.py --port 8080

# Oder: Prozess auf Port 5000 beenden
# Linux/Mac:
lsof -ti:5000 | xargs kill -9

# Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

---

## 🎯 Schnellstart-Zusammenfassung

Für eilige Nutzer - die wichtigsten Schritte:

```bash
# 1. Token erstellen auf github.com (Abschnitt 2)
# 2. Repository klonen
git clone https://github.com/USERNAME/github-auto-coder.git
cd github-auto-coder

# 3. Virtuelle Umgebung & Installation
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt

# 4. Token konfigurieren
echo "GITHUB_TOKEN=ghp_xxx" > .env
echo "GITHUB_USERNAME=YourUsername" >> .env

# 5. Erstes Projekt erstellen
python auto_coder.py "Erstelle eine Python Flask Web-App"

# Fertig! 🎉
```

---

## 📚 Weiterführende Ressourcen

- **GitHub API Dokumentation**: https://docs.github.com/en/rest
- **PyGithub Dokumentation**: https://pygithub.readthedocs.io/
- **Flask Dokumentation**: https://flask.palletsprojects.com/
- **Python Best Practices**: https://peps.python.org/pep-0008/

---

## 💡 Tipps für beste Ergebnisse

1. **Seien Sie spezifisch**: Je genauer Ihre Aufgabenbeschreibung, desto besser das Ergebnis
   - ❌ Schlecht: "Erstelle eine Website"
   - ✅ Gut: "Erstelle eine Portfolio-Website mit HTML, CSS, JavaScript und Kontaktformular"

2. **Geben Sie die Technologie an**: Erwähnen Sie bevorzugte Frameworks/Bibliotheken
   - "Erstelle eine REST API mit **FastAPI**" (nicht nur "REST API")
   - "Erstelle ein Frontend mit **React und TypeScript**"

3. **Strukturieren Sie große Projekte**: Für komplexe Projekte, teilen Sie in mehrere Repositories
   - Frontend separat
   - Backend separat
   - Gemeinsame Libraries separat

4. **Nutzen Sie Templates**: Schauen Sie in `examples/` für Vorlagen
   ```bash
   python auto_coder.py --template web-app "Meine Shopping-App"
   ```

5. **Überprüfen Sie den generierten Code**: Das System erstellt Basis-Code, den Sie anpassen können
   - Klonen Sie das erstellte Repository
   - Passen Sie den Code an Ihre Bedürfnisse an
   - Committen und pushen Sie Ihre Änderungen

---

## 🔒 Sicherheitshinweise

1. **Token-Sicherheit**:
   - ❌ Niemals Token in Code einfügen
   - ❌ Niemals Token committen
   - ✅ Immer `.env` nutzen
   - ✅ `.env` in `.gitignore` eintragen

2. **Repository-Visibility**:
   - Überlegen Sie, ob Repositories wirklich public sein müssen
   - Nutzen Sie `--private` für sensible Projekte

3. **Regelmäßige Token-Rotation**:
   - Erstellen Sie alle 90 Tage einen neuen Token
   - Löschen Sie alte Tokens

---

**Viel Erfolg mit dem GitHub Auto-Coder System! 🚀**

Bei Fragen oder Problemen: Erstellen Sie ein Issue auf GitHub.
