---
name: geo-meta
description: >-
  Metadata standaarden voor geodata. Gebruik deze skill wanneer de gebruiker
  vraagt over 'metadata', 'ISO 19115', 'ISO 19119', 'CSW',
  'NGR', 'nationaal georegister', 'Nationaal Georegister',
  'DCAT geo', 'metadata profiel', 'metadata publiceren',
  'metadata validatie', 'geodata catalogus', 'discovery service'.
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

# Metadata voor Geodata

**Agent-instructie:** Deze skill helpt bij het opstellen, publiceren en valideren van metadata conform het Nederlands profiel op ISO 19115/19119. Gebruik de CSW-voorbeelden voor het doorzoeken van het NGR. Metadata (ISO 19115/19119) is verplicht onder ['pas-toe-of-leg-uit'](https://www.forumstandaardisatie.nl/open-standaarden/geo-standaarden) van het Forum Standaardisatie.

Metadata beschrijft geodata en -services zodat ze vindbaar, bruikbaar en beoordeelbaar zijn. Het [Nationaal Georegister (NGR)](https://www.nationaalgeoregister.nl/) is het centrale portaal voor het zoeken en publiceren van metadata over Nederlandse geodatasets en -services. Geonovum beheert het [Nederlands profiel op ISO 19115/19119](https://docs.geostandaarden.nl/md/mdprofiel-iso19115/) als basis voor alle metadata.

## Standaarden Overzicht

| Standaard | Type | Doel | Forum status |
|-----------|------|------|-------------|
| ISO 19115:2003/19115-1:2014 | Metadata | Beschrijving van datasets | Verplicht |
| ISO 19119:2005 | Metadata | Beschrijving van services | Verplicht |
| NL profiel ISO 19115 | Profiel | Nederlandse invulling van ISO 19115 | Verplicht |
| CSW 2.0.2 | Protocol | Catalogue Service for the Web — zoeken/harvesten | Geen eigen Forum status |
| DCAT | Vocabulaire | Data Catalog Vocabulary, geo-extensie | Aanbevolen |

## Repositories

| Repository | Beschrijving | Licentie |
|-----------|-------------|--------|
| [Geonovum/Metadata-ISO19115](https://github.com/Geonovum/Metadata-ISO19115) | Nederlands profiel op ISO 19115 voor geografie | CC-BY-4.0 |
| [Geonovum/Metadata-handreiking](https://github.com/Geonovum/Metadata-handreiking) | Handreiking voor metadata | CC-BY-4.0 |

## Nederlands Profiel ISO 19115

Het [Nederlands profiel](https://docs.geostandaarden.nl/md/mdprofiel-iso19115/) specificeert welke metadata-elementen verplicht, conditioneel of optioneel zijn voor Nederlandse geodatasets.

### Verplichte elementen (dataset)

| Element | XPath (vereenvoudigd) | Beschrijving |
|---------|----------------------|-------------|
| Titel | `identificationInfo/citation/title` | Naam van de dataset |
| Samenvatting | `identificationInfo/abstract` | Korte beschrijving |
| Datum | `identificationInfo/citation/date` | Publicatie-/revisiedatum |
| Verantwoordelijke organisatie | `identificationInfo/pointOfContact` | Naam, rol, contactinfo |
| Trefwoorden | `identificationInfo/descriptiveKeywords` | Minstens 1 trefwoord |
| Beperkingen | `identificationInfo/resourceConstraints` | Gebruikscondities |
| Ruimtelijk referentiesysteem | `referenceSystemInfo` | CRS (bijv. EPSG:28992) |
| Ruimtelijke resolutie | `identificationInfo/spatialResolution` | Schaalniveau of grondresolutie |
| Taal | `identificationInfo/language` | Taal van de dataset (dut/nld) |
| Onderwerp | `identificationInfo/topicCategory` | ISO-categorie |
| Omgrenzende rechthoek | `identificationInfo/extent/geographicElement` | Bbox van de dataset |
| Temporele dekking | `identificationInfo/extent/temporalElement` | Tijdsperiode |
| Distributie-informatie | `distributionInfo` | Toegang (URL, formaat) |
| Metadata-standaard | `metadataStandardName` | "ISO 19115" |
| Metadata-datum | `dateStamp` | Datum van metadata |
| Metadata-taal | `language` | dut of nld |

### Voorbeeld Metadata XML (NL profiel)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<gmd:MD_Metadata
  xmlns:gmd="http://www.isotc211.org/2005/gmd"
  xmlns:gco="http://www.isotc211.org/2005/gco"
  xmlns:gml="http://www.opengis.net/gml/3.2">

  <gmd:language>
    <gmd:LanguageCode codeList="http://www.loc.gov/standards/iso639-2/"
      codeListValue="dut">Nederlands</gmd:LanguageCode>
  </gmd:language>

  <gmd:metadataStandardName>
    <gco:CharacterString>ISO 19115</gco:CharacterString>
  </gmd:metadataStandardName>
  <gmd:metadataStandardVersion>
    <gco:CharacterString>Nederlands metadata profiel op ISO 19115 voor geografie 2.1.0</gco:CharacterString>
  </gmd:metadataStandardVersion>

  <gmd:identificationInfo>
    <gmd:MD_DataIdentification>
      <gmd:citation>
        <gmd:CI_Citation>
          <gmd:title>
            <gco:CharacterString>Basisregistratie Adressen en Gebouwen (BAG)</gco:CharacterString>
          </gmd:title>
          <gmd:date>
            <gmd:CI_Date>
              <gmd:date><gco:Date>2024-01-15</gco:Date></gmd:date>
              <gmd:dateType>
                <gmd:CI_DateTypeCode codeList="http://www.isotc211.org/2005/resources/codeList.xml#CI_DateTypeCode"
                  codeListValue="publication">publicatie</gmd:CI_DateTypeCode>
              </gmd:dateType>
            </gmd:CI_Date>
          </gmd:date>
        </gmd:CI_Citation>
      </gmd:citation>

      <gmd:abstract>
        <gco:CharacterString>De BAG bevat gegevens over alle adressen en gebouwen in Nederland.</gco:CharacterString>
      </gmd:abstract>

      <gmd:pointOfContact>
        <gmd:CI_ResponsibleParty>
          <gmd:organisationName>
            <gco:CharacterString>Kadaster</gco:CharacterString>
          </gmd:organisationName>
          <gmd:role>
            <gmd:CI_RoleCode codeList="http://www.isotc211.org/2005/resources/codeList.xml#CI_RoleCode"
              codeListValue="owner">eigenaar</gmd:CI_RoleCode>
          </gmd:role>
        </gmd:CI_ResponsibleParty>
      </gmd:pointOfContact>

      <gmd:descriptiveKeywords>
        <gmd:MD_Keywords>
          <gmd:keyword><gco:CharacterString>adressen</gco:CharacterString></gmd:keyword>
          <gmd:keyword><gco:CharacterString>gebouwen</gco:CharacterString></gmd:keyword>
        </gmd:MD_Keywords>
      </gmd:descriptiveKeywords>

      <gmd:extent>
        <gmd:EX_Extent>
          <gmd:geographicElement>
            <gmd:EX_GeographicBoundingBox>
              <gmd:westBoundLongitude><gco:Decimal>3.37</gco:Decimal></gmd:westBoundLongitude>
              <gmd:eastBoundLongitude><gco:Decimal>7.21</gco:Decimal></gmd:eastBoundLongitude>
              <gmd:southBoundLatitude><gco:Decimal>50.75</gco:Decimal></gmd:southBoundLatitude>
              <gmd:northBoundLatitude><gco:Decimal>53.47</gco:Decimal></gmd:northBoundLatitude>
            </gmd:EX_GeographicBoundingBox>
          </gmd:geographicElement>
        </gmd:EX_Extent>
      </gmd:extent>
    </gmd:MD_DataIdentification>
  </gmd:identificationInfo>
</gmd:MD_Metadata>
```

## CSW (Catalogue Service for the Web)

CSW is het OGC-protocol voor het zoeken en harvesten van metadata. Het NGR biedt een CSW-endpoint.

```bash
# CSW GetCapabilities — NGR
curl -s "https://www.nationaalgeoregister.nl/geonetwork/srv/dut/csw?\
service=CSW&request=GetCapabilities&version=2.0.2" | head -80

# CSW GetRecords — zoeken op trefwoord
curl -s "https://www.nationaalgeoregister.nl/geonetwork/srv/dut/csw?\
service=CSW&version=2.0.2&request=GetRecords&\
ElementSetName=summary&resultType=results&\
maxRecords=5&\
constraint=AnyText+like+%25bag%25&\
constraintLanguage=CQL_TEXT&\
outputSchema=http://www.isotc211.org/2005/gmd"

# CSW GetRecordById — specifiek record ophalen
curl -s "https://www.nationaalgeoregister.nl/geonetwork/srv/dut/csw?\
service=CSW&version=2.0.2&request=GetRecordById&\
ElementSetName=full&\
outputSchema=http://www.isotc211.org/2005/gmd&\
Id=aa3b5e6e-7baa-40c0-8972-3353e927ec2f"
```

### Python CSW-query

```python
from owslib.csw import CatalogueServiceWeb

# Verbinding met NGR
csw = CatalogueServiceWeb(
    "https://www.nationaalgeoregister.nl/geonetwork/srv/dut/csw"
)
print(f"Service: {csw.identification.title}")

# Zoeken op trefwoord
from owslib.fes import PropertyIsLike

query = PropertyIsLike("csw:AnyText", "%hoogtebestand%")
csw.getrecords2(constraints=[query], maxrecords=10)

for rec_id, rec in csw.records.items():
    print(f"  {rec.title}")
    print(f"    ID: {rec_id}")
    print(f"    Type: {rec.type}")
```

## DCAT voor Geodata

DCAT (Data Catalog Vocabulary) wordt steeds meer gebruikt naast ISO 19115. Het profiel GeoDCAT-AP biedt een mapping van ISO 19115 naar DCAT.

### Verhouding ISO 19115 en DCAT

| ISO 19115 element | DCAT property |
|-------------------|--------------|
| Titel | `dct:title` |
| Samenvatting | `dct:description` |
| Verantwoordelijke organisatie | `dct:publisher` |
| Trefwoorden | `dcat:keyword` |
| Datum (publicatie) | `dct:issued` |
| Distributie (URL) | `dcat:distribution` |
| Ruimtelijke dekking (bbox) | `dct:spatial` |
| Temporele dekking | `dct:temporal` |

## Veelvoorkomende Problemen

| Probleem | Oorzaak | Oplossing |
|----------|---------|-----------|
| Metadata wordt niet gevonden in NGR | Niet gepubliceerd of niet geharvest | Publiceer via NGR-editor of eigen CSW, wacht op harvest-cyclus |
| Validatiefout: ontbrekende elementen | Verplichte elementen niet ingevuld | Controleer NL profiel verplichte elementen (zie tabel) |
| Validatiefout: verkeerd datumformaat | Niet-ISO datum (YYYY-MM-DD) | Gebruik `<gco:Date>2024-01-15</gco:Date>` |
| Metadata niet zichtbaar voor INSPIRE | INSPIRE-trefwoorden ontbreken | Voeg INSPIRE thematrefwoord toe (GEMET thesaurus) |
| CSW retourneert 0 resultaten | Verkeerde CQL-syntax | Gebruik `AnyText like '%term%'` (procent-teken als wildcard) |
| Harvesting mislukt | Endpoint onbereikbaar of te traag | Controleer CSW-endpoint beschikbaarheid, timeout-instellingen |

## Publiceren in het NGR

Stappen om metadata te publiceren in het [Nationaal Georegister](https://www.nationaalgeoregister.nl/):

1. **Maak metadata** conform het NL profiel ISO 19115 (gebruik bovenstaand XML-sjabloon)
2. **Valideer** de metadata (zie reference.md voor validatietools)
3. **Publiceer** via:
   - Direct invoeren in de NGR-editor (webinterface)
   - Eigen CSW-endpoint aanbieden dat door NGR geharvest wordt
   - Uploaden via GeoNetwork REST API
4. **Controleer** of de metadata vindbaar is via CSW of de webinterface

## Cross-referenties

- Gebruik `/geo-api` voor de services waar deze metadata naar verwijst.
- Gebruik `/geo-inspire` voor INSPIRE-specifieke metadata-eisen.
- Gebruik `/geo-model` voor informatiemodellen waarnaar metadata kan verwijzen.

## Achtergrondinfo

Zie [reference.md](reference.md) voor de volledige lijst van metadata-elementen, validatieregels, en het NGR-publicatieworkflow in detail.
