def words(num):
    ones = [
        "Zero",
        "Nje",
        "Dy",
        "Tre",
        "Kater",
        "Pese",
        "Gjashte",
        "Shtate",
        "Tete",
        "nente",
    ]
    tens = [
        "",
        "Dhjete",
        "Njezet",
        "Tridhjete",
        "Dyzet",
        "Pesedhjete",
        "Gjashtedhjete",
        "Shtatedhjete",
        "Tetedhjete",
        "Nentedhjete",
    ]
    teens = [
        "Dhjete",
        "Njembedhjete",
        "Dymbedhjete",
        "Trembedhjete",
        "Katermbedhjete",
        "Pesembedhjete",
        "Gjashtembedhjete",
        "Shtatembedhjete",
        "Tetembedhjete",
        "Nentembedhjete",
    ]

    if num < 10:
        return ones[num]
    elif num < 20:
        return teens[num - 10]
    elif num < 100:
        return tens[num // 10] + ("" if num % 10 == 0 else "-" + ones[num % 10])
    elif num < 1000:
        return (
            words(num // 100)
            + " Qinde"
            + ("" if num % 100 == 0 else " e " + words(num % 100))
        )
    elif num < 1000000:
        return (
            words(num // 1000)
            + " Mije"
            + ("" if num % 1000 == 0 else " e " + words(num % 1000))
        )
    elif num < 1000000000:
        return (
            words(num // 1000000)
            + " Milion"
            + ("" if num % 1000000 == 0 else " e " + words(num % 1000000))
        )
    elif num < 1000000000000:
        return (
            words(num // 1000000000)
            + " Miliard"
            + ("" if num % 1000000000 == 0 else " e " + words(num % 1000000000))
        )
    elif num < 1000000000000000:
        return (
            words(num // 1000000000000)
            + " Triljard"
            + ("" if num % 1000000000000 == 0 else " e " + words(num % 1000000000000))
        )
    else:
        return "Number too large"
