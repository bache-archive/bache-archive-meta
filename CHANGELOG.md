# Changelog
All notable changes to **bache-archive-meta** will be documented here.  
Format: Keep a Changelog (human-readable), semver-ish tags aligned to registry milestones.

## [Unreleased]
- (placeholder) Add new entities and identifiers as needed.
- (placeholder) Non-breaking schema clarifications (bump x-version patch only).

## [v1.1] — 2025-11-01
### Added
- **OpenAlex Author ID** for Christopher M. Bache: `A5045900737` in `identifiers.json`.
- **ISBNs** for major works:
  - *LSD and the Mind of the Universe* — ISBN-10 `1620559706`, ISBN-13 `9781620559703`
  - *Dark Night, Early Dawn* — ISBN-10 `0791446069`, ISBN-13 `9780791446065`
  - *The Living Classroom* — ISBN-13 `9780791476468` (paperback 2008)
  - *Lifecycles* — ISBN-10 `1557786453`, ISBN-13 `9781557786456`

### CI
- Tightened workflow triggers, Python 3.11/3.12 matrix, pip cache, weekly schedule, and JSON sanity checks.

### Notes
- No breaking schema changes. Downstream repos may safely update their pin to `v1.1`.

## [v1.0] — 2025-10-XX
### Initial
- Registry initialization:
  - `wikidata.jsonld` for canonical QIDs.
  - `identifiers.json` scaffold (Wikidata, ORCID, OpenAlex, VIAF, ISBN).
  - Base schemas (`schema/manifest-schema.json`, `schema/citation-entry.json`, `schema/topic-frontmatter.yaml`).
  - Local validator and CI.

---

## Versioning Policy
- **vX.Y** corresponds to registry milestones:
  - **Y bump** for new identifiers/entities and non-breaking schema metadata (e.g., `$id`, `x-version`).
  - **X bump** for breaking schema changes (require downstream action).
- Schemas expose a non-breaking version via `x-version`. Patch this for constraint clarifications.

## Downstream Pinning Guidance
- Pin to a **tag** of this repo (e.g., `v1.1`) to ensure reproducible builds.
- Read identifiers from `identifiers.json` and QIDs from `wikidata.jsonld`.
- Validate manifests with `tools/validate_identifiers.py` and the published schema `$id`.
