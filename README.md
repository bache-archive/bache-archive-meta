# 🧩 Bache Archive Meta

**Repository:** [bache-archive-meta](https://github.com/bache-archive/bache-archive-meta)  
**Maintainer:** Bache Archive Project · 📧 bache-archive@tuta.com  
**License:** CC0 1.0 Universal (Public Domain)  
**Version:** v1.0 — Metadata Registry Initialization (November 2025)

---

## 🧭 Purpose

`bache-archive-meta` is the **central metadata registry** of the [Bache Archive Project](https://github.com/bache-archive).  
It provides a **single, FAIR-compliant source of truth** for identifiers, schemas, and provenance shared across all repositories.

This repository ensures that every layer of the ecosystem — corpus, bibliography, educational docs, RAG APIs, and graph —  
references the same verified identifiers for *Christopher M. Bache* and his published works.

---

## 🧱 Structure

bache-archive-meta/
├── README.md
├── wikidata.jsonld
├── identifiers.json
├── schema/
│   ├── manifest-schema.json
│   ├── topic-frontmatter.yaml
│   └── citation-entry.json
├── provenance/
│   ├── FAIR-metadata.md
│   └── LICENSE-CC0.txt
└── .github/
└── workflows/
└── validate_identifiers.yml

---

## 📚 Contents

### `wikidata.jsonld`
Canonical **Wikidata QID registry** for Christopher M. Bache and his four major works.

```json
{
  "@context": { "wd": "https://www.wikidata.org/entity/" },
  "entities": {
    "christopher_m_bache": "wd:Q112496741",
    "lsdmu": "wd:Q136684740",
    "dark_night_early_dawn": "wd:Q136684765",
    "living_classroom": "wd:Q136684793",
    "lifecycles": "wd:Q136684807"
  }
}

Referenced by:
	•	chris-bache-archive → transcript metadata and fixity manifests
	•	lsdmu-bibliography → CSL-JSON records and x-bache extensions
	•	bache-educational-docs → YAML front-matter for topic summaries
	•	lsdmu-rag-api → embedding provenance metadata
	•	bache-graph → node and edge definitions
	•	bache-archive.github.io → semantic web JSON-LD in site footer

⸻

identifiers.json

Aggregates cross-platform identifiers (DOI, ORCID, OpenAlex, ROR) for each relevant entity.

{
  "christopher_m_bache": {
    "wikidata": "Q112496741",
    "orcid": "0000-0002-0000-0000",
    "openalex": "A123456789",
    "viaf": "32119876"
  },
  "lsdmu": {
    "wikidata": "Q136684740",
    "doi": "10.5281/zenodo.17477237"
  }
}

(Placeholder values shown; updated entries are synchronized via CI.)

⸻

schema/

Validation schemas shared across repositories:

File	Purpose
manifest-schema.json	Defines required fields for transcript & media manifests
topic-frontmatter.yaml	Ensures uniform YAML metadata for educational docs
citation-entry.json	Standardizes CSL-JSON extensions for bibliographic entries


⸻

provenance/

FAIR metadata and licensing for reuse, including:
	•	FAIR-metadata.md — explains alignment with FAIR principles
	•	LICENSE-CC0.txt — metadata and identifiers dedicated to the public domain

⸻

.github/workflows/validate_identifiers.yml

Automated consistency check ensuring that all dependent repositories reference only valid QIDs and identifiers.

Example GitHub Action step:

- name: Validate identifier consistency
  run: |
    python tools/validate_identifiers.py --registry wikidata.jsonld


⸻

🌐 FAIR Principles

Principle	Implementation
Findable	Every entity linked to a persistent QID / DOI
Accessible	CC0-licensed JSON-LD published openly on GitHub + Zenodo
Interoperable	JSON-LD & YAML schemas compatible with schema.org / SKOS / PROV-O
Reusable	All metadata public-domain; provenance tracked via Git history


⸻

🔗 Related Repositories

Repository	Role
chris-bache-archive￼	Canonical transcripts & fixity
lsdmu-bibliography￼	CSL-JSON bibliography & citations
bache-educational-docs￼	Educational topic summaries
bache-graph￼	Semantic graph of works, authors, and ideas
lsdmu-rag-api￼	Retrieval and embedding pipeline
bache-archive.github.io￼	Public site, search & semantic metadata layer


⸻

🧩 Usage

Clone or add as a submodule in any dependent repository:

git submodule add https://github.com/bache-archive/bache-archive-meta meta

Or pull the canonical registry directly in CI:

curl -sSL https://raw.githubusercontent.com/bache-archive/bache-archive-meta/main/wikidata.jsonld -o wikidata.jsonld


⸻

🏷️ Versioning

Each major alignment milestone is tagged across all repositories:
	•	v3.2-preservation-baseline → Preservation Epoch complete
	•	v3.3-wikidata-integration → Cross-repository semantic alignment
	•	Future: v3.4-openalex-linkage → Global scholarly identifier sync

⸻

💫 License

All metadata and schemas in this repository are released under CC0 1.0 Universal (Public Domain Dedication).
They may be freely reused, remixed, and redistributed without restriction.

⸻

Bache Archive Project — stewarding the Chris Bache Archive (2009–2025 → ∞)
A living, open infrastructure for preserving, linking, and transmitting wisdom.
