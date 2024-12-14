import random as r
meme_dict = {
            "CHAMBA": "Una forma de decir trabajo",
            "GIGACHAD": "Para hacer referencia a un hombre exitoso",
            "LOL": "Es un metodo usado cuando te ríes a carcajadas",
            "":""
            }

print(meme_dict.keys())
word = input("Escribe una palabra que no entiendas o escribe sorprendeme: ").upper()

if word in meme_dict.keys():
    print ("significado de", word,":",meme_dict [word]) 
    # ¿Qué debemos hacer si se encuentra la palabra?
elif word == "SORPRENDEME":
    ramdom = r.choice(list(meme_dict.keys()))
    print("La palabra que conoceras es",ramdom,":",meme_dict[ramdom])
else: 
    print("Esta palabra aun no existe")
    # ¿Qué hacer si no se encuentra la palabra?
