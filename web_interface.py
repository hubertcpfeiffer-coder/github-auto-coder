#!/usr/bin/env python3
"""
Web Interface für GitHub Auto-Coder
"""
from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import json
from auto_coder import GitHubAutoCoder

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'

# Initialisiere Auto-Coder
try:
    coder = GitHubAutoCoder()
except Exception as e:
    print(f"Warning: {e}")
    coder = None


@app.route('/')
def index():
    """Hauptseite"""
    return render_template('index.html')


@app.route('/api/create', methods=['POST'])
def create_project():
    """API Endpoint zum Erstellen eines Projekts"""
    try:
        data = request.json
        task = data.get('task')
        repo_name = data.get('repo_name')
        local_only = data.get('local_only', False)
        private = data.get('private', False)
        
        if not task:
            return jsonify({'error': 'Keine Aufgabenbeschreibung angegeben'}), 400
        
        if not coder:
            return jsonify({'error': 'GitHub Auto-Coder nicht initialisiert'}), 500
        
        # Erstelle Projekt
        result = coder.create_project(
            task_description=task,
            repo_name=repo_name if repo_name else None,
            local_only=local_only,
            private=private
        )
        
        return jsonify({
            'success': True,
            'result': result
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/examples')
def get_examples():
    """Gibt Beispiel-Aufgaben zurück"""
    examples = [
        {
            'title': 'Flask Web-App',
            'description': 'Erstelle eine Flask-Webapplikation mit Login-System und SQLite-Datenbank',
            'language': 'Python',
            'type': 'Web App'
        },
        {
            'title': 'React Dashboard',
            'description': 'Erstelle ein React Dashboard mit Charts und Datenvisualisierung',
            'language': 'JavaScript',
            'type': 'Web App'
        },
        {
            'title': 'FastAPI REST API',
            'description': 'Erstelle eine FastAPI REST API mit Authentifizierung und Datenbank',
            'language': 'Python',
            'type': 'API'
        },
        {
            'title': 'CLI Tool',
            'description': 'Erstelle ein Python CLI-Tool für Datei-Backup und Synchronisation',
            'language': 'Python',
            'type': 'CLI'
        },
        {
            'title': 'Discord Bot',
            'description': 'Erstelle einen Discord-Bot mit Moderations-Features',
            'language': 'Python',
            'type': 'Bot'
        },
        {
            'title': 'Data Analysis',
            'description': 'Erstelle ein Jupyter Notebook Projekt für Verkaufsdaten-Analyse mit Pandas',
            'language': 'Python',
            'type': 'Data Science'
        }
    ]
    
    return jsonify(examples)


@app.route('/api/health')
def health():
    """Health Check Endpoint"""
    return jsonify({
        'status': 'healthy',
        'authenticated': coder.authenticated if coder else False
    })


if __name__ == '__main__':
    print("🚀 Starting GitHub Auto-Coder Web Interface...")
    print("📱 Open http://localhost:5000 in your browser")
    app.run(debug=True, host='0.0.0.0', port=5000)
