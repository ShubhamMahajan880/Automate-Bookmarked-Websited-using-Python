import argparse
from src.loader import load_from_txt, load_from_html
from src.validator import normalize_urls, filter_valid_urls
from src.opener import open_urls


def main():
    parser = argparse.ArgumentParser(
        description="Automated Bookmark Management System"
    )

    parser.add_argument(
        "--input-type",
        choices=["txt", "html"],
        required=True,
        help="Type of bookmark input file"
    )

    parser.add_argument(
        "--file",
        required=True,
        help="Path to bookmark file"
    )

    args = parser.parse_args()

    if args.input_type == "txt":
        urls = load_from_txt(args.file)
    else:
        urls = load_from_html(args.file)

    urls = normalize_urls(urls)
    valid_urls, invalid_urls = filter_valid_urls(urls)

    print("\nSummary")
    print("-------")
    print(f"Total URLs found: {len(urls)}")
    print(f"Valid URLs: {len(valid_urls)}")
    print(f"Invalid URLs skipped: {len(invalid_urls)}\n")

    if valid_urls:
        open_urls(valid_urls)
    else:
        print("No valid URLs to open.")


if __name__ == "__main__":
    main()
