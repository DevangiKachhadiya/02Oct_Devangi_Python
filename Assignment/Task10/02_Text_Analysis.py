#  Text Analysis with Constraints.
'''Given a large paragraph of text, write a Python program that:
• Counts the frequency of each word, ignoring common stop words (the, is, at, on, in, and,
etc.).
• Allows efficient querying, for example:
• "Return the top 3 most frequent words starting with the prefix 'th'."
• Optimize for performance.
'''

from collections import Counter

stop_words = {"the", "is", "at", "on", "in", "and"}

def text_analysis(text, prefix=None, top_n=3):
    words = [word.lower() for word in text.split() if word.lower() not in stop_words]
    word_count = Counter(words)
    if prefix:
        filtered_words = {word: count for word, count in word_count.items() if word.startswith(prefix)}
        return dict(sorted(filtered_words.items(), key=lambda item: item[1], reverse=True)[:top_n])
    return word_count.most_common(top_n)

text = "The quick brown fox jumped over the lazy dog. The fox was quick."
print(text_analysis(text, prefix="qu", top_n=3))
