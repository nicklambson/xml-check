import re
import regexps


def get_content(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def get_placeholders(content):
    all_hits = []
    for pattern in regexps.ALL_PATTERNS:
        hits = [hit for hit in re.findall(pattern, content)]
        for hit in hits:
            all_hits.append(hit)
    sorted_hits = sorted(all_hits)
    return sorted_hits


def print_error(name: str = None,
                error_type: str = None,
                source_placeholders: list = None,
                target_placeholders: list = None):
    print(f"Error in file: {name}")
    print(f"Error type: {error_type}")
    if source_placeholders:
        print("Source placeholders:")
        for item in source_placeholders:
            print(item)
    if target_placeholders:
        print("Target Placeholders:")
        for item in source_placeholders:
            print(item)
