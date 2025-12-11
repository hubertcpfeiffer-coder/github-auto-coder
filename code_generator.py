"""
Code Generator - Generiert Code-Dateien basierend auf Projektplänen
"""
from typing import Dict, List
from task_parser import ProjectPlan


class CodeGenerator:
    """Generiert Code für verschiedene Sprachen und Projekttypen"""
    
    def __init__(self):
        """Initialisiert den Code Generator"""
        pass
    
    def generate_files(self, plan: ProjectPlan) -> Dict[str, str]:
        """
        Generiert alle Dateien für ein Projekt
        
        Args:
            plan: ProjectPlan mit allen Details
            
        Returns:
            Dictionary mit {Dateipfad: Dateiinhalt}
        """
        files = {}
        
        # 1. README.md
        files['README.md'] = self._generate_readme(plan)
        
        # 2. .gitignore
        if plan.gitignore_template:
            files['.gitignore'] = plan.gitignore_template
        
        # 3. LICENSE
        files['LICENSE'] = self._generate_license(plan.license)
        
        # 4. Dependencies-Datei
        if plan.language == 'python':
            files['requirements.txt'] = self._generate_requirements(plan.dependencies)
        elif plan.language in ['javascript', 'typescript']:
            files['package.json'] = self._generate_package_json(plan)
        elif plan.language == 'java':
            files['pom.xml'] = self._generate_pom_xml(plan)
        elif plan.language == 'go':
            files['go.mod'] = self._generate_go_mod(plan)
        
        # 5. Hauptcode-Dateien
        main_files = self._generate_main_code(plan)
        files.update(main_files)
        
        # 6. Test-Dateien
        test_files = self._generate_test_files(plan)
        files.update(test_files)
        
        # 7. Konfigurationsdateien
        config_files = self._generate_config_files(plan)
        files.update(config_files)
        
        # 8. Leere Ordner (mit .gitkeep)
        for folder in plan.folders:
            files[f"{folder}/.gitkeep"] = ""
        
        return files
    
    def _generate_readme(self, plan: ProjectPlan) -> str:
        """Generiert README.md"""
        readme = f"""# {plan.repo_name}

{plan.description}

## 🚀 Features

- Modern {plan.language.capitalize()} {plan.project_type.replace('_', ' ')}
- Clean and maintainable code structure
- Comprehensive documentation
- Ready for deployment

## 📋 Prerequisites

- {self._get_language_requirement(plan.language)}
"""
        
        if plan.dependencies:
            readme += """
## 🔧 Installation

"""
            if plan.language == 'python':
                readme += """```bash
pip install -r requirements.txt
```
"""
            elif plan.language in ['javascript', 'typescript']:
                readme += """```bash
npm install
# or
yarn install
```
"""
        
        readme += """
## 💻 Usage

```bash
# Add usage instructions here
```

## 🧪 Testing

"""
        if plan.language == 'python':
            readme += """```bash
pytest
```
"""
        elif plan.language in ['javascript', 'typescript']:
            readme += """```bash
npm test
```
"""
        
        readme += f"""
## 📝 License

{plan.license} License - see LICENSE file for details

## 👤 Author

Generated with GitHub Auto-Coder
"""
        
        return readme
    
    def _generate_license(self, license_type: str) -> str:
        """Generiert LICENSE-Datei"""
        if license_type == 'MIT':
            return """MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
        return ""
    
    def _generate_requirements(self, dependencies: List[str]) -> str:
        """Generiert requirements.txt für Python"""
        return "\n".join(dependencies)
    
    def _generate_package_json(self, plan: ProjectPlan) -> str:
        """Generiert package.json für JavaScript/TypeScript"""
        import json
        
        package = {
            "name": plan.repo_name,
            "version": "1.0.0",
            "description": plan.description,
            "main": "src/index.js" if plan.language == 'javascript' else "dist/index.js",
            "scripts": {
                "start": "node src/index.js",
                "test": "jest",
                "build": "tsc" if plan.language == 'typescript' else "echo 'No build step'"
            },
            "keywords": [plan.project_type],
            "author": "",
            "license": plan.license,
            "dependencies": {},
            "devDependencies": {
                "jest": "^29.0.0"
            }
        }
        
        # Füge Dependencies hinzu
        for dep in plan.dependencies:
            package["dependencies"][dep] = "^latest"
        
        return json.dumps(package, indent=2)
    
    def _generate_pom_xml(self, plan: ProjectPlan) -> str:
        """Generiert pom.xml für Java"""
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <groupId>com.example</groupId>
    <artifactId>{plan.repo_name}</artifactId>
    <version>1.0.0</version>
    
    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
    </properties>
    
    <dependencies>
        <!-- Add dependencies here -->
    </dependencies>
</project>
"""
    
    def _generate_go_mod(self, plan: ProjectPlan) -> str:
        """Generiert go.mod für Go"""
        return f"""module github.com/username/{plan.repo_name}

go 1.21

require (
    // Add dependencies here
)
"""
    
    def _generate_main_code(self, plan: ProjectPlan) -> Dict[str, str]:
        """Generiert Hauptcode-Dateien"""
        files = {}
        
        if plan.language == 'python':
            files.update(self._generate_python_code(plan))
        elif plan.language in ['javascript', 'typescript']:
            files.update(self._generate_js_code(plan))
        elif plan.language == 'java':
            files.update(self._generate_java_code(plan))
        elif plan.language == 'go':
            files.update(self._generate_go_code(plan))
        
        return files
    
    def _generate_python_code(self, plan: ProjectPlan) -> Dict[str, str]:
        """Generiert Python-Code basierend auf Projekttyp"""
        files = {}
        
        if plan.project_type == 'web_app':
            if 'flask' in [d.lower() for d in plan.dependencies]:
                files['app/main.py'] = """from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
"""
                files['app/templates/index.html'] = """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My App</title>
</head>
<body>
    <h1>Welcome to the App!</h1>
</body>
</html>
"""
        
        elif plan.project_type == 'cli':
            files['src/main.py'] = """#!/usr/bin/env python3
\"\"\"
Main CLI Application
\"\"\"
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description='CLI Tool')
    parser.add_argument('command', help='Command to execute')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    print(f"Executing: {args.command}")
    
    if args.verbose:
        print("Verbose mode enabled")

if __name__ == '__main__':
    main()
"""
        
        elif plan.project_type == 'api':
            if 'fastapi' in [d.lower() for d in plan.dependencies]:
                files['api/main.py'] = """from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="My API", version="1.0.0")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
"""
        
        else:
            # Generic Python module
            files['src/__init__.py'] = ""
            files['src/main.py'] = """\"\"\"
Main module
\"\"\"

def hello_world():
    \"\"\"Main function\"\"\"
    print("Hello, World!")
    return "Hello, World!"

if __name__ == '__main__':
    hello_world()
"""
        
        return files
    
    def _generate_js_code(self, plan: ProjectPlan) -> Dict[str, str]:
        """Generiert JavaScript/TypeScript-Code"""
        files = {}
        ext = 'ts' if plan.language == 'typescript' else 'js'
        
        if plan.project_type == 'web_app' and 'react' in [d.lower() for d in plan.dependencies]:
            files[f'src/App.{ext}'] = """import React from 'react';

function App() {
  return (
    <div className="App">
      <h1>Welcome to the App</h1>
    </div>
  );
}

export default App;
"""
            files[f'src/index.{ext}'] = """import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
"""
        
        elif plan.project_type == 'api' and 'express' in [d.lower() for d in plan.dependencies]:
            files[f'src/index.{ext}'] = """const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.get('/', (req, res) => {
  res.json({ message: 'Welcome to the API' });
});

app.get('/health', (req, res) => {
  res.json({ status: 'healthy' });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
"""
        
        else:
            files[f'src/index.{ext}'] = """console.log('Hello, World!');

export function main() {
  console.log('Application started');
}

main();
"""
        
        if plan.language == 'typescript':
            files['tsconfig.json'] = """{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
"""
        
        return files
    
    def _generate_java_code(self, plan: ProjectPlan) -> Dict[str, str]:
        """Generiert Java-Code"""
        files = {}
        
        files['src/main/java/com/example/Main.java'] = """package com.example;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
"""
        
        return files
    
    def _generate_go_code(self, plan: ProjectPlan) -> Dict[str, str]:
        """Generiert Go-Code"""
        files = {}
        
        files['cmd/main.go'] = """package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
"""
        
        return files
    
    def _generate_test_files(self, plan: ProjectPlan) -> Dict[str, str]:
        """Generiert Test-Dateien"""
        files = {}
        
        if plan.language == 'python':
            files['tests/test_main.py'] = """import pytest

def test_example():
    assert True

def test_hello_world():
    result = "Hello, World!"
    assert result == "Hello, World!"
"""
        
        elif plan.language in ['javascript', 'typescript']:
            ext = 'ts' if plan.language == 'typescript' else 'js'
            files[f'tests/main.test.{ext}'] = """describe('Main Tests', () => {
  test('example test', () => {
    expect(true).toBe(true);
  });
});
"""
        
        return files
    
    def _generate_config_files(self, plan: ProjectPlan) -> Dict[str, str]:
        """Generiert Konfigurationsdateien"""
        files = {}
        
        # GitHub Actions CI/CD
        files['.github/workflows/ci.yml'] = f"""name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup {plan.language}
      uses: actions/setup-{self._get_setup_action(plan.language)}@v3
    
    - name: Install dependencies
      run: {self._get_install_command(plan.language)}
    
    - name: Run tests
      run: {self._get_test_command(plan.language)}
"""
        
        return files
    
    def _get_language_requirement(self, language: str) -> str:
        """Gibt Sprachanforderungen zurück"""
        requirements = {
            'python': 'Python 3.8+',
            'javascript': 'Node.js 16+',
            'typescript': 'Node.js 16+ and TypeScript',
            'java': 'Java 17+',
            'go': 'Go 1.21+',
            'rust': 'Rust 1.70+',
            'ruby': 'Ruby 3.0+',
            'php': 'PHP 8.0+'
        }
        return requirements.get(language, language.capitalize())
    
    def _get_setup_action(self, language: str) -> str:
        """Gibt Setup-Action für GitHub Actions zurück"""
        actions = {
            'python': 'python',
            'javascript': 'node',
            'typescript': 'node',
            'java': 'java',
            'go': 'go'
        }
        return actions.get(language, 'node')
    
    def _get_install_command(self, language: str) -> str:
        """Gibt Install-Command zurück"""
        commands = {
            'python': 'pip install -r requirements.txt',
            'javascript': 'npm install',
            'typescript': 'npm install',
            'java': 'mvn install',
            'go': 'go mod download'
        }
        return commands.get(language, 'echo "No install command"')
    
    def _get_test_command(self, language: str) -> str:
        """Gibt Test-Command zurück"""
        commands = {
            'python': 'pytest',
            'javascript': 'npm test',
            'typescript': 'npm test',
            'java': 'mvn test',
            'go': 'go test ./...'
        }
        return commands.get(language, 'echo "No test command"')
