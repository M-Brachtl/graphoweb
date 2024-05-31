# Popis
Projekt se skládá ze dvou částí:
* Front-end
* Back-end   

Dohromady tvoří webovou stránku, na které si uživatel zadá tabulku dat, konkrétně bodů za jednotlivé disciplíny. Může přidávat a odebírat jednotlivé účastníky.   
Po zmáčknutí tlačítka 'Otevřít graf' se otevře graf z hodnot v tabulce.

## Front-end
Na front-endu si uživatel zadá své data, jak popsáno dříve. Po zmáčknutí tlačítka k otevření grafu JavaScript sesbírá data z tabulky, uspořádá je do JSON objektu a pošle na server.  
Poté čeká, až server zpátky pošle obrázek 'output.png', který je oním grafem. Ten se poté zobrazí.

## Back-end
Back-end je tvořen pomocí Pythonu, konkrétně pomocí FastAPI.  
Po zisku dat z Back-endu je Python ještě jednou přeuspořádá do dvou listů, které potom zpracuje pomocí matplotlib. Výstupem pak je sloupcový graf.

## Nastavení prostředí pro server
Pokud uživatel nemá knihovny FastAPI a Matplotlib nainstalované globálně, může tak učinit pomocí posledních dvou příkazů.  
Druhou možností je vytvořit virtuální prostředí tímto způsobem:
```bash
    python -m venv venv
    venv\Scripts\activate
    pip install fastapi
    pip install matplotlib
```
Pokud terminál ve VScode odmítá spustit script, je možné, že to blokuje PowerShell. Můžete zkusit to samá udělat přes cmd.exe

## Spuštění
První je potřeba spustit server, tedy soupor 'server.py'   
Poté už může uživatel otevřít svůj prohlížeč a do adresního řádku zadat [localhost:8000](localhost:8000), kde se web nachází.
