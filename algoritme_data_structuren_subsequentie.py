# Gegeven twee lijsten X en Y.
# We zeggen dat X een 'subsequentie' is van Y als elk van de elementen van X
# in dezelfde volgorde voorkomen in Y, maar niet noodzakelijk op dezelfde posities.
# Bv. als X en Y strings zijn (en dus lijsten zijn van 'characters'), dan is de
# string "PLAT" een subsequentie van de string "AOPPPQRNMLA4DIPTPLA". De letters
# van "PLAT" zijn in dezelfde volgorde terug te vinden in "AOPPPQRNMLA4DIPTPLA",
# nl. als volgt:
#       "AO P PPQRNM L A 4DIP T PLA" (spaties werden toegevoegd om dit te verduidelijken)
#
# Nog enkele voorbeelden:
#      [1, 8, 5, 6] is een subsequentie van [10, 5, 1, 8, 1, 8, 5, 1, 8, 6]
#      [10, 5, 1, 8, 1, 8, 5, 1, 8, 6] is geen subsequentie van [1, 8, 5, 6]
#      [4, 9] is een subsequentie van [4, 9]
#      [ "alfa", "beta" ] is geen subsequentie van ["beta", "gamma", "dzeta", "alfa"]
#      [ ] is een subsequentie van ["beta", "gamma", "dzeta", "alfa"]
#      [ 5, "test" ] is een subsequentie van [ 10, 8, 5, "", "gamma", "test", "5"]
#
# Implementeer een algoritme dat nagaat of X een subsequentie is van Y.
#
# @param X    - een lijst van elementen (daar mag je vanuit gaan)
# @param Y    - een lijst van elementen (daar mag je vanuit gaan)
# @return     - een boolean die weergeeft of X een subsequentie is van Y
#
def is_subsequentie ( X, Y ):
    # vervang 'pass' door je eigen implementatie
    index = 0
    for i in Y:
        if X[index] == i:
            index += 1
    return index == len(X)-1



#################################################################################################
# Deze main-functie kan je gebruiken om zelf je programma te testen.                            #
# In deze main wordt het algoritme al voor een aantal gevallen getest.                          #
# Pas deze functie aan om functies afzonderlijk te testen, of om andere gevallen te testen.     #
# Er staan geen punten op deze main-functie.                                                    #
#################################################################################################
def main ():
    assert is_subsequentie([4], [4, 2]) == True
    assert is_subsequentie([5], [4, 2]) == False
    assert is_subsequentie([ ], ["beta", "gamma", "dzeta", "alfa"]) == True
    assert is_subsequentie([1, 8, 5, 6], [10, 5, 1, 8, 1, 8, 5, 1, 8, 6]) == True
    assert is_subsequentie([10, 5, 1, 8, 1, 8, 5, 1, 8, 6], [1, 8, 5, 6]) == False
    assert is_subsequentie([4, 9], [4, 9]) == True
    assert is_subsequentie([ "alfa", "beta" ], ["beta", "gamma", "dzeta", "alfa"]) == False
    assert is_subsequentie([ 5, "test" ], [ 10, 8, 5, "", "gamma", "test", "5"]) == True


# WIJZIG NIETS AAN DE LIJNEN HIERONDER
if __name__ == "__main__":
    main()
