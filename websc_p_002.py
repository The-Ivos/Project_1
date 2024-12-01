from bs4 import BeautifulSoup as bs
import requests
import sys

def get_web():
    url = sys.argv[1]
    base_url_og = url.split("/")
    url_praha.append(base_url_og[-1])
    print(url_praha)
    base_url_og.pop(-1)
    base_url_og = "/".join(base_url_og)+"/"
    base_url.append(base_url_og)

    web = requests.get(url).content
    soup = bs(web,"html.parser")

    return soup

def get_locations(location):
    links = []
    locations = location.find_all(class_="cislo")
    for cislo in locations:
        link_number = cislo.find("a").get("href")
        links.append(f"{base_url[0]}{link_number}")
    # print(links)
    return links

def get_results(list_of_locs):
    elections_header = ""
    for location in list_of_locs:
        elections = {}
        web = requests.get(location).content
        soup = bs(web,"html.parser")
        party_list = soup.find_all(class_="overflow_name")
        delimiter_code = "obec="
        loc_code = location[location.find(delimiter_code)+len(delimiter_code):location.find("&xvyber")]
        # print(loc_code)
        elections["code"] = loc_code

        delimiter_name = "Obec: "
        if "kraj=1" in url_praha[0]:
            loc_name = (soup.select_one("#publikace > h3:nth-child(3)").getText()).strip()
        else:
            loc_name = (soup.select_one("#publikace > h3:nth-child(4)").getText()).strip()
        loc_name = loc_name[loc_name.find(delimiter_name)+len(delimiter_name):]
        elections["location"] = loc_name

        voters = soup.find("td",{"headers":"sa2"}).getText()
        elections["registered"] = voters

        envelopes = soup.find("td",{"headers":"sa3"}).getText()
        elections["envelopes"] = envelopes

        valid = soup.find("td",{"headers":"sa6"}).getText()
        elections["valid"] = valid

        parties = soup.find_all(class_="overflow_name")
        parties_votes1 = soup.find_all("td",{"headers":"t1sa2 t1sb3"})
        parties_votes2 = soup.find_all("td", {"headers": "t2sa2 t2sb3"})
        parties_votes = parties_votes1 + parties_votes2

        # print(parties)

        for i in range(len(parties)):
            if "," in parties[i].getText():
                elections[parties[i].getText().replace(",","-")] = parties_votes[i].getText()
            else:
                elections[parties[i].getText()] = parties_votes[i].getText()
            # print(parties[i].getText(),parties_votes[i].getText())


        # print(len(parties))
        # print(len(parties_votes1),len(parties_votes2))
        # print(len(parties_votes))


        elections_keys = ",".join(list(elections.keys()))
        elections_header = elections_keys
        elections_values = ",".join(list(elections.values()))
        ele_cont.append(elections_values)
        # print(f"{elections_keys}\n{elections_values}")
        # print(",".join(list(elections.keys()))+"\n"+",".join(list(elections.values())))



    ele_header.append(elections_header)

        # for strana in party_list:
        #     print(strana.getText())




if len(sys.argv) < 2:
    print("nic, sorry!")
else:
    url_praha = []
    base_url = []
    ele_header = []
    ele_cont = []

    get_results(get_locations(get_web()))
    # print("ele header:",ele_header[0])
    # for i in ele_cont:
    #     print(i)

    with open(sys.argv[2],"w",encoding="utf-8") as file:
        file.write(ele_header[0]+"\n")
        for i in ele_cont:
            file.write(i+"\n")

    print(url_praha)

    # print("base url:",base_url)


