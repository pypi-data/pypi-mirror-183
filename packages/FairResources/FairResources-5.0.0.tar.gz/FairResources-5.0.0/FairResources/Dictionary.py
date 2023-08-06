import FairResources

def simple_word_lookup(word):
    dic = FairResources.load_json("english_dictionary")
    word_upper = str(word).upper()
    if word_upper in dic:
        return dic[word_upper]
    return "Word Not Found."
