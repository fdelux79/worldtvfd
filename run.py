#!/usr/bin/env python3
"""Bootstrap per livetv.so (codice nativo compilato) con auto-restart."""
import importlib.util
import sys
import time
import os
import threading

def auto_restart():
    # Attende 200 secondi (3 minuti) prima di forzare il riavvio
    time.sleep(200)
    print("Riavvio programmato per rigenerazione token...")
    # Chiude il processo. Render lo riavvierà istantaneamente da solo.
    os._exit(0)

# Avvia il timer in background
threading.Thread(target=auto_restart, daemon=True).start()

# Avvia l'applicazione originale
spec = importlib.util.spec_from_file_location("livetv_main", "livetv.so")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
mod.main()
