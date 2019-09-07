import re
import regexps
import os
import shutil


def get_content(path, type):
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


def get_named_html_entities(path):
    named_html_entity_regexps = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f.read().splitlines():
            truncated = line[1:]
            from_ws = "&amp;" + truncated
            named_html_entity_regexps.append((re.compile(from_ws), line))
    return named_html_entity_regexps


def make_dirs(*argv, remove_existing: bool = True):
    for folder in argv:
        if remove_existing:
            shutil.rmtree(folder)
        if not os.path.exists(folder):
            os.makedirs(folder)
        else:
            print(f"Folder Already Exists. Not making folder {folder}")
