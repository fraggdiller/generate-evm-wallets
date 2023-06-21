# main.py
from utils.wallet_generator import WalletGenerator

num_wallets = int(input("Введите количество кошельков для генерации: "))

wallet_generator = WalletGenerator(num_wallets)
wallet_generator.generate_wallets()

print(f"{num_wallets} кошельков сгенерировано и сохранено в файлах")
