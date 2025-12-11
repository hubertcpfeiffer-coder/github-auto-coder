#!/usr/bin/env python3
"""
Round Table Dashboard - Web-basiertes Interface für das Round Table System
"""
from flask import Flask, render_template, request, jsonify, session
import os
import sys
import asyncio
import json
from datetime import datetime
from pathlib import Path

# Importiere Round Table
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from round_table import RoundTable

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'dev-secret-key-change-in-production')

# Initialisiere Round Table
round_table = RoundTable()

# Historie speichern
history = []


@app.route('/')
def index():
    """Hauptseite - Dashboard"""
    return render_template('dashboard.html')


@app.route('/api/discuss', methods=['POST'])
def api_discuss():
    """API Endpoint für Round Table Diskussion"""
    try:
        data = request.json
        task = data.get('task')
        language = data.get('language', 'python')
        project_type = data.get('project_type', 'module')
        
        if not task:
            return jsonify({'error': 'Keine Aufgabe angegeben'}), 400
        
        # Führe Round Table Diskussion aus
        context = {
            'language': language,
            'project_type': project_type
        }
        
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        result = loop.run_until_complete(
            round_table.discuss(task, context)
        )
        
        loop.close()
        
        # Formatiere Ergebnis für JSON
        response_data = {
            'success': True,
            'task': result.task,
            'consensus_code': result.consensus_code,
            'discussion_summary': result.discussion_summary,
            'final_recommendation': result.final_recommendation,
            'timestamp': result.timestamp.isoformat(),
            'individual_responses': [
                {
                    'model': r.model.value,
                    'focus_area': r.focus_area,
                    'recommendation': r.recommendation,
                    'confidence': r.confidence
                }
                for r in result.individual_responses
            ]
        }
        
        # Speichere in Historie
        history.append({
            'task': task,
            'language': language,
            'project_type': project_type,
            'timestamp': result.timestamp.isoformat(),
            'code_length': len(result.consensus_code)
        })
        
        return jsonify(response_data)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/history')
def api_history():
    """Gibt die Historie zurück"""
    return jsonify(history[-10:])  # Letzte 10 Einträge


@app.route('/api/examples')
def api_examples():
    """Gibt Beispiel-Aufgaben zurück"""
    examples = [
        {
            'task': 'Erstelle ein User Authentication Modul mit JWT',
            'language': 'python',
            'project_type': 'api',
            'category': 'Sicherheit'
        },
        {
            'task': 'Entwickle eine wiederverwendbare Button Komponente',
            'language': 'typescript',
            'project_type': 'web_app',
            'category': 'Frontend'
        },
        {
            'task': 'Baue ein Logging-Modul mit verschiedenen Log-Levels',
            'language': 'python',
            'project_type': 'library',
            'category': 'Infrastruktur'
        },
        {
            'task': 'Erstelle einen REST API Client mit Retry-Logik',
            'language': 'javascript',
            'project_type': 'library',
            'category': 'API'
        },
        {
            'task': 'Entwickle ein Data Validation Modul mit Pydantic',
            'language': 'python',
            'project_type': 'library',
            'category': 'Datenverarbeitung'
        },
        {
            'task': 'Baue einen Configuration Manager mit YAML Support',
            'language': 'python',
            'project_type': 'library',
            'category': 'Konfiguration'
        }
    ]
    
    return jsonify(examples)


@app.route('/api/health')
def api_health():
    """Health Check"""
    return jsonify({
        'status': 'healthy',
        'round_table_initialized': round_table is not None,
        'history_count': len(history)
    })


@app.route('/api/stats')
def api_stats():
    """Statistiken"""
    total_tasks = len(history)
    
    if total_tasks == 0:
        return jsonify({
            'total_tasks': 0,
            'languages': {},
            'project_types': {}
        })
    
    # Zähle Sprachen
    languages = {}
    for item in history:
        lang = item.get('language', 'unknown')
        languages[lang] = languages.get(lang, 0) + 1
    
    # Zähle Projekt-Typen
    project_types = {}
    for item in history:
        ptype = item.get('project_type', 'unknown')
        project_types[ptype] = project_types.get(ptype, 0) + 1
    
    return jsonify({
        'total_tasks': total_tasks,
        'languages': languages,
        'project_types': project_types
    })


if __name__ == '__main__':
    print("🚀 Starting Round Table Dashboard...")
    print("📱 Open http://localhost:5000 in your browser")
    print("🤖 Round Table System ready!")
    
    # Erstelle templates Verzeichnis falls nicht vorhanden
    templates_dir = Path(__file__).parent / 'templates'
    templates_dir.mkdir(exist_ok=True)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
