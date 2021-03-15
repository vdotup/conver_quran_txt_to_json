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
        f.write("[\n")
        surahId = -1
        verseId = 0
        for i in range(len(array)):
            if "سُورَةُ" in array[i]:
                surahId += 1
                verseId = 0
                if surahId != 0:
                    # close previous verses array
                    f.write("\t\t]\n")
                    f.write("\t},\n")
                # open verses array
                f.write("\t{\n")
                f.write("\t\t" + "\"id\": " + str(surahId) + ",")
                f.write("\n\t\t\"verses\": [\n")
            f.write("\t\t\t{\n")
            f.write("\t\t\t\t" + "\"id\": " + str(verseId) + ",")
            f.write("\n\t\t\t\t" + "\"verse\": " +
                    "\"" + array[i].strip() + "\"")
            f.write("\n\t\t\t},\n")
            verseId += 1
        f.write("\t\t],\n")
        f.write("\t},\n")
        f.write("]")


def clean(text):
    cleaned = text.replace("\n", " ")
    cleaned = cleaned.replace("\t", " ")
    cleaned = cleaned.replace("  ", " ")
    cleaned = en_to_ar_num(cleaned)
    verses = [x for x in range(300)]
    verses = reversed(verses)
    for verse in verses:
        arN = en_to_ar_num(str(verse))
        cleaned = cleaned.replace(arN, ";")
    return cleaned


fullText = read("fullQuran.txt")
fullText = clean(fullText)
separated = re.split(";", fullText)
write(separated, 'output/result.json')
