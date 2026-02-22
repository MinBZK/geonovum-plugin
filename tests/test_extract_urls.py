"""Tests voor scripts/extract_urls.py."""

from pathlib import Path

from extract_urls import (
    classify_url,
    clean_url,
    extract_all,
    extract_urls_from_file,
    is_excluded,
    normalize_github_url,
)

# --- clean_url() ---


class TestCleanUrl:
    def test_trailing_punctuatie(self):
        assert clean_url("https://example.com/path.") == "https://example.com/path"
        assert clean_url("https://example.com/path,") == "https://example.com/path"
        assert clean_url("https://example.com/path;") == "https://example.com/path"

    def test_gebalanceerde_haakjes(self):
        assert clean_url("https://example.com/path)") == "https://example.com/path"
        assert clean_url("https://example.com/path(1)") == "https://example.com/path(1)"

    def test_trailing_slash(self):
        assert clean_url("https://example.com/path/") == "https://example.com/path"


# --- is_excluded() ---


class TestIsExcluded:
    def test_example_domains(self):
        assert is_excluded("https://example.com/test") is True
        assert is_excluded("https://api.example.com/v1") is True

    def test_localhost(self):
        assert is_excluded("http://localhost:8080") is True
        assert is_excluded("http://127.0.0.1:3000") is True

    def test_namespace_urls(self):
        assert is_excluded("https://www.opengis.net/gml/3.2") is True

    def test_echte_urls_niet_uitgesloten(self):
        assert is_excluded("https://github.com/Geonovum/ogc-checker") is False
        assert is_excluded("https://docs.geostandaarden.nl/nen3610/nldp") is False
        assert is_excluded("https://www.forumstandaardisatie.nl/open-standaarden") is False


# --- classify_url() ---


class TestClassifyUrl:
    def test_github_repo(self):
        url = "https://github.com/Geonovum/ogc-checker"
        assert classify_url(url) == "github_repo"

    def test_geonovum_doc(self):
        url = "https://docs.geostandaarden.nl/nen3610/nldp"
        assert classify_url(url) == "geonovum_doc"

    def test_forum(self):
        url = "https://www.forumstandaardisatie.nl/open-standaarden/geo-standaarden"
        assert classify_url(url) == "forum"

    def test_pdok(self):
        url = "https://www.pdok.nl/introductie"
        assert classify_url(url) == "pdok"

    def test_geonovum_site(self):
        url = "https://www.geonovum.nl/geo-standaarden"
        assert classify_url(url) == "geonovum_site"

    def test_onbekende_url(self):
        assert classify_url("https://www.google.com") is None


# --- normalize_github_url() ---


class TestNormalizeGithubUrl:
    def test_tags_verwijderd(self):
        assert (
            normalize_github_url("https://github.com/Geonovum/ogc-checker/tags")
            == "https://github.com/Geonovum/ogc-checker"
        )

    def test_tree_main_verwijderd(self):
        assert (
            normalize_github_url("https://github.com/Geonovum/ogc-checker/tree/main")
            == "https://github.com/Geonovum/ogc-checker"
        )

    def test_passthrough_base_url(self):
        url = "https://github.com/Geonovum/ogc-checker"
        assert normalize_github_url(url) == url

    def test_passthrough_niet_geonovum(self):
        url = "https://github.com/other-org/some-repo/tags"
        assert normalize_github_url(url) == url


# --- extract_urls_from_file() ---


class TestExtractUrlsFromFile:
    def test_sample_skill(self):
        fixture = Path(__file__).parent / "fixtures" / "sample_skill.md"
        results = extract_urls_from_file(fixture)

        urls = [r["url"] for r in results]

        assert "https://github.com/Geonovum/ogc-checker" in urls
        assert "https://docs.geostandaarden.nl/nen3610/nldp" in urls
        assert "https://www.forumstandaardisatie.nl/open-standaarden/geo-standaarden" in urls

        excluded_urls = [u for u in urls if "example.com" in u or "your-domain" in u]
        assert excluded_urls == []

    def test_types_correct(self):
        fixture = Path(__file__).parent / "fixtures" / "sample_skill.md"
        results = extract_urls_from_file(fixture)

        type_map = {r["url"]: r["type"] for r in results}
        assert type_map["https://github.com/Geonovum/ogc-checker"] == "github_repo"
        assert type_map["https://docs.geostandaarden.nl/nen3610/nldp"] == "geonovum_doc"
        assert (
            type_map["https://www.forumstandaardisatie.nl/open-standaarden/geo-standaarden"]
            == "forum"
        )


# --- extract_all() deduplicatie ---


class TestExtractAll:
    def test_deduplicatie(self, tmp_path):
        skill_dir = tmp_path / "skills" / "test-skill"
        skill_dir.mkdir(parents=True)

        url = "https://github.com/Geonovum/ogc-checker"

        (skill_dir / "SKILL.md").write_text(
            f"---\nname: test\ndescription: test\nmodel: sonnet\n---\n\nRepo: {url}\n"
        )
        (skill_dir / "reference.md").write_text(f"# Ref\n\nZie ook: {url}\n")

        results = extract_all(tmp_path / "skills")
        urls = [r["url"] for r in results]

        assert urls.count(url) == 1

    def test_lege_directory(self, tmp_path):
        skill_dir = tmp_path / "skills"
        skill_dir.mkdir()
        assert extract_all(skill_dir) == []
