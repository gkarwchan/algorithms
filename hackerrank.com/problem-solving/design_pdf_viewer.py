def designerPdfViewer(h, word):
    a_ord = ord('a')
    maxHeight = max(map(lambda x: h[x], list(map(lambda l: ord(l) - a_ord, word))))
    return maxHeight * len(word)
