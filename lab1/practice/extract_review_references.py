#!/usr/bin/env python3
import re
import csv
import os
import sys
from typing import List, Tuple

# Heuristic: journals that are predominantly reviews
REVIEW_JOURNAL_PATTERNS = [
    r"\bNature Reviews\b|\bNat(ure)?\.?\s+Rev\.",
    r"\bAnnual Review\b|\bAnnu\.?\s+Rev\.",
    r"\bTrends\b",  # e.g., Trends Genet., Trends Mol. Med.
    r"\bCurr\.?\s+Opin\.|\bCurrent\s+Opinion\b",
    r"\bBrief\.?\b",  # Briefings in ... often review-style
]
REVIEW_RE = re.compile("|".join(REVIEW_JOURNAL_PATTERNS), re.IGNORECASE)


def read_file(fp: str) -> str:
    with open(fp, 'r', encoding='utf-8') as f:
        return f.read()


def extract_references_block(text: str) -> str:
    # Capture content between 'References' and next major section marker
    m = re.search(
        r"\nReferences\n([\s\S]*?)(?:\nDownload references|\nAcknowledgements|\nAuthor information|\nRights and permissions|\nAbout this article|\nThis article is cited by|$)",
        text,
        re.IGNORECASE,
    )
    if m:
        return m.group(1).strip()
    # Fallback: from References to end
    m2 = re.search(r"\nReferences\n([\s\S]*)$", text, re.IGNORECASE)
    return m2.group(1).strip() if m2 else ""


def split_reference_entries(ref_block: str) -> List[str]:
    entries: List[str] = []
    current_lines: List[str] = []

    lines = ref_block.splitlines()
    for line in lines:
        stripped = line.strip()
        if not stripped:
            # blank lines: keep accumulating; we'll split on metadata markers
            continue
        # Metadata marker lines typically start with 'Article' or contain 'Google Scholar'/'PubMed'
        if stripped.startswith('Article') or 'Google Scholar' in stripped or 'PubMed' in stripped or 'CAS' in stripped:
            # finalize: take the last non-empty line accumulated as the core reference line
            core_line = ""
            for prev in reversed(current_lines):
                if prev.strip():
                    core_line = prev.strip()
                    break
            if core_line:
                entries.append(core_line)
            current_lines = []
            # do not add metadata line
        else:
            current_lines.append(stripped)

    # If leftover lines form a final entry, add it
    if current_lines:
        core_line = ""
        for prev in reversed(current_lines):
            if prev.strip():
                core_line = prev.strip()
                break
        if core_line:
            entries.append(core_line)

    # Deduplicate while preserving order
    seen = set()
    unique_entries = []
    for e in entries:
        if e not in seen:
            seen.add(e)
            unique_entries.append(e)
    return unique_entries


def parse_reference_line(line: str) -> Tuple[str, str, str, str]:
    """
    Return (authors, title, journal, year) best-effort from a single-line reference.
    Assumes pattern: Authors. Title. Journal vol, pages (year).
    """
    year_match = re.search(r"\((\d{4})\)", line)
    year = year_match.group(1) if year_match else ""

    # Split by '. ' into segments
    parts = [p.strip() for p in line.split('. ') if p.strip()]
    authors = parts[0] if parts else ""
    title = parts[1] if len(parts) > 1 else ""

    # Journal part: try to capture substring after title period up to year parenthesis
    journal = ""
    if year:
        try:
            # find index right after title end
            title_pos = line.find(title)
            after_title = line[title_pos + len(title):]
            # remove leading punctuation and spaces
            after_title = after_title.lstrip('. ').strip()
            # up to year
            up_to_year = after_title.split(f'({year})')[0].strip()
            # journal is the first token(s) before volume number; but allow dots in journal names
            # Often formatted like: Journal 24, pages...
            jmatch = re.match(r"(.+?)\s+\d|(.+?)\s*,", up_to_year)
            if jmatch:
                journal = (jmatch.group(1) or jmatch.group(2) or up_to_year).strip()
            else:
                journal = up_to_year
        except Exception:
            journal = ""
    else:
        # Fallback: assume third segment is journal
        journal = parts[2] if len(parts) > 2 else ""

    return authors, title.rstrip('.'), journal.rstrip('.'), year


def is_review_journal(journal: str) -> bool:
    if not journal:
        return False
    return bool(REVIEW_RE.search(journal))


def main():
    input_path = (
        sys.argv[1]
        if len(sys.argv) > 1
        else "/workspaces/Agent4BioPhD/lab1/data/Badia-i-Mompel et al 2023.md"
    )
    output_path = (
        sys.argv[2]
        if len(sys.argv) > 2
        else "/workspaces/Agent4BioPhD/lab1/practice/review_articles.csv"
    )

    if not os.path.exists(input_path):
        print(f"Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    text = read_file(input_path)
    ref_block = extract_references_block(text)
    if not ref_block:
        print("Could not locate References section.", file=sys.stderr)
        sys.exit(2)

    entries = split_reference_entries(ref_block)

    parsed = []
    for e in entries:
        authors, title, journal, year = parse_reference_line(e)
        parsed.append({
            'authors': authors,
            'title': title,
            'journal': journal,
            'year': year,
            'raw': e,
            'is_review': 'yes' if is_review_journal(journal) else 'no',
        })

    # Filter for review entries
    reviews = [row for row in parsed if row['is_review'] == 'yes']

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            'authors', 'year', 'title', 'journal', 'raw_reference',
            'note: heuristic journal-based detection (Nat/Nature Reviews, Annual Review, Trends, Current Opinion, Briefings)'
        ])
        for r in reviews:
            writer.writerow([r['authors'], r['year'], r['title'], r['journal'], r['raw']])

    print(f"Found {len(reviews)} review-like references out of {len(parsed)} total.\nOutput: {output_path}")


if __name__ == '__main__':
    main()
