import re


# Транслятор, который удаляет HTML-теги и оставляет обычный текст
def html_del(hypertext: str) -> str:
    return re.sub('<[^>]*>', '', hypertext)

# mutmut run --paths-to-mutate mutmut/html_del.py