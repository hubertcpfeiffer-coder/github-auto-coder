#!/usr/bin/env python3
"""
Round Table CLI - Direkter Zugriff auf den Runden Tisch
"""
import argparse
import sys
import asyncio
from colorama import init, Fore, Style
from round_table import RoundTable

# Initialisiere Colorama
init(autoreset=True)


async def main():
    """Hauptfunktion für Round Table CLI"""
    parser = argparse.ArgumentParser(
        description='Round Table - Multi-AI Kollaborations-System',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Beispiele:
  python round_table_cli.py "Erstelle ein User Management Modul"
  python round_table_cli.py "Entwickle eine API für Produktverwaltung" --language python
  python round_table_cli.py "Baue eine React Komponente für Login" --language typescript
  python round_table_cli.py --interactive
        """
    )
    
    parser.add_argument(
        'task',
        nargs='?',
        help='Aufgabenbeschreibung für den Runden Tisch'
    )
    
    parser.add_argument(
        '--language',
        '-l',
        default='python',
        choices=['python', 'javascript', 'typescript', 'java', 'go', 'rust'],
        help='Programmiersprache für den generierten Code'
    )
    
    parser.add_argument(
        '--project-type',
        '-t',
        default='module',
        choices=['web_app', 'api', 'cli', 'library', 'module'],
        help='Art des Projekts'
    )
    
    parser.add_argument(
        '--output',
        '-o',
        help='Ausgabedatei für den generierten Code'
    )
    
    parser.add_argument(
        '--interactive',
        '-i',
        action='store_true',
        help='Interaktiver Modus'
    )
    
    args = parser.parse_args()
    
    # Initialisiere Round Table
    round_table = RoundTable()
    
    # Interaktiver Modus
    if args.interactive:
        await interactive_mode(round_table)
        return
    
    # Prüfe ob Task angegeben wurde
    if not args.task:
        parser.print_help()
        sys.exit(1)
    
    # Starte Diskussion
    context = {
        'language': args.language,
        'project_type': args.project_type
    }
    
    print(f"{Fore.CYAN}{'='*70}")
    print(f"{Fore.CYAN}🤖 Round Table - Multi-AI Kollaboration")
    print(f"{Fore.CYAN}{'='*70}\n")
    
    result = await round_table.discuss(args.task, context)
    
    # Formatiere und zeige Ergebnis
    formatted_output = round_table.format_result(result)
    print(formatted_output)
    
    # Optional: Speichere in Datei
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(result.consensus_code)
        print(f"{Fore.GREEN}✅ Code gespeichert in: {args.output}")
        
        # Speichere auch die Dokumentation
        doc_file = args.output.replace('.', '_discussion.')
        if '.' not in doc_file:
            doc_file = args.output + '_discussion.md'
        else:
            doc_file = doc_file.rsplit('.', 1)[0] + '.md'
        
        with open(doc_file, 'w', encoding='utf-8') as f:
            f.write(formatted_output)
        print(f"{Fore.GREEN}✅ Dokumentation gespeichert in: {doc_file}")


async def interactive_mode(round_table: RoundTable):
    """Interaktiver Modus für Round Table"""
    print(f"{Fore.CYAN}{'='*70}")
    print(f"{Fore.CYAN}🤖 Round Table - Interaktiver Modus")
    print(f"{Fore.CYAN}{'='*70}\n")
    print("Beschreiben Sie Ihre Aufgabe (oder 'exit' zum Beenden):\n")
    
    while True:
        try:
            task = input(f"{Fore.YELLOW}Aufgabe >>> {Style.RESET_ALL}").strip()
            
            if task.lower() in ['exit', 'quit', 'q']:
                print(f"{Fore.CYAN}Auf Wiedersehen! 👋")
                break
            
            if not task:
                continue
            
            # Frage nach Sprache
            print(f"\n{Fore.CYAN}Programmiersprache (python/javascript/typescript/java/go, Standard: python):")
            language = input(f"{Fore.YELLOW}>>> {Style.RESET_ALL}").strip().lower() or 'python'
            
            # Frage nach Projekt-Typ
            print(f"\n{Fore.CYAN}Projekt-Typ (web_app/api/cli/library/module, Standard: module):")
            project_type = input(f"{Fore.YELLOW}>>> {Style.RESET_ALL}").strip().lower() or 'module'
            
            print()
            
            # Diskussion starten
            context = {
                'language': language,
                'project_type': project_type
            }
            
            result = await round_table.discuss(task, context)
            
            # Zeige Ergebnis
            formatted_output = round_table.format_result(result)
            print(formatted_output)
            
            # Frage ob speichern
            print(f"\n{Fore.CYAN}Code speichern? (j/n, Standard: n):")
            save_input = input(f"{Fore.YELLOW}>>> {Style.RESET_ALL}").strip().lower()
            
            if save_input in ['j', 'ja', 'y', 'yes']:
                print(f"\n{Fore.CYAN}Dateiname:")
                filename = input(f"{Fore.YELLOW}>>> {Style.RESET_ALL}").strip()
                
                if filename:
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(result.consensus_code)
                    print(f"{Fore.GREEN}✅ Code gespeichert in: {filename}")
                    
                    # Speichere Dokumentation
                    doc_file = filename.rsplit('.', 1)[0] + '_discussion.md'
                    with open(doc_file, 'w', encoding='utf-8') as f:
                        f.write(formatted_output)
                    print(f"{Fore.GREEN}✅ Dokumentation gespeichert in: {doc_file}")
            
            print(f"\n{Fore.GREEN}Bereit für die nächste Aufgabe!\n")
            
        except KeyboardInterrupt:
            print(f"\n{Fore.CYAN}Auf Wiedersehen! 👋")
            break
        except Exception as e:
            print(f"{Fore.RED}❌ Fehler: {e}\n")


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n{Fore.CYAN}Auf Wiedersehen! 👋")
        sys.exit(0)
