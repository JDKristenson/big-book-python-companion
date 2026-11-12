"""Render this map's editable Excalidraw elements without third-party packages."""

import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "learning-map.excalidraw"
TARGET = ROOT / "learning-map.svg"


def render():
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    assert data["type"] == "excalidraw" and data["version"] == 2
    assert not data.get("files"), "External/embedded files are not supported"
    elements = [e for e in data["elements"] if not e.get("isDeleted")]
    assert len({e["id"] for e in elements}) == len(elements), "Duplicate IDs"
    out = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 760" role="img" aria-labelledby="title desc">',
        '<title id="title">Unofficial book companion: learning and reference map</title>',
        '<desc id="desc">External book resources lead to local guides and quick references. Practice resources are not included. This is not proof of completed exercises or code lineage.</desc>',
        '<rect width="1000" height="760" fill="white"/>',
        '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z" fill="#495057"/></marker></defs>',
    ]
    for e in elements:
        assert e["type"] in {"rectangle", "text", "arrow"}, "Unsupported element"
        assert e.get("angle", 0) == 0, "Rotated elements are unsupported"
        x, y, w, h = (e[k] for k in ("x", "y", "width", "height"))
        assert 0 <= x <= x + w <= 1000 and 0 <= y <= y + h <= 760
        color = html.escape(e["strokeColor"], quote=True)
        if e["type"] == "rectangle":
            assert e["strokeStyle"] in {"solid", "dashed"}
            dash = ' stroke-dasharray="8 5"' if e["strokeStyle"] == "dashed" else ""
            fill = html.escape(e["backgroundColor"], quote=True)
            out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{color}" stroke-width="2"{dash}/>')
        elif e["type"] == "text":
            assert e["textAlign"] == "left" and e.get("containerId") is None
            size = e["fontSize"]
            lines = e["text"].splitlines()
            out.append(f'<text x="{x}" y="{y + size}" font-family="Arial, sans-serif" font-size="{size}" fill="{color}">')
            for i, line in enumerate(lines):
                out.append(f'<tspan x="{x}" dy="{0 if i == 0 else size * e["lineHeight"]}">{html.escape(line)}</tspan>')
            out.append('</text>')
        else:
            assert e.get("startBinding") is None and e.get("endBinding") is None
            assert e.get("startArrowhead") is None and e.get("endArrowhead") == "arrow"
            assert len(e["points"]) == 2, "Only straight arrows supported"
            (x1, y1), (x2, y2) = e["points"]
            out.append(f'<line x1="{x+x1}" y1="{y+y1}" x2="{x+x2}" y2="{y+y2}" stroke="{color}" stroke-width="2" marker-end="url(#arrow)"/>')
    return "\n".join(out + ['</svg>', ''])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if saved SVG differs")
    args = parser.parse_args()
    svg = render()
    if args.check:
        if not TARGET.exists() or TARGET.read_text(encoding="utf-8") != svg:
            parser.exit(1, "Preview is stale; run python3 docs/render_learning_map.py\n")
        print("PASS: editable map structure and matching SVG")
    else:
        TARGET.write_text(svg, encoding="utf-8")
        print("Rendered docs/learning-map.svg")


if __name__ == "__main__":
    main()
