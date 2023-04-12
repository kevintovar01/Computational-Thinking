#jazz, pop, rock, hip hop, Opera, punk, Soul, Reggae, Electronic, Country, Classical, Heavy metal, Alternative, Folk, Gospel, Blues


choise = {
        "Frutas":{      
            "rojas":{            #fresas, cerezas, -- platanos, limones, mangos -- naranjas -- uvas -- kiwis
                "grandes":"fresas",
                "pequenas":"cerezas"
            },
            "amarillas":{
                "dulces":{
                            "grandes":"fresas",
                            "pequenas":"cerezas"
                        },
                "acidos":"limon"
            },

            "naranja":"naranja",
            "moradas":"uvas",
            "verde":"kiwis"
        },

        "Animales":{       
            "mamiferos":{
                "hervivoro":"caballo",
                "carnivoro": "orca"
            },
            "peces":{
                "grande": "manta_raya",
                "pequeno": "pez payaso"
            },
            "reptiles":{
                "grande": "cocodrilo",
                "pequeno": "serpiente" 
            },
            "aves":{
                "altos":"avestruz",
                "bajos":"pinguinos"
            }
        }
    }


def tree_of_decisions(choise):
    for key,value in choise.items():
        if input(f"Es {key}: ").lower() == "si":
            if type(value) == dict:
                choise = value
                break
            else:
                print(value)
                return 
    
    tree_of_decisions(choise)

if __name__ == '__main__':
    tree_of_decisions(choise)
    