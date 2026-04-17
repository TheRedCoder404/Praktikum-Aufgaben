# Praktikum-Aufgaben – Fun with Webdevelopment

In diesem Projekt lernst du Schritt für Schritt die Grundlagen der Webentwicklung kennen: **HTML**, **CSS** und **React mit TypeScript**.

---

## 1. Tags, Tags, Tags

HTML-Tags sind die **Bausteine einer Webseite**. Mit ihnen sagst du dem Browser, was ein Stück Inhalt ist – z. B. eine Überschrift, ein Absatz, ein Bild oder ein Link.

Viele Tags bekommen zusätzliche Infos über sogenannte **Attribute**. Sie stehen direkt im öffnenden Tag und sehen so aus: `name="wert"`.

### Los geht's

1. Öffne `01-html-grundstruktur/standard_html.html` und schau dir die Grundstruktur einer HTML-Datei an.
2. Wechsle dann zu `01-html-grundstruktur/uebung01_tags.html` und bearbeite die Aufgaben, die dort als Kommentare stehen.

---

## 2. Styling

**Styling** heißt: der Webseite ein Aussehen geben – Farben, Schriftarten, Abstände, Layout. HTML sagt, **was** etwas ist. CSS sagt, **wie** es aussieht.

Es gibt drei Wege, HTML zu stylen:

1. **Inline-Styling** – direkt am Tag über das `style`-Attribut.
2. **Internes Styling** – im `<style>`-Tag im `<head>` der HTML-Datei.
3. **Externes Styling** – eine eigene `.css`-Datei, die per `<link>` eingebunden wird. Das ist der sauberste Weg, weil HTML und Styling getrennt sind.

Nimm dir gerne zur Bearbeitung der Aufgaben dieses Cheatsheet zur Hilfe: https://hacker-school.notion.site/Cheatsheet-HTML-CSS-1ab82980cc338085b27add57d898cf83

💡 Später wirst du vielleicht auch von **CSS-Frameworks** (z. B. Tailwind, Bootstrap) oder **CSS-in-JS** hören. Das sind nur andere Verpackungen für dieselbe Idee.

### Los geht's

1. Öffne `02-html-styling/uebung02_styling.html` und bearbeite **Aufgabe 1 und 2**.
2. Bevor du mit **Aufgabe 3** (externes Stylesheet) startest, schau dir `02-html-styling/standard_html_styled.html` an. Diese Datei ist eine Kopie von `standard_html.html`, aber mit einem kleinen Unterschied: Sie ist mit `standard_style.css` verknüpft.
3. Öffne auch `02-html-styling/standard_style.css`. Erkennst du einige Begriffe wieder?
4. Wenn du dich bereit fühlst, deine eigene CSS-Datei zu schreiben → weiter mit **Aufgabe 3**.

---

## 3. Der Inspektor

Der **Inspektor** (engl. *DevTools*) ist eines der wichtigsten Werkzeuge in der Webentwicklung. Mit ihm kannst du dir den Code jeder Webseite anschauen und **temporär verändern** – perfekt, um Dinge auszuprobieren, ohne die echte Seite zu beeinflussen.

### So öffnest du ihn

- **Rechtsklick** auf die Seite → **„Untersuchen"** / **„Inspect"**, oder
- Taste **F12** drücken (auf Mac: `Cmd + Option + I`).

### Was du damit machen kannst

- Den **HTML-Aufbau** einer Seite ansehen (Reiter *Elements*).
- **CSS-Styles** live ändern und sofort sehen, wie sich die Seite verändert.
- Sehen, wie eine Seite auf **verschiedenen Bildschirmgrößen** aussieht (Handy, Tablet, Desktop).

### Los geht's

Öffne diese Beispielseite und probiere den Inspektor aus:  
https://www.w3schools.com/w3css/tryw3css_templates_gourmet_catering.htm

👉 Versuch's mal: Ändere eine Überschrift, tausche eine Farbe aus, oder versteck ein Bild. Keine Angst – beim Neuladen ist alles wieder beim Alten!

---

## 4. React & TypeScript

**React** ist eine JavaScript-Bibliothek, mit der man Webseiten aus **wiederverwendbaren Komponenten** baut. Statt eine große HTML-Datei zu schreiben, zerlegst du die Seite in kleine Bausteine, die du beliebig kombinieren kannst.

**TypeScript** ist JavaScript mit sogenannten **Typen**. Du sagst dem Code vorher, welche Art von Daten erwartet werden – z. B. dass eine Variable eine Zahl ist. Dadurch werden Fehler schon beim Schreiben erkannt, nicht erst im Browser.

### Los geht's

1. Öffne den Ordner `03-react` und klick dich durch die Dateien. Kannst du dir vorstellen, was in den einzelnen Datein passiert? Erkennst du etwas wieder? Keine Sorge, wir gehen den Code gemeinsam durch.
2. **Erste React-Aufgabe:** Starte das Projekt lokal. Führe dazu im Terminal aus:
   ```bash
   cd 03-react
   npm run dev
   ```
   Wenn alles funktioniert, erscheint im Terminal ein Link – klick ihn an, um deine Seite im Browser zu sehen.
3. **Zweite React-Aufgabe:** Baue einen **MUI-Button** in die Datei `03-react/src/components/App.tsx` ein.

> 💡 MUI (Material UI) ist eine Bibliothek mit fertigen React-Komponenten. Schau dir die Doku an: https://mui.com/material-ui/react-button/

---

## 5. Real-life-Projekte aus Conversion

Jetzt schauen wir uns an, wie die Dinge, die du gerade gelernt hast, **in echten Projekten** eingesetzt werden.

### 🎮 Landingpage Anubis

Eine echte Landingpage aus unserem Conversion-Team:  
https://xc-play.heroesofhistorygame.com/?distinct=anubis

**Was wir gemeinsam machen:**
1. Die Seite im Browser öffnen und mit dem **Inspektor** anschauen.
2. Entdecken, aus welchen Bausteinen sie besteht – und vielleicht etwas ausprobieren.
3. Anschließend die **Codebase** öffnen und schauen, wie die Seite wirklich aufgebaut ist.

### 🛠️ OneLPS – unser Admin-Tool

**OneLPS** ist unser eigenes Admin-Tool. Damit kann man Bundles, Routing, A/B-Tests und vieles mehr ganz einfach über eine **Benutzeroberfläche (UI)** einstellen – ohne jedes Mal Code anfassen zu müssen.

Das Frontend von OneLPS ist ebenfalls mit **React** geschrieben – also genau mit der Technologie, die du gerade kennengelernt hast. 🎉

---

Viel Spaß beim Coden! 🚀