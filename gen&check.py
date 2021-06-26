import time
import os

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')

import random
import string
import ctypes

try:
    from discord_webhook import DiscordWebhook
except ImportError:
    input(f"A 'discord_webhook' module nincs letöltve, '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nNyomj Entert a kilépéshez")
    exit()
try:
    import requests
except ImportError:
    input(f"A 'requests' module nincs letöltve, '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nNyomj Entert a kilépéshez")
    exit()


class NitroGen:
    def __init__(self):
        self.fileName = "Nitro kódok.txt"

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if os.name == "nt":
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW("Nitro Generátor and Ellenőző - by ! Barni#7207")
        else:
            print(f'\33]0;Nitro Generátor és Ellenőrző - by ! Barni#7207\a', end='', flush=True)

        print("""██████╗░░█████╗░███╗░░░███╗███╗░░██╗
██╔══██╗██╔══██╗████╗░████║████╗░██║
██║░░██║███████║██╔████╔██║██╔██╗██║
██║░░██║██╔══██║██║╚██╔╝██║██║╚████║
██████╔╝██║░░██║██║░╚═╝░██║██║░╚███║
╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚══╝
                                                        """)
        time.sleep(2)
        self.slowType("by ! Barni#7207", .02)
        time.sleep(1)
        self.slowType("\nÍrd be, hogy mennyi kódot szeretnél generálni és ellenőrizni: ", .02, newLine = False)

        num = int(input(''))

        self.slowType("\nSzeretnél használni discord webhookot? \nÍrd be ide, ha nem akkor nyomj Entert: ", .02, newLine = False)
        url = input('')
        webhook = url if url != "" else None

        valid = []
        invalid = 0

        for i in range(num):
            try:
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                ))
                url = f"https://discord.gift/{code}"

                result = self.quickChecker(url, webhook)

                if result:
                    valid.append(url)
                else:
                    invalid += 1
            except Exception as e:
                print(f" Hiba | {url} ")

            if os.name == "nt":
                ctypes.windll.kernel32.SetConsoleTitleW(f"Nitro Generátor és Ellenőrző - {len(valid)} Működő | {invalid} Nem működő - by ! Barni#7207")
                print("")
            else:
                print(f'\33]0;Nitro Generátor és Ellenőrző - {len(valid)} Működő | {invalid} Nem működő - by ! Barni#7207\a', end='', flush=True)

        print(f"""
Végeredmény:
 Működő: {len(valid)}
 Nem működő: {invalid}
 Működő linkek: {', '.join(valid )}""")

        input("\nVége a folyamatnak! Ha be szeretnéd zárni a progtamot, akkor nyomd meg 5x az Entert!")
        [input(i) for i in range(4,0,-1)]


    def slowType(self, text, speed, newLine = True):
        for i in text:
            print(i, end = "", flush = True)
            time.sleep(speed)
        if newLine:
            print()

    def generator(self, amount):
        with open(self.fileName, "w", encoding="utf-8") as file:
            print("Váj egy kicsit... Generálás folyamatban...")

            start = time.time()

            for i in range(amount):
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                ))

                file.write(f"https://discord.gift/{code}\n")

            print(f"Legenerálva {amount} kód | Igénybe vett idő: {round(time.time() - start, 5)}s\n")

    def fileChecker(self, notify = None):
        valid = []
        invalid = 0
        with open(self.fileName, "r", encoding="utf-8") as file:
            for line in file.readlines():
                nitro = line.strip("\n")

                url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

                response = requests.get(url)

                if response.status_code == 200:
                    print(f" Működő | {nitro} ")
                    valid.append(nitro)

                    if notify is not None:
                        DiscordWebhook(
                            url = notify,
                            content = f"Működő Nitro link sikeres keresése! @everyone \n{nitro}"
                        ).execute()
                    else:
                        break

                else:
                    print(f" Nem működő | {nitro} ")
                    invalid += 1

        return {"valid" : valid, "invalid" : invalid}

    def quickChecker(self, nitro, notify = None):
        url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200:
            print(f" Működő | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n")
            with open("Nitro kódok.txt", "w") as file:
                file.write(nitro)

            if notify is not None:
                DiscordWebhook(
                    url = notify,
                    content = f"Működő Nitro link sikeres keresése! @everyone \n{nitro}"
                ).execute()

            return True

        else:
            print(f" Nem működő | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n")
            return False

if __name__ == '__main__':
    Gen = NitroGen()
    Gen.main()
