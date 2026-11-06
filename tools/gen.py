#!/usr/bin/env python3
"""Genera le pagine HTML del sito dai testi qui sotto. Uso: python3 tools/gen.py (dalla radice)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://www.lachi.solutions"
LANGS = ["fr", "en", "it", "sl"]
EMAIL, PHONE, PHONE_HREF = "info@lachi.solutions", "+41 78 452 07 30", "+41784520730"
ADDRESS = "Rue Rothschild 54<br>1202 Genève, Suisse"
LINKEDIN = "https://www.linkedin.com/company/lachi-solutions-geneve"
LI_ICON = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.03-3.04-1.85-3.04'
           '-1.85 0-2.14 1.45-2.14 2.94v5.67H9.36V9h3.41v1.56h.05c.47-.9 1.63-1.85 3.36-1.85 3.6 0 4.27 2.37 4.27 5.45'
           'v6.29zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77'
           'C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"/></svg>')

T = {
 "fr": dict(
  title="Lachi Solutions — Conseil IT, fintech et transformation numérique à Genève",
  desc="Conseil indépendant en informatique, produits fintech, gestion de contenu d'entreprise et intelligence artificielle. Lachi Solutions, Genève.",
  h1="Conseil IT, fintech et transformation numérique",
  lead="Lachi Solutions accompagne les PME et les organisations, de la définition du projet à sa mise en œuvre, depuis Genève.",
  cta="Contact", nav=("Services", "Approche", "Contact"),
  services=[
   ("Transformation numérique et gestion de projets IT",
    "Feuille de route, PMO et pilotage de projets, du cahier des charges à la mise en production. Gouvernance et conformité (LPD, RGPD)."),
   ("Produits fintech et paiements",
    "Product management de portefeuilles numériques, cartes prépayées et en marque blanche, paiements alternatifs et programmes de fidélité. Parcours KYC/KYB, intégration avec émetteurs et processeurs."),
   ("Gestion de contenu d'entreprise (ECM)",
    "Choix et déploiement de solutions ECM, archivage, flux documentaires et intégration avec les systèmes existants. Expérience Alfresco, Kofax, Java/Spring, BPM."),
   ("Intelligence artificielle et données",
    "Identification des cas d'usage, agents et assistants IA intégrés aux processus métier, automatisation, analyse de données et détection de fraude."),
  ],
  about=[
   "Lachi Solutions est le cabinet de conseil indépendant d'Ivo Lachi, ingénieur informaticien italien établi à Genève. Plus de quinze ans entre développement logiciel, architecture de plateformes de paiement et product management dans la fintech, ainsi que la co-fondation, comme CTO, d'une entreprise de marketing numérique.",
   "Il suit personnellement chaque mandat et fait appel, selon les besoins, à un réseau d'experts. Le fil conducteur: relier la technologie aux objectifs de l'entreprise, de la définition du projet à son exécution.",
  ],
  langs="Langues de travail: français, anglais, italien, slovène.",
  contact_lead="Un projet, une question? Écrivez-nous ou appelez.",
  labels=("E-mail", "Téléphone", "Adresse"),
  legal_form="Entreprise individuelle", city="Genève", ide="IDE",
  legal_link=("Mentions légales", "mentions-legales.html"), privacy_link=("Confidentialité", "confidentialite.html"),
  legal_dir="fr",
 ),
 "en": dict(
  title="Lachi Solutions — IT, fintech and digital transformation consulting, Geneva",
  desc="Independent consulting in IT, fintech products, enterprise content management and artificial intelligence. Lachi Solutions, Geneva.",
  h1="IT, fintech and digital transformation consulting",
  lead="Lachi Solutions supports SMEs and organisations from project definition to delivery, from Geneva.",
  cta="Contact", nav=("Services", "Approach", "Contact"),
  services=[
   ("Digital transformation and IT project management",
    "Roadmaps, PMO and project steering, from requirements to go-live. Governance and compliance (Swiss FADP, GDPR)."),
   ("Fintech products and payments",
    "Product management of digital wallets, prepaid and private-label cards, alternative payments and loyalty programmes. KYC/KYB flows, integration with issuers and processors."),
   ("Enterprise content management (ECM)",
    "Selection and deployment of ECM solutions, archiving, document workflows and integration with existing systems. Experience with Alfresco, Kofax, Java/Spring, BPM."),
   ("Artificial intelligence and data",
    "Use-case identification, AI agents and assistants embedded in business processes, automation, data analysis and fraud detection."),
  ],
  about=[
   "Lachi Solutions is the independent consultancy of Ivo Lachi, an Italian computer engineer based in Geneva. Over fifteen years across software development, payment platform architecture and fintech product management, plus the co-founding, as CTO, of a digital marketing company.",
   "He follows every engagement personally and brings in a network of experts when needed. The common thread: connecting technology with business goals, from project definition to execution.",
  ],
  langs="Working languages: French, English, Italian, Slovenian.",
  contact_lead="A project or a question? Write to us or call.",
  labels=("E-mail", "Phone", "Address"),
  legal_form="Sole proprietorship", city="Geneva", ide="UID",
  legal_link=("Legal notice", "legal-notice.html"), privacy_link=("Privacy", "privacy.html"),
  legal_dir="en",
 ),
 "it": dict(
  title="Lachi Solutions — Consulenza IT, fintech e trasformazione digitale a Ginevra",
  desc="Consulenza indipendente in informatica, prodotti fintech, gestione documentale e intelligenza artificiale. Lachi Solutions, Ginevra.",
  h1="Consulenza IT, fintech e trasformazione digitale",
  lead="Lachi Solutions accompagna PMI e organizzazioni dalla definizione del progetto alla sua realizzazione, da Ginevra.",
  cta="Contatti", nav=("Servizi", "Approccio", "Contatti"),
  services=[
   ("Trasformazione digitale e gestione progetti IT",
    "Roadmap, PMO e pilotaggio dei progetti, dal capitolato alla messa in produzione. Governance e conformità (LPD, GDPR)."),
   ("Prodotti fintech e pagamenti",
    "Product management di wallet digitali, carte prepagate e private label, pagamenti alternativi e programmi fedeltà. Flussi KYC/KYB, integrazione con emittenti e processor."),
   ("Gestione documentale (ECM)",
    "Scelta e deployment di soluzioni ECM, archiviazione, flussi documentali e integrazione con i sistemi esistenti. Esperienza Alfresco, Kofax, Java/Spring, BPM."),
   ("Intelligenza artificiale e dati",
    "Individuazione dei casi d'uso, agenti e assistenti IA integrati nei processi aziendali, automazione, analisi dei dati e rilevamento delle frodi."),
  ],
  about=[
   "Lachi Solutions è lo studio di consulenza indipendente di Ivo Lachi, ingegnere informatico italiano stabilito a Ginevra. Oltre quindici anni tra sviluppo software, architettura di piattaforme di pagamento e product management in ambito fintech, oltre alla co-fondazione, come CTO, di un'azienda di marketing digitale.",
   "Segue personalmente ogni mandato e attiva, quando serve, una rete di esperti. Il filo conduttore: collegare la tecnologia agli obiettivi dell'azienda, dalla definizione del progetto alla sua esecuzione.",
  ],
  langs="Lingue di lavoro: francese, inglese, italiano, sloveno.",
  contact_lead="Un progetto, una domanda? Scriveteci o chiamateci.",
  labels=("E-mail", "Telefono", "Indirizzo"),
  legal_form="Ditta individuale", city="Ginevra", ide="IDE",
  legal_link=("Note legali", "mentions-legales.html"), privacy_link=("Privacy", "confidentialite.html"),
  legal_dir="fr",
 ),
 "sl": dict(
  title="Lachi Solutions — IT svetovanje, fintech in digitalna preobrazba, Ženeva",
  desc="Neodvisno svetovanje na področju informatike, fintech produktov, upravljanja dokumentov in umetne inteligence. Lachi Solutions, Ženeva.",
  h1="IT svetovanje, fintech in digitalna preobrazba",
  lead="Lachi Solutions spremlja mala in srednja podjetja ter organizacije od opredelitve projekta do njegove izvedbe, iz Ženeve.",
  cta="Kontakt", nav=("Storitve", "Pristop", "Kontakt"),
  services=[
   ("Digitalna preobrazba in vodenje IT projektov",
    "Načrt razvoja, PMO in vodenje projektov od specifikacije zahtev do uvedbe v produkcijo. Upravljanje in skladnost (LPD, GDPR)."),
   ("Fintech produkti in plačila",
    "Produktno vodenje digitalnih denarnic, predplačniških kart in kart pod lastno blagovno znamko, alternativnih plačil in programov zvestobe. Postopki KYC/KYB, integracija z izdajatelji in procesorji."),
   ("Upravljanje dokumentov (ECM)",
    "Izbira in uvedba rešitev ECM, arhiviranje, dokumentni tokovi in integracija z obstoječimi sistemi. Izkušnje z Alfresco, Kofax, Java/Spring, BPM."),
   ("Umetna inteligenca in podatki",
    "Opredelitev primerov uporabe, agenti in asistenti z umetno inteligenco, vključeni v poslovne procese, avtomatizacija, analiza podatkov in odkrivanje goljufij."),
  ],
  about=[
   "Lachi Solutions je neodvisno svetovalno podjetje Iva Lachija, italijanskega računalniškega inženirja s sedežem v Ženevi. Več kot petnajst let izkušenj z razvojem programske opreme, arhitekturo plačilnih platform in produktnim vodenjem na področju fintecha; soustanovitelj in CTO podjetja za digitalni marketing.",
   "Vsak mandat vodi osebno, po potrebi pa vključi mrežo strokovnjakov. Rdeča nit: povezati tehnologijo s poslovnimi cilji, od opredelitve projekta do njegove izvedbe.",
  ],
  langs="Delovni jeziki: francoščina, angleščina, italijanščina, slovenščina.",
  contact_lead="Projekt ali vprašanje? Pišite nam ali pokličite.",
  labels=("E-pošta", "Telefon", "Naslov"),
  legal_form="Samostojni podjetnik", city="Ženeva", ide="IDE",
  legal_link=("Pravno obvestilo", "legal-notice.html"), privacy_link=("Zasebnost", "privacy.html"),
  legal_dir="en",
 ),
}

LEGAL = {
 "fr": dict(
  legal_title="Mentions légales — Lachi Solutions",
  legal=[("Mentions légales", None),
         ("Éditeur du site", "Lachi Solutions, entreprise individuelle inscrite au Registre du commerce de Genève.<br>Rue Rothschild 54, 1202 Genève, Suisse.<br>IDE CHE-432.855.350.<br>Titulaire: Ivo Lachi."),
         ("Contact", f'<a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="tel:{PHONE_HREF}">{PHONE}</a>'),
         ("Responsabilité", "Le contenu de ce site est fourni à titre d'information. Lachi Solutions s'efforce de le maintenir exact et à jour, sans garantie d'exhaustivité.")],
  privacy_title="Confidentialité — Lachi Solutions",
  privacy=[("Confidentialité", None),
           ("Aucun cookie, aucun suivi", "Ce site n'utilise ni cookies ni outils de suivi ou d'analyse d'audience. Aucune donnée personnelle n'est collectée lors de la simple consultation. L'hébergeur peut conserver des journaux techniques (adresse IP, date, page consultée) à des fins de sécurité, pour une durée limitée."),
           ("Données transmises par e-mail ou téléphone", "Les données que vous nous transmettez sont traitées uniquement pour répondre à votre demande et, le cas échéant, préparer un mandat, conformément à la loi fédérale sur la protection des données (LPD). Elles ne sont ni vendues ni transmises à des tiers à des fins de marketing."),
           ("Vos droits", f'Vous pouvez demander l\'accès à vos données, leur rectification ou leur suppression en écrivant à <a href="mailto:{EMAIL}">{EMAIL}</a>.'),
           ("Responsable du traitement", "Ivo Lachi, Lachi Solutions, Rue Rothschild 54, 1202 Genève, Suisse.")],
  back="Retour à l'accueil",
 ),
 "en": dict(
  legal_title="Legal notice — Lachi Solutions",
  legal=[("Legal notice", None),
         ("Publisher", "Lachi Solutions, sole proprietorship (entreprise individuelle) registered with the Geneva Commercial Register.<br>Rue Rothschild 54, 1202 Geneva, Switzerland.<br>UID CHE-432.855.350.<br>Owner: Ivo Lachi."),
         ("Contact", f'<a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="tel:{PHONE_HREF}">{PHONE}</a>'),
         ("Liability", "The content of this website is provided for information purposes. Lachi Solutions endeavours to keep it accurate and up to date, without guarantee of completeness.")],
  privacy_title="Privacy — Lachi Solutions",
  privacy=[("Privacy", None),
           ("No cookies, no tracking", "This website uses neither cookies nor tracking or analytics tools. No personal data is collected when you simply browse it. The hosting provider may keep technical logs (IP address, date, page requested) for security purposes, for a limited time."),
           ("Data sent by e-mail or phone", "Data you send us is processed only to answer your request and, where applicable, to prepare an engagement, in accordance with the Swiss Federal Act on Data Protection (FADP). It is neither sold nor passed on to third parties for marketing purposes."),
           ("Your rights", f'You may request access to your data, its correction or its deletion by writing to <a href="mailto:{EMAIL}">{EMAIL}</a>.'),
           ("Data controller", "Ivo Lachi, Lachi Solutions, Rue Rothschild 54, 1202 Geneva, Switzerland.")],
  back="Back to home",
 ),
}

def head(lang, title, desc, path, alternates=True):
    alt = ""
    if alternates:
        alt = "\n".join(f'  <link rel="alternate" hreflang="{l}" href="{SITE}/{l}/">' for l in LANGS)
        alt += f'\n  <link rel="alternate" hreflang="x-default" href="{SITE}/fr/">'
    locale = {"fr": "fr_CH", "en": "en_GB", "it": "it_CH", "sl": "sl_SI"}[lang]
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{SITE}/{path}">
{alt}
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{SITE}/{path}">
  <meta property="og:locale" content="{locale}">
  <meta name="theme-color" content="#f3f2f2">
  <link rel="icon" href="../assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="../assets/style.css">
</head>"""

def header(lang):
    items = "".join(
        f'<li><a href="../{l}/" hreflang="{l}" lang="{l}"{" aria-current=\"page\"" if l == lang else ""}>{l.upper()}</a></li>'
        for l in LANGS)
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="logo" href="../{lang}/" aria-label="Lachi Solutions"><span class="logo-word">lachi<span class="logo-dot"></span></span><span class="logo-bar" style="display:block"></span><span class="logo-sub">solutions</span></a>
    <nav aria-label="Language"><ul class="lang">{items}</ul></nav>
  </div>
</header>"""

def footer(lang):
    t = T[lang]
    return f"""<footer class="site-footer">
  <div class="wrap">
    <p>Lachi Solutions · {t["legal_form"]} · {t["city"]} · {t["ide"]} CHE-432.855.350</p>
    <nav aria-label="Legal">
      <a href="../{t["legal_dir"]}/{t["legal_link"][1]}">{t["legal_link"][0]}</a>
      <a href="../{t["legal_dir"]}/{t["privacy_link"][1]}">{t["privacy_link"][0]}</a>
      <a href="{LINKEDIN}" rel="noopener" target="_blank" aria-label="LinkedIn">{LI_ICON}</a>
    </nav>
  </div>
</footer>
<script src="../assets/lang.js"></script>
</body>
</html>
"""

def home(lang):
    t = T[lang]
    services = "\n".join(f"      <article>\n        <h3>{h}</h3>\n        <p>{p}</p>\n      </article>" for h, p in t["services"])
    about = "\n".join(f"      <p>{p}</p>" for p in t["about"])
    s, a, c = t["nav"]
    l1, l2, l3 = t["labels"]
    return f"""{head(lang, t["title"], t["desc"], f"{lang}/")}
<body>
{header(lang)}
<main>
  <section class="hero">
    <div class="wrap">
      <h1>{t["h1"]}</h1>
      <p class="lead">{t["lead"]}</p>
      <a class="btn" href="#contact">{t["cta"]}</a>
    </div>
  </section>

  <section id="services">
    <div class="wrap">
      <span class="eyebrow">01</span>
      <h2>{s}</h2>
      <div class="services">
{services}
      </div>
    </div>
  </section>

  <section id="about">
    <div class="wrap">
      <span class="eyebrow">02</span>
      <h2>{a}</h2>
      <div class="prose">
{about}
      <p class="langs">{t["langs"]}</p>
      </div>
    </div>
  </section>

  <section id="contact">
    <div class="wrap">
      <span class="eyebrow">03</span>
      <h2>{c}</h2>
      <p class="prose">{t["contact_lead"]}</p>
      <dl class="contact-list">
        <div><dt>{l1}</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
        <div><dt>{l2}</dt><dd><a href="tel:{PHONE_HREF}">{PHONE}</a></dd></div>
        <div><dt>{l3}</dt><dd><address>{ADDRESS}</address></dd></div>
      </dl>
    </div>
  </section>
</main>
{footer(lang)}"""

def legal_page(lang, title, sections, back, path):
    body = []
    for h, txt in sections:
        if txt is None:
            body.append(f"    <h1>{h}</h1>")
        else:
            body.append(f"    <h2>{h}</h2>\n    <p>{txt}</p>")
    return f"""{head(lang, title, title, path, alternates=False)}
<body>
{header(lang)}
<main class="page">
  <div class="wrap">
{chr(10).join(body)}
    <a class="back" href="../{lang}/">{back}</a>
  </div>
</main>
{footer(lang)}"""

ROOT_INDEX = f"""<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>Lachi Solutions</title>
  <meta name="robots" content="noindex">
  <meta http-equiv="refresh" content="0; url=fr/">
  <link rel="canonical" href="{SITE}/fr/">
  <script>
    (function () {{
      var langs = ["fr", "en", "it", "sl"], pick = "fr";
      try {{ pick = localStorage.getItem("ls-lang") || (navigator.language || "fr").slice(0, 2).toLowerCase(); }} catch (e) {{}}
      if (langs.indexOf(pick) < 0) pick = "fr";
      location.replace(pick + "/" + (location.protocol === "file:" ? "index.html" : ""));
    }})();
  </script>
</head>
<body>
  <p><a href="fr/">Français</a> · <a href="en/">English</a> · <a href="it/">Italiano</a> · <a href="sl/">Slovenščina</a></p>
</body>
</html>
"""

def main():
    for lang in LANGS:
        (ROOT / lang / "index.html").write_text(home(lang), encoding="utf-8")
    L = LEGAL["fr"]
    (ROOT / "fr/mentions-legales.html").write_text(legal_page("fr", L["legal_title"], L["legal"], L["back"], "fr/mentions-legales.html"), encoding="utf-8")
    (ROOT / "fr/confidentialite.html").write_text(legal_page("fr", L["privacy_title"], L["privacy"], L["back"], "fr/confidentialite.html"), encoding="utf-8")
    L = LEGAL["en"]
    (ROOT / "en/legal-notice.html").write_text(legal_page("en", L["legal_title"], L["legal"], L["back"], "en/legal-notice.html"), encoding="utf-8")
    (ROOT / "en/privacy.html").write_text(legal_page("en", L["privacy_title"], L["privacy"], L["back"], "en/privacy.html"), encoding="utf-8")
    (ROOT / "index.html").write_text(ROOT_INDEX, encoding="utf-8")
    print("ok")

if __name__ == "__main__":
    main()
