"""
Task Parser - Analysiert Programmieraufgaben und erstellt Projektpläne
"""
import re
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass


@dataclass
class ProjectPlan:
    """Datenklasse für einen Projektplan"""
    repo_name: str
    description: str
    language: str
    project_type: str
    files: Dict[str, str]
    folders: List[str]
    dependencies: List[str]
    gitignore_template: Optional[str]
    license: str


class TaskParser:
    """Parser für Programmieraufgaben"""
    
    # Sprach-Erkennung
    LANGUAGE_PATTERNS = {
        'python': ['python', 'py', 'flask', 'django', 'fastapi', 'pandas', 'numpy', 'jupyter'],
        'javascript': ['javascript', 'js', 'node', 'react', 'vue', 'angular', 'express', 'next'],
        'typescript': ['typescript', 'ts', 'tsx'],
        'java': ['java', 'spring', 'maven', 'gradle'],
        'cpp': ['c++', 'cpp', 'cmake'],
        'go': ['go', 'golang'],
        'rust': ['rust', 'cargo'],
        'ruby': ['ruby', 'rails'],
        'php': ['php', 'laravel', 'symfony'],
        'swift': ['swift', 'ios'],
        'kotlin': ['kotlin', 'android'],
        'html': ['html', 'css', 'website', 'webpage']
    }
    
    # Projekt-Typ Erkennung
    PROJECT_TYPES = {
        'web_app': ['webapp', 'web app', 'website', 'webseite', 'dashboard'],
        'api': ['api', 'rest', 'graphql', 'backend'],
        'cli': ['cli', 'command line', 'kommandozeile', 'terminal'],
        'library': ['library', 'bibliothek', 'package', 'paket', 'modul'],
        'bot': ['bot', 'chatbot', 'discord', 'telegram', 'slack'],
        'data_science': ['data', 'analyse', 'analysis', 'jupyter', 'notebook', 'ml', 'machine learning'],
        'mobile': ['mobile', 'app', 'ios', 'android', 'react native', 'flutter'],
        'desktop': ['desktop', 'gui', 'electron', 'pyqt', 'tkinter'],
        'game': ['game', 'spiel', 'pygame', 'unity'],
        'microservice': ['microservice', 'micro service', 'docker', 'kubernetes']
    }
    
    # GitIgnore Templates
    GITIGNORE_TEMPLATES = {
        'python': """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
.venv
pip-log.txt
pip-delete-this-directory.txt
.pytest_cache/
.coverage
htmlcov/
*.egg-info/
dist/
build/
*.egg
.ipynb_checkpoints
""",
        'javascript': """# Node
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.npm
.env
.env.local
.env.production
dist/
build/
coverage/
.cache/
*.log
""",
        'java': """# Java
*.class
*.jar
*.war
*.ear
target/
*.iml
.idea/
.gradle/
build/
out/
""",
        'go': """# Go
*.exe
*.exe~
*.dll
*.so
*.dylib
*.test
*.out
vendor/
go.work
"""
    }
    
    def __init__(self):
        """Initialisiert den Task Parser"""
        pass
    
    def parse_task(self, task_description: str) -> ProjectPlan:
        """
        Analysiert eine Aufgabenbeschreibung und erstellt einen Projektplan
        
        Args:
            task_description: Natürlichsprachliche Aufgabenbeschreibung
            
        Returns:
            ProjectPlan-Objekt mit allen Details
        """
        task_lower = task_description.lower()
        
        # 1. Sprache erkennen
        language = self._detect_language(task_lower)
        
        # 2. Projekt-Typ erkennen
        project_type = self._detect_project_type(task_lower)
        
        # 3. Repository-Name generieren
        repo_name = self._generate_repo_name(task_description, project_type)
        
        # 4. Beschreibung extrahieren
        description = self._generate_description(task_description, language, project_type)
        
        # 5. Ordnerstruktur planen
        folders = self._plan_folder_structure(language, project_type)
        
        # 6. Dependencies ermitteln
        dependencies = self._get_dependencies(language, project_type, task_lower)
        
        # 7. GitIgnore Template auswählen
        gitignore = self.GITIGNORE_TEMPLATES.get(language, '')
        
        # 8. Dateien generieren (wird später vom CodeGenerator gemacht)
        files = {}
        
        return ProjectPlan(
            repo_name=repo_name,
            description=description,
            language=language,
            project_type=project_type,
            files=files,
            folders=folders,
            dependencies=dependencies,
            gitignore_template=gitignore,
            license='MIT'
        )
    
    def _detect_language(self, task_lower: str) -> str:
        """Erkennt die Programmiersprache aus der Aufgabenbeschreibung"""
        for language, keywords in self.LANGUAGE_PATTERNS.items():
            for keyword in keywords:
                if keyword in task_lower:
                    return language
        return 'python'  # Default
    
    def _detect_project_type(self, task_lower: str) -> str:
        """Erkennt den Projekt-Typ aus der Aufgabenbeschreibung"""
        scores = {}
        
        for proj_type, keywords in self.PROJECT_TYPES.items():
            score = sum(1 for keyword in keywords if keyword in task_lower)
            if score > 0:
                scores[proj_type] = score
        
        if scores:
            return max(scores, key=scores.get)
        return 'cli'  # Default
    
    def _generate_repo_name(self, task: str, project_type: str) -> str:
        """Generiert einen sinnvollen Repository-Namen"""
        # Extrahiere wichtige Wörter
        words = re.findall(r'[a-zA-Z]{3,}', task.lower())
        
        # Filtere Stopwörter
        stopwords = {'erstelle', 'create', 'eine', 'ein', 'für', 'for', 'mit', 'with', 'und', 'and', 'das', 'the'}
        words = [w for w in words if w not in stopwords]
        
        # Nimm die ersten 2-3 relevanten Wörter
        name_parts = words[:3] if len(words) >= 3 else words
        
        # Füge Projekt-Typ hinzu wenn sinnvoll
        if not any(pt in task.lower() for pt in ['app', 'tool', 'system', 'api']):
            name_parts.append(project_type.replace('_', '-'))
        
        repo_name = '-'.join(name_parts[:3])
        
        # Bereinige den Namen
        repo_name = re.sub(r'[^a-z0-9-]', '', repo_name.lower())
        
        return repo_name or 'my-project'
    
    def _generate_description(self, task: str, language: str, project_type: str) -> str:
        """Generiert eine Repository-Beschreibung"""
        # Nutze die erste Zeile der Aufgabe als Basis
        first_line = task.split('.')[0].strip()
        
        description = f"{first_line} - {language.capitalize()} {project_type.replace('_', ' ')}"
        
        return description[:150]  # GitHub limit
    
    def _plan_folder_structure(self, language: str, project_type: str) -> List[str]:
        """Plant die Ordnerstruktur basierend auf Sprache und Typ"""
        folders = []
        
        # Basis-Struktur nach Sprache
        if language == 'python':
            if project_type == 'library':
                folders = ['src', 'tests', 'docs']
            elif project_type == 'web_app':
                folders = ['app', 'templates', 'static', 'tests']
            elif project_type == 'data_science':
                folders = ['notebooks', 'data', 'scripts', 'models']
            elif project_type == 'api':
                folders = ['api', 'models', 'tests', 'config']
            else:
                folders = ['src', 'tests']
        
        elif language in ['javascript', 'typescript']:
            if project_type == 'web_app':
                folders = ['src', 'public', 'components', 'utils', 'tests']
            elif project_type == 'api':
                folders = ['src', 'routes', 'controllers', 'models', 'middleware', 'tests']
            else:
                folders = ['src', 'dist', 'tests']
        
        elif language == 'java':
            folders = ['src/main/java', 'src/main/resources', 'src/test/java']
        
        elif language == 'go':
            folders = ['cmd', 'pkg', 'internal', 'api']
        
        else:
            folders = ['src', 'tests']
        
        return folders
    
    def _get_dependencies(self, language: str, project_type: str, task_lower: str) -> List[str]:
        """Ermittelt notwendige Dependencies"""
        dependencies = []
        
        if language == 'python':
            dependencies = ['pytest']
            
            if project_type == 'web_app':
                if 'flask' in task_lower:
                    dependencies.extend(['flask', 'flask-cors'])
                elif 'django' in task_lower:
                    dependencies.append('django')
                elif 'fastapi' in task_lower:
                    dependencies.extend(['fastapi', 'uvicorn'])
            
            if project_type == 'data_science':
                dependencies.extend(['pandas', 'numpy', 'matplotlib', 'jupyter'])
            
            if 'database' in task_lower or 'db' in task_lower:
                dependencies.append('sqlalchemy')
            
            if 'api' in task_lower:
                dependencies.append('requests')
        
        elif language in ['javascript', 'typescript']:
            dependencies = []
            
            if 'react' in task_lower:
                dependencies.extend(['react', 'react-dom'])
            elif 'vue' in task_lower:
                dependencies.append('vue')
            elif 'express' in task_lower:
                dependencies.append('express')
            
            if language == 'typescript':
                dependencies.extend(['typescript', '@types/node'])
        
        return dependencies
    
    def extract_features(self, task: str) -> List[str]:
        """Extrahiert gewünschte Features aus der Aufgabenbeschreibung"""
        features = []
        
        feature_keywords = {
            'login': 'User Authentication',
            'auth': 'Authentication',
            'database': 'Database Integration',
            'api': 'REST API',
            'test': 'Unit Tests',
            'docker': 'Docker Support',
            'cloud': 'Cloud Deployment',
            'ci/cd': 'CI/CD Pipeline'
        }
        
        task_lower = task.lower()
        for keyword, feature in feature_keywords.items():
            if keyword in task_lower:
                features.append(feature)
        
        return features
