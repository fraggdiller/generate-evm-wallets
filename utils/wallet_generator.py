# wallet_generator.py
from eth_account import Account
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes
from utils.wallet import Wallet
from utils.wallet_saver import WalletSaver


class WalletGenerator:
    def __init__(self, num_wallets):
        self.num_wallets = num_wallets
        self.wallets = []

    def generate_wallets(self):
        for _ in range(self.num_wallets):
            mnemonic_generator = Bip39MnemonicGenerator()
            mnemonic = mnemonic_generator.FromWordsNumber(words_num=12)
            seed = Bip39SeedGenerator(mnemonic).Generate()
            bip_obj = Bip44.FromSeed(seed, Bip44Coins.ETHEREUM)

            private_key = bip_obj.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0).PrivateKey().Raw().ToBytes()
            account = Account.from_key(private_key)

            wallet = Wallet(
                mnemonic=mnemonic,
                address=account.address,
                private_key=private_key.hex()
            )

            self.wallets.append(wallet)

        wallet_saver = WalletSaver()
        wallet_saver.save_wallets_to_files(self.wallets)
