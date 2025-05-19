import re
import unidecode


def preprocessar(frase):
    frase = frase.lower()
    frase = unidecode.unidecode(frase)
    frase = re.sub(r"[^\w\s]", "", frase)
    return frase

