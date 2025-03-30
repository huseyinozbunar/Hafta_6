print(tam_link)
with open('ist.txt', 'a', encoding="utf-8") as file: # Corrected indentation
    file.write(tam_link + "\n")

listem = [
    'https://www.milligazete.com.tr/arsiv/2025-03-22', # Replace ‘ with '
    'https://www.milligazete.com.tr/arsiv/2025-03-23', # Replace ‘ with '
    'https://www.milligazete.com.tr/arsiv/2025-03-24', # Replace ‘ with '
    'https://www.milligazete.com.tr/arsiv/2025-03-25', # Replace ‘ with '
    'https://www.milligazete.com.tr/arsiv/2025-03-26'  # Replace ‘ with '
]

for s in listem:
    haber_linklerini_getir(s)