#!/usr/bin/env python3
"""Lightweight release checks for the generated Quantactic landing site."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LANGS = {"en": "en", "es": "es", "ja": "ja", "ko": "ko", "zh-Hans": "zh-Hans"}
APP_STORE_URL = "https://apps.apple.com/app/id6795746505"
OLD_BRAND = "Quant" + "fox"
FORBIDDEN_COPY = ("SAVE 0%", "SAVE 50%", "See the market.", "Test the range.", "Decide with context.", "experimental sampled")
APP_ADS_RECORD = "google.com, pub-6317048078552057, DIRECT, f08c47fec0942fa0"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.lang = ""
        self.title = ""
        self._in_title = False
        self.images: list[tuple[str, str]] = []
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "html":
            self.lang = values.get("lang", "") or ""
        elif tag == "title":
            self._in_title = True
        elif tag == "img":
            self.images.append((values.get("src", "") or "", values.get("alt", "") or ""))
        elif tag == "a":
            self.links.append(values.get("href", "") or "")

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title += data


def fail(message: str) -> None:
    raise RuntimeError(message)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_pages() -> None:
    expected = [ROOT / "index.html", ROOT / "privacy.html", ROOT / "terms.html"]
    for code in LANGS:
        expected.extend(ROOT / code / name for name in ("index.html", "privacy.html", "terms.html"))
    for path in expected:
        if not path.is_file():
            fail(f"missing generated page: {path.relative_to(ROOT)}")

    for path in expected:
        parser = PageParser()
        text = read(path)
        parser.feed(text)
        relative = path.relative_to(ROOT)
        code = "en" if len(relative.parts) == 1 else relative.parts[0]
        if parser.lang != LANGS[code]:
            fail(f"{relative}: expected html lang {LANGS[code]!r}, found {parser.lang!r}")
        if not parser.title.strip():
            fail(f"{relative}: missing title")
        if "privacy.html" not in parser.links or "terms.html" not in parser.links:
            fail(f"{relative}: missing local Privacy / Terms navigation")
        for src, alt in parser.images:
            if not src:
                fail(f"{relative}: image has no source")
            if not src.endswith("quant-app-icon.png") and not alt.strip():
                fail(f"{relative}: non-brand image has empty alt text: {src}")
            if src.startswith(("assets/", "../assets/")):
                asset = (path.parent / src).resolve()
                if not asset.is_file():
                    fail(f"{relative}: missing referenced asset {src}")

        if path.name == "index.html":
            if APP_STORE_URL not in text:
                fail(f"{relative}: wrong or missing App Store URL")
            for phrase in ("What changed", "Model track record", "Quantactic Pro Annual"):
                if phrase not in text and code == "en":
                    fail(f"{relative}: missing required product copy: {phrase}")


def check_text() -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() in {".png", ".jpg", ".jpeg", ".ico"}:
            continue
        if path == Path(__file__).resolve():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if OLD_BRAND.lower() in text.lower():
            fail(f"obsolete brand reference in {path.relative_to(ROOT)}")
        lowered = text.lower()
        for phrase in FORBIDDEN_COPY:
            if phrase.lower() in lowered:
                fail(f"outdated or forbidden copy in {path.relative_to(ROOT)}: {phrase}")
        if re.search(r"\b(?:todo|lorem\s+ipsum|tbd)\b", lowered):
            fail(f"placeholder content in {path.relative_to(ROOT)}")


def check_app_ads() -> None:
    path = ROOT / "app-ads.txt"
    if not path.is_file():
        fail("missing root app-ads.txt")
    if read(path).strip() != APP_ADS_RECORD:
        fail("app-ads.txt does not exactly match the authorized AdMob seller record")


def main() -> int:
    try:
        check_pages()
        check_text()
        check_app_ads()
    except RuntimeError as error:
        print(f"verify_site: FAIL: {error}", file=sys.stderr)
        return 1
    print("verify_site: PASS — pages, locales, assets, app-ads.txt, App Store URL, pricing, and brand checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
