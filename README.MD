# Генерация Metamask кошельков

Этот код позволит сгенерировать заданное количество Metamask кошельков и сохранить их в файлы.

## Установка зависимостей

Для работы кода необходимо установить следующие зависимости:
- openpyxl
- eth_account
- bip_utils

Вы можете установить их, используя команду:
```commandline
pip install openpyxl eth_account bip_utils
```
или:
```commandline
pip install -r requirements.txt
```
## Генерация кошельков
Чтобы сгенерировать Ethereum кошельки, запустите скрипт и введите количество кошельков, которые требуется сгенерировать.

```python
num_wallets = int(input("Введите количество кошельков для генерации: "))
wallets = generate_wallets(num_wallets)
save_wallets_to_xlsx(wallets, 'wallets.xlsx')
save_wallets_to_files(wallets)
print(f"{num_wallets} кошельков сгенерировано и сохранено в файлах")
```
## Сохранение в файлы

Сгенерированные кошельки сохраняются в несколько файлов:
- wallets.xlsx: Файл Excel (.xlsx), содержащий список кошельков с адресами, приватными ключами и сид-фразами.
- seeds.txt: Текстовый файл (.txt) с перечислением сид-фраз каждого кошелька.
- addresses.txt: Текстовый файл (.txt) с перечислением адресов каждого кошелька.
- private_key.txt: Текстовый файл (.txt) с перечислением приватных ключей каждого кошелька.

## Поддержка/Вопросы
Metamask: 0x52924cD11D8A41F99ECfD5eD4852d2489611E060

Telegram: @fraggdiller