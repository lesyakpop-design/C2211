from colorama import init, Fore, Back, Style


init(autoreset=True)

# ---------- КОЛЬОРИ ТЕКСТУ (Fore) ----------
print(Fore.RED + "Це червоний текст")        # Fore.RED — змінює колір тексту на червоний
print(Fore.GREEN + "Це зелений текст")       # Fore.GREEN — зелений текст
print(Fore.BLUE + "Це синій текст")          # Fore.BLUE — синій текст
print(Fore.YELLOW + "Це жовтий текст")       # Fore.YELLOW — жовтий текст
print(Fore.WHITE + "Це білий текст")         # Fore.WHITE — білий текст

# ---------- КОЛЬОРИ ФОНУ (Back) ----------
print(Back.RED + "Червоний фон")             # Back.RED — змінює фон тексту
print(Back.GREEN + "Зелений фон")            # Back.GREEN — зелений фон
print(Back.BLUE + "Синій фон")               # Back.BLUE — синій фон

# Style.RESET_ALL — скидає ВСІ стилі (колір тексту, фон і стиль)
print(Fore.RED + "Червоний" + Style.RESET_ALL + " звичайний")

# ---------- ПРИКЛАД КОМБІНАЦІЇ ----------
print(Fore.YELLOW + Back.BLUE + Style.BRIGHT + "Комбінований стиль")
# Жовтий текст + синій фон + яскравий стиль