text = """Primele jocuri video au fost realizate între anii 1950 și 1960 de Jon Snell și rulau pe platforme cum ar fi osciloscopul, sau computere EDSAC. 
Cel mai vechi joc pe calculator, o simulare de rachete, a fost creat în 1947 de către Thomas T. Goldsmith Jr. și de Estle Ray Mann. 
O cerere pentru acordarea de drepturi de autor a fost făcută pe 25 ianuarie 1947 și patentată ca U.S. Patent #2,455,992 din data de 14 decembrie 1948. 
Mai târziu în 1952, o versiune a jocului X și 0 numită Noughts and Crosses a fost creată de A. S. Douglas ca parte a disertației de doctorat la Universitatea din Cambridge. 
Jocul rula pe un computer al universității numit Electronic Delay Storage Automatic Calculator (EDSAC). 
În 1958 William Higinbotham - care a ajutat să se construiască prima bombă atomică - a creat Tennis For Two în laboratoarele naționale din Brookhaven, situate în Upton, New York, pentru a distra vizitatorii laboratorului. 
În 1962 Steve Russel a creat jocul Spacewar!, un joc de simulare spațială. 
Programul rula pe un DEC PDP-1 și este considerat de mulți specialiști atât primul joc pentru calculator cât și printre cele mai importante realizate vreodată. 
Jocul s-a răspândit rapid la universități și laboratoare de cercetare din țară. 
În 1968 Ralph Baer, care va fi cunoscut mai târziu și ca Părintele Jocurilor Video, a patentat o versiune a unei console de jocuri numită Television Gaming and Training Apparatus. 
În 1967, Baer a creat un joc gen ping-pong pentru consolă care semăna cu Tennis for Two (și cu viitorul joc arcade Pong). 
A lucrat cu Magnavox și a creat în 1972 prima consolă, numită Magnavox Odyssey."""


# Lungime
lungime = len(text)
jumatate = lungime//2
prima=text[:jumatate]
text_doi=text[jumatate:]

#Partea 1
upper = prima.upper()
strip = upper.strip()

#Partea 2
intoarcere = text_doi[::-1]
capitalize = text_doi.capitalize()
a = text_doi.replace(",", "")
b = a.replace(".", "")
c = b.replace("!", "")
d = c.replace("?", "")

#Partea 3

print (strip+d)

