from pprint import pprint

def vytvor_slovnik(**kwargs):
    slovnik = dict()

    for i,j in kwargs.items():
        slovnik[i] = j
    
    return slovnik

pprint(vytvor_slovnik(
 jmeno="Ivos", prijmeni="Srot", vek=36, email="srot.ivo@gmail.com"),sort_dicts=False,width=1)