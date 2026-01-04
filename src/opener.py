import webbrowser


def open_urls(urls):
    browser = webbrowser.get()
    for url in urls:
        browser.open_new_tab(url)
