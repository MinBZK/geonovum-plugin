# OGC API Services - Achtergrondinfo

Deze pagina bevat aanvullende technische details over OGC-protocollen, coördinaatreferentiesystemen en de PDOK-servicecatalogus.

## Coördinaatreferentiesystemen (CRS)

### Belangrijkste CRS-en in Nederland

| CRS | EPSG-code | Gebruik | Coördinaatvolgorde |
|-----|-----------|---------|-------------------|
| RD New (Amersfoort) | EPSG:28992 | Nederlandse kaarten en data | x, y (oost, noord) in meters |
| ETRS89 / UTM zone 31N | EPSG:25831 | INSPIRE, Europese data | x, y (oost, noord) in meters |
| WGS 84 | EPSG:4326 | GPS, internationaal gebruik | lat, lon (breedte, lengte) in graden |
| WGS 84 (lon/lat) | CRS84 | OGC API standaard CRS | lon, lat (lengte, breedte) in graden |
| ETRS89 geografisch | EPSG:4258 | INSPIRE verplicht | lat, lon (breedte, lengte) in graden |

### Coördinaatvolgorde

Let op: de coördinaatvolgorde verschilt per protocol en CRS.

- **WMS 1.3.0**: Volgt de CRS-definitie. Voor EPSG:4326 is dat lat/lon (y,x). Voor EPSG:28992 is dat x,y.
- **WFS 2.0**: Volgt de CRS-definitie, tenzij anders geconfigureerd.
- **OGC API Features**: Gebruikt standaard CRS84 (lon/lat). Andere CRS via `crs` parameter.
- **GeoJSON (RFC 7946)**: Altijd lon/lat (WGS 84).

### CRS-transformatie met PROJ

```bash
# RD New naar WGS 84
echo "155000 463000" | cs2cs EPSG:28992 EPSG:4326

# WGS 84 naar RD New
echo "52.15517 5.38720" | cs2cs EPSG:4326 EPSG:28992
```

### Python CRS-transformatie

```python
from pyproj import Transformer

# RD New naar WGS 84
transformer = Transformer.from_crs("EPSG:28992", "EPSG:4326", always_xy=True)
lon, lat = transformer.transform(155000, 463000)
print(f"WGS 84: {lat:.5f}, {lon:.5f}")

# WGS 84 naar RD New
transformer_inv = Transformer.from_crs("EPSG:4326", "EPSG:28992", always_xy=True)
x, y = transformer_inv.transform(5.38720, 52.15517)
print(f"RD New: {x:.0f}, {y:.0f}")
```

## OGC Protocol Details

### WMS 1.3.0 Parameters

| Parameter | GetCapabilities | GetMap | GetFeatureInfo |
|-----------|----------------|--------|---------------|
| service | WMS | WMS | WMS |
| version | 1.3.0 | 1.3.0 | 1.3.0 |
| request | GetCapabilities | GetMap | GetFeatureInfo |
| layers | - | Verplicht | Verplicht |
| crs | - | Verplicht | Verplicht |
| bbox | - | Verplicht (minx,miny,maxx,maxy) | Verplicht |
| width/height | - | Verplicht (pixels) | Verplicht |
| format | - | image/png, image/jpeg | application/json, text/xml |
| query_layers | - | - | Verplicht |
| i/j | - | - | Verplicht (pixel positie) |
| info_format | - | - | application/json |

### WFS 2.0 Parameters

| Parameter | GetCapabilities | GetFeature | DescribeFeatureType |
|-----------|----------------|------------|-------------------|
| service | WFS | WFS | WFS |
| version | 2.0.0 | 2.0.0 | 2.0.0 |
| request | GetCapabilities | GetFeature | DescribeFeatureType |
| typeName | - | Verplicht | Verplicht |
| count | - | Max features | - |
| outputFormat | - | application/json | - |
| bbox | - | Optioneel (filter) | - |
| Filter | - | Optioneel (XML) | - |
| sortBy | - | Optioneel | - |

### OGC API Features Endpoints

| Endpoint | Methode | Beschrijving |
|----------|---------|-------------|
| `/` | GET | Landing page |
| `/conformance` | GET | Conformance classes |
| `/collections` | GET | Lijst van collecties |
| `/collections/{id}` | GET | Collectie metadata |
| `/collections/{id}/items` | GET | Features (GeoJSON) |
| `/collections/{id}/items/{featureId}` | GET | Enkel feature |
| `/api` | GET | OpenAPI specificatie |

Query parameters voor `/items`:
- `limit` — maximaal aantal features (standaard 10, max verschilt per service)
- `bbox` — ruimtelijke filter (lon_min,lat_min,lon_max,lat_max)
- `datetime` — temporeel filter (ISO 8601)
- `crs` — gewenst CRS (standaard CRS84)
- Additionele property-filters afhankelijk van service

## PDOK Servicecatalogus

### Veelgebruikte PDOK-services

| Service | Type | URL |
|---------|------|-----|
| BRT Achtergrondkaart | WMS | `https://service.pdok.nl/brt/achtergrondkaart/wms/v2_0` |
| BRT Achtergrondkaart | WMTS | `https://service.pdok.nl/brt/achtergrondkaart/wmts/v2_0` |
| BAG (adressen/gebouwen) | WFS | `https://service.pdok.nl/lv/bag/wfs/v2_0` |
| BAG (adressen/gebouwen) | OGC API | `https://api.pdok.nl/lv/bag/ogc/v1` |
| BGT (grootschalige topografie) | WFS | `https://api.pdok.nl/lv/bgt/ogc/v1` |
| BRK (kadastrale kaart) | WMS | `https://service.pdok.nl/kadaster/kadastralekaart/wms/v5_0` |
| CBS Wijken/Buurten | WFS | `https://service.pdok.nl/cbs/wijkenbuurten/2024/wfs/v1_0` |
| Luchtfoto (actueel) | WMS | `https://service.pdok.nl/hwh/luchtfotorgb/wms/v1_0` |
| AHN (hoogtedata) | WCS | `https://service.pdok.nl/rws/ahn/wcs/v1_0` |
| Bestuurlijke grenzen | WFS | `https://service.pdok.nl/kadaster/bestuurlijkegebieden/wfs/v1_0` |

### PDOK API-key

Voor intensief gebruik van PDOK-services is een API-key beschikbaar. Aanvragen via [pdok.nl](https://www.pdok.nl/). De key wordt meegegeven als HTTP-header:

```bash
curl -s -H "X-Api-Key: <jouw-key>" \
  "https://api.pdok.nl/lv/bag/ogc/v1/collections/pand/items?limit=100"
```

## Repository Exploratie

```bash
# ogc-checker broncode bekijken
gh api repos/Geonovum/ogc-checker/contents --jq '.[].name'

# Laatste commits
gh api repos/Geonovum/ogc-checker/commits \
  --jq '.[:5] | .[] | "\(.commit.committer.date) \(.commit.message | split("\n")[0])"'

# Open issues
gh issue list --repo Geonovum/ogc-checker

# Zoek naar OGC-gerelateerde repos
gh api orgs/Geonovum/repos --paginate \
  --jq '.[] | select(.name | test("ogc|wms|wfs|api"; "i")) | "\(.name): \(.description)"'
```

## Gerelateerde Skills

| Skill | Relatie |
|-------|---------|
| `/geo-meta` | Metadata voor services (ISO 19115, CSW) |
| `/geo-model` | Informatiemodellen achter de data (NEN 3610) |
| `/geo-inspire` | INSPIRE-conforme services |
| `/geo-3d` | 3D-services en -data |
| `/ls-api` | ADR geo-module voor REST API richtlijnen |
| `/geo` | Overzicht alle geo-standaarden |
