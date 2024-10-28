import random
import unidecode


zamestnanci_raw = """
Helena Vybíralová
Wendy Štrumlová
Marie Vybíralová
Stanislav Bechyňka
Zdeňka Urbánková
Lukáš Riečan
Veronika Koudelová
Františka Vorlová
Ilie Seleš
Martin Železný
Petra Niklesová
Bohumil Skok
Jakub Šmíd
Jarmila Procházková
Dagmar Hlavatá
Jiří Nguyen Thanh
Marie Franková
Dana Ulrichová
Jana Hranická
Hana Budošová
Ivan Široký
Květoslava Jiráčková
Pavel Przywara
Josef Umlauf
Tomáš Granzer
Miroslav Kuba
Miloslava Adámková
Marie Karlíková
Jaroslav Hronský
Vlasta Karlíková
Andrea Žatková
Zuzana Lokočová
Ondřej Ptáček
Zdeněk Najman
Tereza Šebešová
Antonie Skokánková
Jan Lion
Václav Vecko
František Vajgl
Adéla Kavková
Amália Vacková
Anna Pažická
Ivo Pustějovský
Antonín Pavela
Jitka Adamová
Libuše Hamroziová
Drahomíra Balzerová
Marek Suchánek
Petr Vavrinec
Jonáš Stuchlý
Jaromír Pecen
Markéta Kyliánková
Marina Pečenková
Ivana Perdochová
Michaela Drápalová
Michael Mentlík
Rudolf Špičák
Žaneta Holá
Blanka Lišková
Eva Svatoňová
Rostislav Hoang
Martina Kalivodová
Milan Hruška
Zdenka Marková
Lenka Schambergerová
Růžena Martinů
Věra Řezanková
Marie Pečenková
Miloš Váchal
Jaroslava Hrubá
Petr Pecen
Pavla Konvicová
Lucie Marešová
Květuše Zdráhalová
Vlastimila Svatošová
Zora Michalčíková
Daniel Švejnoha
Klára Brunclíková
Vladimír Bauer
Michal Slaný
Jiřina Novosadová
Karel Sršeň
Stanislava Lakosilová
Filip Černý
Alena Kubiková
Sára Kotrlová
Alois Rejlek
Božena Novotná
Maryana Nováková
Kateřina Máslová
Ladislav Dvořák
Radek Varga
Petr Dvořák
Ludmila Jaklová
Renáta Foubíková
Nikola Lehká
Dominika Riegerová
Patrik Polák
Soňa Štrbová
David Matoušek
Liubov Hollíková
Monika Poláková
Marie Jaklová
Aleš Svoboda
Roman Kolínský
Karolína Košiková
"""
zamestnanci_div = zamestnanci_raw.split("\n")
zamestnanci_list = []
complicated_names = []

for i in zamestnanci_div:
    if i:
        zamestnanci_list.append(i)

# for i in zamestnanci_list:
#     temp_name = i.split(" ")
#     if len(temp_name) >= 3:
#         print(temp_name)
#         complicated_name = []
#         for n in temp_name:
#             if n != temp_name[0] and n != temp_name[-1]:
#                 n = "split"+n[0]+"."
#                 complicated_name.append(n)
#             else:
#                 complicated_name.append(n)
#         print(complicated_name)
#         restring_name = " ".join(complicated_name)
#         print(restring_name)
#         complicated_names.append(restring_name.split("split"))

# print(complicated_names)


zamestnanci = {"zamestnanec_id":"",
               "jmeno":"",
               "prijmeni":"",
               "telefon":"",
               "email":"",
               "vytvoreno":""
}

# zamestnanec id
zamestnanci_ids = []
for i in range(len(zamestnanci_list)):
    zamestnanci_ids.append(i+1)
zamestnanci["zamestnanec_id"] = tuple(zamestnanci_ids)

# zamestnanec jmeno
zamestnanci_jmena = []
for i in zamestnanci_list:
    temp_name = i.split(" ")
    zamestnanci_jmena.append(temp_name[0])
zamestnanci["jmeno"] = tuple(zamestnanci_jmena)   

# zamestnanec prijmeni
zamestnanci_prijmeni = []
for i in zamestnanci_list:
    temp_name = i.split(" ")
    zamestnanci_prijmeni.append(temp_name[-1])
zamestnanci["prijmeni"] = tuple(zamestnanci_prijmeni)

# telefon
zamestnanci_telefon = []
for i in range(len(zamestnanci_list)):
    temp_number = ["+420"]
    for k in range(3):
        temp_m = []
        for j in range(3):
            m = random.randint(0,9)
            temp_m.append(str(m))
            temp_m_str = "".join(temp_m)
        temp_number.append(temp_m_str)
    number = " ".join(temp_number)
    zamestnanci_telefon.append(number)
zamestnanci["telefon"] = tuple(zamestnanci_telefon)

# email
email = []
for i in zamestnanci_list:
    temp_name = i.split(" ")
    a = temp_name[0][0]
    b = temp_name[-1]
    email_temp = a.lower()+"."+b.lower()+"@firma.cz"
    email.append(unidecode.unidecode(email_temp))
zamestnanci["email"] = tuple(email)

# vytvoreno
# vytvoreno = []
# for i in range(len(zamestnanci_list)):



        


        

        
    



        



print(zamestnanci)


