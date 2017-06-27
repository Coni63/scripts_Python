from functions import *

class New_Simulation():
    def __init__(self, account, setting):
        self.setup = setting
        self.start_val = account
        self.pet = account.pet
        self.kero = account.kero
        self.money = account.money
        self.acc = account.acc
        self.diams = account.diams
        self.loop = 0
        self.factor = self.setup.event_factor.value() * self.setup.ratio_factor.value()
        self.gain = int(self.acc / 10000 * self.factor)
        self.result_pet = [self.pet]
        self.result_kero = [self.kero]
        self.result_money = [self.money]
        self.result_acc = [self.acc]
        self.result_gain = [self.gain]
        self.result_loop = [self.loop]
        self.result_diams = [self.diams]

    def run(self, i):
        while self.diams > 0:
            # achat de pet
            Qty_pet = int(self.money * self.setup.HB_ratio.value() / (self.setup.trade_ratio.value() * 500))
            Prix_pet = int(Qty_pet * 500 * self.setup.trade_ratio.value())
            self.pet += Qty_pet
            self.money -= Prix_pet
            # print("Achat de %s pet pour %s $" % (convert(Qty_pet), convert(Prix_pet)))

            # conversion en kero
            Qty_kero = self.pet
            self.kero += Qty_kero
            self.pet = 0
            self.money -= 3 * Qty_kero
            # print("Raffinage en %s de kero" % Qty_kero)

            # calcul nouveau val de compte
            index = [500, 4 * (10 * 500 + 3), (5 * 500 + 2), 7, 1, 1000]
            values = [self.pet, self.kero,  self.start_val.diesel,  self.start_val.muni, self.money,  self.start_val.gold]
            self.acc = sum([int(a * b) for a, b in zip(index, values)])
            # print("Nouvelle valeur de compte %s" % convert(self.temp_acc))

            # calcul du gain par diams
            self.gain = int(self.acc / 10000 * self.factor)
            # print("Gain de %s $/diams" % convert(Gain))

            # Trade
            Qte_diams = min(self.diams, i)
            self.money += Qte_diams * self.gain
            self.diams -= Qte_diams
            # print("Nouveau Hors Banque %s" % convert(self.temp_money))
            # print("Diams restant %s" % self.temp_diam)

            self.loop += 1

            #ajout des valuer dans le tableau
            self.result_pet.append(self.pet)
            self.result_kero.append(self.kero)
            self.result_money.append(self.money)
            self.result_acc.append(self.acc)
            self.result_gain.append(self.gain)
            self.result_loop.append(self.loop)
            self.result_diams.append(self.diams)

class Account:
    def __init__(self):
        self.pet = 0
        self.kero = 0
        self.diesel = 0
        self.muni = 0
        self.money = 0
        self.gold = 0
        self.diams = 1
        self.acc = 0
        self.keys = ["pet", "kero", "diesel", "muni", "money", "gold", "diams", "acc"]

    def return_as_object(self):
        values = [self.pet, self.kero, self.diesel, self.muni, self.money, self.gold, self.diams, self.acc]
        return dict(zip(self.keys, values))

    def update(self, dictionnaire):
        self.pet = dictionnaire.get("pet",0)
        self.kero = dictionnaire.get("kero",0)
        self.diesel = dictionnaire.get("diesel",0)
        self.muni = dictionnaire.get("muni",0)
        self.money = dictionnaire.get("money",0)
        self.gold = dictionnaire.get("gold",0)
        self.diams = dictionnaire.get("diams",0)
        self.acc = dictionnaire.get("acc", 0)
        self.account_value()

    def account_value(self):
        index = [500, 4*(10*500+3), (5*500+2), 7, 1, 1000]
        values = [self.pet, self.kero, self.diesel, self.muni, self.money, self.gold]
        self.acc = sum([a * int(b) for a, b in zip(index, values)])

    def reset_account(self):
        self.pet = 0
        self.kero = 0
        self.diesel = 0
        self.muni = 0
        self.money = 0
        self.gold = 0
        self.diams = 1
        self.acc = 0


