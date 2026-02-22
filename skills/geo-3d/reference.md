# 3D Standaarden - Achtergrondinfo

Deze pagina bevat aanvullende technische details over CityGML-encoding, 3D Tiles, en LOD-specificaties.

## CityGML Encoding Details

### CityGML 2.0 Namespaces

| Prefix | Namespace URI | Module |
|--------|--------------|--------|
| `core` | `http://www.opengis.net/citygml/2.0` | Kern |
| `bldg` | `http://www.opengis.net/citygml/building/2.0` | Gebouwen |
| `tran` | `http://www.opengis.net/citygml/transportation/2.0` | Transport |
| `veg` | `http://www.opengis.net/citygml/vegetation/2.0` | Begroeiing |
| `wtr` | `http://www.opengis.net/citygml/waterbody/2.0` | Water |
| `luse` | `http://www.opengis.net/citygml/landuse/2.0` | Landgebruik |
| `brid` | `http://www.opengis.net/citygml/bridge/2.0` | Bruggen |
| `tun` | `http://www.opengis.net/citygml/tunnel/2.0` | Tunnels |
| `frn` | `http://www.opengis.net/citygml/cityfurniture/2.0` | Straatmeubilair |
| `dem` | `http://www.opengis.net/citygml/relief/2.0` | Terrein |
| `gen` | `http://www.opengis.net/citygml/generics/2.0` | Generiek |
| `app` | `http://www.opengis.net/citygml/appearance/2.0` | Uiterlijk |

### CityGML 3.0 Veranderingen

CityGML 3.0 brengt belangrijke wijzigingen:

| Aspect | CityGML 2.0 | CityGML 3.0 |
|--------|------------|------------|
| LOD-concept | LOD0-4 (vast) | Space concept (flexibel) |
| Encoding | Alleen GML | GML + CityJSON + database |
| Interieur | LOD4 (gebouw-specifiek) | Aparte Construction module |
| Versioning | Niet ingebouwd | Versioning module |
| PointCloud | Niet ondersteund | PointCloud module |
| Dynamiek | Niet ondersteund | Dynamizer module |

### CityGML LOD Specificaties (2.0)

#### LOD0 — Regionaal Model
- Geometrie: `MultiSurface` (footprint of dakrand als vlak)
- Hoogte: geen of gemiddelde hoogte als attribuut
- Toepassing: landelijk overzicht, statistiek

#### LOD1 — Blokmodel
- Geometrie: `Solid` (extrusie van footprint naar gemiddelde dakrand)
- Hoogte: uniforme hoogte per gebouw
- Toepassing: ruimtelijke analyses, schaduwberekening, geluid

#### LOD2 — Dak- en Muurmodel
- Geometrie: `MultiSurface` of `Solid` met dakvlakken en muurvlakken
- Dak: werkelijke dakvormen (plat, schuin, zadeldak)
- Toepassing: zonnepanelen-potentie, energiemodellering

#### LOD3 — Architectonisch Model
- Geometrie: gedetailleerde oppervlakken inclusief ramen, deuren, balkons
- Texturen: foto-realistisch mogelijk
- Toepassing: visualisatie, ventilatie-analyse

#### LOD4 — Interieur Model
- Geometrie: binnenruimtes, verdiepingen, kamers
- Toepassing: indoor navigatie, facilitair management

### 3D Basisvoorziening LOD-niveaus

De Nederlandse 3D Basisvoorziening biedt:

| Product | LOD | Bron | Beschrijving |
|---------|-----|------|-------------|
| 3D Gebouwen | LOD1.2 | BAG + AHN | Gebouwen met plat dak op werkelijke hoogte |
| 3D Gebouwen | LOD1.3 | BAG + AHN | Gebouwen met nokhoogte |
| 3D Gebouwen | LOD2.2 | BAG + AHN + puntenwolk | Gebouwen met werkelijke dakvormen |
| 3D Terrein | - | AHN | TIN-model van het maaiveld |
| 3D Bomen | - | AHN + BGT | Bomen als punten met hoogte |

## 3D Tiles Specificatie

### Tileset.json Structuur

```json
{
  "asset": {
    "version": "1.1"
  },
  "geometricError": 500,
  "root": {
    "boundingVolume": {
      "region": [
        0.0854, 0.9116, 0.0897, 0.9147, 0, 100
      ]
    },
    "geometricError": 100,
    "refine": "ADD",
    "content": {
      "uri": "root.b3dm"
    },
    "children": [
      {
        "boundingVolume": {
          "region": [0.0854, 0.9116, 0.0875, 0.9130, 0, 50]
        },
        "geometricError": 10,
        "content": {
          "uri": "tiles/tile_0.b3dm"
        }
      }
    ]
  }
}
```

### Bounding Volumes

| Type | Parameters | Gebruik |
|------|-----------|--------|
| `region` | [west, south, east, north, minHeight, maxHeight] | Geografische data (radialen) |
| `box` | [center_x, center_y, center_z, ...halfAxes] | Lokale data |
| `sphere` | [center_x, center_y, center_z, radius] | Ronde objecten |

### Tile Formaten

| Formaat | Extensie | Beschrijving |
|---------|----------|-------------|
| Batched 3D Model | .b3dm | Meerdere 3D-objecten met attributen |
| Instanced 3D Model | .i3dm | Herhaalde objecten (bomen, lantaarnpalen) |
| Point Cloud | .pnts | Puntenwolk |
| Composite | .cmpt | Combinatie van bovenstaande |
| glTF | .glb/.gltf | Nieuw (3D Tiles 1.1), vervangt b3dm |

### Refinement Strategieen

| Strategie | Beschrijving | Gebruik |
|-----------|-------------|--------|
| `ADD` | Kindtegels worden toegevoegd aan ouder | Puntenwolken, terrein |
| `REPLACE` | Kindtegels vervangen ouder | Gebouwen, objecten |

### Geometric Error

De `geometricError` (in meters) bepaalt wanneer een tegel wordt verfijnd:
- Hoge waarde (bijv. 500): tegel wordt pas bij ver inzoomen geladen
- Lage waarde (bijv. 1): tegel wordt al snel vervangen door gedetailleerdere kinderen
- Waarde 0: bladtegel (geen verdere verfijning)

## Validatietools

### val3dity

[val3dity](https://github.com/tudelft3d/val3dity) valideert 3D geometrie:

```bash
# Installatie
pip install val3dity

# CityGML valideren
val3dity input.gml

# CityJSON valideren
val3dity input.city.json
```

### cjio (CityJSON CLI)

```bash
# Installatie
pip install cjio

# CityJSON info
cjio input.city.json info

# Converteren naar CityGML
cjio input.city.json save output.gml

# Subset maken (bbox)
cjio input.city.json subset --bbox 120000 487000 121000 488000 save output.city.json

# Statistieken
cjio input.city.json info --stats
```

### 3D Conversietools

| Tool | Van | Naar | Beschrijving |
|------|-----|------|-------------|
| cjio | CityJSON | GML, OBJ, STL | CityJSON CLI tool |
| citygml-tools | CityGML | CityJSON, diverse | Java-based converter |
| FME | Alles | Alles | Commerciele ETL tool |
| 3dfier | 2D + AHN | CityGML/CityJSON | Maakt LOD1 van 2D data + hoogte |
| GDAL/OGR | Diverse | Diverse | Open source geo-converter |

## 3D CRS-en

Voor 3D data in Nederland:

| CRS | EPSG-code | Beschrijving |
|-----|-----------|-------------|
| RD + NAP | EPSG:7415 | RD New horizontaal + NAP hoogte (samengesteld) |
| ETRS89 + NAP | EPSG:7423 | ETRS89 horizontaal + NAP hoogte |
| ETRS89 3D | EPSG:4937 | ETRS89 ellipsoidisch 3D |

NAP (Normaal Amsterdams Peil) is het Nederlandse hoogtesysteem. De 3D Basisvoorziening gebruikt EPSG:7415 (RD + NAP).

## Python 3D Workflow

```python
import json
from pathlib import Path

# CityJSON inlezen
with open("gebouwen.city.json") as f:
    cityjson = json.load(f)

print(f"Versie: {cityjson['version']}")
print(f"Aantal objecten: {len(cityjson['CityObjects'])}")

# Gebouwen filteren
gebouwen = {
    k: v for k, v in cityjson["CityObjects"].items()
    if v["type"] == "Building"
}

# Hoogte-statistieken
hoogtes = []
for geb_id, geb in gebouwen.items():
    h = geb.get("attributes", {}).get("measuredHeight")
    if h:
        hoogtes.append(h)

if hoogtes:
    print(f"Gemiddelde hoogte: {sum(hoogtes)/len(hoogtes):.1f} m")
    print(f"Maximale hoogte: {max(hoogtes):.1f} m")
```

## Repository Exploratie

```bash
# GeoBIM repo
gh api repos/Geonovum/GeoBIM/contents --jq '.[].name'

# Zoek naar 3D-gerelateerde repos
gh api orgs/Geonovum/repos --paginate \
  --jq '.[] | select(.name | test("3d|3D|city|bim"; "i")) | "\(.name): \(.description)"'

# Laatste wijzigingen GeoBIM
gh api repos/Geonovum/GeoBIM/commits \
  --jq '.[:5] | .[] | "\(.commit.committer.date) \(.commit.message | split("\n")[0])"'
```

## Gerelateerde Skills

| Skill | Relatie |
|-------|---------|
| `/geo-model` | NEN 3610 als basis voor 3D informatiemodellen |
| `/geo-api` | OGC services voor 3D data |
| `/geo-inspire` | INSPIRE gebouwen (LOD0-2) |
| `/geo-meta` | Metadata voor 3D datasets |
| `/geo` | Overzicht alle geo-standaarden |
