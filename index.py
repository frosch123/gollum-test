#!/usr/bin/env python3
import os
import sys
import re

REPO_PATH = sys.argv[1]

# TODO differential updates
# TODO cleanup old files

PAT_TRANSLATION = re.compile("\[\[\s*Translation:([^]|]*)\]\]")
PAT_CATEGORY = re.compile("\[\[\s*Category:([^]|]*)\]\]")

categories = dict()
translations = dict()

for dirpath, _, filenames in os.walk(REPO_PATH):
    assert dirpath.startswith(REPO_PATH)
    dirpath = dirpath[(len(REPO_PATH)+1):]
    if dirpath.startswith(".") or dirpath.startswith("uploads"):
        continue
    for fn in filenames:
        filename = os.path.join(dirpath, fn)
        if not filename.endswith(".mediawiki"):
            continue
        pagename = filename[0:-10]
        filename = os.path.join(REPO_PATH, filename)

        with open(filename, "rt") as f:
            content = f.read()

        translation = PAT_TRANSLATION.search(content)
        if translation:
            en = translation.group(1).strip()
            translations.setdefault(en, set()).add(pagename)

        for category in PAT_CATEGORY.finditer(content):
            name = category.group(1).strip()
            categories.setdefault(name, set()).add(pagename)


for name, members in categories.items():
    filename = os.path.join(REPO_PATH, ".category", name + ".mediawiki")
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    member_categories = sorted([n for n in members if n.startswith("Category/")], key=str.lower)
    member_pages = sorted([n for n in members if not n.startswith("Category/")], key=str.lower)

    with open(filename, "wt") as f:
        if member_categories:
            f.write("\n== Subcategories ==\n")
            for member in member_categories:
                f.write("[[{}]]\n".format(member))
        if member_pages:
            f.write("\n== Pages ==\n")
            for member in member_pages:
                f.write("[[{}]]\n".format(member))

for name, members in translations.items():
    filename = os.path.join(REPO_PATH, ".translation", name + ".html")
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    members = sorted(members, key=lambda n: (n.find("/en/") < 0, n.lower()))
    with open(filename, "wt") as f:
        f.write("""<div style="float: right; border: 1px solid #c7c8fe; background-color: #EEE; padding:0px;">\n""")
        for member in members:
            language = member.split("/")[1]
            f.write("""<div style="display:inline-block;  height: 3em; width: 26px; text-align:center;">""" +
                    """<a href="/{}"><img src="/uploads/{}/Flag.png"</img><br/>{}</a>""".format(member, language, language.upper()) +
                    """</div>\n""")
        f.write("""</div>\n""")
