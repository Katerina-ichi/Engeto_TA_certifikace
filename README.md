# Engeto_TA_certifikace
prostor pro odevzdani zaverecnych projektu

Soubor "Nemeckova_final_project_1.pdf" obsahuje testovaci scenare a vysledky testu dle zadani prvniho projektu, jehoz cilem bylo pomoci SQL Workbench a Postman otestovat REST rozhrani - manipulaci s daty studentu pomoci metod GET, POST a DELETE.

Soubor "test_clickandfeed.py" obsahuje automatické testy pro webovou stranku www.clickandfeed.cz dle zadani druheho projektu, jehoz cilem bylo pouziti frameworku Playwright. Testy kontroluji rychlost nacteni stranky, funkci hlavniho tlacitka na "naplneni misky" (a overeni, ze druhy klik jiz misku nenaplni) a funkci rozbalovaciho menu. Test probiha pouze v prohlizecich chromium a firefox, protoze webkit na Linuxu s Playwright zatim neni stabilni.

platform linux -- Python 3.12.3, pytest-8.3.4, pluggy-1.5.0 -- plugins: playwright-0.7.0, base-url-2.1.0
