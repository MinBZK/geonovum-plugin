---
name: geo-3d
description: >-
  3D standaarden voor ruimtelijke data. Gebruik deze skill wanneer de
  gebruiker vraagt over '3D', 'CityGML', '3D tiling', '3D Tiles',
  'GeoBIM', 'digital twin', '3D geo', '3D standaarden',
  '3D basisvoorziening', 'BIM GIS', 'IFC', 'LOD', 'level of detail',
  '3D stadsmodel', 'Cesium', '3D visualisatie geo'.
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

# 3D Standaarden voor Geodata

**Agent-instructie:** Deze skill helpt bij het werken met 3D geo-standaarden, van CityGML-modellering tot 3D Tiles-visualisatie. Gebruik de voorbeelden voor het benaderen van de 3D Basisvoorziening en het converteren tussen formaten. Verwijs naar `/geo-model` voor de relatie met NEN 3610 en informatiemodellen.

Nederland loopt voorop in 3D geo-informatie met de [3D Basisvoorziening](https://www.pdok.nl/introductie/-/article/3d-basisvoorziening-1) — een landsdekkend 3D-model. Geonovum werkt aan standaarden voor 3D data-uitwisseling, integratie van GIS en BIM (GeoBIM), en digital twin-toepassingen. De 3D-standaarden bouwen voort op internationale OGC-standaarden zoals CityGML en 3D Tiles.

## Standaarden Overzicht

| Standaard | Type | Doel |
|-----------|------|------|
| CityGML 2.0 / 3.0 | Datamodel & encoding | 3D stadsmodellen (OGC-standaard) |
| 3D Tiles 1.1 | Streaming | 3D content streamen voor visualisatie (OGC/Cesium) |
| CityJSON 1.1 / 2.0 | Encoding | JSON-gebaseerde encoding voor CityGML |
| IFC | BIM standaard | Building Information Modeling (buildingSMART) |
| NEN 3610 3D | Profiel | 3D-extensie op het basismodel geo-informatie |

## Repositories

| Repository | Beschrijving | Licentie |
|-----------|-------------|--------|
| [Geonovum/GeoBIM](https://github.com/Geonovum/GeoBIM) | Integratie van GIS en BIM | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode.en) |

## CityGML

CityGML is de OGC-standaard voor het modelleren en uitwisselen van 3D stadsmodellen. Het definieert een semantisch model met meerdere detailniveaus (Levels of Detail).

### Levels of Detail (LOD)

| LOD | Naam | Beschrijving | Geometrie |
|-----|------|-------------|-----------|
| LOD0 | Regionaal | 2.5D footprint/dakrand | Vlak (2.5D) |
| LOD1 | Blokmodel | Extrusie van footprint | Blok (prisma) |
| LOD2 | Basismodel | Dak- en muurvlakken | Oppervlakken met dakvormen |
| LOD3 | Gedetailleerd | Ramen, deuren, balkons | Gedetailleerde oppervlakken |
| LOD4 | Interieur | Binnenruimtes, meubels | Interieur geometrie |

### CityGML Thematische Modules

| Module | Beschrijving | Voorbeelden |
|--------|-------------|-------------|
| Building | Gebouwen | Woningen, kantoren, scholen |
| Transportation | Infrastructuur | Wegen, spoorwegen, fietspaden |
| Vegetation | Begroeiing | Bomen, parken |
| WaterBody | Water | Rivieren, kanalen, meren |
| LandUse | Landgebruik | Bestemmingsplannen |
| Bridge | Bruggen | Viaducten, voetgangersbruggen |
| Tunnel | Tunnels | Wegtunnels, spoortunnels |
| CityFurniture | Straatmeubilair | Lantaarnpalen, bankjes |
| Relief | Terrein | Digitaal terreinmodel |
| Construction (3.0) | Constructies | Andere bouwwerken dan gebouwen |

### CityGML Voorbeeld (LOD1 gebouw)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<CityModel xmlns="http://www.opengis.net/citygml/2.0"
  xmlns:bldg="http://www.opengis.net/citygml/building/2.0"
  xmlns:gml="http://www.opengis.net/gml">

  <cityObjectMember>
    <bldg:Building gml:id="building_001">
      <bldg:yearOfConstruction>1985</bldg:yearOfConstruction>
      <bldg:function>1000</bldg:function>
      <bldg:measuredHeight uom="m">12.5</bldg:measuredHeight>
      <bldg:storeysAboveGround>3</bldg:storeysAboveGround>

      <bldg:lod1Solid>
        <gml:Solid srsName="urn:ogc:def:crs:EPSG::7415">
          <gml:exterior>
            <gml:CompositeSurface>
              <!-- Muurvlakken en dakvlak -->
              <gml:surfaceMember>
                <gml:Polygon>
                  <gml:exterior>
                    <gml:LinearRing>
                      <gml:posList>
                        120000 487000 0
                        120010 487000 0
                        120010 487010 0
                        120000 487010 0
                        120000 487000 0
                      </gml:posList>
                    </gml:LinearRing>
                  </gml:exterior>
                </gml:Polygon>
              </gml:surfaceMember>
            </gml:CompositeSurface>
          </gml:exterior>
        </gml:Solid>
      </bldg:lod1Solid>
    </bldg:Building>
  </cityObjectMember>
</CityModel>
```

### CityJSON Voorbeeld

CityJSON is een compactere JSON-representatie van CityGML:

```json
{
  "type": "CityJSON",
  "version": "2.0",
  "CityObjects": {
    "building_001": {
      "type": "Building",
      "attributes": {
        "yearOfConstruction": 1985,
        "measuredHeight": 12.5,
        "function": "1000",
        "storeysAboveGround": 3
      },
      "geometry": [{
        "type": "Solid",
        "lod": "1",
        "boundaries": [
          [[[0, 1, 2, 3]], [[4, 5, 6, 7]], [[0, 1, 5, 4]],
           [[1, 2, 6, 5]], [[2, 3, 7, 6]], [[3, 0, 4, 7]]]
        ]
      }]
    }
  },
  "vertices": [
    [120000, 487000, 0],
    [120010, 487000, 0],
    [120010, 487010, 0],
    [120000, 487010, 0],
    [120000, 487000, 12.5],
    [120010, 487000, 12.5],
    [120010, 487010, 12.5],
    [120000, 487010, 12.5]
  ],
  "metadata": {
    "referenceSystem": "https://www.opengis.net/def/crs/EPSG/0/7415"
  }
}
```

## 3D Tiles

3D Tiles is de OGC-standaard (oorspronkelijk Cesium) voor het streamen van 3D-content. Het wordt gebruikt voor visualisatie van grote 3D-datasets in webbrowsers.

### 3D Tiles Structuur

```
tileset.json          ← Hoofdbestand (metadata + boomstructuur)
├── tile_L0.b3dm      ← Level 0 (grof)
├── tiles/
│   ├── tile_L1_0.b3dm  ← Level 1 (detail)
│   ├── tile_L1_1.b3dm
│   └── ...
```

### 3D Basisvoorziening via PDOK

De [3D Basisvoorziening](https://www.pdok.nl/introductie/-/article/3d-basisvoorziening-1) is het landsdekkende 3D-model van Nederland, beschikbaar via PDOK.

```bash
# 3D Basisvoorziening metadata ophalen
curl -s "https://api.pdok.nl/kadaster/3d-basisvoorziening/ogc/v1/collections" \
  | python3 -m json.tool

# 3D Tiles tileset ophalen (gebouwen)
curl -s "https://api.pdok.nl/kadaster/3d-basisvoorziening/ogc/v1_0/collections/gebouwen/3dtiles" \
  | python3 -m json.tool | head -30
```

### Cesium Viewer Voorbeeld

```html
<!DOCTYPE html>
<html>
<head>
  <script src="https://cesium.com/downloads/cesiumjs/releases/1.113/Build/Cesium/Cesium.js"></script>
  <link href="https://cesium.com/downloads/cesiumjs/releases/1.113/Build/Cesium/Widgets/widgets.css" rel="stylesheet">
</head>
<body>
  <div id="cesiumContainer" style="width:100%; height:100vh;"></div>
  <script>
    const viewer = new Cesium.Viewer('cesiumContainer');

    // 3D Basisvoorziening laden
    const tileset = viewer.scene.primitives.add(
      new Cesium.Cesium3DTileset({
        url: 'https://api.pdok.nl/kadaster/3d-basisvoorziening/ogc/v1_0/collections/gebouwen/3dtiles'
      })
    );

    // Camera naar Nederland
    viewer.camera.flyTo({
      destination: Cesium.Cartesian3.fromDegrees(4.9, 52.37, 1500),
      orientation: {
        heading: Cesium.Math.toRadians(0),
        pitch: Cesium.Math.toRadians(-45),
        roll: 0
      }
    });
  </script>
</body>
</html>
```

## GeoBIM — Integratie GIS en BIM

GeoBIM combineert geo-informatie (GIS) met bouwinformatie (BIM/IFC) voor toepassingen als:
- Omgevingsvergunningen (toetsing bouwaanvraag aan bestemmingsplan)
- Ondergrondse infrastructuur (kabels/leidingen + bouwput)
- Assetmanagement (civiele kunstwerken)

### Verschil GIS en BIM

| Aspect | GIS (CityGML) | BIM (IFC) |
|--------|--------------|-----------|
| Scope | Stad/regio | Gebouw/object |
| CRS | Geografisch (EPSG:28992) | Lokaal (relatief) |
| Detailniveau | LOD0-3 | Constructiedetail |
| Focus | Buitenkant, context | Binnenkant, constructie |
| Formaat | GML, CityJSON, GeoJSON | IFC, BCF |
| Standaardorganisatie | OGC, Geonovum | buildingSMART |

### GeoBIM Workflow

1. **BIM-model (IFC)** exporteren vanuit ontwerpomgeving
2. **Georeferencing** — IFC lokale coordinaten koppelen aan RD-coordinaten
3. **Conversie** naar CityGML/CityJSON op het gewenste LOD
4. **Integratie** met bestaande geo-data (BGT, BAG, AHN)
5. **Publicatie** als 3D Tiles of WFS

## Digital Twins

Digital twins gebruiken 3D geo-standaarden als basis:

| Component | Standaard | Rol |
|-----------|----------|-----|
| 3D stadsmodel | CityGML / 3D Tiles | Visuele basis |
| Terrein | AHN (raster) | Hoogtemodel |
| Gebouwen | BAG + 3D Basisvoorziening | Gebouwgeometrie |
| Infrastructuur | BGT + IMKL | Wegen, kabels, leidingen |
| Sensordata | SensorThings API | Real-time metingen |
| Simulatie | Diverse | Wateroverlast, wind, geluid |

## Veelvoorkomende Problemen

| Probleem | Oorzaak | Oplossing |
|----------|---------|-----------|
| CityGML-bestand te groot | Heel stadsmodel in 1 bestand | Splits op in tegels, gebruik 3D Tiles voor visualisatie |
| Geometrie niet valide | Zelf-intersecties, gaten | Valideer met val3dity, repareer met tools als 3dfier |
| CRS-mismatch bij GeoBIM | IFC lokale coordinaten | Gebruik georeferencing tools (bijv. IfcMapConversion) |
| 3D Tiles laden traag | Tiles te groot of niet geoptimaliseerd | Gebruik geometric error goed, comprimeer met Draco |
| LOD niet beschikbaar | Data alleen in LOD1 | Gebruik 3D Basisvoorziening (LOD1.2/1.3 landsdekkend) |
| CityJSON niet herkend | Software ondersteunt alleen CityGML/XML | Converteer met cjio (CityJSON CLI) naar GML |

## Cross-referenties

- Gebruik `/geo-model` voor NEN 3610 als basis voor 3D informatiemodellen.
- Gebruik `/geo-api` voor het ontsluiten van 3D data via OGC services.
- Gebruik `/geo-inspire` voor INSPIRE-eisen aan 3D gebouwendata.
- Gebruik `/geo-meta` voor metadata van 3D datasets.

## Achtergrondinfo

Zie [reference.md](reference.md) voor gedetailleerde CityGML-encoding, 3D Tiles specificatie-details, en LOD-uitleg.
