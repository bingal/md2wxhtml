import re
from collections import OrderedDict
from typing import Dict, Tuple


def md_links_to_index(markdown: str) -> Tuple[str, Dict[str, Tuple[int, str]]]:
    """
    Convert markdown links to numbered references.

    Converts [text](url) to text[n] and appends a reference list at the end.

    Args:
        markdown: The input markdown text.

    Returns:
        A tuple of (converted_markdown, links_dict) where:
        - converted_markdown: The markdown with links replaced by numbered references
        - links_dict: A dict mapping url to (index, original_text) tuples
    """
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    links = OrderedDict()
    index = 1

    def replace(match):
        nonlocal index
        text, url = match.group(1), match.group(2)
        if url not in links:
            links[url] = (index, text)
            index += 1
        return f"{text}[{links[url][0]}]"

    body = link_pattern.sub(replace, markdown)

    if not links:
        return markdown, {}

    refs = "\n\n---\n\n参考链接：\n"
    for url, (i, text) in links.items():
        refs += f"[{i}] {text}：{url}\n"

    return body + refs, links
