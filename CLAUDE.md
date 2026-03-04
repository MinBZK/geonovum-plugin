# Geonovum Plugin - Werkinstructies

## Taal

Alle content in deze repo is in het **Nederlands**: skill descriptions, body tekst, commit messages, en documentatie. Gebruik Nederlands tenzij de gebruiker expliciet in het Engels communiceert.

## Repo structuur

- `.claude-plugin/plugin.json` - Plugin manifest (versie wordt automatisch gebumpt door release-please)
- `skills/geo/SKILL.md` - Meta-skill (overzicht, routing)
- `skills/geo-<domein>/SKILL.md` - Domein-skills (5 stuks)
- `skills/geo-<domein>/reference.md` - Achtergrondinfo per domein
- `scripts/extract_urls.py` - Extraheert monitorbare URLs uit skill-bestanden
- `scripts/monitor_content.py` - Detecteert content-wijzigingen (GitHub API + HTTP checks)
- `tests/` - Pytest tests voor de scripts
- `.github/workflows/ci.yml` - CI: structuurvalidatie, ruff, markdownlint, pytest
- `.github/workflows/release-please.yml` - Automatische releases via conventional commits
- `.github/workflows/monitoring-content.yml` - Dagelijkse content monitoring (07:00 UTC)
- `.github/workflows/monitoring-links.yml` - Dagelijkse link checks met lychee (06:00 UTC)
- `.github/workflows/labeler.yml` - Automatische PR-labels op basis van gewijzigde bestanden

## Conventies voor skills

### SKILL.md opbouw
1. YAML frontmatter met `name`, `description`, `model: sonnet`, `allowed-tools`
2. Agent-instructie (2-3 zinnen, vetgedrukt: wanneer wordt deze skill gebruikt, wat moet de agent doen)
3. Korte intro (wat is dit domein, link naar Forum Standaardisatie)
4. Standaarden overzicht (per standaard: wat, waarom, hoe gebruiken)
5. Repository tabel(len)
6. Implementatievoorbeelden - realistische code en configuratie
7. Veelvoorkomende problemen - troubleshooting, foutmeldingen
8. Achtergrondinfo (verwijzing naar reference.md)

Elke skill moet genoeg bevatten zodat een agent standaard-conforme code kan genereren zonder externe bronnen op te halen. Encyclopedische uitleg hoort in `reference.md`, niet in `SKILL.md`.

### Repository tabel format

```markdown
| Repository | Beschrijving |
|-----------|-------------|
| [Naam](https://github.com/Geonovum/REPO) | Omschrijving |
```

### reference.md patroon
Achtergrondkennis die niet direct nodig is voor code-generatie wordt verplaatst naar `reference.md`. Denk aan:
- Architectuurbeschrijvingen en conceptuele uitleg
- OGC specificatiedetails en protocol-uitleg
- INSPIRE technische richtlijnen
- CRS-transformatieregels en coördinatenstelsels
- Exploratie commando's (`gh api`, `curl`, `ogr2ogr`)

### Description triggers
Descriptions bevatten zowel Nederlandse als technische Engelse triggerwoorden zodat de skill bij relevante vragen wordt geactiveerd.

### Allowed tools
Standaard set:
- `Bash(gh api *)`, `Bash(curl -s *)`, `WebFetch(*)`
- `Bash(ogr2ogr *)`, `Bash(ogrinfo *)` voor GDAL/OGR diagnostiek

### Maximale omvang
SKILL.md bestanden mogen maximaal **500 regels** bevatten. Grotere content hoort in `reference.md`.

## Content strategie

**On-demand ophalen, niet opslaan.** De GitHub repos van Geonovum zijn de bron van waarheid. Skills bevatten samenvattingen en structuur; actuele content wordt live opgehaald via `gh api` of `WebFetch`.

## GitHub organisatie

Alle repos staan onder: `https://github.com/Geonovum/`
Gepubliceerde standaarden: `https://docs.geostandaarden.nl/`
Geonovum website: `https://www.geonovum.nl/`

## Development

### Vereisten

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) als package manager
- `uv sync` om dependencies te installeren

### Linting en tests

```bash
uv run ruff check scripts/ tests/       # Linting
uv run ruff format --check scripts/ tests/  # Format check
uv run pytest -v                         # Tests
```

Pre-commit hooks draaien automatisch ruff + markdownlint bij elke commit.

### CI/CD

**Branch protection** is actief op `main` met verplichte status checks: `validate`, `lint-python`, `lint-markdown`, `test-python`. Directe pushes naar main zijn geblokkeerd — alle wijzigingen gaan via PRs.

**Releases** worden automatisch beheerd door [release-please](https://github.com/googleapis/release-please):
1. Gebruik [Conventional Commits](https://www.conventionalcommits.org/): `feat:`, `fix:`, `chore:`, `docs:`
2. release-please maakt automatisch een Release PR aan met gebumpte versies en CHANGELOG
3. Bij merge van Release PR: GitHub Release + git tag + versie gebumpt in `plugin.json`, `pyproject.toml`, `publiccode.yml`

## Cross-references

- `/geo-api` verwijst naar `/ls-api` (uit skills-standaarden) voor de ADR geo-module
- `/ls-api` kan terugverwijzen naar `/geonovum` voor diepere geo-standaarden

## Plugin testen

Verificatievragen:
- "Welke geo-standaarden zijn er?" -> moet `/geo` triggeren
- "Welke geo-API standaard moet ik gebruiken?" -> moet `/geo-api` triggeren
- "Hoe publiceer ik metadata in het NGR?" -> moet `/geo-meta` triggeren
- "Wat is NEN 3610?" -> moet `/geo-model` triggeren
- "Hoe voldoe ik aan INSPIRE?" -> moet `/geo-inspire` triggeren
- "Hoe werk ik met CityGML?" -> moet `/geo-3d` triggeren
