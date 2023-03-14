def name():
    nime = {"а":1, "б":2, "в":3, "г":4, "д":5, "е":6, "ё":7, "ж":8, "з":9,
            "и":1, "й":2, "к":3, "л":4, "м":5, "н":6, "о":7, "п":8, "р":9,
            "с":1, "т":2, "у":3, "ф":4, "х":5, "ц":6, "ч":7, "ш":8, "щ":9,
            "ъ":1, "ы":2, "ь":3, "э":4, "ю":5, "я":6}
    
    name = input("Sisestage teie nimi: ").lower()
    name_value = []
   
    for index, letter in enumerate(name):
        if letter in nime:
            value = nime[letter]
            name_value.append(value)
            print(f"{letter},{value}")
   
    name_sum = sum(name_value)
   
    print(f"Numbrid vastavate tähtedega {name_value}") #Цифры с соответствующими буквами
    print(f"Lisa kõik numbrid kokku ja sa saad arvu {name_sum}") #Складываем все числа, и получаем число {name_sum}