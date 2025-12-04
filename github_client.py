"""
GitHub Client - Verwaltet alle Interaktionen mit der GitHub API
"""
import os
import json
import base64
from typing import Dict, List, Optional
from github import Github, GithubException, Repository
from datetime import datetime
import time


class GitHubClient:
    """Client für GitHub API Operationen"""
    
    def __init__(self, config_path: str = 'config.json'):
        """
        Initialisiert den GitHub Client
        
        Args:
            config_path: Pfad zur Konfigurationsdatei
        """
        self.config = self._load_config(config_path)
        self.token = self.config.get('github_token')
        self.username = self.config.get('github_username')
        
        if not self.token:
            raise ValueError("GitHub Token nicht in config.json gefunden!")
        
        self.client = Github(self.token)
        self.user = self.client.get_user()
        self.rate_limit_delay = self.config.get('rate_limit_delay', 1.0)
        
    def _load_config(self, config_path: str) -> Dict:
        """Lädt Konfiguration aus JSON-Datei"""
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config-Datei nicht gefunden: {config_path}")
        
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def create_repository(self, 
                         repo_name: str, 
                         description: str = "",
                         private: bool = False,
                         auto_init: bool = False) -> Repository.Repository:
        """
        Erstellt ein neues GitHub Repository
        
        Args:
            repo_name: Name des Repositories
            description: Beschreibung des Repositories
            private: Ob das Repo privat sein soll
            auto_init: Ob ein README.md automatisch erstellt werden soll
            
        Returns:
            Repository-Objekt
        """
        try:
            print(f"📦 Erstelle Repository: {repo_name}")
            repo = self.user.create_repo(
                name=repo_name,
                description=description,
                private=private,
                auto_init=auto_init
            )
            print(f"✅ Repository erstellt: {repo.html_url}")
            time.sleep(self.rate_limit_delay)
            return repo
            
        except GithubException as e:
            if e.status == 422:
                print(f"⚠️  Repository '{repo_name}' existiert bereits")
                # Versuche existierendes Repo zu holen
                repo = self.user.get_repo(repo_name)
                return repo
            else:
                raise Exception(f"Fehler beim Erstellen des Repositories: {e}")
    
    def create_file(self, 
                   repo: Repository.Repository,
                   file_path: str,
                   content: str,
                   commit_message: str = None) -> None:
        """
        Erstellt eine neue Datei im Repository
        
        Args:
            repo: Repository-Objekt
            file_path: Pfad der Datei im Repo
            content: Inhalt der Datei
            commit_message: Commit-Nachricht
        """
        if commit_message is None:
            commit_message = f"Add {file_path}"
        
        try:
            repo.create_file(
                path=file_path,
                message=commit_message,
                content=content,
                branch=self.config.get('default_branch', 'main')
            )
            print(f"  ✅ Datei erstellt: {file_path}")
            time.sleep(self.rate_limit_delay)
            
        except GithubException as e:
            if e.status == 422:
                print(f"  ⚠️  Datei existiert bereits: {file_path}")
            else:
                raise Exception(f"Fehler beim Erstellen der Datei: {e}")
    
    def create_multiple_files(self,
                             repo: Repository.Repository,
                             files: Dict[str, str],
                             commit_message: str = "Add project files") -> None:
        """
        Erstellt mehrere Dateien auf einmal
        
        Args:
            repo: Repository-Objekt
            files: Dictionary mit {Pfad: Inhalt}
            commit_message: Commit-Nachricht
        """
        print(f"📝 Erstelle {len(files)} Dateien...")
        
        for file_path, content in files.items():
            self.create_file(repo, file_path, content, f"Add {file_path}")
    
    def get_repository(self, repo_name: str) -> Repository.Repository:
        """
        Holt ein existierendes Repository
        
        Args:
            repo_name: Name des Repositories
            
        Returns:
            Repository-Objekt
        """
        try:
            return self.user.get_repo(repo_name)
        except GithubException as e:
            raise Exception(f"Repository nicht gefunden: {repo_name}")
    
    def delete_repository(self, repo_name: str) -> None:
        """
        Löscht ein Repository (Vorsicht!)
        
        Args:
            repo_name: Name des Repositories
        """
        try:
            repo = self.user.get_repo(repo_name)
            repo.delete()
            print(f"🗑️  Repository gelöscht: {repo_name}")
        except GithubException as e:
            raise Exception(f"Fehler beim Löschen: {e}")
    
    def check_rate_limit(self) -> Dict:
        """
        Prüft das aktuelle Rate Limit
        
        Returns:
            Dictionary mit Rate Limit Informationen
        """
        rate_limit = self.client.get_rate_limit()
        core = rate_limit.core
        
        return {
            'limit': core.limit,
            'remaining': core.remaining,
            'reset_time': core.reset
        }
    
    def get_repo_info(self, repo: Repository.Repository) -> Dict:
        """
        Holt Informationen über ein Repository
        
        Args:
            repo: Repository-Objekt
            
        Returns:
            Dictionary mit Repository-Informationen
        """
        return {
            'name': repo.name,
            'full_name': repo.full_name,
            'url': repo.html_url,
            'description': repo.description,
            'private': repo.private,
            'created_at': repo.created_at,
            'default_branch': repo.default_branch,
            'size': repo.size,
            'language': repo.language
        }
