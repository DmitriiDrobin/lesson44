def all_variants(text):
    len(text)
    for i in range(1, len(text) + 1):
        for l in range(len(text) - i + 1):
            yield text[l:l + i]

a = all_variants("abc")
for i in a:
    print(i)