Input: /workspaces/Agent4BioPhD/lab1/data/Badia-i-Mompel et al 2023.md
Task: Review the References section of the paper and locate review articles. Generate a CSV listing those articles and place it in the practice folder.

Automated solution:
1. Script: `extract_review_references.py` created in this folder.
2. Heuristic: Flags references whose journal name matches common review sources (Nature Reviews*, Annual Review*, Trends*, Current Opinion*, Brief.*).
3. Run:
	python3 extract_review_references.py 
	(Optional arguments: input_path output_path)
4. Output file: `review_articles.csv` (already generated if you see it here).

Improvement ideas:
- Enhance parsing of authors/title segments (current single-line heuristic splits may misalign commas).
- Add manual override list for known review journals or article-type keywords ("Review", "Perspective").
- Integrate DOI extraction.

Output: /workspaces/Agent4BioPhD/lab1/practice/review_articles.csv