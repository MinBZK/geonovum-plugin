# INSPIRE Implementatie - Achtergrondinfo

Deze pagina bevat gedetailleerde informatie over data-thema mapping, transformatieregels en monitoring/rapportage.

## Data-thema Mapping: NL Sectormodellen naar INSPIRE

### Annex I Mappings

| INSPIRE Thema | NL Sectormodel | NL Bron | Transformatie |
|---------------|---------------|---------|---------------|
| Adressen (AD) | IMBAG | BAG (Kadaster) | BAG Nummeraanduiding → INSPIRE Address |
| Administratieve eenheden (AU) | Bestuurlijke Grenzen | Kadaster | Directe mapping |
| Kadastrale percelen (CP) | IMKAD | BRK (Kadaster) | BRK Perceel → INSPIRE CadastralParcel |
| Geografische namen (GN) | IMBRT | BRT (Kadaster) | Toponiemen → INSPIRE GeographicalName |
| Hydrografie (HY) | IMWA | NWB Vaarwegen (RWS) | Waterlopen → INSPIRE WatercourseLink |
| Beschermde gebieden (PS) | - | Natura2000 (LNV) | Gebieden → INSPIRE ProtectedSite |
| Transportnetwerken (TN) | NWB | NWB (RWS) | Wegsegmenten → INSPIRE RoadLink |

### Annex II Mappings

| INSPIRE Thema | NL Sectormodel | NL Bron | Transformatie |
|---------------|---------------|---------|---------------|
| Hoogte (EL) | AHN model | AHN (RWS) | Grid → INSPIRE ElevationGridCoverage |
| Bodemgebruik (LC) | LGN | BRP/LGN | Classificatie mapping |
| Orthobeeldvorming (OI) | - | Luchtfoto's (Kadaster) | TIFF/ECW → INSPIRE OrthoimageCoverage |
| Geologie (GE) | IMBRO | BRO (TNO) | Boringen → INSPIRE GeologicUnit |

### Annex III Mappings

| INSPIRE Thema | NL Sectormodel | NL Bron | Opmerkingen |
|---------------|---------------|---------|-------------|
| Gebouwen (BU) | IMBAG + IMGeo | BAG + BGT | BAG Pand → INSPIRE Building (2D footprint + attributen) |
| Bodem (SO) | IMBRO | BRO bodemkaart (WUR) | Bodemtypen mapping |
| Landgebruik (LU) | BRP model | BRP (RVO) | Gewaspercelen → INSPIRE ExistingLandUse |
| Spreiding bevolking (PD) | - | CBS (vierkantstatistieken) | Grid → INSPIRE StatisticalDistribution |
| Statistische eenheden (SU) | - | CBS wijken/buurten | Gebieden → INSPIRE StatisticalUnit |
| Nutsdiensten (US) | - | Diverse | Per sector verschillend |

## Transformatieregels

### Algemene Principes

1. **Identificatie**: NEN3610ID wordt vertaald naar INSPIRE `inspireId` (namespace + localId + versionId)
2. **Geometrie**: CRS transformatie van EPSG:28992 (RD New) naar EPSG:4258 (ETRS89)
3. **Codelijsten**: NL-waarden worden gemapped naar INSPIRE codelijsten
4. **Temporele attributen**: beginGeldigheid/eindGeldigheid worden vertaald naar INSPIRE temporeel model

### Voorbeeld Transformatie: BAG Adres naar INSPIRE Address

**Bron (BAG/NL):**
```json
{
  "nummeraanduiding": {
    "identificatie": "0363200012345678",
    "huisnummer": 10,
    "huisletter": "A",
    "postcode": "1012AB",
    "woonplaatsnaam": "Amsterdam",
    "openbareruimtenaam": "Damrak"
  }
}
```

**Doel (INSPIRE Address):**
```xml
<ad:Address gml:id="AD.Address.0363200012345678">
  <ad:inspireId>
    <base:Identifier>
      <base:localId>0363200012345678</base:localId>
      <base:namespace>NL.KAD.BAG</base:namespace>
    </base:Identifier>
  </ad:inspireId>
  <ad:position>
    <ad:GeographicPosition>
      <ad:geometry>
        <gml:Point srsName="urn:ogc:def:crs:EPSG::4258">
          <gml:pos>52.37403 4.89693</gml:pos>
        </gml:Point>
      </ad:geometry>
      <ad:specification>entrance</ad:specification>
    </ad:GeographicPosition>
  </ad:position>
  <ad:locator>
    <ad:AddressLocator>
      <ad:designator>
        <ad:LocatorDesignator>
          <ad:designator>10A</ad:designator>
          <ad:type>2</ad:type>
        </ad:LocatorDesignator>
      </ad:designator>
    </ad:AddressLocator>
  </ad:locator>
  <ad:component xlink:href="#TF.0363200012345678"/>
</ad:Address>
```

### CRS Transformatie

Bij INSPIRE-data moet de geometrie in EPSG:4258 (ETRS89) staan. Transformatie vanuit EPSG:28992 (RD New):

```bash
# ogr2ogr voor CRS-transformatie
ogr2ogr -f "GML" inspire_output.gml source_data.gml \
  -s_srs EPSG:28992 -t_srs EPSG:4258

# Python met pyproj
from pyproj import Transformer
t = Transformer.from_crs("EPSG:28992", "EPSG:4258", always_xy=True)
lon, lat = t.transform(121687, 487484)
```

## Monitoring en Rapportage

### Jaarlijkse Monitoring Indicatoren

| Indicator | Beschrijving | Doel |
|-----------|-------------|------|
| MDi1 | Metadata beschikbaarheid | 100% |
| MDi2 | Metadata conformiteit | 100% |
| DSi1 | Ruimtelijke datasets met metadata | 100% |
| DSi2 | Ruimtelijke datasets met view service | 100% |
| DSi3 | Ruimtelijke datasets met download service | 100% |
| NSi1 | Conformiteit metadata services | 100% |
| NSi2 | Conformiteit view services | 100% |
| NSi3 | Conformiteit download services | 100% |
| NSi4 | Services beschikbaarheid (uptime) | ≥99% |

### Monitoring Commando's

```bash
# Controleer INSPIRE-gerelateerde metadata in NGR
curl -s "https://www.nationaalgeoregister.nl/geonetwork/srv/dut/csw?\
service=CSW&version=2.0.2&request=GetRecords&\
ElementSetName=summary&resultType=hits&\
constraint=keyword=%27INSPIRE%27&constraintLanguage=CQL_TEXT"

# Controleer view service beschikbaarheid
curl -s -o /dev/null -w "%{http_code}" \
  "https://service.pdok.nl/brt/achtergrondkaart/wms/v2_0?service=WMS&request=GetCapabilities"

# Controleer download service beschikbaarheid
curl -s -o /dev/null -w "%{http_code}" \
  "https://service.pdok.nl/lv/bag/wfs/v2_0?service=WFS&request=GetCapabilities"
```

## INSPIRE Validator Details

### Beschikbare Testsuites (selectie)

| Testsuite | Test-ID | Beschrijving |
|-----------|---------|-------------|
| Metadata | EID-md-common | Gemeenschappelijke metadata-eisen |
| Metadata (datasets) | EID-md-datasets | Dataset-specifieke metadata |
| Metadata (services) | EID-md-services | Service-specifieke metadata |
| View Service (WMS) | EID-wms-view | WMS conformiteit |
| Download Service (WFS) | EID-wfs-download | WFS conformiteit |
| Download Service (Atom) | EID-atom-download | Atom feed conformiteit |
| GML encoding | EID-gml | GML 3.2.1 conformiteit |

### Validatie Workflow

1. **Metadata validatie** — eerst metadata op orde brengen
2. **Service validatie** — view en download services testen
3. **Data validatie** — GML data tegen INSPIRE schema testen
4. **Interoperabiliteit** — end-to-end test van discovery→view→download

### Lokale Validatie met ETF

De INSPIRE Validator is gebaseerd op het [ETF testing framework](https://github.com/etf-validator/etf-webapp). Je kunt een lokale instantie draaien:

```bash
# ETF lokaal draaien met Docker
docker run -d -p 8080:8080 \
  --name etf-validator \
  iide/etf-webapp:latest

# Toegang via http://localhost:8080/etf-webapp
```

## INSPIRE en OGC API Features

OGC API Features is inmiddels erkend als INSPIRE Good Practice voor download services. De implementatie-eisen:

1. Landingspagina met INSPIRE metadata-link
2. Collecties mappen op INSPIRE feature types
3. GeoJSON-output met INSPIRE-conforme attributen
4. CRS-ondersteuning voor EPSG:4258
5. Filtering op INSPIRE-attributen

```bash
# OGC API Features als INSPIRE download service
curl -s "https://api.pdok.nl/lv/bag/ogc/v1/collections" \
  -H "Accept: application/json" | python3 -m json.tool
```

## Repository Exploratie

```bash
# INSPIRE handreiking inhoud
gh api repos/Geonovum/inspire-handreiking/contents --jq '.[].name'

# Laatste wijzigingen
gh api repos/Geonovum/inspire-handreiking/commits \
  --jq '.[:5] | .[] | "\(.commit.committer.date) \(.commit.message | split("\n")[0])"'

# Zoek naar INSPIRE-gerelateerde repos
gh api orgs/Geonovum/repos --paginate \
  --jq '.[] | select(.name | test("inspire|INSPIRE"; "i")) | "\(.name): \(.description)"'

# Open issues
gh issue list --repo Geonovum/inspire-handreiking
```

## Gerelateerde Skills

| Skill | Relatie |
|-------|---------|
| `/geo-api` | Technische implementatie van OGC services |
| `/geo-meta` | INSPIRE-metadata (ISO 19115/19119, NGR) |
| `/geo-model` | NEN 3610 als basis voor INSPIRE-mapping |
| `/geo-3d` | 3D gebouwendata in INSPIRE (LoD) |
| `/geo` | Overzicht alle geo-standaarden |
