#!/usr/bin/env python3
"""
Detailed Usage Examples for Top 10 ToolUniverse Tools
Relevant to Gene Regulatory Network Inference

Author: AI Agent for Agent4BioPhD
Date: November 7, 2025
"""

from tooluniverse import ToolUniverse

# Initialize ToolUniverse
tu = ToolUniverse()
tu.load_tools()

print("="*80)
print("ToolUniverse: Top 10 Tools for GRN Inference - Usage Examples")
print("="*80)
print()

# =============================================================================
# Tool 1: ENCODE_search_experiments
# =============================================================================
print("1. ENCODE_search_experiments")
print("-" * 80)
print("Search ENCODE for chromatin accessibility experiments")
print()

# Example: Search for ATAC-seq experiments in neural cells
encode_search = {
    "name": "ENCODE_search_experiments",
    "arguments": {
        "assay_title": "ATAC-seq",
        "biosample_ontology": "neural",
        "limit": 5
    }
}
print("Query:", encode_search)
print("\nApplication: Find chromatin accessibility data for GRN inference")
print("Use Case: Identify open chromatin regions for regulatory element mapping")
print()

# =============================================================================
# Tool 2: UniProt_get_function_by_accession
# =============================================================================
print("2. UniProt_get_function_by_accession")
print("-" * 80)
print("Retrieve transcription factor functional annotations")
print()

# Example: Get function of TP53 (tumor suppressor & TF)
uniprot_query = {
    "name": "UniProt_get_function_by_accession",
    "arguments": {
        "accession": "P04637"  # TP53 UniProt ID
    }
}
print("Query:", uniprot_query)
print("\nApplication: Annotate TFs identified in GRN")
print("Use Case: Understand regulatory mechanisms of predicted TF-gene links")
print()

# =============================================================================
# Tool 3: GO_get_annotations_for_gene
# =============================================================================
print("3. GO_get_annotations_for_gene")
print("-" * 80)
print("Gene Ontology annotations for functional characterization")
print()

# Example: Get GO terms for a regulatory gene
go_query = {
    "name": "GO_get_annotations_for_gene",
    "arguments": {
        "gene_id": "ENSG00000141510",  # TP53 Ensembl ID
        "ontology": "biological_process"
    }
}
print("Query:", go_query)
print("\nApplication: Functionally characterize gene modules in GRN")
print("Use Case: Validate co-regulation based on shared biological processes")
print()

# =============================================================================
# Tool 4: enrichr_gene_enrichment_analysis
# =============================================================================
print("4. enrichr_gene_enrichment_analysis")
print("-" * 80)
print("Gene set enrichment for TF activity inference")
print()

# Example: Enrichment analysis of predicted TF targets
enrichr_query = {
    "name": "enrichr_gene_enrichment_analysis",
    "arguments": {
        "gene_list": ["TP53", "MDM2", "CDKN1A", "BAX", "PUMA"],
        "library": "ENCODE_TF_ChIP-seq_2015"
    }
}
print("Query:", enrichr_query)
print("\nApplication: Infer active TFs from target gene expression")
print("Use Case: Validate GRN predictions against ChIP-seq databases")
print()

# =============================================================================
# Tool 5: HPA_get_rna_expression_in_specific_tissues
# =============================================================================
print("5. HPA_get_rna_expression_in_specific_tissues")
print("-" * 80)
print("Tissue-specific expression for GRN contextualization")
print()

# Example: Get brain-specific expression
hpa_query = {
    "name": "HPA_get_rna_expression_in_specific_tissues",
    "arguments": {
        "gene": "TP53",
        "tissue": "cerebral cortex"
    }
}
print("Query:", hpa_query)
print("\nApplication: Contextualize GRNs by tissue/cell type")
print("Use Case: Compare regulatory programs across biological contexts")
print()

# =============================================================================
# Tool 6: BLAST_protein_search
# =============================================================================
print("6. BLAST_protein_search")
print("-" * 80)
print("Sequence similarity for evolutionary conservation")
print()

# Example: Find homologous TFs across species
blast_query = {
    "name": "BLAST_protein_search",
    "arguments": {
        "sequence": "MEEPQSDPSVEPPLSQETFSDLWKLLPENNVL",  # TP53 N-terminus
        "database": "nr",
        "organism": "Mus musculus",
        "max_hits": 10
    }
}
print("Query:", blast_query)
print("\nApplication: Identify conserved TFs across species")
print("Use Case: Validate regulatory interactions via evolutionary conservation")
print()

# =============================================================================
# Tool 7: HPA_get_protein_interactions_by_gene
# =============================================================================
print("7. HPA_get_protein_interactions_by_gene")
print("-" * 80)
print("Protein-protein interactions for TF cooperativity")
print()

# Example: Get interacting proteins for a TF
ppi_query = {
    "name": "HPA_get_protein_interactions_by_gene",
    "arguments": {
        "gene": "TP53"
    }
}
print("Query:", ppi_query)
print("\nApplication: Identify TF co-factors and binding partners")
print("Use Case: Validate cooperative TF binding in GRNs")
print()

# =============================================================================
# Tool 8: ENCODE_list_files
# =============================================================================
print("8. ENCODE_list_files")
print("-" * 80)
print("Download ENCODE processed data files")
print()

# Example: List bigWig files for an ATAC-seq experiment
encode_files_query = {
    "name": "ENCODE_list_files",
    "arguments": {
        "experiment_id": "ENCSR000ATV",
        "file_format": "bigWig",
        "output_type": "signal"
    }
}
print("Query:", encode_files_query)
print("\nApplication: Access chromatin accessibility signal tracks")
print("Use Case: Download processed peak files for regulatory element annotation")
print()

# =============================================================================
# Tool 9: OpenTargets_get_target_gene_ontology_by_ensemblID
# =============================================================================
print("9. OpenTargets_get_target_gene_ontology_by_ensemblID")
print("-" * 80)
print("Disease associations and druggability information")
print()

# Example: Get target information for a regulatory gene
opentargets_query = {
    "name": "OpenTargets_get_target_gene_ontology_by_ensemblID",
    "arguments": {
        "ensembl_id": "ENSG00000141510"  # TP53
    }
}
print("Query:", opentargets_query)
print("\nApplication: Link GRNs to disease mechanisms")
print("Use Case: Identify therapeutic targets in regulatory networks")
print()

# =============================================================================
# Tool 10: kegg_find_genes
# =============================================================================
print("10. kegg_find_genes")
print("-" * 80)
print("KEGG pathway integration")
print()

# Example: Search for TFs in KEGG
kegg_query = {
    "name": "kegg_find_genes",
    "arguments": {
        "keywords": "p53 signaling",
        "organism": "hsa"  # Homo sapiens
    }
}
print("Query:", kegg_query)
print("\nApplication: Place GRNs in pathway context")
print("Use Case: Integrate GRNs with metabolic/signaling networks")
print()

# =============================================================================
# Integrated Workflow Example
# =============================================================================
print("="*80)
print("INTEGRATED WORKFLOW: Complete GRN Analysis Pipeline")
print("="*80)
print()

workflow = """
Step 1: Data Discovery
-----------------------
# Find relevant ATAC-seq data
atac_experiments = tu.run({
    "name": "ENCODE_search_experiments",
    "arguments": {"assay_title": "ATAC-seq", "biosample_ontology": "K562"}
})

Step 2: Download Data Files
----------------------------
# Get processed peak files
peak_files = tu.run({
    "name": "ENCODE_list_files",
    "arguments": {"experiment_id": experiment_id, "file_format": "bed"}
})

Step 3: TF Annotation
----------------------
# For each predicted TF, get functional information
for tf_id in predicted_tfs:
    tf_info = tu.run({
        "name": "UniProt_get_function_by_accession",
        "arguments": {"accession": tf_id}
    })

Step 4: Target Gene Analysis
-----------------------------
# Perform enrichment on predicted targets
enrichment = tu.run({
    "name": "enrichr_gene_enrichment_analysis",
    "arguments": {
        "gene_list": target_genes,
        "library": "GO_Biological_Process_2021"
    }
})

Step 5: Validation
------------------
# Check protein interactions
interactions = tu.run({
    "name": "HPA_get_protein_interactions_by_gene",
    "arguments": {"gene": tf_name}
})

Step 6: Expression Context
---------------------------
# Get tissue-specific expression
expression = tu.run({
    "name": "HPA_get_rna_expression_in_specific_tissues",
    "arguments": {"gene": tf_name, "tissue": tissue_name}
})

Step 7: Evolutionary Conservation
----------------------------------
# Check conservation across species
homologs = tu.run({
    "name": "BLAST_protein_search",
    "arguments": {"sequence": tf_sequence, "organism": "Mus musculus"}
})

Step 8: Disease Context
------------------------
# Get disease associations
disease_info = tu.run({
    "name": "OpenTargets_get_target_gene_ontology_by_ensemblID",
    "arguments": {"ensembl_id": ensembl_id}
})

Step 9: Pathway Integration
----------------------------
# Place in pathway context
pathway_info = tu.run({
    "name": "kegg_find_genes",
    "arguments": {"keywords": pathway_name, "organism": "hsa"}
})

Step 10: GO Annotation
-----------------------
# Final functional annotation
go_terms = tu.run({
    "name": "GO_get_annotations_for_gene",
    "arguments": {"gene_id": ensembl_id}
})
"""

print(workflow)
print()

# =============================================================================
# Practical Example with Real Data
# =============================================================================
print("="*80)
print("PRACTICAL EXAMPLE: Analyzing TP53 Regulatory Network")
print("="*80)
print()

practical_example = """
# Scenario: You've identified TP53 as a key hub in your inferred GRN
# and want to comprehensively characterize its regulatory role

# 1. Get TP53 functional annotation
tp53_function = tu.run({
    "name": "UniProt_get_function_by_accession",
    "arguments": {"accession": "P04637"}
})
# Returns: DNA-binding TF, apoptosis regulator, cell cycle control

# 2. Identify TP53 target genes (from your GRN inference)
predicted_targets = ["MDM2", "CDKN1A", "BAX", "PUMA", "BBC3"]

# 3. Validate targets with enrichment analysis
enrichment = tu.run({
    "name": "enrichr_gene_enrichment_analysis",
    "arguments": {
        "gene_list": predicted_targets,
        "library": "ENCODE_TF_ChIP-seq_2015"
    }
})
# Check if TP53 is significantly enriched

# 4. Get protein interaction partners
partners = tu.run({
    "name": "HPA_get_protein_interactions_by_gene",
    "arguments": {"gene": "TP53"}
})
# Identify co-factors like MDM2, ATM, etc.

# 5. Check tissue-specific expression
brain_expression = tu.run({
    "name": "HPA_get_rna_expression_in_specific_tissues",
    "arguments": {"gene": "TP53", "tissue": "cerebral cortex"}
})

# 6. Get GO annotations for target genes
for target in predicted_targets:
    go_annot = tu.run({
        "name": "GO_get_annotations_for_gene",
        "arguments": {"gene_id": ensembl_id_map[target]}
    })
# Group targets by shared biological processes

# 7. Link to disease
disease_links = tu.run({
    "name": "OpenTargets_get_target_gene_ontology_by_ensemblID",
    "arguments": {"ensembl_id": "ENSG00000141510"}
})
# Identify cancer associations

# 8. Check conservation
mouse_homolog = tu.run({
    "name": "BLAST_protein_search",
    "arguments": {
        "sequence": tp53_sequence,
        "organism": "Mus musculus",
        "max_hits": 1
    }
})
# Validate that regulatory relationship is conserved

# 9. Pathway context
pathway = tu.run({
    "name": "kegg_find_genes",
    "arguments": {"keywords": "p53 signaling", "organism": "hsa"}
})
# Place in broader signaling context

# 10. Access experimental validation data
chip_data = tu.run({
    "name": "ENCODE_search_experiments",
    "arguments": {
        "assay_title": "ChIP-seq",
        "target": "TP53",
        "limit": 10
    }
})
# Find ChIP-seq datasets for validation
"""

print(practical_example)
print()

print("="*80)
print("For complete documentation, see:")
print("https://zitniklab.hms.harvard.edu/ToolUniverse/")
print("="*80)
