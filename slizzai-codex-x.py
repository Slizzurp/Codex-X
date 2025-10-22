import time
from datetime import datetime

class EchoMatrix:
    def __init__(self):
        self.echo_log = {}

    def store_echo(self, glyph_name, echo):
        timestamp = datetime.utcnow().isoformat()
        self.echo_log.setdefault(glyph_name, []).append((timestamp, echo))
        print(f"📜 [{glyph_name}] Echo stored: {echo} @ {timestamp}")

class OrbitalArchive:
    def __init__(self):
        self.entries = []

    def log_entry(self, glyph_name, event_type):
        timestamp = datetime.utcnow().isoformat()
        entry = f"{timestamp} | {glyph_name} | {event_type}"
        self.entries.append(entry)
        print(f"🗂️ Archived: {entry}")

class Glyph:
    def __init__(self, name, symbol, role, status, sync_depth):
        self.name = name
        self.symbol = symbol
        self.role = role
        self.status = status
        self.sync_depth = sync_depth
        self.echoes = []

    def log_event(self, event_type, echo_matrix, archive):
        print(f"🔧 [{self.name}] Logging event: {event_type}")
        archive.log_entry(self.name, event_type)
        self.sync_echo(event_type, echo_matrix)

    def sync_echo(self, event_type, echo_matrix):
        for depth in range(1, self.sync_depth + 1):
            echo = f"{event_type}_echo_{depth}"
            self.echoes.append(echo)
            echo_matrix.store_echo(self.name, echo)
            print(f"→ Echoed: {echo}")

class InvocationEngine:
    def __init__(self, glyphs, echo_matrix, archive):
        self.glyphs = glyphs
        self.echo_matrix = echo_matrix
        self.archive = archive

    def launch(self):
        print("🚀 Codex X Launch Ritual Initiated...")
        for glyph in self.glyphs:
            glyph.log_event("Codex_Sync", self.echo_matrix, self.archive)

# Initialize components
echo_matrix = EchoMatrix()
archive = OrbitalArchive()

glyphs = [
    Glyph("Seer of the Surface", "🜁", "Observer", "Active", 2),
    Glyph("Whisperer Beyond", "🜃", "Relay", "Online", 3),
    Glyph("Guardian of Silence", "🜄", "Sentinel", "Monitoring", 1),
    Glyph("Archivist of Orbits", "🜂", "Archivist", "Deploying", 2)
]

engine = InvocationEngine(glyphs, echo_matrix, archive)
engine.launch()