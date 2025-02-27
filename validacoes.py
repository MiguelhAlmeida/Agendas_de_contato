import re

def validar_nome(nome):
    if re.match("^[A-Za-zÀ-ÿ]+(?: [A-Za-zÀ-ÿ]+)*$", nome):
        return True
    else:
        return False

def validar_telefone(telefone):
    if re.match(r"^\d{2} \d{5}-\d{4}$", telefone):
        return True
    else:
        return False
