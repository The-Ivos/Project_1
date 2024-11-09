kombinace = 1.234
presnost_str = "Hello"
presnost_cisla = 123.456

formatovana_presnost = f"|{presnost_cisla:.3}|{presnost_cisla:.4}|{presnost_cisla:.5}|"
formatovana_kombinace = f"|{kombinace:$<6.4}|"
formatovana_presnost_str = f"|{presnost_str:.4}|"

print(f"""\
Naformatovana presnost: \t{formatovana_presnost}
Naformatovana kombinace: \t{formatovana_kombinace}
Naformatovany string: \t\t{formatovana_presnost_str}

""")

open("vysledek.txt","w").close()
with open("vysledek.txt","r+",encoding="utf-8") as file:
    file.write("\n".join((formatovana_presnost,
    formatovana_kombinace,
    formatovana_presnost_str
    )))
    file.seek(0)
    content = file.read()

print(content)