import argparse, json, re, sys
from jsonschema import Draft202012Validator

QID_RE = re.compile(r"^Q\d+$")

def fail(msg):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--wikidata", required=True)
    p.add_argument("--ids", required=True)
    p.add_argument("--schema", required=True)
    args = p.parse_args()

    # Load wikidata.jsonld
    with open(args.wikidata, "r", encoding="utf-8") as f:
        wd = json.load(f)
    entities = wd.get("entities", {})
    if not entities:
        fail("wikidata.jsonld: 'entities' map is empty")

    # Validate wd:Q… format
    for key, val in entities.items():
        if not isinstance(val, str) or not val.startswith("wd:Q"):
            fail(f"wikidata.jsonld: entity '{key}' has invalid value '{val}' (must start with 'wd:Q')")
        if not re.match(r"^wd:Q\d+$", val):
            fail(f"wikidata.jsonld: entity '{key}' value '{val}' not in 'wd:Q[digits]' format")

    # Load identifiers.json
    with open(args.ids, "r", encoding="utf-8") as f:
        ids = json.load(f)
    ents = ids.get("entities", {})
    if not ents:
        fail("identifiers.json: 'entities' map is empty")

    # Cross-check identifiers.json -> wikidata QIDs exist and look valid
    for key, data in ents.items():
        q = data.get("wikidata", "")
        if q:
            if not QID_RE.match(q):
                fail(f"identifiers.json: entity '{key}' has invalid wikidata '{q}' (expected Q[digits])")
            # Ensure entity key exists in wikidata.jsonld (by friendly key), if present
            if key not in entities and not any(v.endswith(q) for v in entities.values()):
                fail(f"identifiers.json: entity '{key}' wikidata '{q}' not found in wikidata.jsonld")

    # Load and sanity-check manifest schema
    with open(args.schema, "r", encoding="utf-8") as f:
        manifest_schema = json.load(f)
    Draft202012Validator.check_schema(manifest_schema)

    print("OK: wikidata.jsonld, identifiers.json, and schema validated.")

if __name__ == "__main__":
    main()
