# Informatiemodellen - Achtergrondinfo

Deze pagina bevat aanvullende details over NEN 3610 UML-structuur, MIM-modelleringsregels, en een overzicht van alle sectormodellen.

## NEN 3610 UML Klassediagram

### Basisklassen

Het UML-model van NEN 3610 is opgebouwd rond de volgende kernklassen:

```
<<featureType>> GeoObject
  + identificatie: NEN3610ID [1..1]
  + domein: CharacterString [0..1]
  + tijdstipRegistratie: DateTime [1..1]
  + eindRegistratie: DateTime [0..1]
  + beginGeldigheid: DateTime [1..1]
  + eindGeldigheid: DateTime [0..1]
  + geometrie: GM_Object [1..*]
  + status: StatusType [0..1]

<<dataType>> NEN3610ID
  + namespace: CharacterString [1..1]
  + lokaalID: CharacterString [1..1]
  + versie: CharacterString [0..1]
```

### Specialisaties van GeoObject (NEN 3610:2022)

```
GeoObject
├── ReëelObject
│   + hoogte: Measure [0..1]
│   + materiaal: CharacterString [0..1]
│
└── VirtueleRuimte
    ├── RegistratieveRuimte
    │   + grens: GM_Surface [0..1]
    ├── FunctioneleRuimte
    │   + functie: CharacterString [1..1]
    ├── JuridischeRuimte
    │   + definitie: CharacterString [0..1]
    └── GeografischeRuimte
```

### Temporeel Model

NEN 3610 ondersteunt bitemporeel modelleren:

| Tijd-as | Eigenschap | Beschrijving |
|---------|-----------|-------------|
| Registratietijd | tijdstipRegistratie / eindRegistratie | Wanneer het object in de registratie is opgenomen/verwijderd |
| Geldigheidstijd | beginGeldigheid / eindGeldigheid | Wanneer de informatie in de werkelijkheid geldig is/was |

Dit maakt het mogelijk om de toestand van de registratie op elk moment in het verleden te reconstrueren (tijdreizen).

## MIM Modelleringsregels

### Stereotypen

| Stereotype | Beschrijving | Gebruik |
|-----------|-------------|--------|
| `<<objecttype>>` | Klasse van objecten met identiteit | Hoofdobjecten in het model |
| `<<attribuutsoort>>` | Eigenschap van een objecttype | Kenmerken van objecten |
| `<<relatiesoort>>` | Relatie tussen objecttypen | Associaties |
| `<<gegevensgroeptype>>` | Groep van samenhangende gegevens | Herbruikbare attributengroep |
| `<<enumeratie>>` | Vaste waardelijst | Toegestane waarden |
| `<<codelijst>>` | Uitbreidbare waardelijst | Dynamische waardelijsten |
| `<<datatype>>` | Samengesteld datatype | Structuren zonder identiteit |
| `<<keuze>>` | Keuze-element | Union types |
| `<<constraint>>` | Restrictie | OCL-expressies |

### Naamgevingsregels

| Element | Conventie | Voorbeeld |
|---------|----------|-----------|
| Objecttype | UpperCamelCase, enkelvoud | `Wegdeel`, `Waterdeel` |
| Attribuutsoort | lowerCamelCase | `bouwjaar`, `oppervlakte` |
| Relatiesoort | lowerCamelCase, werkwoord | `ligtIn`, `hoortBij` |
| Enumeratie | UpperCamelCase | `StatusType` |
| Enumeratiewaarde | lowerCamelCase of code | `inGebruik`, `nietInGebruik` |

### Cardinaliteit

| Notatie | Betekenis |
|---------|----------|
| `[1..1]` | Verplicht, precies 1 |
| `[0..1]` | Optioneel, maximaal 1 |
| `[1..*]` | Verplicht, 1 of meer |
| `[0..*]` | Optioneel, 0 of meer |

### Geometrietypen (ISO 19107)

| Type | Beschrijving | Dimensie |
|------|-------------|----------|
| GM_Point | Punt | 0D |
| GM_Curve | Lijn | 1D |
| GM_Surface | Vlak | 2D |
| GM_Solid | Volume | 3D |
| GM_MultiPoint | Meerdere punten | 0D |
| GM_MultiCurve | Meerdere lijnen | 1D |
| GM_MultiSurface | Meerdere vlakken | 2D |
| GM_Object | Willekeurig geometrietype | Variabel |

## Volledig Overzicht Sectormodellen

### Basisregistraties

| Sectormodel | Basisregistratie | Beheerder | NEN 3610 |
|-------------|-----------------|-----------|----------|
| IMBAG | BAG (Adressen en Gebouwen) | Kadaster | Ja |
| IMGeo/BGT | BGT (Grootschalige Topografie) | Geonovum/SVB-BGT | Ja |
| IMBRT | BRT (Topografie) | Kadaster | Ja |
| IMBRO | BRO (Ondergrond) | TNO | Ja |
| IMKAD | BRK (Kadaster) | Kadaster | Ja |

### Domeinmodellen

| Sectormodel | Domein | Beheerder | NEN 3610 |
|-------------|--------|-----------|----------|
| IMRO | Ruimtelijke Ordening | Geonovum | Ja |
| IMKL | Kabels en Leidingen | Kadaster/KLIC | Ja |
| IMWA | Waterbeheer | Informatiehuis Water | Ja |
| IMNAB | Natuur | BIJ12 | Ja |
| IMEV | Externe Veiligheid | RIVM | Ja |
| IMGEO+ | Optionele BGT-uitbreiding | Geonovum | Ja |
| IMBOR | Beheer Openbare Ruimte | CROW | Gedeeltelijk |

### Relatie tussen Sectormodellen en NEN 3610

Elk sectormodel breidt NEN 3610 uit door:
1. Objecttypen te specialiseren (overerving van GeoObject)
2. Domein-specifieke attributen toe te voegen
3. Domein-specifieke waardelijsten te definiëren
4. Domein-specifieke relaties te leggen

Voorbeeld: IMGeo specialiseert `FysiekObject` naar `Wegdeel`, `Waterdeel`, etc.

## Linked Data Implementatie

### NEN 3610 Ontologie

De NEN 3610 ontologie is beschikbaar als RDF/OWL:

```turtle
@prefix nen3610: <https://definities.geostandaarden.nl/nen3610-2022/nl/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .

nen3610:GeoObject a owl:Class ;
  rdfs:subClassOf geo:Feature ;
  rdfs:label "Geo-object"@nl .

nen3610:RegistratiefObject a owl:Class ;
  rdfs:subClassOf nen3610:GeoObject ;
  rdfs:label "Registratief object"@nl .

nen3610:FysiekObject a owl:Class ;
  rdfs:subClassOf nen3610:GeoObject ;
  rdfs:label "Fysiek object"@nl .

nen3610:identificatie a owl:ObjectProperty ;
  rdfs:domain nen3610:GeoObject ;
  rdfs:range nen3610:NEN3610ID ;
  rdfs:label "identificatie"@nl .
```

### SPARQL Voorbeelden

```sparql
# Alle gebouwen in een gemeente
PREFIX nen3610: <https://definities.geostandaarden.nl/nen3610-2022/nl/>
PREFIX geo: <http://www.opengis.net/ont/geosparql#>

SELECT ?gebouw ?geometrie
WHERE {
  ?gebouw a nen3610:Gebouw ;
          geo:hasGeometry/geo:asWKT ?geometrie .
}
LIMIT 100
```

### URI Dereferencing

Voor een werkende linked data-implementatie is content negotiation nodig:

```
HTTP GET https://data.example.nl/id/pand/0363100012345678
Accept: text/turtle
→ 303 See Other → https://data.example.nl/doc/pand/0363100012345678.ttl

HTTP GET https://data.example.nl/id/pand/0363100012345678
Accept: text/html
→ 303 See Other → https://data.example.nl/page/pand/0363100012345678
```

## Tooling

### Enterprise Architect

Enterprise Architect (Sparx Systems) is de standaardtool voor het opstellen van MIM-conforme informatiemodellen. Er is een MIM-profiel beschikbaar.

### Imvertor

[Imvertor](https://github.com/Imvertor/Imvertor-Maven) transformeert UML-modellen naar technische schema's:
- UML → XSD (GML application schema)
- UML → JSON Schema
- UML → RDF/SKOS/SHACL
- UML → Documentatie (HTML)

### ShapeChange

[ShapeChange](https://shapechange.net/) (interactive instruments) is een alternatieve tool voor het genereren van GML application schema's uit UML-modellen.

## Repository Exploratie

```bash
# NEN 3610 linked data repo
gh api repos/Geonovum/NEN3610-Linkeddata/contents --jq '.[].name'

# MIM werkomgeving
gh api repos/Geonovum/MIM-Werkomgeving/contents --jq '.[].name'

# IMGeo model
gh api repos/Geonovum/IMGeo/contents --jq '.[].name'

# Zoek naar informatiemodel-repos
gh api orgs/Geonovum/repos --paginate \
  --jq '.[] | select(.name | test("IM|NEN|MIM|model"; "i")) | "\(.name): \(.description)"'

# Laatste wijzigingen aan NEN 3610
gh api repos/Geonovum/NEN3610-Linkeddata/commits \
  --jq '.[:5] | .[] | "\(.commit.committer.date) \(.commit.message | split("\n")[0])"'
```

## Gerelateerde Skills

| Skill | Relatie |
|-------|---------|
| `/geo-api` | Ontsluiting van data conform deze modellen |
| `/geo-meta` | Metadata die verwijst naar informatiemodellen |
| `/geo-inspire` | INSPIRE-harmonisatie op basis van NEN 3610 |
| `/geo-3d` | 3D-extensies (CityGML) op NEN 3610 |
| `/geo` | Overzicht alle geo-standaarden |
