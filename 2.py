def search_keywords(text):
    keywords = ['sang gajah', 'serigala', 'harimau']
    result = []
    for keyword in keywords:
        count = text.count(keyword)
        result.extend([keyword] * count)
    return ' - '.join(result)

# Contoh pemanggilan fungsi dengan teks sebagai masukan
input_text = "Berikut adalah kisah sang gajah. Sang gajah memiliki teman serigala bernama DoeSang. Gajah sering dibela oleh serigala ketika harimau mendekati gajah."
output = search_keywords(input_text)
print(output)