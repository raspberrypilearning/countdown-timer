## Aftellen met tekst

Laten we eerst aftellen van 5 naar 0 door getallen weer te geven met behulp van het pixeldisplay van de Sense HAT.

+ Open de afteltimer starttrinket: <a href="http://jumpto.cc/timer-go" target="_blank">jumpto.cc/timer-go</a>
    
    **De code voor het instellen van de Sense HAT is voor je meegeleverd.**

+ Je gaat tot 5 tellen, want dat is makkelijker. Voeg de gemarkeerde code onder aan je script toe:
    
    ![schermafbeelding](images/timer-count.png)
    
    Het commando `sense.show_letter()` geeft een enkele letter op de Sense HAT weer. Het staat geen getallen toe, dus je moet `str()` gebruiken om het getal te wijzigen in een formaat dat het kan weergeven.
    
    `sleep(1)` wacht een seconde voordat de code doorgaat naar de volgende stap.

+ In Python geeft `range(1, 6)` de getallen 1 tot en met 5. Je hoeft niet alleen met stappen van 1 te tellen:
    
    + range(1, 10, 2) zou in in stappen van 2 tellen, wat 1, 3, 5, 7 en 9 geeft
    + range(5, 0, -1) telt af met 1 door er steeds -1 af te halen, en geeft 5, 4, 3, 2, 1
    
    Wijzig de range in je code zodat deze aftelt naar 0:
    
    ![schermafbeelding](images/timer-numbers.png)

+ Het getal op de LED's hoeft niet wit te zijn — de Sense HAT kan veel kleuren tonen. Het gebruikt RGB kleuren (rood, groen en blauw).
    
    Probeer groen te gebruiken:
    
    ![schermafbeelding](images/timer-green.png)