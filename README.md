# OpenWorld
Keine stare Reihenfolge

1. [] **Game Server Verwaltung** -> Start/Stop/Deploy/Remove   
   - [] Docker SDK
   - [] Bibliothek Client (PWA) -> Anzeige der Konfigurierten Game Server und dessen Verwaltung
2. [] **Game Katalog** -> Auswahl von vor konfigurierten images
   - [] JSON Katalog -> Enthält Spiel Eckdaten und Server Konfiguration, sowie den pfad zum downloaden des Images
   - [] Katalog Service -> Business Logik für das Laden und aufsetzen von Game Servern
   - [] Katalog / Game Server auswahl Client (PWA)
3. [] **Chat**
   - [] Websocket 
     - [] Server
     - [] Client (PWA)
   - [] Gruppen Chat
   - [] Private Chat
4. [] **Authentication** -> Gruppe / Rollen / Rechte
5. [] **Website die von Flask geliefert wird Installierbar auf Homescreen/Desktop** -> PWA 
   - [] Manifest
   - [] Favicon verschiedene Auflösung
   - [] Serviceworker
6. [] **Notification System** -> Informiert alle aus der Gruppe wenn ein server gestartet oder gestoppt wird
   - [] Signals
   - [] Push Notificaion Client (PWA)
7. [] **Game Server Backup**
   - [] FTP File Server Konfiguration
   - [] Git LFS alternative
   - [] Docker Volume alternative