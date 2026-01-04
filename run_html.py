from src.loader import load_from_html
from src.validator import normalize_urls, filter_valid_urls
from src.opener import open_urls

BOOKMARK_FILE = "bookmarks/bookmarks.html"


def main():
    urls = load_from_html(BOOKMARK_FILE)
    urls = normalize_urls(urls)
    valid_urls, invalid_urls = filter_valid_urls(urls)

    print("Summary")
    print("-------")
    print(f"Total URLs found: {len(urls)}")
    print(f"Valid URLs: {len(valid_urls)}")
    print(f"Invalid URLs skipped: {len(invalid_urls)}")

    if valid_urls:
        open_urls(valid_urls)
    else:
        print("No valid URLs to open.")


if __name__ == "__main__":
    main()
