# Metadata voor Geodata - Achtergrondinfo

Deze pagina bevat aanvullende details over metadata-elementen, validatieregels en het NGR-publicatieproces.

## Volledige Elementenlijst NL Profiel ISO 19115

### Dataset Metadata

| Element | Verplichting | Herhaalbaar | Beschrijving |
|---------|-------------|-------------|-------------|
| fileIdentifier | Verplicht | Nee | Unieke ID van het metadata-record (UUID) |
| language | Verplicht | Nee | Taal van de metadata (dut/nld) |
| characterSet | Conditioneel | Nee | Tekenset (utf8 standaard) |
| hierarchyLevel | Verplicht | Nee | dataset, series, of service |
| contact | Verplicht | Ja | Contactgegevens metadata-beheerder |
| dateStamp | Verplicht | Nee | Datum van metadata (YYYY-MM-DD) |
| metadataStandardName | Verplicht | Nee | "ISO 19115" |
| metadataStandardVersion | Verplicht | Nee | Versie van het NL profiel |
| referenceSystemInfo | Verplicht | Ja | CRS (bijv. EPSG:28992) |
| identificationInfo | Verplicht | Nee | Identificatie van de dataset |
| distributionInfo | Verplicht | Nee | Distributie-informatie |
| dataQualityInfo | Conditioneel | Ja | Kwaliteitsinformatie |

### Identificatie-elementen (MD_DataIdentification)

| Element | Verplichting | Beschrijving |
|---------|-------------|-------------|
| citation/title | Verplicht | Titel van de dataset |
| citation/date | Verplicht | Datum (publicatie, revisie, creatie) |
| citation/identifier | Optioneel | Unieke identifier van de dataset |
| abstract | Verplicht | Samenvatting |
| status | Optioneel | Status (completed, onGoing, etc.) |
| pointOfContact | Verplicht | Verantwoordelijke organisatie |
| resourceMaintenance | Optioneel | Bijhoudingsfrequentie |
| descriptiveKeywords | Verplicht | Trefwoorden (minstens 1) |
| resourceConstraints | Verplicht | Gebruiksbeperkingen |
| spatialRepresentationType | Optioneel | vector, grid, textTable |
| spatialResolution | Verplicht | Schaal of grondresolutie |
| language | Verplicht | Taal van de dataset |
| characterSet | Conditioneel | Tekenset van de dataset |
| topicCategory | Verplicht | ISO-categorie (minstens 1) |
| extent | Verplicht | Ruimtelijke en temporele dekking |

### ISO Topic Categories

| Code | Beschrijving |
|------|-------------|
| boundaries | Bestuurlijke grenzen |
| elevation | Hoogte |
| environment | Milieu |
| geoscientificInformation | Geowetenschappen |
| imageryBaseMapsEarthCover | Basiskaarten, landgebruik |
| inlandWaters | Binnenwater |
| location | Locatie |
| planningCadastre | Ruimtelijke ordening, kadaster |
| structure | Gebouwen, constructies |
| transportation | Transport |
| utilitiesCommunication | Nutsvoorzieningen |

## Service Metadata (ISO 19119)

Voor services (WMS, WFS, CSW) gelden aanvullende elementen:

| Element | Verplichting | Beschrijving |
|---------|-------------|-------------|
| serviceType | Verplicht | OGC:WMS, OGC:WFS, OGC:CSW, etc. |
| serviceTypeVersion | Verplicht | Versie van het service-protocol |
| couplingType | Verplicht | tight, mixed, loose |
| containsOperations | Verplicht | Operaties (GetCapabilities, GetMap, etc.) |
| operatesOn | Conditioneel | Link naar dataset-metadata |
| accessProperties | Optioneel | Toegangseigenschappen |

## Validatieregels

### Structurele validatie

Het metadata-record moet voldoen aan het ISO 19115 XML-schema (gmd namespace). Controleer:

- Correcte namespace-declaraties
- Verplichte elementen aanwezig
- Correcte datatypen (Date, Decimal, CharacterString)
- Geldige codelijstwaarden

### Inhoudelijke validatie (NL profiel)

- Titel is niet leeg en beschrijvend
- Samenvatting bevat minimaal 25 tekens
- Minstens 1 trefwoord aanwezig
- Contactgegevens bevatten organisatienaam en e-mailadres
- Bounding box valt binnen Nederland (lat: 50.75-53.47, lon: 3.37-7.21) of is breder
- CRS is gespecificeerd en geldig
- Distributie-URL is bereikbaar

### Validatietools

```bash
# Metadata valideren via de Geonovum validator
curl -s -X POST "https://validatie.geostandaarden.nl/etf-webapp/v2/TestRuns" \
  -H "Content-Type: application/json" \
  -d '{"label": "NL profiel check", "executableTestSuiteIds": ["..."]}'

# XML-schema validatie met xmllint
xmllint --schema http://www.isotc211.org/2005/gmd/gmd.xsd metadata.xml --noout
```

## NGR Publicatieworkflow

### Stap 1: Metadata Aanmaken

Gebruik het XML-sjabloon uit SKILL.md als basis. Vul alle verplichte elementen in.

### Stap 2: Metadata Valideren

Valideer tegen het NL profiel voordat je publiceert. Gebruik de Geonovum validator of een lokale tool.

### Stap 3: Publiceren

#### Optie A: NGR-editor (webinterface)

1. Log in op [nationaalgeoregister.nl](https://www.nationaalgeoregister.nl/)
2. Ga naar de metadata-editor
3. Vul de velden in of importeer een XML-bestand
4. Sla op en publiceer

#### Optie B: CSW Harvesting

1. Publiceer metadata op een eigen CSW-endpoint (bijv. GeoNetwork)
2. Registreer het endpoint bij het NGR
3. NGR harvest periodiek de metadata

#### Optie C: GeoNetwork REST API
```bash
# Metadata uploaden via GeoNetwork REST API
curl -X PUT "https://www.nationaalgeoregister.nl/geonetwork/srv/api/records" \
  -H "Content-Type: application/xml" \
  -H "X-XSRF-TOKEN: <token>" \
  --data-binary @metadata.xml
```

### Stap 4: Verifieer Publicatie

```bash
# Zoek naar je metadata via CSW
curl -s "https://www.nationaalgeoregister.nl/geonetwork/srv/dut/csw?\
service=CSW&version=2.0.2&request=GetRecords&\
ElementSetName=summary&resultType=results&maxRecords=5&\
constraint=AnyText+like+%25jouw-dataset-naam%25&\
constraintLanguage=CQL_TEXT"
```

## DCAT en GeoDCAT-AP

GeoDCAT-AP is een Europees profiel dat ISO 19115 metadata mapt naar DCAT (RDF). Dit is relevant voor koppeling met data.overheid.nl en het Europese data-portaal.

### Voorbeeld GeoDCAT-AP (Turtle)

```turtle
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct:  <http://purl.org/dc/terms/> .
@prefix locn: <http://www.w3.org/ns/locn#> .

<https://www.nationaalgeoregister.nl/geonetwork/srv/metadata/aa3b5e6e>
  a dcat:Dataset ;
  dct:title "Basisregistratie Adressen en Gebouwen (BAG)"@nl ;
  dct:description "De BAG bevat gegevens over adressen en gebouwen."@nl ;
  dct:publisher <https://www.kadaster.nl/> ;
  dcat:keyword "adressen"@nl, "gebouwen"@nl ;
  dct:issued "2024-01-15"^^xsd:date ;
  dct:spatial [
    a dct:Location ;
    locn:geometry "POLYGON((3.37 50.75, 7.21 50.75, 7.21 53.47, 3.37 53.47, 3.37 50.75))"^^locn:wktLiteral
  ] ;
  dcat:distribution [
    a dcat:Distribution ;
    dcat:accessURL <https://service.pdok.nl/lv/bag/wfs/v2_0> ;
    dct:format "WFS"
  ] .
```

## Repository Exploratie

```bash
# Metadata profiel bekijken
gh api repos/Geonovum/Metadata-ISO19115/contents --jq '.[].name'

# Laatste wijzigingen
gh api repos/Geonovum/Metadata-ISO19115/commits \
  --jq '.[:5] | .[] | "\(.commit.committer.date) \(.commit.message | split("\n")[0])"'

# Handreiking bekijken
gh api repos/Geonovum/Metadata-handreiking/contents --jq '.[].name'

# Zoek naar metadata-gerelateerde repos
gh api orgs/Geonovum/repos --paginate \
  --jq '.[] | select(.name | test("metadata|meta|csw"; "i")) | "\(.name): \(.description)"'
```

## Gerelateerde Skills

| Skill | Relatie |
|-------|---------|
| `/geo-api` | Services waar metadata naar verwijst |
| `/geo-inspire` | INSPIRE-specifieke metadata-eisen |
| `/geo-model` | Informatiemodellen waarnaar metadata kan verwijzen |
| `/geo` | Overzicht alle geo-standaarden |
