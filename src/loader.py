from bs4 import BeautifulSoup


def load_from_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def load_from_html(file_path):
    urls = []
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
        for link in soup.find_all("a"):
            href = link.get("href")
            if href:
                urls.append(href.strip())
    return urls
