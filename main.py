app_token_bike = 'd28721be-fd2d-4b45-869e-9f253b554e50'
promo_id_bike = '43e35910-c168-4634-ad4f-52fd764a843f'
app_token_clone = '74ee0b5b-775e-4bee-974f-63e7f4d5bacb'
promo_id_clone = 'fe693b26-b342-4159-8808-15e3ff7f8767'
app_token_cube = 'd1690a07-3780-4068-810f-9b5bbf2931b2'
promo_id_cube = 'b4170868-cef0-424f-8eb9-be0622e8e8e3'
app_token_train = '82647f43-3f87-402d-88dd-09a90025313f'
promo_id_train = 'c4480ac7-e178-4973-8061-9ed5b2e17954'
app_token = '82647f43-3f87-402d-88dd-09a90025313f'
promo_id = 'c4480ac7-e178-4973-8061-9ed5b2e17954'
import time
import random
import string
import asyncio
import aiohttp
from colorama import init, Fore, Style
from fake_useragent import UserAgent
from datetime import datetime
percobaan = 20
nunggu = 20
init(autoreset=True)
ua = UserAgent()

def print_welcome_message():
    print(Fore.CYAN + r"""
          
█▀▀ █░█ ▄▀█ █░░ █ █▄▄ █ █▀▀
█▄█ █▀█ █▀█ █▄▄ █ █▄█ █ ██▄
          """ + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "\rKEYGEN HAMSTER KOMBAT")
    print(Fore.LIGHTYELLOW_EX + "\rTribute To All Member GHALIBIE")
    print(Fore.LIGHTYELLOW_EX + """
Please Choose the Voucher You Want to Get:
1. VOC BIKE
2. VOC TRAIN
3. VOC CUBE
4. VOC CLONE
5. VOC ALL
""" + Style.RESET_ALL)

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice in range(1, 6):
                return choice
            else:
                print(Fore.LIGHTRED_EX + "Invalid choice. Please enter a number between 1 and 5." + Style.RESET_ALL)
        except ValueError:
            print(Fore.LIGHTRED_EX + "Invalid input. Please enter a number." + Style.RESET_ALL)

def generate_client_id():
    timestamp = str(int(time.time() * 1000))
    random_digits = ''.join(random.choices(string.digits, k=19))
    return f"{timestamp}-{random_digits}"
def generate_event_id():
    first_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    second_part = ''.join(random.choices(string.digits, k=4))
    third_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
    fourth_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
    fifth_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))
    return f"{first_part}-{second_part}-{third_part}-{fourth_part}-{fifth_part}"
async def get_promo_code(app_token: str,promo_id: str,max_attempts: int,event_timeout: int):
    headers = {"Content-Type": "application/json; charset=utf-8", "Host": "api.gamepromo.io","User-Agent": ua.random}
    async with aiohttp.ClientSession(headers=headers) as http_client:
        client_id = generate_client_id()
        print(Fore.LIGHTCYAN_EX + "\rMulai...           ", end="", flush=True)
        json_data = {"appToken": app_token,"clientId": client_id,"clientOrigin": "deviceid"}
        response = await http_client.post(url="https://api.gamepromo.io/promo/login-client", json=json_data)
        response_json = await response.json()
        access_token = response_json.get("clientToken")
        if not access_token:
            print(Fore.LIGHTRED_EX + f"\rCoba ambil token lagi..", end="", flush=True)
            return
        http_client.headers["Authorization"] = f"Bearer {access_token}"
        await asyncio.sleep(delay=1)
        attempts = 0
        while attempts <= max_attempts:
            try:
                event_id = generate_event_id()
                json_data = {"promoId": promo_id,"eventId": event_id,"eventOrigin": "undefined"}
                response = await http_client.post(url="https://api.gamepromo.io/promo/register-event", json=json_data)
                response_json = await response.json()
                has_code = response_json.get("hasCode", False)
                if has_code:
                    json_data = {"promoId": promo_id}
                    response = await http_client.post(url="https://api.gamepromo.io/promo/create-code", json=json_data)
                    response_json = await response.json()
                    promo_code = response_json.get("promoCode")
                    if promo_code:
                        now = datetime.now()
                        dt_string = now.strftime("%d/%m %H:%M:%S")
                        print(Fore.LIGHTGREEN_EX + f"\r[ {dt_string} ] Pocer: {promo_code}  ", flush=True)
                        with open(output_file, 'a') as f:
                            f.write(f"{promo_code}\n")
                        return promo_code
            except Exception as error:
                print(Fore.LIGHTRED_EX + f"\rErrore: {error}", flush=True)
            attempts += 1
            print(Fore.LIGHTRED_EX + f"\rGagal {attempts}x | Coba lagi ke-{attempts + 1}-> {event_timeout} detik", end="", flush=True)
            await asyncio.sleep(delay=event_timeout)
    print(Fore.LIGHTRED_EX + f"\r{max_attempts}x nyoba, gak nemu Voucher")

print_welcome_message()
choice = get_user_choice()

if choice == 1:
    app_token, promo_id, output_file = app_token_bike, promo_id_bike, "voucher_hamster_bike1.txt"
elif choice == 2:
    app_token, promo_id, output_file = app_token_train, promo_id_train, "voucher_train_miner1.txt"
elif choice == 3:
    app_token, promo_id, output_file = app_token_cube, promo_id_cube, "voucher_chain_cube1.txt"
elif choice == 4:
    app_token, promo_id, output_file = app_token_clone, promo_id_clone, "voucher_clone_army1.txt"
elif choice == 5:
    vouchers = [
        (app_token_bike, promo_id_bike, "voucher_hamster_bike1.txt"),
        (app_token_train, promo_id_train, "voucher_train_miner1.txt"),
        (app_token_cube, promo_id_cube, "voucher_chain_cube1.txt"),
        (app_token_clone, promo_id_clone, "voucher_clone_army1.txt")
    ]

while True:
    if choice == 5:
        app_token, promo_id, output_file = random.choice(vouchers)
    acak = random.randint(1, 5)
    start = asyncio.run(get_promo_code(app_token, promo_id, percobaan, nunggu))
    print(f"\rJeda acak: {acak} detik           ", end="", flush=True)
    time.sleep(acak)
