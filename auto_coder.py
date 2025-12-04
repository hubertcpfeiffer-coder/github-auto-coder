#!/usr/bin/env python3
"""
GitHub Auto-Coder - Automatische GitHub Repository-Erstellung
"""
import argparse
import sys
import os
from typing import Dict, Optional
from colorama import init, Fore, Style

from task_parser import TaskParser, ProjectPlan
from code_generator import CodeGenerator
from github_client import GitHubClient

# Initialisiere Colorama für farbige Ausgabe
init(autoreset=True)


class GitHubAutoCoder:
    """Hauptklasse für GitHub Auto-Coder"""
    
    def __init__(self, config_path: str = 'config.json'):
        """
        Initialisiert den Auto-Coder
        
        Args:
            config_path: Pfad zur Konfigurationsdatei
        """
        self.config_path = config_path
        self.parser = TaskParser()
        self.generator = CodeGenerator()
        
        try:
            self.github = GitHubClient(config_path)
            self.authenticated = True
        except Exception as e:
            print(f"{Fore.YELLOW}⚠️  GitHub-Verbindung fehlgeschlagen: {e}")
            print(f"{Fore.YELLOW}💡 Lokaler Modus aktiviert (kein GitHub-Push)")
            self.authenticated = False
    
    def create_project(self, 
                      task_description: str,
                      repo_name: Optional[str] = None,
                      local_only: bool = False,
                      private: bool = False) -> Dict:
        """
        Erstellt ein komplettes Projekt basierend auf der Aufgabenbeschreibung
        
        Args:
            task_description: Natürlichsprachliche Aufgabenbeschreibung
            repo_name: Optional: Spezifischer Repository-Name
            local_only: Nur lokal generieren, nicht auf GitHub pushen
            private: Ob das Repository privat sein soll
            
        Returns:
            Dictionary mit Projekt-Informationen
        """
        print(f"{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}🤖 GitHub Auto-Coder gestartet")
        print(f"{Fore.CYAN}{'='*60}\n")
        
        # 1. Task parsen
        print(f"{Fore.YELLOW}📋 Analysiere Aufgabe...")
        plan = self.parser.parse_task(task_description)
        
        # Optional: Repository-Name überschreiben
        if repo_name:
            plan.repo_name = repo_name
        
        print(f"{Fore.GREEN}✅ Projekt geplant:")
        print(f"   📦 Repository: {plan.repo_name}")
        print(f"   💻 Sprache: {plan.language}")
        print(f"   🎯 Typ: {plan.project_type}")
        print(f"   📁 Ordner: {len(plan.folders)}")
        print(f"   📦 Dependencies: {len(plan.dependencies)}\n")
        
        # 2. Code generieren
        print(f"{Fore.YELLOW}🔨 Generiere Code-Dateien...")
        files = self.generator.generate_files(plan)
        plan.files = files
        
        print(f"{Fore.GREEN}✅ {len(files)} Dateien generiert\n")
        
        # 3. Lokal speichern
        local_path = self._save_locally(plan)
        print(f"{Fore.GREEN}✅ Lokal gespeichert: {local_path}\n")
        
        result = {
            'repo_name': plan.repo_name,
            'local_path': local_path,
            'files': list(files.keys()),
            'language': plan.language,
            'project_type': plan.project_type
        }
        
        # 4. Auf GitHub pushen (wenn authentifiziert und gewünscht)
        if not local_only and self.authenticated:
            try:
                print(f"{Fore.YELLOW}🚀 Erstelle GitHub Repository...")
                repo = self.github.create_repository(
                    repo_name=plan.repo_name,
                    description=plan.description,
                    private=private
                )
                
                print(f"{Fore.YELLOW}📤 Uploade Dateien zu GitHub...")
                self.github.create_multiple_files(repo, files)
                
                print(f"{Fore.GREEN}✅ Erfolgreich auf GitHub erstellt!")
                print(f"{Fore.CYAN}🔗 URL: {repo.html_url}\n")
                
                result['repo_url'] = repo.html_url
                result['github_success'] = True
                
                # Rate Limit Info
                rate_info = self.github.check_rate_limit()
                print(f"{Fore.CYAN}ℹ️  GitHub API Limit: {rate_info['remaining']}/{rate_info['limit']} verbleibend")
                
            except Exception as e:
                print(f"{Fore.RED}❌ GitHub-Upload fehlgeschlagen: {e}")
                print(f"{Fore.YELLOW}💡 Projekt wurde lokal gespeichert: {local_path}")
                result['github_success'] = False
                result['error'] = str(e)
        else:
            result['github_success'] = False
            if local_only:
                print(f"{Fore.CYAN}ℹ️  Nur lokaler Modus (--local-only)\n")
        
        # 5. Zusammenfassung
        self._print_summary(plan, result)
        
        return result
    
    def _save_locally(self, plan: ProjectPlan) -> str:
        """
        Speichert Projekt lokal
        
        Args:
            plan: ProjectPlan mit allen Dateien
            
        Returns:
            Pfad zum lokalen Projekt
        """
        project_dir = plan.repo_name
        
        # Erstelle Hauptverzeichnis
        os.makedirs(project_dir, exist_ok=True)
        
        # Erstelle alle Ordner
        for folder in plan.folders:
            folder_path = os.path.join(project_dir, folder)
            os.makedirs(folder_path, exist_ok=True)
        
        # Erstelle alle Dateien
        for file_path, content in plan.files.items():
            full_path = os.path.join(project_dir, file_path)
            
            # Erstelle Unterordner falls nötig
            file_dir = os.path.dirname(full_path)
            if file_dir:
                os.makedirs(file_dir, exist_ok=True)
            
            # Schreibe Datei
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
        
        return os.path.abspath(project_dir)
    
    def _print_summary(self, plan: ProjectPlan, result: Dict):
        """Gibt eine Zusammenfassung aus"""
        print(f"{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}📊 Zusammenfassung")
        print(f"{Fore.CYAN}{'='*60}")
        print(f"Repository: {Fore.GREEN}{plan.repo_name}")
        print(f"Sprache: {Fore.GREEN}{plan.language}")
        print(f"Typ: {Fore.GREEN}{plan.project_type}")
        print(f"Dateien: {Fore.GREEN}{len(plan.files)}")
        print(f"Lokaler Pfad: {Fore.GREEN}{result['local_path']}")
        
        if result.get('github_success'):
            print(f"GitHub URL: {Fore.GREEN}{result['repo_url']}")
        
        print(f"{Fore.CYAN}{'='*60}\n")
        
        # Features
        features = self.parser.extract_features(plan.description)
        if features:
            print(f"{Fore.CYAN}🎯 Erkannte Features:")
            for feature in features:
                print(f"   • {feature}")
            print()
    
    def interactive_mode(self):
        """Startet interaktiven Modus"""
        print(f"{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}🤖 GitHub Auto-Coder - Interaktiver Modus")
        print(f"{Fore.CYAN}{'='*60}\n")
        
        print("Beschreiben Sie Ihr Projekt (oder 'exit' zum Beenden):")
        
        while True:
            try:
                task = input(f"{Fore.YELLOW}>>> {Style.RESET_ALL}").strip()
                
                if task.lower() in ['exit', 'quit', 'q']:
                    print(f"{Fore.CYAN}Auf Wiedersehen! 👋")
                    break
                
                if not task:
                    continue
                
                # Frage nach weiteren Optionen
                print(f"\n{Fore.CYAN}Repository-Name (Enter für automatisch):")
                repo_name = input(f"{Fore.YELLOW}>>> {Style.RESET_ALL}").strip() or None
                
                print(f"\n{Fore.CYAN}Privates Repository? (j/n, Standard: n):")
                private_input = input(f"{Fore.YELLOW}>>> {Style.RESET_ALL}").strip().lower()
                private = private_input in ['j', 'ja', 'y', 'yes']
                
                print(f"\n{Fore.CYAN}Nur lokal generieren? (j/n, Standard: n):")
                local_input = input(f"{Fore.YELLOW}>>> {Style.RESET_ALL}").strip().lower()
                local_only = local_input in ['j', 'ja', 'y', 'yes']
                
                print()
                
                # Erstelle Projekt
                self.create_project(
                    task_description=task,
                    repo_name=repo_name,
                    local_only=local_only,
                    private=private
                )
                
                print(f"\n{Fore.GREEN}Bereit für die nächste Aufgabe!\n")
                
            except KeyboardInterrupt:
                print(f"\n{Fore.CYAN}Auf Wiedersehen! 👋")
                break
            except Exception as e:
                print(f"{Fore.RED}❌ Fehler: {e}\n")


def main():
    """Hauptfunktion für CLI"""
    parser = argparse.ArgumentParser(
        description='GitHub Auto-Coder - Automatische Projekt-Erstellung',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Beispiele:
  python auto_coder.py "Erstelle eine Flask Web-App"
  python auto_coder.py "Erstelle eine React Todo-App" --repo-name my-todo-app
  python auto_coder.py "Erstelle eine FastAPI" --local-only
  python auto_coder.py --interactive
        """
    )
    
    parser.add_argument(
        'task',
        nargs='?',
        help='Aufgabenbeschreibung (natürlichsprachlich)'
    )
    
    parser.add_argument(
        '--repo-name',
        '-r',
        help='Spezifischer Repository-Name'
    )
    
    parser.add_argument(
        '--local-only',
        '-l',
        action='store_true',
        help='Nur lokal generieren (nicht auf GitHub pushen)'
    )
    
    parser.add_argument(
        '--private',
        '-p',
        action='store_true',
        help='Privates Repository erstellen'
    )
    
    parser.add_argument(
        '--config',
        '-c',
        default='config.json',
        help='Pfad zur Konfigurationsdatei (Standard: config.json)'
    )
    
    parser.add_argument(
        '--interactive',
        '-i',
        action='store_true',
        help='Interaktiver Modus'
    )
    
    args = parser.parse_args()
    
    # Prüfe ob Config existiert
    if not os.path.exists(args.config):
        print(f"{Fore.RED}❌ Konfigurationsdatei nicht gefunden: {args.config}")
        print(f"{Fore.YELLOW}💡 Kopiere config.example.json zu config.json und füge deinen GitHub Token ein")
        sys.exit(1)
    
    # Initialisiere Auto-Coder
    coder = GitHubAutoCoder(config_path=args.config)
    
    # Interaktiver Modus
    if args.interactive:
        coder.interactive_mode()
        return
    
    # Prüfe ob Task angegeben wurde
    if not args.task:
        parser.print_help()
        sys.exit(1)
    
    # Erstelle Projekt
    try:
        result = coder.create_project(
            task_description=args.task,
            repo_name=args.repo_name,
            local_only=args.local_only,
            private=args.private
        )
        
        if result.get('github_success'):
            sys.exit(0)
        else:
            sys.exit(1)
            
    except Exception as e:
        print(f"{Fore.RED}❌ Fehler: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
