#!/usr/bin/env python3
"""Render the buildless homepage from its HTML template and verified publication data."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]


def render_publications(publications):
    groups = {}
    for paper in sorted(publications, key=lambda p: p["date"], reverse=True):
        groups.setdefault(paper["year"], []).append(paper)
    blocks = []
    for year, papers in groups.items():
        blocks.append(f'<div class="publication-year-group" data-year="{year}">')
        count_label = f"{len(papers)} {'paper' if len(papers) == 1 else 'papers'}"
        blocks.append(f'<h3 class="year-heading">{year}<span>{count_label}</span></h3>')
        blocks.append('<div class="year-papers">')
        for p in papers:
            authors = ", ".join(f'<strong>{escape(a)}</strong>' if a == "Ruiqiang Xiao" else escape(a) for a in p["authors"])
            links = "".join(f'<a href="{escape(url, quote=True)}" target="_blank" rel="noopener noreferrer">{escape(label)} <span aria-hidden="true">↗</span></a>' for label, url in p["links"].items())
            badge = f'<span class="publication-badge">{escape(p["badge"])}</span>' if p.get("badge") else ""
            status = f'<span class="publication-status">{escape(p["status"])}</span>' if p.get("status") else ""
            topics = escape(json.dumps(p["topics"]), quote=True)
            paper_url = escape(p["links"]["Paper"], quote=True)
            blocks.append(f'''<article class="publication" id="paper-{escape(p['id'])}" data-topics="{topics}">
  <a class="publication-image" href="{escape(p['image'], quote=True)}" target="_blank" rel="noopener noreferrer" title="View full-size figure" aria-label="View figure for {escape(p['title'], quote=True)}">
    <img src="{escape(p['image'], quote=True)}" alt="{escape(p['image_alt'], quote=True)}" width="640" height="360" loading="lazy">
  </a>
  <div class="publication-copy">
    <div class="publication-meta"><span class="publication-venue">{escape(p['venue'])}</span>{badge}{status}</div>
    <h4><a href="{paper_url}" target="_blank" rel="noopener noreferrer">{escape(p['title'])}</a></h4>
    <p class="publication-authors">{authors}</p>
    <p class="publication-summary">{escape(p['summary'])}</p>
    <div class="work-links">{links}</div>
  </div>
</article>''')
        blocks.extend(["</div>", "</div>"])
    return "\n".join(blocks)


def main():
    publications = json.loads((ROOT / "data/publications.json").read_text())
    ids = [p["id"] for p in publications]
    if len(ids) != len(set(ids)):
        raise ValueError("Publication IDs must be unique")
    for p in publications:
        if str(p["year"]) != p["date"][:4]:
            raise ValueError(f"Year/date mismatch: {p['id']}")
        if not (ROOT / p["image"].lstrip("/")).is_file():
            raise FileNotFoundError(p["image"])
    template = (ROOT / "templates/homepage.html").read_text()
    if template.count("{{PUBLICATIONS}}") != 1:
        raise ValueError("Expected exactly one publication placeholder")
    output = template.replace("{{PUBLICATIONS}}", render_publications(publications))
    (ROOT / "index.html").write_text(output)
    print(f"Rendered index.html with {len(publications)} publications.")


if __name__ == "__main__":
    main()
