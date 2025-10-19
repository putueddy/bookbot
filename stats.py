def count_words(text):
    return len(text.split())


def chars_freq(text):
    exclude = set(" !@#$%^&*(),.”-'_;:[]{}’—‘•1234567890\t\n?™“/\ufeff")
    freq = {}
    for c in text.lower():
        if not c.isspace() and c not in exclude:
            freq[c] = freq.get(c, 0) + 1

    list = []
    for k, v in freq.items():
        list.append({"char": k, "count": v})

    list.sort(reverse=True, key=sort_on)
    return list


def sort_on(items):
    return items["count"]
