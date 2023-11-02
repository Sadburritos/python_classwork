import re


with open("html.html", "r", encoding="utf-8") as file:
    html_content = file.read()

    title_match = re.search(r"<title>(.*?)</title>", html_content, re.DOTALL)
    if title_match:
        title = title_match.group(1).strip()
        print(title)

    headings = re.findall(r"<h[1-6]>(.*?)</h[1-6]>", html_content, re.DOTALL)
    for heading in headings:
        print(heading.strip())
