import re


def normalize_urls(urls):
    normalized = set()
    for url in urls:
        url = url.strip()
        if url.endswith("/"):
            url = url[:-1]
        normalized.add(url)
    return list(normalized)


def is_valid_url(url):
    pattern = re.compile(
        r"^(https?:\/\/)"
        r"([\w\-]+\.)+[\w\-]+"
        r"(\/[\w\-._~:/?#[\]@!$&'()*+,;=]*)?$"
    )
    return bool(pattern.match(url))


def filter_valid_urls(urls):
    valid = []
    invalid = []
    for url in urls:
        if is_valid_url(url):
            valid.append(url)
        else:
            invalid.append(url)
    return valid, invalid
