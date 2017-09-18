
from unidecode import unidecode

def remove_accents(s):
    t=unidecode(s)
    t.encode("ascii")  #works fine, because all non-ASCII from s are replaced with their equivalents
    return(t)  #gives: 'Montreal, uber, 12.89, Mere, Francoise, noel, 889'



o_sentence = raw_input("Please enter the sentence you want to encrypt: ")
converted_sentence = o_sentence.replace(" ","") #Removing spaces
converted_sentence
converted_sentence = remove_accents(o_sentence)



print converted_sentence
