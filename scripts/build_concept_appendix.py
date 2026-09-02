"""Build the Concepts and notation appendix from marked source boxes.

Run from the book root with:
    python scripts/build_concept_appendix.py
"""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "appendix-concepts.qmd"
CHAPTER_PATTERN = re.compile(r"^(?:0[1-9]|[1-4][0-9])-.*\.qmd$")
OPENING_PATTERN = re.compile(r"^:::\s+\{(?P<attributes>[^}]*)\}\s*$")
ATTRIBUTE_PATTERN = re.compile(r'data-(?P<name>[a-z-]+)="(?P<value>[^"]*)"')


def extract_boxes(path: Path) -> list[dict[str, str]]:
    """Return concept boxes from one chapter, preserving their authored text."""
    entries: list[dict[str, str]] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    index = 0
    while index < len(lines):
        match = OPENING_PATTERN.match(lines[index])
        if not match or ".concept-box" not in match.group("attributes"):
            index += 1
            continue

        attributes = match.group("attributes")
        identifier_match = re.search(r"#([A-Za-z0-9_-]+)", attributes)
        values = {item.group("name"): item.group("value") for item in ATTRIBUTE_PATTERN.finditer(attributes)}
        body: list[str] = []
        index += 1
        while index < len(lines) and lines[index].strip() != ":::":
            body.append(lines[index])
            index += 1
        if index == len(lines):
            raise ValueError(f"Unclosed concept box in {path.name}")
        if not identifier_match or "term" not in values or "domain" not in values:
            raise ValueError(f"Concept box metadata missing in {path.name}")

        entries.append(
            {
                "id": identifier_match.group(1),
                "term": values["term"],
                "domain": values["domain"],
                "kind": "Distinction" if ".concept-distinction" in attributes else "Core concept",
                "chapter": path.name,
                "body": "\n".join(body).strip(),
            }
        )
        index += 1
    return entries


def main() -> None:
    entries = []
    for chapter in sorted(ROOT.iterdir()):
        if CHAPTER_PATTERN.match(chapter.name):
            entries.extend(extract_boxes(chapter))

    grouped: dict[str, list[dict[str, str]]] = {}
    for entry in entries:
        grouped.setdefault(entry["domain"], []).append(entry)

    output = [
        "---",
        'title: "Concepts and Notation"',
        'subtitle: "Definitions collated from the chapter source boxes"',
        "---",
        "",
        "This appendix is generated from the marked concept boxes in the chapters. Definitions remain authored at their first conceptual home.",
        "",
    ]
    for domain in sorted(grouped):
        output.extend([f"## {domain}", ""])
        for entry in sorted(grouped[domain], key=lambda item: item["term"].casefold()):
            chapter_title = re.sub(r"^0?([0-9]+)-", r"Chapter \1: ", entry["chapter"]).replace(".qmd", "").replace("-", " ")
            output.extend(
                [
                    f"### {entry['term']}",
                    "",
                    f"*{entry['kind']}; [{chapter_title}]({entry['chapter']}#{entry['id']}).*",
                    "",
                    entry["body"],
                    "",
                ]
            )

    OUTPUT.write_text("\n".join(output) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT.name} with {len(entries)} concept entries.")


if __name__ == "__main__":
    main()
