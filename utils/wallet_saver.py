import csv
import os


class WalletSaver:
    @staticmethod
    def save_wallets_to_csv(wallets, file_name):
        file_path = os.path.join('data', file_name)

        with open(file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(["Mnemonic", "Address", "Private Key"])

            for wallet in wallets:
                writer.writerow([wallet.mnemonic, wallet.address, wallet.private_key])

    @staticmethod
    def save_wallets_to_files(wallets):
        WalletSaver._save_to_file(wallets, 'seeds.txt', 'mnemonic')
        WalletSaver._save_to_file(wallets, 'addresses.txt', 'address')
        WalletSaver._save_to_file(wallets, 'private_keys.txt', 'private_key')
        WalletSaver.save_wallets_to_csv(wallets, 'wallets.csv')

    @staticmethod
    def _save_to_file(wallets, file_name, attribute):
        file_path = os.path.join('data', file_name)
        with open(file_path, 'w') as f:
            for wallet in wallets:
                f.write(f"{getattr(wallet, attribute)}\n")
