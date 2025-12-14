"""
Sichere, kompatible RoundTable-Implementierung (zum Hinzufügen ins Repo).

API-Kompatibilität:
- RoundTable().discuss(task: str, context: dict | None) -> SimpleNamespace
    - Gibt ein Objekt mit attributes:
        - consensus_code: str
        - individual_responses: list of SimpleNamespace (mit model.value und recommendation)
        - raw_responses: dict (Agent-Antworten)
- RoundTable.format_result(result) -> str
"""
import asyncio
import ast
from types import MethodType, SimpleNamespace
from typing import Any, Dict, List, Optional, Tuple


class Agent:
    def __init__(self, name: str, role: str) -> None:
        self.name = name
        self.role = role

    def respond(self, input_data: str) -> str:
        if self.role == "analysis":
            return f"Analysis Agent: Identified weakness - {input_data}. Potential threats: Regulatory hurdles, competition."
        elif self.role == "creative":
            return f"Creative Agent: Suggest solution - Integrate self-optimization to mitigate {input_data}."
        elif self.role == "tech":
            code_snippet = (
                "def mitigate_weakness(self):\n"
                "    print('Mitigating {} with self-optimization extension.')\n"
            ).format(input_data.replace("'", "\\'"))
            return f"Tech Agent: Generating code extension: {code_snippet}"
        elif self.role == "security":
            return f"Security Agent: Reviewed code for {input_data} - Secure and compliant."
        return f"{self.name}: No response."


class RoundTable:
    def __init__(self) -> None:
        self.agents: List[Agent] = [
            Agent("Analysis-KI", "analysis"),
            Agent("Kreativ-KI", "creative"),
            Agent("Tech-KI", "tech"),
            Agent("Security-KI", "security"),
        ]
        # Gebundene Erweiterungsfunktionen
        self.extensions: Dict[str, Any] = {}

    async def discuss(self, task: str, context: Optional[Dict[str, Any]] = None) -> SimpleNamespace:
        """
        Führt die Diskussionskette aus und liefert ein Ergebnisobjekt zurück.
        Minimal kompatibel zu demo_round_table.py (consensus_code, individual_responses).
        """
        # Context kann genutzt werden, hier nur als Info weitergegeben
        prompt = task
        if context:
            prompt = f"{task} | context: {context}"

        responses: Dict[str, str] = {}
        current_input = prompt
        for agent in self.agents:
            try:
                resp = agent.respond(current_input)
            except Exception as e:
                resp = f"Error in agent.respond: {e}"
            responses[agent.name] = resp
            current_input = resp  # chaining

        # Versuche Self-Extension (sicherheitshalber eingeschränkt)
        tech_response = responses.get("Tech-KI", "")
        consensus_code = ""
        if "Generating code extension:" in tech_response:
            code_snippet = tech_response.split("Generating code extension:", 1)[1].strip()
            # Versuche das Snippet sicher zu validieren + zu laden
            ok, result = self._validate_and_load_extension(code_snippet)
            if ok:
                func_name = result
                consensus_code = code_snippet
                # Rufe gebundene Funktion demonstrativ auf (nur print erlaubt)
                try:
                    fn = self.extensions.get(func_name)
                    if callable(fn):
                        fn()  # bound method
                except Exception:
                    pass

        # Baue individual_responses so auf, dass demo_round_table.py damit arbeiten kann
        individual_responses: List[SimpleNamespace] = []
        for agent in self.agents:
            raw = responses.get(agent.name, "")
            # model.value muss existieren; wir nutzen die Rolle als value
            model = SimpleNamespace(value=agent.role)
            recommendation = raw
            individual_responses.append(SimpleNamespace(model=model, recommendation=recommendation))

        result_obj = SimpleNamespace(
            consensus_code=consensus_code,
            individual_responses=individual_responses,
            raw_responses=responses,
        )
        return result_obj

    def format_result(self, result: SimpleNamespace) -> str:
        """Einfache Formatierhilfe, erzeugt eine lesbare Zusammenfassung."""
        lines: List[str] = []
        lines.append("RoundTable Zusammenfassung:")
        lines.append("- Consensus Code (falls vorhanden):")
        cc = result.consensus_code or "<kein consensus code>"
        lines.append(cc)
        lines.append("- Einzelantworten:")
        for resp in result.individual_responses:
            lines.append(f"  • {resp.model.value.upper()}: {resp.recommendation}")
        return "\n".join(lines)

    def _validate_and_load_extension(self, code_snippet: str) -> Tuple[bool, str]:
        """
        Sehr konservative Validierung und Laden einer einzelnen FunctionDef.
        Erlaubt nur: eine def-Funktion, keine Imports, keine Zuweisungen, nur print()-Aufrufe.
        Bei Erfolg: bindet die Funktion an self und speichert sie unter ihrem Namen.
        Rückgabe:
          (True, func_name) oder (False, error_message)
        """
        try:
            parsed = ast.parse(code_snippet)
        except SyntaxError as se:
            return False, f"SyntaxError: {se}"

        if len(parsed.body) != 1 or not isinstance(parsed.body[0], ast.FunctionDef):
            return False, "Code muss genau eine FunctionDef enthalten."

        func_def = parsed.body[0]
        func_name = func_def.name

        banned_nodes = (
            ast.Import,
            ast.ImportFrom,
            ast.Attribute,
            ast.Subscript,
            ast.Assign,
            ast.AugAssign,
            ast.Global,
            ast.Nonlocal,
            ast.ClassDef,
            ast.Lambda,
            ast.AsyncFunctionDef,
            ast.While,
            ast.For,
            ast.Try,
            ast.With,
            ast.Raise,
            ast.Delete,
            ast.ListComp,
            ast.SetComp,
            ast.DictComp,
            ast.GeneratorExp,
        )

        for node in ast.walk(func_def):
            if isinstance(node, banned_nodes):
                return False, f"Verbotener AST-Knoten: {node.__class__.__name__}"
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    if node.func.id != "print":
                        return False, f"Nur print() erlaubt, gefunden: {node.func.id}"
                else:
                    return False, "Nur direkte Funktionsnamen-Aufrufe (z.B. print()) erlaubt."

        safe_globals: Dict[str, Any] = {"__builtins__": {}, "print": print}
        local_ns: Dict[str, Any] = {}
        try:
            compiled = compile(parsed, filename="<safe_ext>", mode="exec")
            exec(compiled, safe_globals, local_ns)
        except Exception as e:
            return False, f"Fehler beim Ausführen: {e}"

        func_obj = local_ns.get(func_name) or safe_globals.get(func_name)
        if not func_obj or not callable(func_obj):
            return False, "Funktion nicht gefunden nach Ausführung."

        bound = MethodType(func_obj, self)
        self.extensions[func_name] = bound
        return True, func_name


# einfacher CLI-Test wenn als Script ausgeführt
if __name__ == "__main__":
    async def _run_demo():
        rt = RoundTable()
        res = await rt.discuss("Early phase vulnerability in business plan")
        print(rt.format_result(res))

    asyncio.run(_run_demo())
