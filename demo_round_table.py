#!/usr/bin/env python3
"""
Round Table Demo - Zeigt die Funktionalität des Round Table Systems

Dieses Skript demonstriert verschiedene Anwendungsfälle des Round Table Systems.
"""
import asyncio
import sys
import os
from colorama import init, Fore, Style

# Importiere Round Table
from roundtable_safe import RoundTable

# Initialisiere Colorama
init(autoreset=True)


async def demo_basic_usage():
    """Demonstriert grundlegende Verwendung"""
    print(f"{Fore.CYAN}{'='*70}")
    print(f"{Fore.CYAN}DEMO 1: Grundlegende Verwendung")
    print(f"{Fore.CYAN}{'='*70}\n")
    
    rt = RoundTable()
    
    result = await rt.discuss(
        task="Erstelle ein Modul für User Authentication",
        context={'language': 'python', 'project_type': 'api'}
    )
    
    print(rt.format_result(result))
    
    print(f"\n{Fore.GREEN}✅ Demo 1 abgeschlossen!\n")
    input(f"{Fore.YELLOW}Drücke Enter für nächste Demo...")


async def demo_typescript():
    """Demonstriert TypeScript Code-Generierung"""
    print(f"\n{Fore.CYAN}{'='*70}")
    print(f"{Fore.CYAN}DEMO 2: TypeScript Code-Generierung")
    print(f"{Fore.CYAN}{'='*70}\n")
    
    rt = RoundTable()
    
    result = await rt.discuss(
        task="Entwickle eine wiederverwendbare Button Komponente",
        context={'language': 'typescript', 'project_type': 'web_app'}
    )
    
    # Zeige nur den Code
    print(f"{Fore.GREEN}Generierter TypeScript Code:")
    print(f"{Fore.CYAN}{'='*70}")
    print(result.consensus_code)
    print(f"{Fore.CYAN}{'='*70}")
    
    print(f"\n{Fore.GREEN}✅ Demo 2 abgeschlossen!\n")
    input(f"{Fore.YELLOW}Drücke Enter für nächste Demo...")


async def demo_multiple_tasks():
    """Demonstriert mehrere Aufgaben hintereinander"""
    print(f"\n{Fore.CYAN}{'='*70}")
    print(f"{Fore.CYAN}DEMO 3: Mehrere Aufgaben sequenziell")
    print(f"{Fore.CYAN}{'='*70}\n")
    
    rt = RoundTable()
    
    tasks = [
        ("Erstelle ein Logging-Modul", {'language': 'python'}),
        ("Entwickle einen API Client", {'language': 'javascript'}),
        ("Baue ein Data Validation Modul", {'language': 'typescript'})
    ]
    
    for i, (task, context) in enumerate(tasks, 1):
        print(f"{Fore.YELLOW}Aufgabe {i}/{len(tasks)}: {task}")
        
        result = await rt.discuss(task=task, context=context)
        
        # Zeige nur Zusammenfassung
        print(f"{Fore.GREEN}Empfehlungen:")
        for response in result.individual_responses:
            print(f"  • {response.model.value.upper()}: {response.recommendation[:80]}...")
        
        print()
    
    print(f"{Fore.GREEN}✅ Demo 3 abgeschlossen - {len(tasks)} Module generiert!\n")
    input(f"{Fore.YELLOW}Drücke Enter für nächste Demo...")


async def demo_file_export():
    """Demonstriert Datei-Export"""
    print(f"\n{Fore.CYAN}{'='*70}")
    print(f"{Fore.CYAN}DEMO 4: Code-Export in Dateien")
    print(f"{Fore.CYAN}{'='*70}\n")
    
    rt = RoundTable()
    
    result = await rt.discuss(
        task="Erstelle ein Configuration Manager Modul",
        context={'language': 'python', 'project_type': 'library'}
    )
    
    # Exportiere in Dateien
    output_dir = "/tmp/round_table_demo"
    os.makedirs(output_dir, exist_ok=True)
    
    code_file = os.path.join(output_dir, "config_manager.py")
    with open(code_file, 'w', encoding='utf-8') as f:
        f.write(result.consensus_code)
    
    doc_file = os.path.join(output_dir, "discussion.md")
    with open(doc_file, 'w', encoding='utf-8') as f:
        f.write(rt.format_result(result))
    
    print(f"{Fore.GREEN}✅ Dateien exportiert:")
    print(f"   📄 Code: {code_file}")
    print(f"   📄 Dokumentation: {doc_file}")
    
    print(f"\n{Fore.GREEN}✅ Demo 4 abgeschlossen!\n")
    input(f"{Fore.YELLOW}Drücke Enter für nächste Demo...")


async def demo_comparison():
    """Vergleicht verschiedene Ansätze für dieselbe Aufgabe"""
    print(f"\n{Fore.CYAN}{'='*70}")
    print(f"{Fore.CYAN}DEMO 5: Sprachvergleich für dieselbe Aufgabe")
    print(f"{Fore.CYAN}{'='*70}\n")
    
    rt = RoundTable()
    
    task = "Erstelle ein einfaches HTTP Request Modul"
    languages = ['python', 'javascript', 'typescript']
    
    for lang in languages:
        print(f"{Fore.YELLOW}▶ Generiere in {lang.upper()}...")
        
        result = await rt.discuss(
            task=task,
            context={'language': lang, 'project_type': 'library'}
        )
        
        # Zeige Vorschau
        code_preview = result.consensus_code.split('\n')[:15]
        print(f"{Fore.GREEN}Code-Vorschau ({lang}):")
        print(f"{Fore.CYAN}{'-'*70}")
        for line in code_preview:
            print(line)
        print(f"{Fore.CYAN}{'-'*70}\n")
    
    print(f"{Fore.GREEN}✅ Demo 5 abgeschlossen - {len(languages)} Sprachen!\n")
    input(f"{Fore.YELLOW}Drücke Enter zum Beenden...")


async def main():
    """Hauptfunktion"""
    print(f"{Fore.CYAN}{'='*70}")
    print(f"{Fore.CYAN}🤖 ROUND TABLE DEMONSTRATION")
    print(f"{Fore.CYAN}{'='*70}")
    print(f"{Fore.CYAN}Dieses Demo-Skript zeigt verschiedene Anwendungsfälle")
    print(f"{Fore.CYAN}des Round Table Multi-AI Kollaborations-Systems")
    print(f"{Fore.CYAN}{'='*70}\n")
    
    demos = [
        ("Grundlegende Verwendung", demo_basic_usage),
        ("TypeScript Code-Generierung", demo_typescript),
        ("Mehrere Aufgaben sequenziell", demo_multiple_tasks),
        ("Code-Export in Dateien", demo_file_export),
        ("Sprachvergleich", demo_comparison)
    ]
    
    print(f"{Fore.YELLOW}Verfügbare Demos:")
    for i, (name, _) in enumerate(demos, 1):
        print(f"  {i}. {name}")
    
    print(f"\n{Fore.CYAN}Wähle Demo (1-{len(demos)}) oder 'all' für alle:")
    choice = input(f"{Fore.YELLOW}>>> {Style.RESET_ALL}").strip().lower()
    
    if choice == 'all':
        # Führe alle Demos aus
        for name, demo_func in demos:
            await demo_func()
    else:
        # Führe ausgewählte Demo aus
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(demos):
                name, demo_func = demos[idx]
                await demo_func()
            else:
                print(f"{Fore.RED}Ungültige Auswahl!")
        except ValueError:
            print(f"{Fore.RED}Ungültige Eingabe!")
    
    print(f"\n{Fore.CYAN}{'='*70}")
    print(f"{Fore.GREEN}✅ Alle Demos abgeschlossen!")
    print(f"{Fore.CYAN}{'='*70}")
    print(f"\n{Fore.YELLOW}Weitere Informationen:")
    print(f"  📖 Dokumentation: ROUND_TABLE.md")
    print(f"  🔧 CLI Tool: python round_table_cli.py --help")
    print(f"  🤖 Auto-Coder: python auto_coder.py --round-table")
    print()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n{Fore.CYAN}Demo abgebrochen.")
        sys.exit(0)
