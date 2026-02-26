# Geonovum Plugin

[![EUPL-1.2](https://img.shields.io/badge/licentie-EUPL--1.2-blue.svg)](LICENSE)
[![skills](https://img.shields.io/badge/skills-6-green.svg)](#skills)

[Claude Code](https://docs.anthropic.com/en/docs/claude-code) plugin voor het werken met [Geonovum](https://www.geonovum.nl) geo-standaarden voor ruimtelijke data in Nederland. Bevat skills voor OGC API services, metadata, informatiemodellen, INSPIRE en 3D standaarden.

## Installeren

```bash
# Via de overheid-plugins marketplace (aanbevolen)
claude plugin marketplace add developer-overheid-nl/overheid-claude-plugins
claude plugin install geonovum@overheid-plugins

# Per sessie
git clone https://github.com/developer-overheid-nl/geo-plugin.git
claude --plugin-dir ./geo-plugin
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

Deze plugin is onderdeel van de [overheid-claude-plugins](https://github.com/developer-overheid-nl/overheid-claude-plugins) marketplace.

## Disclaimer

Dit is een experimenteel project om te leren hoe generatieve AI gestuurd kan worden om te werken volgens de kaders, richtlijnen en standaarden van de overheid. De skills in deze plugin zijn informatieve samenvattingen — **niet** de officiële standaarden zelf. De definities op [Forum Standaardisatie](https://www.forumstandaardisatie.nl/open-standaarden) en [Geonovum](https://www.geonovum.nl) zijn altijd leidend. Overheidsorganisaties die generatieve AI inzetten dienen te voldoen aan het [Rijksbrede beleidskader voor generatieve AI](https://www.government.nl/documents/policy-notes/2025/01/31/government-wide-position-on-the-use-of-generative-ai). Zie [DISCLAIMER.md](DISCLAIMER.md) voor de volledige disclaimer.

## Licentie

[EUPL-1.2](LICENSE) - European Union Public Licence
