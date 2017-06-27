from bs4 import BeautifulSoup as bs
import requests
import time


def buy(ID, qte):
    global SessID
    print("buying {} pet from offer {}".format(qte, ID))
    url = "http://game.desert-operations.fr/world1/handel.php"
    data = {"tid": ID, "splitted_count" : qte, "buy": "OK"}
    with requests.Session() as s:
        s.headers.update({'cookie': SessID})
        r = s.post(url, data)
        soup = bs(r.text, 'html.parser')
        restricted_soup = str(soup)[-500:]
        if restricted_soup.find("moins 10 secondes") > -1:
            print("Il faut attendre 10s avant chaque achat")
            print("Pause 10s !")
            time.sleep(10)
        elif restricted_soup.find("acquisition") > -1:
            print("Achat effectué avec succes")
            print("Pause 10s !")
            time.sleep(10)
        else:
            print("Oops, bug qq part, l'offre n'existe plus ou il n'y a plus la qté")
            print("Pause 5s, puis retest !")
            time.sleep(5)
    main()


def to_num(val):
    return int(val.replace(',', ''))


def check_offers():
    global max_possible, SessID
    url = 'https://game.desert-operations.fr/world1/handel.php?mode=1&object_id=r_3&goods_partly=1&search_goods=Chercher'
    with requests.Session() as s:
       s.headers.update({'cookie': SessID})
       r = s.get(url)
    soup = bs(r.text, 'html.parser')
    #print(soup.prettify())

    offres = soup.findAll("form", {"class": "tradeBuyOffer"})[:-1]
    print("{} offres disponibles".format(len(offres)))

    if default_selected:
        max_possible = to_num(offres[0].find_all("span", {"class": "tooltipExtention showTooltipDefault"})[2].get('data'))
        print("Vous pouvez acheter au mieux {} pet".format(max_possible))

    for offre in offres[:-1]:
        tid = offre.find("input", {"name": "tid"}).get("value")
        is_lot = (offre.find("input", {"class": "adjNumInput"}) is not None)
        tooltips = offre.find_all("span", {"class": "tooltipExtention showTooltipDefault"})
        qty_offer = to_num(tooltips[0].get('data'))
        limite = max_possible // 10

        qty_to_buy = 0
        if is_lot:
            if qty_offer >= limite:
                qty_to_buy = min(qty_offer, max_possible)
        else:
            if limite <= qty_offer <= max_possible:
                qty_to_buy = qty_offer

        if qty_to_buy > 0:
            buy(tid, qty_to_buy)
            max_possible -= qty_to_buy

    print("Pause 10s ! et restart")
    time.sleep(10)
    main()

def main():
    global max_possible
    if max_possible > SEUIL:
        print("Recherche des offres")
        check_offers()
    else:
        print("Fini !!!")
        return False


if __name__ == "__main__":
    SEUIL = 10E3
    SessID_input = input("Enter your PHP Session ID (format PHPSESSID=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX) :")
    SessID = 'PHPSESSID=' + SessID_input
    expected_qty = input("Enter the expected amount of Pet you want (max = maximum amout possible of pet you can purchase)")
    if expected_qty == "max":
        default_selected = True
    else:
        default_selected = False
        max_possible = to_num(expected_qty)
    if default_selected:
        res = "le max de"
    else:
        res = max_possible
    start = input("votre Session ID est {} - vous desirez acheter {} pet. OK ? Y/N".format(SessID, res))
    if start in ["Y", "y", "yes", "Yes", "YES"]:
        main()
    else:
        print('Bye !')