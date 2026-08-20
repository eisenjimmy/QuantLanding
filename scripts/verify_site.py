#!/usr/bin/env python3
"""Release checks for the generated Quantactic marketing and legal site."""

from __future__ import annotations

import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://quantactic.app"
LANGS = {"en": "en", "es": "es", "ja": "ja", "ko": "ko", "zh-Hans": "zh-Hans"}
APP_STORE_URL = "https://apps.apple.com/app/id6795746505"
APP_ADS_RECORD = "google.com, pub-6317048078552057, DIRECT, f08c47fec0942fa0"
CURRENT_APP_ICON_SHA256 = "b953883a3cd7716324eacaa4bd400d4abb4389e47fdf1e3045ff9c85dac8b653"
SCREENSHOTS = (
    "01-private-ai.png",
    "02-forecast.png",
    "03-model-proof.png",
    "04-signals.png",
    "05-macro.png",
    "06-advanced-chart.png",
)
FORBIDDEN_COPY = (
    "SAVE 0%",
    "SAVE 50%",
    "See the market. Test the range.",
    "experimental sampled",
    "Where required, Quantactic uses Google’s consent messaging",
)
FORBIDDEN_VISUALS = ("#ffab2e", "#ff9f1c", "--orange", "orange-black", "legacy-logo")


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.lang = ""
        self.title = ""
        self.description = ""
        self.canonical = ""
        self.alternates: dict[str, str] = {}
        self.images: list[tuple[str, str]] = []
        self.links: list[str] = []
        self.meta: dict[tuple[str, str], str] = {}
        self.json_ld: list[str] = []
        self._in_title = False
        self._in_json_ld = False
        self._json_chunks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        if tag == "html":
            self.lang = values.get("lang", "")
        elif tag == "title":
            self._in_title = True
        elif tag == "img":
            self.images.append((values.get("src", ""), values.get("alt", "")))
        elif tag == "a":
            self.links.append(values.get("href", ""))
        elif tag == "meta":
            if values.get("name"):
                self.meta[("name", values["name"])] = values.get("content", "")
            if values.get("property"):
                self.meta[("property", values["property"])] = values.get("content", "")
            if values.get("name") == "description":
                self.description = values.get("content", "")
        elif tag == "link":
            rel = values.get("rel", "").split()
            if "canonical" in rel:
                self.canonical = values.get("href", "")
            if "alternate" in rel and values.get("hreflang"):
                self.alternates[values["hreflang"]] = values.get("href", "")
        elif tag == "script" and values.get("type") == "application/ld+json":
            self._in_json_ld = True
            self._json_chunks = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
        elif tag == "script" and self._in_json_ld:
            self.json_ld.append("".join(self._json_chunks))
            self._in_json_ld = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title += data
        if self._in_json_ld:
            self._json_chunks.append(data)


def fail(message: str) -> None:
    raise RuntimeError(message)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def page_paths() -> list[Path]:
    paths = [ROOT / "index.html", ROOT / "privacy.html", ROOT / "terms.html"]
    for code in LANGS:
        paths.extend(ROOT / code / name for name in ("index.html", "privacy.html", "terms.html"))
    return paths


def expected_public_url(code: str, name: str) -> str:
    if code == "en":
        return f"{BASE_URL}/" if name == "index.html" else f"{BASE_URL}/{name}"
    return f"{BASE_URL}/{code}/" if name == "index.html" else f"{BASE_URL}/{code}/{name}"


def resolve_local_asset(page: Path, src: str) -> Path | None:
    if not src or src.startswith(("http://", "https://", "mailto:", "#")):
        return None
    return (page.parent / src.split("?", 1)[0]).resolve()


def check_pages() -> None:
    for path in page_paths():
        if not path.is_file():
            fail(f"missing generated page: {path.relative_to(ROOT)}")
        parser = PageParser()
        text = read(path)
        parser.feed(text)
        relative = path.relative_to(ROOT)
        code = "en" if len(relative.parts) == 1 else relative.parts[0]
        if parser.lang != LANGS[code]:
            fail(f"{relative}: expected html lang {LANGS[code]!r}, found {parser.lang!r}")
        if not parser.title.strip() or len(parser.title.strip()) > 70:
            fail(f"{relative}: missing or overlong title")
        if not parser.description.strip() or len(parser.description.strip()) > 200:
            fail(f"{relative}: missing or overlong meta description")
        if parser.canonical != expected_public_url(code, path.name):
            fail(f"{relative}: bad canonical {parser.canonical!r}")
        expected_hreflangs = set(LANGS.values()) | {"x-default"}
        if set(parser.alternates) != expected_hreflangs:
            fail(f"{relative}: incomplete hreflang set")
        if parser.alternates["x-default"] != expected_public_url("en", path.name):
            fail(f"{relative}: incorrect x-default URL")
        if "privacy.html" not in parser.links or "terms.html" not in parser.links:
            fail(f"{relative}: missing local Privacy / Terms navigation")
        for required in (
            ("name", "robots"),
            ("property", "og:title"),
            ("property", "og:description"),
            ("property", "og:image"),
            ("name", "twitter:card"),
            ("name", "twitter:image"),
        ):
            if not parser.meta.get(required):
                fail(f"{relative}: missing social/search metadata {required[1]}")
        for src, alt in parser.images:
            if not src:
                fail(f"{relative}: image has no source")
            if "quantactic-mark.png" not in src and not alt.strip():
                fail(f"{relative}: content image has empty alt text: {src}")
            asset = resolve_local_asset(path, src)
            if asset and not asset.is_file():
                fail(f"{relative}: missing referenced asset {src}")

        if path.name == "index.html":
            if APP_STORE_URL not in text:
                fail(f"{relative}: wrong or missing App Store URL")
            expected_campaign = {f"assets/campaign/{code}/{name}" for name in SCREENSHOTS}
            normalized_sources = {src.removeprefix("../") for src, _ in parser.images}
            if not expected_campaign.issubset(normalized_sources):
                fail(f"{relative}: not all localized campaign screenshots are present")
            if "quantactic-mark.png" not in text or any("quant-app-icon.png" in src for src, _ in parser.images):
                fail(f"{relative}: page chrome must use only the current blue Q mark")
            if len(parser.json_ld) != 1:
                fail(f"{relative}: expected one JSON-LD block")
            try:
                graph = json.loads(parser.json_ld[0])["@graph"]
            except (json.JSONDecodeError, KeyError, TypeError) as error:
                fail(f"{relative}: invalid JSON-LD: {error}")
            types = {node.get("@type") for node in graph}
            required_types = {"Organization", "WebSite", "SoftwareApplication", "FAQPage"}
            if not required_types.issubset(types):
                fail(f"{relative}: incomplete JSON-LD graph")


def check_assets() -> None:
    current_icon = ROOT / "assets/quant-app-icon.png"
    if sha256(current_icon) != CURRENT_APP_ICON_SHA256:
        fail("quant-app-icon.png is not the approved current blue app icon")
    expected_sizes = {
        ROOT / "assets/quant-app-icon.png": (1024, 1024),
        ROOT / "assets/quantactic-mark.png": (512, 512),
        ROOT / "assets/favicon-32.png": (32, 32),
        ROOT / "assets/apple-touch-icon.png": (180, 180),
    }
    for path, size in expected_sizes.items():
        if not path.is_file():
            fail(f"missing brand asset {path.relative_to(ROOT)}")
        with Image.open(path) as image:
            if image.size != size:
                fail(f"{path.relative_to(ROOT)}: expected {size}, found {image.size}")
    if not (ROOT / "favicon.ico").is_file():
        fail("missing root favicon.ico")
    dither = ROOT / "assets/quantactic-blue-dither-field.png"
    if not dither.is_file():
        fail("missing blue dither background art")
    with Image.open(dither) as image:
        if image.mode != "RGBA":
            fail("dither background must retain a transparent alpha channel")
    for code in LANGS:
        for filename in SCREENSHOTS:
            path = ROOT / "assets/campaign" / code / filename
            if not path.is_file():
                fail(f"missing localized campaign screenshot {path.relative_to(ROOT)}")
            with Image.open(path) as image:
                if image.size != (552, 1200):
                    fail(f"{path.relative_to(ROOT)}: expected 552x1200, found {image.size}")


def check_discovery_files() -> None:
    required = ("robots.txt", "sitemap.xml", "site.webmanifest", "llms.txt", "app-ads.txt")
    for name in required:
        if not (ROOT / name).is_file():
            fail(f"missing discovery file {name}")
    if read(ROOT / "app-ads.txt").strip() != APP_ADS_RECORD:
        fail("app-ads.txt does not exactly match the authorized AdMob seller record")
    if f"Sitemap: {BASE_URL}/sitemap.xml" not in read(ROOT / "robots.txt"):
        fail("robots.txt does not declare the production sitemap")
    manifest = json.loads(read(ROOT / "site.webmanifest"))
    if manifest.get("name") != "Quantactic" or len(manifest.get("icons", [])) < 3:
        fail("site.webmanifest is incomplete")
    tree = ET.parse(ROOT / "sitemap.xml")
    namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = {node.text for node in tree.findall("s:url/s:loc", namespace)}
    expected = {expected_public_url("en", name) for name in ("index.html", "privacy.html", "terms.html")}
    expected |= {
        expected_public_url(code, name)
        for code in ("es", "ja", "ko", "zh-Hans")
        for name in ("index.html", "privacy.html", "terms.html")
    }
    if urls != expected:
        fail("sitemap URL set does not match the canonical public pages")


def check_repository_text() -> None:
    text_extensions = {".css", ".html", ".md", ".py", ".txt", ".xml", ".webmanifest"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.name.startswith("._"):
            fail(f"AppleDouble metadata found: {path.relative_to(ROOT)}")
        if path.suffix.lower() not in text_extensions or path == Path(__file__).resolve():
            continue
        try:
            text = read(path)
        except UnicodeDecodeError:
            continue
        lowered = text.lower()
        for phrase in FORBIDDEN_COPY:
            if phrase.lower() in lowered:
                fail(f"outdated or unverified copy in {path.relative_to(ROOT)}: {phrase}")
        if re.search(r"\b(?:todo|lorem\s+ipsum|tbd)\b", lowered):
            fail(f"placeholder content in {path.relative_to(ROOT)}")
    css = read(ROOT / "css/site.css").lower()
    for token in FORBIDDEN_VISUALS:
        if token in css:
            fail(f"legacy orange/black visual token remains in site.css: {token}")
    if "quantactic-blue-dither-field.png" not in css:
        fail("site.css does not use the transparent blue dither art")


def main() -> int:
    try:
        check_pages()
        check_assets()
        check_discovery_files()
        check_repository_text()
    except (RuntimeError, OSError, ValueError, json.JSONDecodeError, ET.ParseError) as error:
        print(f"verify_site: FAIL: {error}", file=sys.stderr)
        return 1
    print("verify_site: PASS — 18 pages, 5 locales, 30 campaign images, current blue branding, discovery metadata, and rewarded-ad copy verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
