def zobraz_text(func):
    def wrapper(zadany_text):
        print("Formatovany text:")
        func(zadany_text)
    return wrapper

    
@zobraz_text
def preved_format_na_kapitalku(text):
    prevedeno = ""
    for i in text.split():
        prevedeno += i.capitalize() + " "
    return print(prevedeno.strip(" "))

atext = "toto je ukázkový text"

preved_format_na_kapitalku(atext)