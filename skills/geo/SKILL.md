---
name: geo
description: >-
  Overzicht van alle Geonovum geo-standaarden. Gebruik deze skill wanneer de
  gebruiker vraagt over 'geonovum', 'geo standaarden', 'geostandaarden',
  'PDOK', 'ruimtelijke data', 'spatial data', 'GIS overheid',
  'welke geo-standaarden zijn er', 'geo-informatie Nederland',
  'geodata overheid'.
model: sonnet
allowed-tools:
  - Bash(gh api *)
  - Bash(curl -s *)
  - WebFetch(*)
metadata:
  created-with-ai: "true"
  created-with-model: claude-opus-4-20250514
  created-date: "2025-02-22"
  status: concept
---

> **Let op:** Deze skill is geen officieel product van Geonovum. De beschrijvingen zijn informatieve samenvattingen — niet de officiële standaarden zelf. De definities op [forumstandaardisatie.nl](https://www.forumstandaardisatie.nl/open-standaarden) en [Geonovum](https://www.geonovum.nl) zijn altijd leidend. Overheidsorganisaties die generatieve AI inzetten dienen te voldoen aan het [Rijksbrede beleidskader voor generatieve AI](https://www.government.nl/documents/policy-notes/2025/01/31/government-wide-position-on-the-use-of-generative-ai). Zie [DISCLAIMER.md](../../DISCLAIMER.md).

# Geonovum Geo-standaarden - Overzicht

**Agent-instructie:** Gebruik deze skill om de gebruiker naar het juiste geo-domein te routeren. Bij een domein-specifieke vraag, verwijs naar de juiste `/geo-*` skill. Bij brede vragen over het geo-standaarden ecosysteem, gebruik de informatie hieronder en de gh commando's.

[Geonovum](https://www.geonovum.nl/) is de Nederlandse organisatie die geo-standaarden ontwikkelt en beheert. Samen met [PDOK](https://www.pdok.nl/) (Publieke Dienstverlening Op de Kaart), het [Kadaster](https://www.kadaster.nl/), en [Rijkswaterstaat](https://www.rijkswaterstaat.nl/) vormt Geonovum de ruggengraat van de Nederlandse geo-informatie-infrastructuur. De standaarden zijn gepubliceerd op [docs.geostandaarden.nl](https://docs.geostandaarden.nl/).

## Forum Standaardisatie Status

De geo-standaarden staan op de ['pas-toe-of-leg-uit'-lijst](https://www.forumstandaardisatie.nl/open-standaarden/geo-standaarden) van het Forum Standaardisatie. Let op: sinds september 2024 is de samenstelling gewijzigd.

**Verplicht (pas-toe-of-leg-uit) — onderdeel van het Geo-Standaarden-pakket:**

| Standaard | Type | Status |
|-----------|------|--------|
| [GML](https://www.forumstandaardisatie.nl/open-standaarden/geo-standaarden) | Data-encoding | Verplicht |
| [OGC API Features](https://www.forumstandaardisatie.nl/open-standaarden/geo-standaarden) | REST API service | Verplicht |
| [OGC API Tiles](https://www.forumstandaardisatie.nl/open-standaarden/geo-standaarden) | Tileservice | Verplicht |
| [NEN 3610](https://www.forumstandaardisatie.nl/open-standaarden/geo-standaarden) | Informatiemodel | Verplicht |
| [ISO 19115/19119](https://www.forumstandaardisatie.nl/open-standaarden/geo-standaarden) | Metadata | Verplicht |

**Aanbevolen (sinds september 2024 verplaatst van verplicht naar aanbevolen):**

| Standaard | Type | Status |
|-----------|------|--------|
| WMS | Viewservice | Aanbevolen |
| WFS | Downloadservice | Aanbevolen |

## Domeinen

| Skill | Domein | Beschrijving |
|-------|--------|-------------|
| `/geo-api` | OGC Services | WMS, WFS, OGC API Tiles, WCS, OGC API Features, ogc-checker validatie |
| `/geo-meta` | Metadata | NL profiel ISO 19115, CSW, NGR, DCAT |
| `/geo-model` | Informatiemodellen | NEN 3610, MIM, sectormodellen (IMGeo, IMBAG), linked data |
| `/geo-inspire` | INSPIRE | Europese richtlijn implementatie, validatie, ETF |
| `/geo-3d` | 3D Standaarden | CityGML, 3D Tiles, GeoBIM, digital twins |

## Sleutelorganisaties

| Organisatie | Rol | Website |
|-------------|-----|---------|
| [Geonovum](https://www.geonovum.nl/) | Standaardontwikkeling en -beheer | geonovum.nl |
| [PDOK](https://www.pdok.nl/) | Nationale geo-dataportaal, hosting van services | pdok.nl |
| [Kadaster](https://www.kadaster.nl/) | Basisregistraties (BAG, BRK), PDOK-beheer, Landelijke Voorziening BGT | kadaster.nl |
| [Rijkswaterstaat](https://www.rijkswaterstaat.nl/) | Infrastructuurdata, waterdata | rijkswaterstaat.nl |
| [CBS](https://www.cbs.nl/) | Statistische geodata, wijk/buurtkaart | cbs.nl |

## Belangrijke Repositories

| Repository | Beschrijving | Licentie |
|-----------|-------------|--------|
| [Geonovum/ogc-checker](https://github.com/Geonovum/ogc-checker) | Validatietool voor OGC services | [EUPL-1.2](https://eupl.eu/1.2/en) |
| [Geonovum/NEN3610-Linkeddata](https://github.com/Geonovum/NEN3610-Linkeddata) | NEN 3610 linked data profiel | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode.en) |
| [Geonovum/Metadata-ISO19115](https://github.com/Geonovum/Metadata-ISO19115) | Nederlands profiel ISO 19115 metadata | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode.en) |
| [Geonovum/inspire-handreiking](https://github.com/Geonovum/inspire-handreiking) | INSPIRE implementatie handreiking | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode.en) |
| [Geonovum/IMGeo](https://github.com/Geonovum/IMGeo) | Informatiemodel Geografie (BGT/IMGeo) | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode.en) |
| [Geonovum/MIM-Werkomgeving](https://github.com/Geonovum/MIM-Werkomgeving) | Metamodel Informatie Modellering | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode.en) |

## Belangrijke Links

- **Gepubliceerde standaarden:** [docs.geostandaarden.nl](https://docs.geostandaarden.nl/)
- **Forum Standaardisatie:** [forumstandaardisatie.nl/open-standaarden/geo-standaarden](https://www.forumstandaardisatie.nl/open-standaarden/geo-standaarden)
- **PDOK services:** [pdok.nl](https://www.pdok.nl/)
- **Geonovum website:** [geonovum.nl/geo-standaarden](https://www.geonovum.nl/geo-standaarden)
- **GitHub organisatie:** [github.com/Geonovum](https://github.com/Geonovum)

## Organisatie-brede Commando's

```bash
# Alle repos van Geonovum
gh api orgs/Geonovum/repos --paginate --jq '.[].name' | sort

# Zoek in alle repos
gh search code "zoekterm" --owner Geonovum

# Recent gewijzigde repos
gh api orgs/Geonovum/repos --paginate \
  --jq 'sort_by(.pushed_at) | reverse | .[:10] | .[] | "\(.pushed_at) \(.name)"'

# Open issues over alle repos
gh search issues --owner Geonovum --state open --sort created

# Repos met een specifiek onderwerp
gh api orgs/Geonovum/repos --paginate \
  --jq '.[] | select(.topics | index("nen3610") or index("inspire") or index("ogc")) | .name'
```

## Veelvoorkomende Vragen

| Vraag | Routing |
|-------|---------|
| "Welke geo-API standaard moet ik gebruiken?" | `/geo-api` |
| "Hoe publiceer ik metadata in het NGR?" | `/geo-meta` |
| "Wat is NEN 3610?" | `/geo-model` |
| "Hoe voldoe ik aan INSPIRE?" | `/geo-inspire` |
| "Hoe werk ik met CityGML of 3D data?" | `/geo-3d` |
| "Hoe gebruik ik de ADR geo-module?" | `/ls-api` (uit skills-standaarden) |
