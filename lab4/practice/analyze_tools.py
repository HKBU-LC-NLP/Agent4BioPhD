#!/usr/bin/env python3
"""
Analyze ToolUniverse tools relevant to Gene Regulatory Network inference paper
"""

import json
import os
from pathlib import Path

# Key concepts from the paper
PAPER_CONCEPTS = [
    "gene regulatory network",
    "transcription factor",
    "chromatin accessibility",
    "ATAC-seq",
    "RNA-seq",
    "single-cell",
    "gene expression",
    "regulatory elements",
    "genomics",
    "transcriptomics",
    "epigenomics",
    "ChIP-seq",
    "DNA binding",
    "motif",
    "enhancer",
    "promoter",
    "multi-omics",
    "ENCODE",
    "UniProt",
    "protein",
    "gene annotation",
    "pathway",
    "network analysis"
]

def load_tool_metadata():
    """Load tool metadata from ToolUniverse"""
    metadata_path = Path("/workspaces/Agent4BioPhD/lab4/practice/ToolUniverse/src/tooluniverse/tools/.tool_metadata.json")
    
    if metadata_path.exists():
        with open(metadata_path, 'r') as f:
            return json.load(f)
    return {}

def score_tool_relevance(tool_name, concepts):
    """Score tool relevance based on keyword matching"""
    tool_lower = tool_name.lower()
    score = 0
    matched_concepts = []
    
    for concept in concepts:
        concept_lower = concept.lower()
        # Check for exact matches or partial matches
        if concept_lower in tool_lower or any(word in tool_lower for word in concept_lower.split()):
            score += 1
            matched_concepts.append(concept)
    
    return score, matched_concepts

def analyze_tools():
    """Analyze and rank tools by relevance"""
    metadata = load_tool_metadata()
    
    print(f"Total tools found: {len(metadata)}")
    print(f"\nAnalyzing tools for relevance to GRN inference...\n")
    
    # Score all tools
    tool_scores = []
    for tool_name in metadata.keys():
        score, concepts = score_tool_relevance(tool_name, PAPER_CONCEPTS)
        if score > 0:
            tool_scores.append({
                'name': tool_name,
                'score': score,
                'matched_concepts': concepts
            })
    
    # Sort by score
    tool_scores.sort(key=lambda x: x['score'], reverse=True)
    
    # Print top 20 tools
    print(f"\n{'='*80}")
    print(f"TOP 20 MOST RELEVANT TOOLS FOR GRN INFERENCE")
    print(f"{'='*80}\n")
    
    for i, tool in enumerate(tool_scores[:20], 1):
        print(f"{i}. {tool['name']}")
        print(f"   Relevance Score: {tool['score']}")
        print(f"   Matched Concepts: {', '.join(tool['matched_concepts'])}")
        print()
    
    # Save results
    output_file = "/workspaces/Agent4BioPhD/lab4/practice/relevant_tools_analysis.json"
    with open(output_file, 'w') as f:
        json.dump({
            'total_tools': len(metadata),
            'relevant_tools_count': len(tool_scores),
            'top_20_tools': tool_scores[:20],
            'all_relevant_tools': tool_scores
        }, f, indent=2)
    
    print(f"\nDetailed analysis saved to: {output_file}")
    
    return tool_scores

if __name__ == "__main__":
    analyze_tools()
