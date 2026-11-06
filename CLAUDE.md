# CLAUDE.md — Sito istituzionale Lachi Solutions

Questo repository contiene il sito vetrina di Lachi Solutions, consulenza IT indipendente con sede a Ginevra. Obiettivo: una pagina istituzionale molto semplice e pulita, in quattro lingue (FR, EN, IT, SL). Nessun blog, nessun form complesso, nessun framework pesante.

## Struttura del repository

- `index.html` reindirizza a `fr/` (o alla lingua salvata/del browser via JS).
- `fr/`, `en/`, `it/`, `sl/`: una `index.html` per lingua; `fr/mentions-legales.html`, `fr/confidentialite.html`, `en/legal-notice.html`, `en/privacy.html`.
- `assets/style.css`, `assets/lang.js`, `assets/favicon.svg`.
- `tools/gen.py`: generatore opzionale (testi in un dizionario Python → HTML). Non è un build step obbligatorio: le pagine HTML sono committate e si possono modificare a mano; se si usa il generatore, rilanciarlo con `python3 tools/gen.py` dalla radice.

## Regole di lavoro

* Lingua con Ivo: italiano. I testi del sito nelle quattro lingue.
* Non inventare dati societari, clienti, cifre o certificazioni: usare solo quelli in questo file. Se manca qualcosa, lasciare un segnaposto `TODO` e chiederlo.
* Non citare clienti per nome (Epipoli, Cleverad) né LinkedIn nel corpo della pagina. LinkedIn può stare solo come icona nel footer.
* Non usare foto stock di persone, né immagini di terzi. Solo tipografia, spazio bianco, eventualmente un logo/monogramma testuale "LS".
* Nessun tracking, nessun cookie banner: niente analytics di terzi. Se serve statistica in futuro, usare una soluzione cookieless self-hosted.
* Il sito deve funzionare aperto da file e su hosting statico qualunque (Netlify, Cloudflare Pages, GitHub Pages).

## Stack

* HTML statico + CSS, senza framework CSS e senza build step obbligatorio. JavaScript solo per il selettore lingua (poche righe, vanilla).
* Una pagina per lingua in sottocartella (`/fr/index.html`, `/en/`, `/it/`, `/sl/`), con `/index.html` che reindirizza a `/fr/` (lingua di default: francese, sede a Ginevra).
* Tag `hreflang` incrociati tra le quattro versioni. `lang` corretto su `<html>`.
* Font: Archivo self-hosted (pesi 300, 400, 800), subset Latin + Latin Extended. Niente Google Fonts remoto.
* Palette del design system Lachi Solutions: sfondo grigio `#f3f2f2`, testo nero `#201e1d`, un solo accento rosso `#ec3013` (scuro `#ae1800`), angoli vivi, logo tipografico "lachi ■ / solutions" (ExtraBold + quadrato rosso, barra 2 px, sottotitolo Light). Pesi: 300 solo nel logo, 400 testo, 800 titoli.
* Responsive, mobile-first, contrasto AA, HTML semantico, `<title>` e `<meta description>` per lingua, Open Graph minimo, favicon SVG.
* Dimensione totale della pagina sotto i 200 KB.

## Struttura della pagina (una sola pagina, scroll verticale)

1. Header: wordmark "Lachi Solutions", selettore lingua (FR · EN · IT · SL), nulla altro.
2. Hero: titolo di una riga, sottotitolo di una o due righe, un solo pulsante "Contatto" che porta alla sezione contatti.
3. Servizi: quattro blocchi brevi. Titolo + due o tre righe ciascuno. Niente icone elaborate.
4. Approccio / Chi sono: un paragrafo sul fondatore e il modo di lavorare. Niente foto.
5. Contatti: email, telefono, indirizzo. Nessun form.
6. Footer: ragione sociale, forma giuridica, sede, IDE, link a Impressum/Mentions légales e Privacy, icona LinkedIn.

Pagine secondarie minime: `mentions-legales` (Impressum) e `confidentialite` (privacy), solo in FR ed EN, testo essenziale.

## Dati societari (fonte: estratto Registre du commerce, 27.10.2026)

* Ragione sociale: Lachi Solutions
* Forma giuridica: entreprise individuelle (raison individuelle)
* Titolare: Ivo Lachi, firma individuale
* Sede: Genève
* Indirizzo: Rue Rothschild 54, 1202 Genève, Suisse
* IDE: CHE-432.855.350
* Iscrizione RC: 22 ottobre 2026
* Scopo statutario (base per i testi): conseil en informatique et en transformation numérique; conseil et gestion de projets dans les domaines de la gestion de contenu d'entreprise (ECM), des produits fintech et de l'intelligence artificielle; développement, intégration et maintenance de solutions logicielles; prestations de product management et de gestion de projets IT.
* Non ancora iscritta alla TVA: non indicare numero TVA.

## Contatti

* Email: info@lachi.solutions (contatto generale), ivo@lachi.solutions (personale, opzionale nella sezione "Chi sono")
* Telefono: +41 78 452 07 30
* Sito: https://www.lachi.solutions
* LinkedIn aziendale (solo icona footer): linkedin.com/company/lachi-solutions-geneve

## Posizionamento e tono

* Target: PMI e organizzazioni in Svizzera e in Europa. Consulente singolo che lavora da Ginevra con una rete di esperti attivata per mandato.
* Tono: sobrio, professionale, concreto. Frasi corte. Niente superlativi, niente "leader", niente buzzword accumulate. Niente promesse di risultati numerici.
* Il valore da comunicare: collegare tecnologia e obiettivi di business, seguire il progetto dalla definizione all'esecuzione, oltre quindici anni di esperienza tra fintech/pagamenti, ECM e sviluppo software.

## I quattro servizi

1. Trasformazione digitale e gestione progetti IT — roadmap, PMO, pilotaggio di progetti dal cahier des charges al rilascio, governance e conformità (LPD/RGPD).
2. Prodotti fintech e pagamenti — product management di wallet digitali, carte prepagate e private-label, pagamenti alternativi, programmi fedeltà, flussi KYC/KYB, integrazione con emittenti e processor.
3. Gestione documentale (ECM) — scelta e deployment di soluzioni ECM, archiviazione, flussi documentali, integrazione con sistemi esistenti (esperienza Alfresco, Kofax, Java/Spring, BPM).
4. Intelligenza artificiale e dati — casi d'uso, agenti e assistenti IA integrati nei processi aziendali, automazione, analisi dati, rilevamento frodi.

## Il fondatore (sezione "Chi sono")

Ivo Lachi, ingegnere informatico italiano stabilito a Ginevra. Oltre quindici anni tra sviluppo software, architettura di piattaforme di pagamento e product management in ambito fintech, co-fondatore e CTO di un'azienda di marketing digitale. Lavora in francese, inglese, italiano e sloveno. Segue personalmente ogni mandato.

## Lingue

* Ordine nel selettore: FR · EN · IT · SL. Default: FR.
* Scrivere prima il testo francese, poi tradurre con cura mantenendo lo stesso registro. Per lo sloveno usare un registro formale (vikanje). Non usare traduzione letterale dei nomi di servizio: adattare alle convenzioni di ogni lingua.
* Titoli pagina: FR "Lachi Solutions — Conseil IT, fintech et transformation numérique à Genève"; EN "Lachi Solutions — IT, fintech and digital transformation consulting, Geneva"; IT "Lachi Solutions — Consulenza IT, fintech e trasformazione digitale a Ginevra"; SL "Lachi Solutions — IT svetovanje, fintech in digitalna preobrazba, Ženeva".

## Mentions légales (contenuto minimo)

Lachi Solutions, entreprise individuelle, Rue Rothschild 54, 1202 Genève, Suisse. IDE CHE-432.855.350. Titulaire: Ivo Lachi. Contact: info@lachi.solutions, +41 78 452 07 30. Privacy: il sito non usa cookie né strumenti di tracciamento; i dati inviati via email sono trattati solo per rispondere alla richiesta, ai sensi della LPD svizzera.
