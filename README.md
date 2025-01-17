 ![alt text](https://github.com/OShu4/Watch-Out/blob/main/Watch-Out/src/main/python/assets/Logo/applogo.png) 
# Watch-Out!
## Introduzione al progetto

### Scopo del programma: 
##### Creazione di un reaction-game strutturato in 5 livelli. Il giocatore affronterà quindi 5 diversi nemici, con stage a difficoltà crescente, con sempre meno tempo per agire, in un ambiente retrò coinvolgente.

## Sviluppato con 
- Python, libreria pygame

## Partecipanti del gruppo
- **Galantini Corrado**
- **Gallo Valerio**
- **Aprea Mario**      
- **Di Muzio Pietro**
- **Pesaresi Adriano** 
- **Sturniolo Edoardo**

### Installazione del videogioco
L'applicativo sarà scaricabile mediante l'apposito bottone *download* nel sito ufficiale del gioco "link".

## WatchOut.exe e download

### Spiegazione generale del funzionamento del menu del videogioco:
Il gioco, una volta installato e avviato, presenterà un menu di scelta dove l'utente potrà decidere tra:
* **Play** -> Avvia il gioco, partendo dal primo livello.
```python
background_window(OWN_PG, ENEMY_PG,ENEMY_PG_img, EXIT, MENU_MOUSE_POS)
```
* **Set Easy** -> Semplifica il livello di gioco, rallentando i timer prima dello scatto del Watch-Out!
* '''python
* '''
* **Select level** -> Una volta completato il gioco almeno una volta, il giocatore sarà abilitato alla scelta di uno dei 5 livelli disponibili da giocare.
* '''python
* '''
* **Quit** -> Chiude il processo del gioco.
* '''python
* '''

Una volta avviata la partita l'utente troverà a schermo una mappa occupata da due personaggi *(da ora **pg**)*, il pg del giocatore e quello avversario, governato dal computer. I pg rimarranno fermi durante tutto il corso della partita. Dopo un intervallo randomico di secondi apparirà a schermo la scritta **Watch Out**, a quel punto il giocatore dovrà premere il tasto sinistro del mouse prima del pg nemico, aggiudicandosi la vittoria ed il lascia passare al livello successivo.
Inoltre il giocatore, sempre nella schermata di gioco, in alto a destra, troverà il suo numero di vite rimanenti. A partire da 5. Ogni volta che perderà verranno diminuite di 1. Una volta terminate, sarà game over e dovrà ricominciare il gioco da capo.
   

## Classi
- [-] main.py
- [-] button.py
- [-] fileManager.py
- [-] spritesheet.py

## Codice, Protocolli ed Esempi

## Ulteriori informazioni

## Sprite & Assets
Gli sprite, o pixel-art del gioco sono stati disegnati attraverso il software Piskel, a mano. Ogni singolo disegno è originale, inoltre i disegni sono animati a 2 frame per secondo all'interno del gioco.

### Traguardi
- [❌] Funzionamento del gioco su MacOS.
- [✔️] Gestione variabili d'ambiente.
- [✔️] Ottimizzazione per diminuzione dell'uso in percentuale della CPU.
- [✔️] Salvataggio dei dati in file binari. (Dati del punteggio del giocatore, e dati del completamento dei livelli.)
- [✔️] Creazione di tutte le pixel-art.
- [✔️] Sistema delle vite.

## Contatti

### Galantini Corrado
- galantini.corrado@istitutomontani.edu.it
- Git <a href="https://github.com/OShu4">OShu4 </a> 
- Discord Mario Giordano#3698

### Gallo Valerio
- gallo.valerio@istitutomontani.edu.it
- Git <a href="https://github.com/Vallozz">Vallozz </a>
