---
name: geo-model
description: >-
  Informatiemodellen voor geodata. Gebruik deze skill wanneer de gebruiker
  vraagt over 'NEN 3610', 'MIM', 'IMGeo', 'IMBAG', 'IMRO', 'IMKL',
  'informatiemodel', 'BGT', 'basismodel geo-informatie',
  'linked data geo', 'sectormodel', 'metamodel informatie modellering',
  'geo-informatiemodel', 'UML geo'.
model: sonnet
allowed-tools:
  - Bash(gh api *)
  - Bash(curl -s *)
  - WebFetch(*)
---

> **Let op:** De beschrijvingen in deze skill zijn informatieve samenvattingen — niet de officiële standaarden zelf. De definities op [forumstandaardisatie.nl](https://www.forumstandaardisatie.nl/open-standaarden) en [Geonovum](https://www.geonovum.nl) zijn altijd leidend. Overheidsorganisaties die generatieve AI inzetten dienen te voldoen aan het [Rijksbrede beleidskader voor generatieve AI](https://www.government.nl/documents/policy-notes/2025/01/31/government-wide-position-on-the-use-of-generative-ai). Zie [DISCLAIMER.md](../../DISCLAIMER.md).

# Informatiemodellen voor Geodata

**Agent-instructie:** Deze skill helpt bij het werken met Nederlandse geo-informatiemodellen, van het basismodel NEN 3610 tot sectormodellen. Gebruik de modelstructuur en voorbeelden om conforme data-uitwisseling te genereren. NEN 3610 is verplicht onder ['pas-toe-of-leg-uit'](https://www.forumstandaardisatie.nl/open-standaarden/geo-standaarden) van het Forum Standaardisatie.

[NEN 3610](https://docs.geostandaarden.nl/nen3610/) is het basismodel voor geo-informatie in Nederland. Alle sectorale informatiemodellen (IMGeo, IMBAG, IMRO, etc.) zijn hiervan afgeleid. Het [Metamodel Informatie Modellering (MIM)](https://docs.geostandaarden.nl/mim/def-st-mim-20220217/) beschrijft hoe informatiemodellen opgesteld moeten worden. Geonovum beheert beide standaarden.

## Standaarden Overzicht

| Standaard | Type | Doel | Forum status |
|-----------|------|------|-------------|
| NEN 3610:2022 | Basismodel | Fundament voor alle geo-informatiemodellen | Verplicht |
| MIM 1.2 | Metamodel | Regels voor het opstellen van informatiemodellen | Aanbevolen |
| IMGeo 2.2 / BGT | Sectormodel | Grootschalige topografie | Verplicht (als sectormodel) |
| IMBAG | Sectormodel | Adressen en gebouwen | Verplicht (als sectormodel) |
| IMRO | Sectormodel | Ruimtelijke ordening | Verplicht (als sectormodel) |
| IMKL | Sectormodel | Kabels en leidingen | Verplicht (als sectormodel) |

## Repositories

| Repository | Beschrijving |
|-----------|-------------|
| [Geonovum/NEN3610-Linkeddata](https://github.com/Geonovum/NEN3610-Linkeddata) | NEN 3610 linked data profiel |
| [Geonovum/MIM-Werkomgeving](https://github.com/Geonovum/MIM-Werkomgeving) | Metamodel Informatie Modellering |
| [Geonovum/IMGeo](https://github.com/Geonovum/IMGeo) | Informatiemodel Geografie (BGT/IMGeo) |
| [Geonovum/imro](https://github.com/Geonovum/imro) | Informatiemodel Ruimtelijke Ordening |
| [Geonovum/imkl](https://github.com/Geonovum/imkl) | Informatiemodel Kabels en Leidingen |

## NEN 3610 — Basismodel Geo-informatie

NEN 3610:2022 definieert de basisstructuur waar alle Nederlandse geo-informatiemodellen op voortbouwen. De kern bestaat uit een klassenhierarchie met `GeoObject` als basis, onderverdeeld in `ReëelObject` (tastbaar, waarneembaar) en `VirtueleRuimte` (conceptueel, niet-tastbaar).

### Kernconcepten

```
GeoObject (abstract)
├── ReëelObject (tastbaar, waarneembaar)
│   ├── Gebouw (IMBAG)
│   ├── Kunstwerk (bruggen, tunnels)
│   ├── Begroeiing
│   ├── Water
│   └── Wegdeel (IMGeo)
└── VirtueleRuimte (conceptueel, niet-tastbaar)
    ├── Registratieve ruimte
    │   ├── Bestuurlijk gebied (gemeenten, provincies)
    │   └── Nummeraanduiding (adressen)
    ├── Functionele ruimte
    │   ├── Openbare ruimte (wegen, pleinen)
    │   └── Infrastructuur
    ├── Juridische ruimte
    │   └── Planologisch gebied (IMRO)
    └── Geografische ruimte
```

### Verplichte Eigenschappen van GeoObject

| Eigenschap | Type | Beschrijving |
|-----------|------|-------------|
| identificatie | NEN3610ID | Unieke identificatie (namespace + lokaalId + versie) |
| domein | CharacterString | Domein/sectormodel (bijv. "NL.IMGeo") |
| tijdstipRegistratie | DateTime | Wanneer geregistreerd |
| eindRegistratie | DateTime | Wanneer beëindigd (optioneel) |
| beginGeldigheid | DateTime | Begin geldigheidsperiode |
| eindGeldigheid | DateTime | Einde geldigheidsperiode (optioneel) |
| geometrie | GM_Object | Ruimtelijke geometrie |

### NEN3610ID Structuur

```
NEN3610ID:
  namespace: "NL.IMBAG.Pand"
  lokaalID: "0363100012345678"
  versie: "2024-01-15T10:30:00"
```

### GML Voorbeeld (NEN 3610)

```xml
<nen3610:GeoObject gml:id="pand.0363100012345678">
  <nen3610:identificatie>
    <nen3610:NEN3610ID>
      <nen3610:namespace>NL.IMBAG.Pand</nen3610:namespace>
      <nen3610:lokaalID>0363100012345678</nen3610:lokaalID>
    </nen3610:NEN3610ID>
  </nen3610:identificatie>
  <nen3610:beginGeldigheid>2020-03-15</nen3610:beginGeldigheid>
  <nen3610:tijdstipRegistratie>2020-03-15T10:30:00</nen3610:tijdstipRegistratie>
  <nen3610:geometrie>
    <gml:Polygon srsName="urn:ogc:def:crs:EPSG::28992">
      <gml:exterior>
        <gml:LinearRing>
          <gml:posList>120000 487000 120010 487000 120010 487010 120000 487010 120000 487000</gml:posList>
        </gml:LinearRing>
      </gml:exterior>
    </gml:Polygon>
  </nen3610:geometrie>
</nen3610:GeoObject>
```

### JSON-LD Voorbeeld (NEN 3610 Linked Data)

```json
{
  "@context": {
    "nen3610": "https://definities.geostandaarden.nl/nen3610-2022/nl/",
    "geo": "http://www.opengis.net/ont/geosparql#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "https://data.example.nl/id/pand/0363100012345678",
  "@type": "nen3610:Gebouw",
  "nen3610:identificatie": {
    "nen3610:namespace": "NL.IMBAG.Pand",
    "nen3610:lokaalID": "0363100012345678"
  },
  "nen3610:beginGeldigheid": {
    "@value": "2020-03-15",
    "@type": "xsd:date"
  },
  "geo:hasGeometry": {
    "@type": "geo:Geometry",
    "geo:asWKT": "POLYGON((120000 487000, 120010 487000, 120010 487010, 120000 487010, 120000 487000))"
  }
}
```

## MIM — Metamodel Informatie Modellering

MIM beschrijft de regels voor het opstellen van informatiemodellen. Het definieert vier modellagen:

| Laag | Naam | Beschrijving |
|------|------|-------------|
| Niveau 1 | Conceptueel model | Betekenis van begrippen (ontologie) |
| Niveau 2 | Logisch model | Structuur (UML klassen, attributen, relaties) |
| Niveau 3 | Fysiek/technisch model | Implementatie (XSD, JSON Schema, database) |
| Niveau 4 | Data/instanties | Daadwerkelijke data-uitwisseling |

### MIM Modelelementen

| Element | Beschrijving | UML-notatie |
|---------|-------------|-------------|
| Objecttype | Klasse van objecten | UML Class |
| Attribuutsoort | Eigenschap van een objecttype | UML Attribute |
| Relatiesoort | Relatie tussen objecttypen | UML Association |
| Gegevensgroep | Groep van attributen | UML DataType |
| Enumeratie | Lijst van toegestane waarden | UML Enumeration |
| Keuze | Keuze tussen typen | UML Union |

## Sectormodellen

### IMGeo / BGT (Grootschalige Topografie)

De Basisregistratie Grootschalige Topografie (BGT) gebruikt het informatiemodel IMGeo.

| Objectklasse | Voorbeelden | Geometrietype |
|-------------|-------------|---------------|
| Wegdeel | Rijbaan, fietspad, voetpad | Vlak |
| OnbegroeidTerreindeel | Verharding, zand | Vlak |
| BegroeidTerreindeel | Gras, bos, heide | Vlak |
| Waterdeel | Sloot, rivier, meer | Vlak |
| Pand | Gebouwen | Vlak |
| OverigBouwwerk | Schuur, overkapping | Vlak |
| Kunstwerkdeel | Brug, tunnel, sluis | Vlak/Lijn |

### IMBAG (Adressen en Gebouwen)

| Objecttype | Beschrijving |
|-----------|-------------|
| Woonplaats | Officieel aangewezen woonplaats |
| OpenbareRuimte | Straatnaam |
| Nummeraanduiding | Huisnummer + toevoegingen |
| Pand | Fysiek gebouw |
| Verblijfsobject | Eenheid met woonfunctie |
| Standplaats | Plaats voor woonwagen |
| Ligplaats | Plaats voor woonboot |

## URI-strategie voor Linked Data

Geonovum definieert een URI-strategie voor het publiceren van geo-objecten als linked data:

```
https://data.{domein}.nl/id/{objecttype}/{identificatie}
```

Voorbeelden:
- `https://data.kadaster.nl/id/pand/0363100012345678`
- `https://data.bgt.nl/id/wegdeel/G0344.abc123`
- `https://data.rws.nl/id/kunstwerk/BR-0001`

## Veelvoorkomende Problemen

| Probleem | Oorzaak | Oplossing |
|----------|---------|-----------|
| Verkeerde namespace in GML | Niet het juiste sectormodel-schema | Gebruik de juiste namespace-URI voor het sectormodel |
| NEN3610ID niet uniek | Geen unieke combinatie namespace+lokaalID | Zorg voor unieke lokaalID binnen de namespace |
| Geometrie in verkeerd CRS | CRS niet gespecificeerd of verkeerd | Specificeer `srsName` in GML, gebruik EPSG:28992 voor NL |
| MIM-model niet conform | Verkeerde stereotypen of cardinaliteit | Valideer tegen MIM-specificatie, gebruik Enterprise Architect profiel |
| Linked data URIs niet dereferenceable | URIs lossen niet op | Implementeer content negotiation, 303 redirects |
| Sectormodel onbekend | Niet afgeleid van NEN 3610 | Controleer of het model NEN 3610 als basis gebruikt |

## Cross-referenties

- Gebruik `/geo-api` voor het ontsluiten van data conform deze modellen via WFS/OGC API.
- Gebruik `/geo-meta` voor metadata die naar deze informatiemodellen verwijst.
- Gebruik `/geo-inspire` voor INSPIRE data-harmonisatie op basis van NEN 3610.
- Gebruik `/geo-3d` voor 3D-extensies op NEN 3610 (CityGML).

## Achtergrondinfo

Zie [reference.md](reference.md) voor NEN 3610 UML-details, MIM-modelleringsregels, en een uitgebreid overzicht van sectormodellen.
