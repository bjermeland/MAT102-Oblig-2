import math
import RSA as rsa

# Variabler
n = 104523733
e = 137

# Hjelpemetoder
alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def tekstTilTall(s):
    tab = ""
    for bokstav in s:
        bokstav = bokstav.lower()
        if bokstav.isspace():
            tall = "99"
        else:
            tall = "%.2d" % (ord(bokstav) - 97)
        tab += tall
    return [int(tab[x:x + 8]) for x in range(0, len(tab), 8)]


def tallTilTekst(s):
    res = ""
    for i in s:
        i = str(i)
        if len(i) % 2 != 0:
            i = "0" + i
        for j in range(0, len(i) - 1, 2):
            tall = i[j:j + 2]
            if tall == "99":
                res += " "
            else:
                res += chr(int(tall) + 97)
    return res


# a) Dekrypter beskjeden [1041706, 4139999]
T = [1041706, 4139999]
print('a)', tallTilTekst(T))

# b) Kod meldingen HEI SJEF
print('b) HEI SJEF kodet = ', tekstTilTall("HEI SJEF"))


# c) Krypter meldingen HEI SJEF
print('c) HEI SJEF kryptert = ', rsa.RSA_encrypt(n, e, [7040899, 18090405]))

# d) Finn primtallene p og q slik at n = pq
sqrt = int(math.sqrt(n))
primtall = rsa.eratosthenes(sqrt)
for i in primtall:
    if n % i == 0:
        p = i

q = n//p
print('d) p og q = ', p, q)

# e) Sjekk om nokkelen er valid (p, q, e)
print('e) Er nokkel valid = ', rsa.check_key(p, q, e))

# f) Regn ut dekrypteringsnokkelen (n, d) og kontroller svaret
d = rsa.mult_inverse(e, (p-1)*(q-1))
print('f) d = ', d)
T = [80423654, 65341395]  # kryptert representasjon fra "HEI SJEF"i c)
print('Kontrollerer svaret = ', rsa.RSA_encrypt(
    n, d, T) == [7040899, 18090405])

# g) Dekrypter og dekod den hemmelig beskjeden U
U = [16646055, 76586540, 40429350, 81029513, 98012653, 6683466]
P = rsa.RSA_encrypt(n, d, U)
print('g) Dekryptert = ', P)
print('Dekodet = ', tallTilTekst(P))
