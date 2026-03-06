---
name: geo-api
description: >-
  OGC API services en kaartdiensten. Gebruik deze skill wanneer de gebruiker
  vraagt over 'OGC API', 'WMS', 'WFS', 'WCS', 'WMTS',
  'OGC API Features', 'kaartdienst', 'map service', 'ogc-checker',
  'geo API', 'GetCapabilities', 'GetMap', 'GetFeature',
  'PDOK service', 'geo webservice', 'spatial web service'.
model: sonnet
allowed-tools:
  - Bash(gh api *)
  - Bash(curl -s *)
  - Bash(ogr2ogr *)
  - Bash(ogrinfo *)
  - WebFetch(*)
metadata:
  created-with-ai: "true"
  created-with-model: claude-opus-4-20250514
  created-date: "2025-02-22"
  status: concept
---

> **Let op:** Deze skill is geen officieel product van Geonovum. De beschrijvingen zijn informatieve samenvattingen — niet de officiële standaarden zelf. De definities op [forumstandaardisatie.nl](https://www.forumstandaardisatie.nl/open-standaarden) en [Geonovum](https://www.geonovum.nl) zijn altijd leidend. Overheidsorganisaties die generatieve AI inzetten dienen te voldoen aan het [Rijksbrede beleidskader voor generatieve AI](https://www.government.nl/documents/policy-notes/2025/01/31/government-wide-position-on-the-use-of-generative-ai). Zie [DISCLAIMER.md](../../DISCLAIMER.md).

# OGC API Services & Kaartdiensten

**Agent-instructie:** Deze skill helpt bij het implementeren en gebruiken van OGC geo-webservices. Gebruik curl-voorbeelden voor PDOK-services en de ogc-checker voor validatie. OGC API Features en OGC API Tiles zijn verplicht onder ['pas-toe-of-leg-uit'](https://www.forumstandaardisatie.nl/open-standaarden/geo-standaarden); WMS en WFS zijn aanbevolen (sinds september 2024).

OGC-services zijn de standaard manier om geodata beschikbaar te stellen via het web. Nederland gebruikt deze standaarden intensief via [PDOK](https://www.pdok.nl/) — het nationale portaal voor geo-webservices. Geonovum beheert de Nederlandse profielen en de [ogc-checker](https://github.com/Geonovum/ogc-checker) validatietool.

## Standaarden Overzicht

| Standaard | Type | Doel | Forum status |
|-----------|------|------|-------------|
| OGC API Features | REST API | REST-gebaseerde opvolger van WFS (JSON/GeoJSON) | Verplicht |
| OGC API Tiles | Tiles | Opvolger van WMTS (voorgerenderde kaarttegels) | Verplicht |
| WMS 1.3.0 | View | Kaartafbeeldingen (PNG/JPEG) opvragen | Aanbevolen |
| WFS 2.0 | Download | Vector features (GML/GeoJSON) opvragen | Aanbevolen |
| WCS 2.0 | Coverage | Rasterdata (gridded data) ophalen | Geen Forum status |
| GeoPackage 1.3.1 | Bestandsformaat | Lokale opslag van vector- en rasterdata (SQLite) | Verplicht |

## Repositories

| Repository | Beschrijving | Licentie |
|-----------|-------------|--------|
| [Geonovum/ogc-checker](https://github.com/Geonovum/ogc-checker) | Validatietool voor OGC services | [EUPL-1.2](https://eupl.eu/1.2/en) |
| [Geonovum/ogc-checker Tags](https://github.com/Geonovum/ogc-checker/tags) | Versies van ogc-checker | [EUPL-1.2](https://eupl.eu/1.2/en) |

## WMS (Web Map Service)

WMS levert kaartafbeeldingen (rasterformaat). Drie operaties:

- **GetCapabilities** — beschrijft de service en beschikbare lagen
- **GetMap** — haalt een kaartafbeelding op (PNG, JPEG)
- **GetFeatureInfo** — haalt attribuutinfo op voor een punt op de kaart

```bash
# WMS GetCapabilities — Luchtfoto RGB
curl -s "https://service.pdok.nl/hwh/luchtfotorgb/wms/v1_0?service=WMS&request=GetCapabilities" \
  | head -50

# WMS GetMap — kaartafbeelding ophalen (PNG)
curl -s "https://service.pdok.nl/hwh/luchtfotorgb/wms/v1_0?\
service=WMS&version=1.3.0&request=GetMap&\
layers=Actueel_orthoHR&crs=EPSG:28992&\
bbox=120000,480000,130000,490000&\
width=800&height=800&format=image/png" -o /tmp/kaart.png

# WMS GetFeatureInfo — attribuutinfo op een punt
curl -s "https://service.pdok.nl/hwh/luchtfotorgb/wms/v1_0?\
service=WMS&version=1.3.0&request=GetFeatureInfo&\
layers=Actueel_orthoHR&query_layers=Actueel_orthoHR&\
crs=EPSG:28992&bbox=120000,480000,130000,490000&\
width=800&height=800&i=400&j=400&\
info_format=application/json"
```

## WFS (Web Feature Service)

WFS levert vectordata als features (GML of GeoJSON). Belangrijke operaties:

- **GetCapabilities** — beschrijft de service
- **DescribeFeatureType** — beschrijft het schema van een featuretype
- **GetFeature** — haalt features op, met filters

```bash
# WFS GetCapabilities — BAG (Basisregistratie Adressen en Gebouwen)
curl -s "https://service.pdok.nl/lv/bag/wfs/v2_0?\
service=WFS&request=GetCapabilities" | head -80

# WFS GetFeature — eerste 10 panden als GeoJSON
curl -s "https://service.pdok.nl/lv/bag/wfs/v2_0?\
service=WFS&version=2.0.0&request=GetFeature&\
typeName=bag:pand&count=10&\
outputFormat=application/json"

# WFS met ruimtelijk filter (BBOX)
curl -s "https://service.pdok.nl/lv/bag/wfs/v2_0?\
service=WFS&version=2.0.0&request=GetFeature&\
typeName=bag:pand&count=10&\
outputFormat=application/json&\
bbox=52.37,4.89,52.38,4.91,urn:ogc:def:crs:EPSG::4326"

# WFS DescribeFeatureType
curl -s "https://service.pdok.nl/lv/bag/wfs/v2_0?\
service=WFS&version=2.0.0&request=DescribeFeatureType&\
typeName=bag:pand"
```

## WMTS (Web Map Tile Service)

WMTS levert voorgerenderde kaarttegels. Veel sneller dan WMS voor basemaps.

```bash
# WMTS GetCapabilities — BRT Achtergrondkaart
curl -s "https://service.pdok.nl/brt/achtergrondkaart/wmts/v2_0?\
service=WMTS&request=GetCapabilities" | head -80

# WMTS GetTile — enkele tegel ophalen
curl -s "https://service.pdok.nl/brt/achtergrondkaart/wmts/v2_0?\
service=WMTS&version=1.0.0&request=GetTile&\
layer=standaard&style=default&\
tilematrixset=EPSG:28992&tilematrix=10&\
tilerow=300&tilecol=350&format=image/png" -o /tmp/tile.png
```

## WCS (Web Coverage Service)

WCS levert rasterdata (gridded coverages) zoals hoogtemodellen.

```bash
# WCS GetCapabilities — AHN (Actueel Hoogtebestand Nederland)
curl -s "https://service.pdok.nl/rws/ahn/wcs/v1_0?\
service=WCS&request=GetCapabilities" | head -50
```

## OGC API Features

REST-gebaseerde opvolger van WFS. Gebruikt JSON/GeoJSON, OpenAPI-specificatie, en standaard HTTP-methoden.

```bash
# Beschikbare collecties ophalen (Bestuurlijke Gebieden)
curl -s "https://api.pdok.nl/kadaster/brk-bestuurlijke-gebieden/ogc/v1/collections?f=json" \
  | python3 -m json.tool

# Specifieke collectie bekijken
curl -s "https://api.pdok.nl/kadaster/brk-bestuurlijke-gebieden/ogc/v1/collections/gemeentegebied?f=json" \
  | python3 -m json.tool

# Features ophalen (eerste 10 gemeenten)
curl -s "https://api.pdok.nl/kadaster/brk-bestuurlijke-gebieden/ogc/v1/collections/gemeentegebied/items?limit=10&f=json" \
  | python3 -m json.tool

# Feature op basis van ID
curl -s "https://api.pdok.nl/kadaster/brk-bestuurlijke-gebieden/ogc/v1/collections/gemeentegebied/items/{id}?f=json" \
  | python3 -m json.tool

# Ruimtelijke filter met bbox
curl -s "https://api.pdok.nl/kadaster/brk-bestuurlijke-gebieden/ogc/v1/collections/gemeentegebied/items?\
bbox=4.89,52.37,4.91,52.38&limit=10&f=json" | python3 -m json.tool

# OpenAPI spec van de service
curl -s "https://api.pdok.nl/kadaster/brk-bestuurlijke-gebieden/ogc/v1/api?f=json" \
  | python3 -m json.tool | head -50
```

## Python Implementatie

### Met requests (OGC API Features)

```python
import requests

# OGC API Features — bestuurlijke gebieden ophalen
base_url = "https://api.pdok.nl/kadaster/brk-bestuurlijke-gebieden/ogc/v1"

# Collecties ophalen
collecties = requests.get(f"{base_url}/collections", params={"f": "json"}).json()
for c in collecties["collections"]:
    print(f"  {c['id']}: {c.get('title', '')}")

# Features met bbox-filter
params = {
    "bbox": "4.89,52.37,4.91,52.38",
    "limit": 50,
    "f": "json",
}
response = requests.get(f"{base_url}/collections/gemeentegebied/items", params=params)
features = response.json()
print(f"Gevonden: {features.get('numberMatched', len(features.get('features', [])))} gemeenten")
for feature in features["features"]:
    print(f"  ID: {feature['id']}, Naam: {feature['properties'].get('naam')}")
```

### Met OWSLib (WMS/WFS)

```python
from owslib.wms import WebMapService
from owslib.wfs import WebFeatureService

# WMS — kaartafbeelding ophalen
wms = WebMapService("https://service.pdok.nl/hwh/luchtfotorgb/wms/v1_0")
print("Lagen:", list(wms.contents))

img = wms.getmap(
    layers=["Actueel_orthoHR"],
    srs="EPSG:28992",
    bbox=(120000, 480000, 130000, 490000),
    size=(800, 800),
    format="image/png",
)
with open("/tmp/kaart.png", "wb") as f:
    f.write(img.read())

# WFS — features ophalen
wfs = WebFeatureService(
    "https://service.pdok.nl/lv/bag/wfs/v2_0", version="2.0.0"
)
print("Feature types:", list(wfs.contents))

response = wfs.getfeature(
    typename=["bag:pand"],
    maxfeatures=10,
    outputFormat="application/json",
)
import json
data = json.loads(response.read())
print(f"Gevonden: {len(data['features'])} panden")
```

## ogc-checker Validatie

De [ogc-checker](https://github.com/Geonovum/ogc-checker) is een validatietool van Geonovum om OGC-services te controleren op conformiteit.

```bash
# Repo-informatie ophalen
gh api repos/Geonovum/ogc-checker --jq '{name, description, language, updated_at}'

# Laatste releases bekijken
gh api repos/Geonovum/ogc-checker/tags --jq '.[].name'

# Issues bekijken
gh issue list --repo Geonovum/ogc-checker

# Broncode verkennen
gh api repos/Geonovum/ogc-checker/contents --jq '.[].name'
```

## GDAL/OGR Diagnostiek

```bash
# WFS-service testen met ogrinfo
ogrinfo "WFS:https://service.pdok.nl/lv/bag/wfs/v2_0" -summary

# Features downloaden naar GeoJSON
ogr2ogr -f "GeoJSON" /tmp/panden.geojson \
  "WFS:https://service.pdok.nl/lv/bag/wfs/v2_0" bag:pand \
  -where "1=1" -limit 10

# CRS-transformatie bij download
ogr2ogr -f "GeoJSON" /tmp/panden_wgs84.geojson \
  "WFS:https://service.pdok.nl/lv/bag/wfs/v2_0" bag:pand \
  -t_srs EPSG:4326 -limit 10
```

## Veelvoorkomende Problemen

| Probleem | Oorzaak | Oplossing |
|----------|---------|-----------|
| `InvalidParameterValue` bij WMS/WFS | Verkeerde CRS of lagen-naam | Controleer GetCapabilities voor juiste waarden |
| Lege response bij bbox-filter | Verkeerde coördinaatvolgorde | WMS 1.3.0 respecteert CRS-asvolgorde: voor EPSG:4326 is dat lat/lon; voor EPSG:28992 is het x/y |
| Timeout bij grote WFS-requests | Te veel features opgevraagd | Gebruik `count`/`maxFeatures` parameter of bbox-filter |
| `text/xml` in plaats van GeoJSON | outputFormat niet ondersteund | Controleer GetCapabilities voor beschikbare formaten |
| 403 bij PDOK-service | Rate limiting of IP-blokkade | Gebruik API-key voor intensief gebruik (via PDOK) |
| OGC API Features geeft HTML | Geen Accept-header meegegeven | Voeg `Accept: application/geo+json` header toe |

## Cross-referenties

- Gebruik `/ls-api` (uit skills-standaarden) voor de **ADR geo-module** — richtlijnen voor GeoJSON, CRS-negotiatie en bbox in REST APIs.
- Gebruik `/geo-meta` voor metadata van services (ISO 19115, CSW).
- Gebruik `/geo-inspire` voor INSPIRE-conforme view en download services.

## Achtergrondinfo

Zie [reference.md](reference.md) voor uitgebreide OGC-protocoldetails, CRS-handling (EPSG:28992/RD New), en de volledige PDOK-servicecatalogus.
