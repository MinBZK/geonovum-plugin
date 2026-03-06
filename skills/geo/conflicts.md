# Geonovum Geo-standaarden - Bronconflicten

Geconstateerd: 2026-03-05

## Ontbrekende licentie in GitHub-repositories

De meeste Geonovum-repositories bevatten geen expliciet `LICENSE`-bestand in GitHub. De gepubliceerde standaarden op [docs.geostandaarden.nl](https://docs.geostandaarden.nl/) vermelden een Creative Commons-licentie via de ReSpec-configuratie. De meeste standaarden gebruiken CC-BY-4.0, maar sommige (zoals inspire-handreiking en imro) gebruiken CC-BY-ND-4.0. Uitzondering is [ogc-checker](https://github.com/Geonovum/ogc-checker) dat een EUPL-1.2-licentie heeft.

| Repository | GitHub LICENSE | Gepubliceerde licentie | Status |
|-----------|--------------|----------------------|--------|
| [Geonovum/ogc-checker](https://github.com/Geonovum/ogc-checker) | EUPL-1.2 | N.v.t. (tooling) | OK |
| [Geonovum/NEN3610-Linkeddata](https://github.com/Geonovum/NEN3610-Linkeddata) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [Geonovum/Metadata-ISO19115](https://github.com/Geonovum/Metadata-ISO19115) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [Geonovum/inspire-handreiking](https://github.com/Geonovum/inspire-handreiking) | Geen | CC-BY-ND-4.0 (ReSpec) | Discrepantie |
| [Geonovum/IMGeo](https://github.com/Geonovum/IMGeo) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [Geonovum/MIM-Werkomgeving](https://github.com/Geonovum/MIM-Werkomgeving) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [Geonovum/GeoBIM](https://github.com/Geonovum/GeoBIM) | Geen | Geen (geen ReSpec config aanwezig) | Niet gespecificeerd |
| [Geonovum/Metadata-handreiking](https://github.com/Geonovum/Metadata-handreiking) | Geen | CC-BY-4.0 (ReSpec) | Discrepantie |
| [Geonovum/imro](https://github.com/Geonovum/imro) | Geen | CC-BY-ND-4.0 (ReSpec) | Discrepantie |
| [Geonovum/imkl](https://github.com/Geonovum/imkl) | Geen | Geen (geen ReSpec config aanwezig) | Niet gespecificeerd |

### Aandachtspunt

De licentie-informatie in de SKILL.md is gebaseerd op de gepubliceerde ReSpec-documenten. Het verdient aanbeveling dat de repositories expliciet een `LICENSE`-bestand toevoegen om juridische duidelijkheid te bieden, met name voor hergebruik onder artikel 15n Auteurswet (text and data mining exceptie).
