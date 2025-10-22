from fastapi import FastAPI
from codex_engine.invocation import InvocationEngine
from codex_engine.echo_matrix import echo_matrix
from codex_engine.archive import archive
from codex_engine.glyphs import glyphs

app = FastAPI()

@app.post("/launch")
def launch_codex():
    engine = InvocationEngine(glyphs, echo_matrix, archive)
    engine.launch()
    return {"status": "Codex X launched"}