import re


def en_to_ar_num(number_string):
    lis = []
    dic = {
        '0': '٠',
        '1': '١',
        '2': '٢',
        '3': '٣',
        '4': '٤',
        '5': '٥',
        '6': '٦',
        '7': '٧',
        '8': '٨',
        '9': '٩',
    }
    for char in number_string:
        if char in dic:
            lis.append(dic[char])
        else:
            lis.append(char)
    return "".join(lis)


def read(name):
    print("reading")
    f = open(name, encoding="utf8")
    return f.read()


def write(array, name):
    print('writing')
    with open(name, "w", encoding="utf8") as f:
        output = ""
        output += "[\n"
        surahId = -1
        surahName = ""
        verseId = 0
        for i in range(len(array)):
            if "#" in array[i]:
                verse = array[i].strip()
                surahName = verse.split("#")[0]
                surahId += 1
                verseId = 0
                if surahId != 0:
                    # close previous verses array
                    output += "\t\t]"
                    output += "\n\t},\n"

                output += "\t{\n"
                output += "\t\t" + "\"id\": " + str(surahId) + ","
                output += "\n\t\t" + \
                    "\"name\": {\n\t\t\t\"ar\": " + "\"" + \
                    surahName.strip() + "\"\n\t\t},"
                # open verses array
                output += "\n\t\t\"verses\": [\n"

            output += "\t\t\t{\n"
            output += "\t\t\t\t" + "\"id\": " + str(verseId) + ","
            if verseId == 0 and surahId == 0:
                # add basmalah as first verse to fatihah only
                output += "\n\t\t\t\t" + \
                    "\"verse\": {\n\t\t\t\t\t\"ar\": " + "\"" + \
                    "بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ" + "\"\n\t\t\t\t}"
            elif verseId == 0:
                verse = array[i].strip().split("#")
                output += "\n\t\t\t\t" + \
                    "\"verse\": {\n\t\t\t\t\t\"ar\": " + "\"" + \
                    verse[1].strip() + "\"\n\t\t\t\t}"
            else:
                output += "\n\t\t\t\t" + \
                    "\"verse\": {\n\t\t\t\t\t\"ar\": " + "\"" + \
                    array[i].strip() + "\"\n\t\t\t\t}"

            output += "\n\t\t\t},\n"
            verseId += 1
        output += "\t\t],\n"
        output += "\t},\n"
        output += "]"
        output = output.replace("},\n\t\t]", "}\n\t\t]")
        output = output.replace("],\n\t},", "]\n\t}")
        f.write(output)


def clean(text):
    cleaned = text.replace("\n", " ")
    cleaned = cleaned.replace("\t", " ")
    cleaned = cleaned.replace("  ", " ")
    cleaned = cleaned.replace("إِنَّهُۥ مِن سُلَيۡمَٰنَ وَإِنَّهُۥ بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ",
                              "%")
    cleaned = cleaned.replace("بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ", "#")
    cleaned = cleaned.replace("بِّسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ", "#")

    cleaned = cleaned.replace("%",
                              "إِنَّهُۥ مِن سُلَيۡمَٰنَ وَإِنَّهُۥ بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ")
    cleaned = cleaned.replace("سُورَةُ التَّوۡبَةِ بَرَآءَةٞ مِّنَ ٱللَّهِ وَرَسُولِهِۦٓ إِلَى ٱلَّذِينَ عَٰهَدتُّم مِّنَ ٱلۡمُشۡرِكِينَ",
                              "سُورَةُ التَّوۡبَةِ#بَرَآءَةٞ مِّنَ ٱللَّهِ وَرَسُولِهِۦٓ إِلَى ٱلَّذِينَ عَٰهَدتُّم مِّنَ ٱلۡمُشۡرِكِينَ")
    cleaned = en_to_ar_num(cleaned)

    # save for debug
    with open("debug.txt", "w", encoding="utf8") as f:
        f.write(cleaned)
    #
    verses = [x for x in range(300)]
    verses = reversed(verses)
    for verse in verses:
        arN = en_to_ar_num(str(verse))
        cleaned = cleaned.replace(arN, ";")
    return cleaned


fullText = read("fullQuran.txt")
fullText = clean(fullText)
separated = re.split(";", fullText)
print("[" + separated[len(separated)-1] + "]")
for item in separated:
    if item == " ":
        separated.remove(item)
write(separated, 'output/result.json')
