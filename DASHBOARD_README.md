# 🎨 Round Table Dashboard - Anleitung

## Überblick

Das Round Table Dashboard ist eine moderne Web-Oberfläche zur Bedienung des Round Table Multi-AI Systems. Es bietet eine intuitive, visuelle Möglichkeit, Code mit Hilfe von 4 KI-Modellen zu generieren.

## 🚀 Dashboard starten

### Schnellstart

```bash
cd /home/runner/work/github-auto-coder/github-auto-coder
python dashboard.py
```

Das Dashboard wird auf **http://localhost:5000** verfügbar sein.

### Mit benutzerdefinierten Port

```bash
# In dashboard.py die letzte Zeile ändern:
app.run(debug=True, host='0.0.0.0', port=8080)
```

## 🎯 Features

### 1. **Aufgabenbeschreibung**
- Textfeld für natürlichsprachliche Beschreibung
- Sprachauswahl (Python, JavaScript, TypeScript, Java, Go, Rust)
- Projekt-Typ Auswahl (Modul, API, Web App, CLI, Library)

### 2. **Beispiele**
Vorgefertigte Beispiele zum schnellen Start:
- **Sicherheit**: User Authentication mit JWT
- **Frontend**: Wiederverwendbare Komponenten
- **Infrastruktur**: Logging-Module
- **API**: REST API Clients
- **Datenverarbeitung**: Validation Module
- **Konfiguration**: Configuration Manager

### 3. **Live-Diskussion**
Zeigt die Empfehlungen aller 4 KI-Modelle:
- 🏛️ **Grok**: Architektur & Design
- ✨ **Claude**: Code-Qualität & Wartbarkeit
- 📚 **GPT**: Best Practices & Dokumentation
- ⚡ **Gemini**: Performance & Skalierbarkeit

### 4. **Code-Anzeige**
- Tabs für Code, Empfehlung und Zusammenfassung
- Syntax-Highlighting
- Download-Funktion für generierten Code

### 5. **Statistiken**
- Anzahl generierter Module
- Aktive KI-Modelle
- Unterstützte Sprachen

## 📋 Verwendung

### Schritt 1: Aufgabe eingeben
1. Beschreibe in natürlicher Sprache, was du entwickeln möchtest
2. Wähle die Programmiersprache
3. Wähle den Projekt-Typ

**Beispiel:**
```
Aufgabe: Erstelle ein User Authentication Modul mit JWT und Passwort-Hashing
Sprache: Python
Typ: API
```

### Schritt 2: Code generieren
1. Klicke auf "✨ Code Generieren"
2. Der Round Table diskutiert (4 KI-Modelle geben Empfehlungen)
3. Konsens-Code wird generiert

### Schritt 3: Ergebnis nutzen
1. Betrachte die KI-Diskussion
2. Lese die Empfehlungen
3. Kopiere oder lade den Code herunter

## 🔧 API-Endpunkte

Das Dashboard stellt folgende API-Endpunkte bereit:

### `POST /api/discuss`
Startet eine Round Table Diskussion.

**Request:**
```json
{
  "task": "Erstelle ein User Management Modul",
  "language": "python",
  "project_type": "api"
}
```

**Response:**
```json
{
  "success": true,
  "task": "Erstelle ein User Management Modul",
  "consensus_code": "...",
  "individual_responses": [...],
  "final_recommendation": "...",
  "discussion_summary": "..."
}
```

### `GET /api/examples`
Gibt vorgefertigte Beispiele zurück.

### `GET /api/history`
Gibt die letzten 10 generierten Projekte zurück.

### `GET /api/stats`
Gibt Statistiken zurück (Gesamtzahl, Sprachen, Projekt-Typen).

### `GET /api/health`
Health-Check Endpunkt.

## 🌐 Zugriff von anderen Geräten

### Lokal im Netzwerk

Das Dashboard läuft auf `0.0.0.0:5000`, daher ist es von anderen Geräten im gleichen Netzwerk erreichbar:

1. Finde die IP-Adresse des Servers:
   ```bash
   hostname -I
   ```

2. Öffne im Browser eines anderen Geräts:
   ```
   http://[SERVER-IP]:5000
   ```

### Mit ngrok (öffentlich zugänglich)

```bash
# Installiere ngrok
# Dann:
ngrok http 5000
```

Ngrok gibt dir eine öffentliche URL, die du teilen kannst.

## 🎨 Anpassungen

### Farben ändern
Bearbeite in `templates/dashboard.html` die CSS-Variablen:

```css
/* Hauptfarben */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Ändern zu z.B.: */
background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
```

### Weitere Beispiele hinzufügen
Bearbeite in `dashboard.py` die Funktion `api_examples()`:

```python
examples.append({
    'task': 'Deine neue Aufgabe',
    'language': 'python',
    'project_type': 'api',
    'category': 'Kategorie'
})
```

### Logo/Branding ändern
Passe den Header in `templates/dashboard.html` an:

```html
<h1>🤖 Round Table Dashboard</h1>
<!-- Ändern zu: -->
<h1>Dein Logo/Name</h1>
```

## 🔒 Produktions-Deployment

Für Produktionsumgebungen:

### 1. Verwende einen Production Server

```bash
pip install gunicorn

# Starte mit Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 dashboard:app
```

### 2. Setze Secret Key

```bash
export FLASK_SECRET_KEY="dein-sehr-sicherer-zufalls-string"
```

### 3. Deaktiviere Debug-Modus

In `dashboard.py`:
```python
app.run(debug=False, host='0.0.0.0', port=5000)
```

### 4. Verwende HTTPS

Mit nginx als Reverse Proxy:

```nginx
server {
    listen 443 ssl;
    server_name deine-domain.de;
    
    ssl_certificate /pfad/zu/cert.pem;
    ssl_certificate_key /pfad/zu/key.pem;
    
    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## 📱 Mobile Nutzung

Das Dashboard ist responsive und funktioniert auf:
- 📱 Smartphones
- 📱 Tablets
- 💻 Desktop

Die Darstellung passt sich automatisch an die Bildschirmgröße an.

## 🐛 Troubleshooting

### Port bereits belegt
```bash
# Finde Prozess auf Port 5000
lsof -i :5000

# Beende Prozess
kill -9 [PID]
```

### Dashboard lädt nicht
1. Prüfe ob Flask installiert ist: `pip install flask`
2. Prüfe Firewall-Einstellungen
3. Prüfe Server-Logs: `tail -f /tmp/dashboard.log`

### Keine Verbindung von anderen Geräten
1. Prüfe ob Server auf `0.0.0.0` lauscht
2. Prüfe Firewall auf Server
3. Prüfe dass Geräte im gleichen Netzwerk sind

## 💡 Tipps

### Beste Ergebnisse
- Sei spezifisch in der Aufgabenbeschreibung
- Gib Kontext an (z.B. "mit JWT", "mit TypeScript")
- Wähle die richtige Sprache und Projekt-Typ

### Effizienz
- Nutze die Beispiele als Ausgangspunkt
- Speichere häufig genutzte Aufgaben
- Lade generierten Code direkt herunter

### Code-Qualität
- Lese die KI-Empfehlungen
- Prüfe den Konsens-Code
- Passe den Code an deine Bedürfnisse an

## 📊 Vergleich mit anderen Interfaces

| Feature | Dashboard | CLI | Streamlit |
|---------|-----------|-----|-----------|
| **GUI** | ✅ Modern | ❌ Text | ✅ Basic |
| **Beispiele** | ✅ Integriert | ❌ Manuell | ✅ Basic |
| **Live-Updates** | ✅ Ja | ❌ Nein | ✅ Ja |
| **Download** | ✅ Button | ✅ Datei | ⚠️ Manuell |
| **Mobile** | ✅ Responsive | ❌ Nein | ⚠️ Basic |
| **Statistiken** | ✅ Live | ❌ Nein | ✅ Basic |

## 🔗 Links

- **Dashboard**: http://localhost:5000
- **API Docs**: http://localhost:5000/api/health
- **Hauptdokumentation**: [ROUND_TABLE.md](ROUND_TABLE.md)
- **CLI Tool**: [round_table_cli.py](round_table_cli.py)

## 📝 Lizenz

Siehe [LICENSE](LICENSE) im Hauptverzeichnis.

---

**Viel Erfolg mit dem Round Table Dashboard! 🚀**
