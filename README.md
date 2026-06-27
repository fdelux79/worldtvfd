# Livetv — Proxy per stream TV

Server proxy che autentica e ritrasmette stream WebM per usarli in VLC/MPV/IINA.

Aprendo il pannello web trovi le liste TV pronte da copiare per ogni paese.

## Avvio su Docker

```bash
docker build -t livetv-native .
docker run -d -p 7860:7860 --name livetv livetv-native
```

Poi apri il pannello web per copiare i link delle liste da mettere sul programma IPTV.

## Su Hugging Face Spaces

1. Crea uno Space con **Docker**.
2. Carica i file di nel repo (senza il README.md).
3. Apri il pannello web dello Space per copiare i link delle liste.
