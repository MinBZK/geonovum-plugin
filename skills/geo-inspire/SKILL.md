---
name: geo-inspire
description: >-
  INSPIRE Europese richtlijn voor geodata. Gebruik deze skill wanneer de
  gebruiker vraagt over 'INSPIRE', 'INSPIRE validator', 'ETF',
  'Europese richtlijn geo', 'INSPIRE implementatie',
  'INSPIRE datathema', 'INSPIRE download service',
  'INSPIRE view service', 'INSPIRE discovery', 'INSPIRE handreiking',
  'Annex I', 'Annex II', 'Annex III'.
model: sonnet
allowed-tools:
  - Bash(gh api *)
  - Bash(curl -s *)
  - WebFetch(*)
---

> **Let op:** De beschrijvingen in deze skill zijn informatieve samenvattingen — niet de officiële standaarden zelf. De definities op [forumstandaardisatie.nl](https://www.forumstandaardisatie.nl/open-standaarden) en [Geonovum](https://www.geonovum.nl) zijn altijd leidend. Overheidsorganisaties die generatieve AI inzetten dienen te voldoen aan het [Rijksbrede beleidskader voor generatieve AI](https://www.government.nl/documents/policy-notes/2025/01/31/government-wide-position-on-the-use-of-generative-ai). Zie [DISCLAIMER.md](../../DISCLAIMER.md).

# INSPIRE Implementatie

**Agent-instructie:** Deze skill helpt bij het implementeren van INSPIRE-conforme services en data voor Nederlandse organisaties. Gebruik de validatievoorbeelden om services te toetsen en de handreiking van Geonovum voor implementatieadvies. INSPIRE is een Europese verplichting voor overheden die ruimtelijke data beheren.

De [INSPIRE-richtlijn](https://inspire.ec.europa.eu/) (2007/2/EG) verplicht Europese lidstaten om ruimtelijke data over 34 thema's interoperabel beschikbaar te stellen via view-, download- en discovery-services. Geonovum ondersteunt de Nederlandse implementatie via de [INSPIRE handreiking](https://docs.geostandaarden.nl/eu/INSPIRE-handreiking/) en technische richtlijnen.

## Standaarden Overzicht

| Component | Standaard | Beschrijving |
|-----------|----------|-------------|
| View services | WMS 1.3.0 / WMTS 1.0.0 | Kaartafbeeldingen bekijken |
| Download services | WFS 2.0 / Atom / OGC API Features | Data downloaden |
| Discovery services | CSW 2.0.2 | Metadata zoeken (via NGR) |
| Data-encoding | GML 3.2.1 | Geo-data uitwisselen |
| Metadata | ISO 19115/19119 | Beschrijving van data en services |
| Datamodellen | INSPIRE data specificaties | 34 geharmoniseerde themamodellen |

## Repositories

| Repository | Beschrijving |
|-----------|-------------|
| [Geonovum/inspire-handreiking](https://github.com/Geonovum/inspire-handreiking) | Nederlandse INSPIRE implementatie handreiking |

## INSPIRE Data Thema's

### Annex I — Referentiedata (sinds 2010)

| Nr | Thema | NL-dataset (voorbeeld) |
|----|-------|----------------------|
| 1 | Coordinaatreferentiesystemen | RDNAPTRANS (Kadaster) |
| 2 | Geografisch rastersysteem | Inspireconforme grid |
| 3 | Geografische namen | Kadaster toponiemen |
| 4 | Administratieve eenheden | Bestuurlijke grenzen (Kadaster) |
| 5 | Adressen | BAG (Kadaster) |
| 6 | Kadastrale percelen | BRK (Kadaster) |
| 7 | Transportnetwerken | NWB (RWS) |
| 8 | Hydrografie | Waterdata (RWS) |
| 9 | Beschermde gebieden | Natura2000 (LNV) |

### Annex II — Fysisch milieu (sinds 2013)

| Nr | Thema | NL-dataset (voorbeeld) |
|----|-------|----------------------|
| 1 | Hoogte | AHN (RWS) |
| 2 | Bodemgebruik | LGN/BRP |
| 3 | Orthobeeldvorming | Luchtfoto's (Kadaster) |
| 4 | Geologie | BRO (TNO) |

### Annex III — Milieu en maatschappij (sinds 2013)

| Nr | Thema | NL-dataset (voorbeeld) |
|----|-------|----------------------|
| 1 | Statistische eenheden | CBS wijken/buurten |
| 2 | Gebouwen | BAG + BGT (Kadaster) |
| 3 | Bodem | BRO bodemkaart (WUR) |
| 4 | Landgebruik | BRP (RVO) |
| 5 | Gezondheid en veiligheid | GGD-data |
| 6 | Nutsdiensten en overheidsdiensten | Diverse |
| 7 | Milieucontrolevoorzieningen | RIVM |
| 8 | Productiefaciliteiten en industriefaciliteiten | E-PRTR (RIVM) |
| 9 | Landbouw- en aquacultuurvoorzieningen | RVO |
| 10 | Spreiding bevolking | CBS |
| 11 | Gebiedsbeheer / gebieden waar beperkingen gelden | Diverse |
| 12 | Natuurrisicogebieden | Diverse |
| 13 | Atmosferische omstandigheden | KNMI |
| 14 | Meteorologisch-geografische kenmerken | KNMI |
| 15 | Oceanografisch-geografische kenmerken | RWS |
| 16 | Zeegebieden | RWS |
| 17 | Biogeografische gebieden | LNV |
| 18 | Habitats en biotopen | LNV |
| 19 | Spreiding van soorten | NDFF |
| 20 | Energiebronnen | TNO |
| 21 | Minerale bronnen | TNO |

## Technische Implementatie

### View Service (WMS/WMTS)

INSPIRE view services moeten voldoen aan:
- WMS 1.3.0 of WMTS 1.0.0
- INSPIRE Extended Capabilities in GetCapabilities
- Ondersteuning voor EPSG:4258 (ETRS89) en optioneel EPSG:3035 (ETRS89-LAEA)
- Meertalige ondersteuning (minimaal Engels en Nederlands)
- Specifieke laagnamen conform INSPIRE data specificaties

```xml
<!-- INSPIRE Extended Capabilities in WMS -->
<inspire_vs:ExtendedCapabilities>
  <inspire_common:MetadataUrl>
    <inspire_common:URL>https://www.nationaalgeoregister.nl/geonetwork/srv/dut/csw?
      service=CSW&amp;version=2.0.2&amp;request=GetRecordById&amp;
      Id=aa3b5e6e-7baa-40c0-8972-3353e927ec2f</inspire_common:URL>
    <inspire_common:MediaType>application/vnd.ogc.csw.GetRecordByIdResponse_xml</inspire_common:MediaType>
  </inspire_common:MetadataUrl>
  <inspire_common:SupportedLanguages>
    <inspire_common:DefaultLanguage>
      <inspire_common:Language>dut</inspire_common:Language>
    </inspire_common:DefaultLanguage>
    <inspire_common:SupportedLanguage>
      <inspire_common:Language>eng</inspire_common:Language>
    </inspire_common:SupportedLanguage>
  </inspire_common:SupportedLanguages>
  <inspire_common:ResponseLanguage>
    <inspire_common:Language>dut</inspire_common:Language>
  </inspire_common:ResponseLanguage>
</inspire_vs:ExtendedCapabilities>
```

### Download Service (WFS / Atom / OGC API Features)

INSPIRE download services kunnen op drie manieren geimplementeerd worden:

| Methode | Geschikt voor | Voordelen |
|---------|--------------|-----------|
| WFS 2.0 | Direct access download | Filtering, ruimtelijk/thematisch |
| Atom feed | Pre-defined datasets | Eenvoudig, bulk download |
| OGC API Features | Moderne REST-aanpak | JSON/GeoJSON, OpenAPI |

```bash
# WFS Download Service voorbeeld
curl -s "https://service.pdok.nl/lv/bag/wfs/v2_0?\
service=WFS&version=2.0.0&request=GetFeature&\
typeName=bag:pand&count=5&\
outputFormat=application/gml+xml;+version=3.2&\
srsName=urn:ogc:def:crs:EPSG::4258"

# Atom feed voorbeeld (veelgebruikt voor bulk downloads)
curl -s "https://service.pdok.nl/kadaster/bag/atom/bag.xml" | head -50
```

### Discovery Service (CSW)

De Nederlandse INSPIRE discovery service is het [NGR](https://www.nationaalgeoregister.nl/).

```bash
# INSPIRE metadata zoeken via NGR CSW
curl -s "https://www.nationaalgeoregister.nl/geonetwork/srv/dut/csw?\
service=CSW&version=2.0.2&request=GetRecords&\
ElementSetName=summary&resultType=results&maxRecords=5&\
constraint=keyword=%27INSPIRE%27&constraintLanguage=CQL_TEXT"
```

## INSPIRE Validatie

De [INSPIRE Validator](https://inspire.ec.europa.eu/validator/) (ETF-gebaseerd) toetst services en data op conformiteit.

### Validatie via de API

```bash
# Beschikbare testsuites ophalen
curl -s "https://inspire.ec.europa.eu/validator/v2/ExecutableTestSuites" \
  | python3 -m json.tool | head -60

# WMS validatie starten
curl -s -X POST "https://inspire.ec.europa.eu/validator/v2/TestRuns" \
  -H "Content-Type: application/json" \
  -d '{
    "label": "WMS Validatie",
    "executableTestSuiteIds": ["EID-wms-view-service"],
    "arguments": {
      "files_to_test": "none",
      "tests_to_execute": "*"
    },
    "testObject": {
      "resources": [{
        "resource": {
          "href": "https://service.pdok.nl/hwh/luchtfotorgb/wms/v1_0?service=WMS&request=GetCapabilities"
        }
      }]
    }
  }'

# Status van een testrun ophalen
curl -s "https://inspire.ec.europa.eu/validator/v2/TestRuns/{testRunId}" \
  | python3 -m json.tool
```

### Veelvoorkomende Validatiefouten

| Fout | Oorzaak | Oplossing |
|------|---------|-----------|
| Missing Extended Capabilities | INSPIRE metadata ontbreekt in GetCapabilities | Voeg `<inspire_vs:ExtendedCapabilities>` toe |
| MetadataUrl not resolvable | Link naar metadata in NGR werkt niet | Controleer de metadata-URL in GetCapabilities |
| Unsupported CRS | EPSG:4258 niet ondersteund | Voeg ETRS89 (EPSG:4258) toe als ondersteund CRS |
| Missing language support | Geen meertalige ondersteuning | Implementeer `AcceptLanguages` parameter |
| Schema validation failed | GML niet conform INSPIRE data spec | Gebruik het juiste INSPIRE application schema |
| Missing keyword "INSPIRE" | INSPIRE trefwoord ontbreekt in metadata | Voeg "INSPIRE" en het juiste thema-trefwoord toe |

## Nederlandse Implementatie

### Geonovum Handreiking

De [INSPIRE handreiking](https://docs.geostandaarden.nl/eu/INSPIRE-handreiking/) van Geonovum beschrijft:
- Hoe Nederlandse organisaties moeten voldoen aan INSPIRE
- Welke datasets als INSPIRE-plichtig zijn aangemerkt
- Hoe view/download/discovery services ingericht moeten worden
- Hoe data getransformeerd moet worden naar INSPIRE-datamodellen

### Monitoring en Rapportage

Nederland rapporteert jaarlijks aan de EU over INSPIRE-implementatie. De monitoring omvat:
- Aantal beschikbare datasets per thema
- Conformiteit van services
- Metadata-volledigheid
- Toegankelijkheid van services

## Veelvoorkomende Problemen

| Probleem | Oorzaak | Oplossing |
|----------|---------|-----------|
| Niet weten of data INSPIRE-plichtig is | Onduidelijke scope | Raadpleeg de Geonovum handreiking, bijlage met NL datasets |
| Data past niet in INSPIRE-model | Mismatch NL sectormodel en INSPIRE thema | Gebruik mapping/transformatieregels uit INSPIRE data specs |
| Validator geeft veel fouten | Service niet INSPIRE-conform | Begin met metadata en capabilities, daarna data |
| Atom feed structuur onjuist | Verouderd template | Gebruik de actuele INSPIRE Atom implementatie-richtlijn |
| OGC API Features niet geaccepteerd | Nog niet overal erkend als INSPIRE download service | OGC API Features is inmiddels erkend (Good Practice) |

## Cross-referenties

- Gebruik `/geo-api` voor technische details van WMS, WFS, WMTS.
- Gebruik `/geo-meta` voor INSPIRE-metadata (ISO 19115/19119).
- Gebruik `/geo-model` voor NEN 3610 als basis voor INSPIRE-mapping.
- Gebruik `/geo-3d` voor 3D-data in INSPIRE-context (bijv. gebouwen LoD).

## Achtergrondinfo

Zie [reference.md](reference.md) voor gedetailleerde data-thema mapping, transformatieregels, en monitoring/rapportage-eisen.
