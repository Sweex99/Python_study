#!/usr/bin/env python3

def to_samples(amount: float) -> str:
    if amount >= 1000000: raise ValueError('Not supporter over million')
    sample = []
    numbers = {1: 'один', 2: 'два', 3: 'три', 4: 'чотири', 5: 'п\'ять', 6: 'шість', 
    7: 'сім', 8: 'вісім', 9: 'дев\'ять', 10: 'десять', 11: 'одинадцять',
    12: 'дванадцять', 13: 'тринадцять', 14: 'чотирнадцять', 15: 'п\'ятнадцять',
    16: 'шістнадцять', 17: 'сімнадцять', 18: 'вісімнадцять', 19: 'дев\'ятнадцять',
    20: 'двадцять', 30: 'тридцять', 40: 'сорок', 50: 'п\'ятдесят', 60: 'шістдесят', 
    70: 'сімдесять', 80: 'вісімдесять', 90: 'дев\'яносто', 100: 'сто',
    200: 'двісті', 300: 'триста', 400: 'чотириста', 500: 'п\'ятсот', 600: 'шістсот',
    700: 'сімсот', 800: 'вісімсот', 900: 'дев\'ятсот', 0: ''}
    lst = list(str(int(amount * 100)))
    rate = 5
    index = -(rate + 2)
    while lst[index] == '1' and index != -1:
        lst[index] += lst[index + 1]
        lst[index + 1] = '0'
        index += 3
    while len(lst) > rate:
        poped = lst.pop(0)
        sample.append(numbers[int(poped) * 10 ** (len(lst) - len(poped) - rate + 1)])
    if "один" in sample:
        sample[sample.index("один")] = "одна"
        sample.append("тисяча")
    elif "два" in sample:
        sample[sample.index("два")] = "дві"
        sample.append("тисячі")
    else: sample.append("тисяч")
    rate -= 3
    while len(lst) > rate:
        poped = lst.pop(0)
        sample.append(numbers[int(poped) * 10 ** (len(lst) - len(poped) - rate + 1)])
    if "один" in sample:
        sample[sample.index("один")] = "одна"
        sample.append("гривня")
    elif "два" in sample:
        sample[sample.index("два")] = "дві"
        sample.append("гривні")
    else: sample.append("гривень")
    coins = int(''.join(lst))
    sample.append(str(coins))
    if coins > 10 and coins < 20: sample.append("копійок")
    elif coins % 10 > 1 and coins % 10 < 5: sample.append("копійки")
    elif coins % 10 == 1: sample.append("копійка")
    else: sample.append("копійок")
    return ' '.join(' '.join(sample).split()).capitalize()

print(to_samples(float(input("Input your amount: "))))
