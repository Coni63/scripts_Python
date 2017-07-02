from bs4 import BeautifulSoup as bs
import requests
import time

def to_num(val):
    return int(val.replace(',', ''))

class Bot:
    def __init__(self, PHP_Sess_ID, qte=-1):
        self.seuil = 10e16 # 1C
        self.qty_requested = qte
        self.PHP_Sess_ID = PHP_Sess_ID
        self.qty_remaining = qte
        self.limite = max(qte // 10, self.seuil)

    def buy(self, ID, qte):
        print("buying {} pet from offer {}".format(qte, ID))
        url = "http://game.desert-operations.fr/world1/handel.php"
        data = {"tid": ID, "splitted_count" : qte, "buy": "OK"}
        with requests.Session() as s:
            s.headers.update({'cookie': SessID, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'})
            r = s.post(url, data)
        soup = bs(r.text, 'html.parser')
        restricted_soup = str(soup)[-500:]
        if restricted_soup.find("moins 10 secondes") > -1:
            print("Il faut attendre 10s avant chaque achat")
            print("Pause 10s !")
            time.sleep(10)
        elif restricted_soup.find("acquisition") > -1:
            print("Achat effectué avec succes")
            self.qty_remaining -= qte
            print("Pause 10s !")
            time.sleep(10)
        else:
            print("Oops, bug qq part, l'offre n'existe plus ou il n'y a plus la qté")
            print("Pause 5s, puis retest !")
            time.sleep(5)
        return 1


    def check_offers(self):
        url = 'https://game.desert-operations.fr/world1/handel.php?mode=1&object_id=r_3&goods_partly=1&search_goods=Chercher'
        with requests.Session() as s:
            s.headers.update({'cookie': SessID, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'})
            r = s.get(url)
        soup = bs(r.text, 'html.parser')
        #print(soup.prettify())

        offres = soup.findAll("form", {"class": "tradeBuyOffer"})[:-1]
        print("{} offres disponibles".format(len(offres)))

        status = 0

        if len(offres) > 0:
            if self.qty_requested == -1:
                max_possible = to_num(offres[0].find_all("span", {"class": "tooltipExtention showTooltipDefault"})[2].get('data'))
                print("Vous pouvez acheter au mieux {} pet".format(max_possible))
                self.qty_requested = max_possible
                self.qty_remaining = max_possible
                self.limite = max(max_possible // 10, 10e16)

            for offre in offres[:-1]:
                tid = offre.find("input", {"name": "tid"}).get("value")
                is_lot = (offre.find("input", {"class": "adjNumInput"}) is not None)
                tooltips = offre.find_all("span", {"class": "tooltipExtention showTooltipDefault"})
                qty_offer = to_num(tooltips[0].get('data'))

                qty_to_buy = 0
                if is_lot:
                    if qty_offer >= self.limite:
                        qty_to_buy = min(qty_offer, self.qty_remaining)
                else:
                    if self.limite <= qty_offer <= self.qty_remaining:
                        qty_to_buy = qty_offer

                if qty_to_buy > 0 and status == 0:
                    status = self.buy(tid, qty_to_buy)
        
        if status == 0:
            print("Pause 10s ! et restart\n")
            time.sleep(10)
        self.main()

    def main(self):
        global qty_requested
        if self.qty_remaining > self.seuil or self.qty_remaining == -1:
            print("Recherche des offres")
            self.check_offers()
        else:
            print("Fini !!!")
            return False


if __name__ == "__main__":
    SessID_input = input("Enter your PHP Session ID (format PHPSESSID=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX) :")
    SessID = 'PHPSESSID=' + SessID_input
    expected_qty = input("Enter the expected amount of Pet you want (max = maximum amout possible of pet you can purchase)")
    if expected_qty == "max":
        qty_requested = -1
        phrase = "le max de"
    else:
        qty_requested = to_num(expected_qty)
        phrase = qty_requested

    start = input("votre Session ID est {} - vous desirez acheter {} pet. OK ? Y/N".format(SessID, phrase))
    if start.lower() in ["y", "yes", "1", "true", "o", "oui"]:
        bot = Bot(SessID, qty_requested)
        bot.main()
    else:
        print('Bye !')