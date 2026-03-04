# Geo - Claude Code Plugin

[![EUPL-1.2](https://img.shields.io/badge/licentie-EUPL--1.2-blue.svg)](LICENSE)
[![skills](https://img.shields.io/badge/skills-6-green.svg)](#skills)

[Claude Code](https://docs.anthropic.com/en/docs/claude-code) plugin voor Nederlandse geo-standaarden voor ruimtelijke data. Bevat skills voor standaarden beheerd door [Geonovum](https://www.geonovum.nl): OGC API services, metadata, informatiemodellen, INSPIRE en 3D standaarden.

## Installeren

```bash
# Via de overheid-plugins marketplace (aanbevolen)
claude plugin marketplace add developer-overheid-nl/skills-marketplace
claude plugin install geonovum@overheid-plugins

# Per sessie
git clone https://github.com/developer-overheid-nl/skills-geo.git
claude --plugin-dir ./skills-geo
```

## Skills

| Skill | Beschrijving |
|-------|-------------|
| `/geo` | Overzicht geo-standaarden ecosysteem, routing naar sub-skills |
| `/geo-api` | OGC API services: WMS, WFS, WMTS, OGC API Features, ogc-checker validatie |
| `/geo-meta` | Metadata: NL profiel ISO 19115, NGR, DCAT, validatie |
| `/geo-model` | Informatiemodellen: NEN 3610, MIM, linked data |
| `/geo-inspire` | INSPIRE: implementatie, validatie, handreiking |
| `/geo-3d` | 3D standaarden: CityGML, 3D Tiles, GeoBIM |

## Voorbeeldvragen

- "Welke geo-API standaard moet ik gebruiken?" -> `/geo-api`
- "Hoe publiceer ik metadata in het NGR?" -> `/geo-meta`
- "Wat is NEN 3610?" -> `/geo-model`
- "Hoe voldoe ik aan INSPIRE?" -> `/geo-inspire`
- "Hoe werk ik met CityGML?" -> `/geo-3d`

## Bronnen

De skills zijn gebaseerd op:
- [Geonovum](https://github.com/Geonovum) GitHub organisatie (100+ repos)
- [docs.geostandaarden.nl](https://docs.geostandaarden.nl) — gepubliceerde standaarden
- [Forum Standaardisatie](https://www.forumstandaardisatie.nl) — geo-standaarden op de lijst
- [PDOK](https://www.pdok.nl) — praktische implementatie en services

## Onderdeel van

Deze plugin is onderdeel van de [skills-marketplace](https://github.com/developer-overheid-nl/skills-marketplace) marketplace.

## Disclaimer

**Deze plugin is geen officieel product van [Geonovum](https://www.geonovum.nl).** Het is een experimenteel project van [developer.overheid.nl](https://developer.overheid.nl), gebaseerd op publiek beschikbare standaarden en documentatie. De skills zijn informatieve samenvattingen — **niet** de officiële standaarden zelf. De definities op [Forum Standaardisatie](https://www.forumstandaardisatie.nl/open-standaarden) en [Geonovum](https://www.geonovum.nl) zijn altijd leidend. Overheidsorganisaties die generatieve AI inzetten dienen te voldoen aan het [Rijksbrede beleidskader voor generatieve AI](https://www.government.nl/documents/policy-notes/2025/01/31/government-wide-position-on-the-use-of-generative-ai). Zie [DISCLAIMER.md](DISCLAIMER.md) voor de volledige disclaimer.

## Licentie

[EUPL-1.2](LICENSE) - European Union Public Licence
