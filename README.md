# Wortkasten

Englisch-Vokabeltrainer für Emil und Paula auf dem iPad.
Adresse: https://vokabeltrainer-ebg.github.io/

## Einrichten auf dem iPad
1. Adresse in **Safari** öffnen.
2. Code eingeben (`emil` oder `paula`, Groß-/Kleinschreibung egal). Die App merkt sich den Code.
3. Teilen → „Zum Home-Bildschirm“.
4. Umzug: Im alten Trainer unter Eltern → Einstellungen „Sicherungscode kopieren“, dann in der neuen App auf der Startseite einfügen und „Übernehmen“ tippen.
5. Unter „Eltern“ ist danach die PIN aus dem alten Trainer gültig.

Zum Wechseln des Kindes: Eltern → Einstellungen → Profil → Abmelden. Der Lernstand bleibt auf dem iPad gespeichert.

## Aufbau
```
src/app.html             Quelle (alle Kinder gemeinsam, Profile oben in PROFILES)
index.html               python3 tools/build_index.py
emil/lektionen/*.txt     Vokabellisten Emil (Lighthouse, Klasse 7)
paula/lektionen/*.txt    Vokabellisten Paula (Lighthouse 1, Jahrgang 6)
<kind>/lektionen.json    python3 tools/build_lessons.py (baut alle Kinder)
icon.png                 neutrales Icon (vor der Code-Eingabe)
icon-<kind>.png          Icon pro Kind
```
Lernstand pro Kind im localStorage unter `wortkasten-<kind>.v1`, gewähltes Profil unter `wortkasten.profil`.

## Neues Kind
In `src/app.html` bei `PROFILES` eintragen, Ordner `<kind>/lektionen/` anlegen, `icon-<kind>.png` hinzufügen, eigene Farben über `:root[data-kid="<kind>"]` in der CSS, dann beide Build-Skripte ausführen.

## Lektionsformat
```
# Lektion: Lighthouse – Unit 2 – S. 216–217
Englisch ; Deutsch ; Satz Englisch ; Satz Deutsch ; Formen (go - went - gone)
```
Mehrere richtige Antworten mit `/`. Das Zielwort muss wörtlich im englischen Satz stehen (führendes „to“ wird ignoriert). Veröffentlichte Lektionen nicht umbenennen, sonst geht der Lernstand verloren.

## Farm (Belohnungsspiel)
- Ordner `farm/` (Spiel + Bilder). Wird mit `python3 tools/build_farm.py <Farm-Quellordner>` erzeugt – nicht von Hand ändern.
- Jede richtige Antwort im Wortkasten landet in `farm-<kind>.inbox` (pro Tag, leicht/schwer getrennt). Die Farm übernimmt sie beim Öffnen: Samen (leicht 1, schwer 2, ab 30 Antworten am Tag halb) und Zähler bis 60 → Spielen freigeschaltet.
- Spielstand: `farm-<kind>.v1`. Ohne Profil leitet die Farm zum Wortkasten zurück.
- Testbereich der Farm nur mit `farm/?test`.
