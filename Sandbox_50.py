def muj_dekorator(func):
    def zobraz_text(a):
        print("Formatovany text:")
        func(a)

# @muj_dekorator
def preved_format_na_kapitalku(text):
    text = text.split()
    print(text)
    # prevdeno = ""
    # for i in text:
    #     prevdeno += i.capitalize()

textik = "Zdar vole, jak se mas?"

preved_format_na_kapitalku(textik)
