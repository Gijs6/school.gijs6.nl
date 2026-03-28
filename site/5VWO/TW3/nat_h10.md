---
subject: NAT
title: H10
description: Zonnestelsel
---

## Cirkelbanen

Tussen 2 massa's, zoals de aarde en de maan, werkt een **gravitatiekracht**. Je kent deze kracht als de **zwaartekracht**. De gravitatiekracht grijpt aan in het zwaartepunt van het voorwerp.

De maan heeft precies de juiste snelheid om op die afstand van de aarde een **eenparige cirkelbeweging** uit te voeren. De **baansnelheid** (de snelheid waarmee een voorwerp langs een cirkel beweegt) heeft bij zo'n beweging een constante grootte, maar wel een steeds veranderende richting. Een verandering van de richting van de snelheid is ook een snelheidsverandering, en voor elke snelheidsverandering is een kracht nodig (2e wet van Newton). Deze kracht is de **middelpuntzoekende kracht**. Dit is een **rol** die een van de krachten op het voorwerp heeft (en is dus geen aparte kracht naast alle bestaande krachten). Deze kracht staat loodrecht op de baansnelheid en altijd in de richting van het middelpunt van de cirkelbaan.

In een draaimolen is de spankracht in het touw de middelpuntzoekende kracht. Bij een hemellichaam is dit de gravitatiekracht.

De benodigde middelpuntzoekende kracht voor een eenparige cirkelbeweging hangt af van de massa van het voorwerp, de baansnelheid en de straal van de cirkelbaan:

$$F_\text{mpz} = \frac{mv^2}{r}$$

Hierin is $F_\text{mpz}$ de middelpuntzoekende kracht (in $\mathrm{N}$), $m$ de massa (in $\mathrm{kg}$), $v$ de snelheid (in $\mathrm{m}/\mathrm{s}$) en $r$ de straal van de cirkelbaan (in $\mathrm{m}$).

De **omlooptijd** is de tijd die het voorwerp nodig heeft voor 1 rondje op de cirkelbaan.

$$T = \frac{2\pi r}{v}$$

Hierin is $T$ de omlooptijd (in $\mathrm{s}$), $r$ de straal van de cirkelbaan (in $\mathrm{m}$) en $v$ de baansnelheid (in $\mathrm{m}/\mathrm{s}$). Deze formule is afgeleid van de formule $t=\frac{s}{v}$. Hierin is $2\pi r$ gelijk aan $s$, want dat is de omtrek van de cirkelbaan.

## Gravitatiekracht

De **gravitatiekracht** is een wisselwerking tussen 2 massa's. Deze kracht is altijd voor beide massa's even groot, tegengesteld gericht, en hij werkt langs de lijn tussen de 2 zwaartepunten.

> De gravitatiekracht op 2 massa's is even groot, ook al zijn hun massa's dat niet, zoals bij de maan en de aarde. Dit lijkt misschien vreemd, maar het is eigenlijk heel logisch. De aarde veroorzaakt een grote zwaartekrachtsversnelling, maar de maan heeft een kleine massa, dus is de kracht van de aarde op de maan: grote versnelling op kleine massa. De maan veroorzaakt juist een kleine zwaartekrachtsversnelling, maar de aarde heeft een grote massa, dus is de kracht van de maan op de aarde: kleine versnelling op grote massa. Grote versnelling op kleine massa geeft dezelfde kracht als kleine versnelling op grote massa, waardoor de gravitatiekrachten op beide voorwerpen even groot zijn. <!-- Credits naar Mika voor zijn uitleg want dit staat heel raar in het boek waardoor ik er niets van snapte -->

De gravitatiekracht hangt af van de massa van beide voorwerpen en van de afstand tussen de massamiddelpunten.

$$F_g = G\frac{mM}{r^2}$$

Hierin is $F_g$ de gravitatiekracht (in $\mathrm{N}$), is $G$ de **gravitatieconstante** ($6{,}674 \cdot 10^{-11}\,\mathrm{N}\,\mathrm{m}^2\,\mathrm{kg}^{-2}$), zijn $m$ en $M$ de massa's van de 2 voorwerpen (in $\mathrm{kg}$) en is $r$ de afstand tussen de zwaartepunten (in $\mathrm{m}$).

De gravitatieconstante laat zien hoe groot de gravitatiekracht is tussen 2 voorwerpen van elk 1 kg op een afstand van 1 m. Die kracht is dus ongelofelijk klein, maar hij is er wel. En aangezien hemellichamen zeer grote massa's hebben, speelt de gravitatiekracht daar wel een rol.

De zwaartekracht is de gravitatiekracht aan het planeetoppervlak: $F_z = F_g$.

### Baansnelheden van hemellichamen

Als we de formules $F_g = G\frac{mM}{r^2}$ en $F_\text{mpz} = \frac{mv^2}{r}$ naast elkaar leggen, zie je dat de gravitatiekracht bij een grotere baanstraal sneller afneemt dan de benodigde middelpuntzoekende kracht (bij dezelfde baansnelheid). Daarom is de baansnelheid kleiner bij een grotere baanstraal.

Bij een cirkelbaan van de planeet geldt $F_\text{mpz} = F_g$ (aangezien de gravitatiekracht de middelpuntzoekende kracht is). Hieruit is een formule voor de baansnelheid af te leiden:

$$F_\text{mpz} = F_g \rightarrow \frac{mv^2}{r} = G\frac{mM}{r^2} \rightarrow v^2 = G\frac{M}{r} \rightarrow v = \sqrt{G\frac{M}{r}}$$

De baansnelheid is dus omgekeerd evenredig met de wortel van de baanstraal.

### Satellieten

Veel satellieten staan vanaf de aarde gezien op een vaste plaats boven een punt op de aarde, anders zou je niet op een satelliet kunnen richten met een schotelantenne. De baan van deze satellieten is een **geostationaire baan**. Een geostationaire baan is alleen mogelijk boven en evenwijdig aan de evenaar. De hoogte en snelheid van zo'n satelliet zijn dus zo gekozen dat de omlooptijd precies gelijk is aan de rotatietijd van de aarde: 23 uur, 56 minuten en 4 seconden. <!-- Misschien denk je: huh, dat is toch 24 uur? Maar nee! De tijd dat de aarde precies 360 graden heeft gedraaid is 23 uur, 56 minuten en 4,0905 seconden (oftewel 23,9344696 uur), en dit noemen we de siderische dag. Maar de siderische dag is niet hetzelfde als een gewone dag van 24 uur. Want als de aarde 360 graden heeft gedraaid, staat de zon niet meer op dezelfde positie aan de hemel, omdat de aarde ook een stukje verder om de zon is gedraaid. De aarde moet dus net iets meer dan 360 graden draaien voordat de zon weer op zijn hoogste punt staat. Stel je voor dat de zon om 12 uur precies op zijn hoogste punt staat: als je dan 23 uur, 56 minuten en 4 seconden later kijkt, staat de zon net iets voorbij zijn hoogste punt. Als je trouwens elke siderische dag zou kijken waar de zon staat, en je begon op 1 januari, dan zou je halverwege het jaar precies om middernacht kijken (oke, niet precies want schrikkeljaren). Want de aarde heeft dan een half rondje om de zon gemaakt, en als jij altijd kijkt wanneer de aarde 360 graden heeft gedraaid, kijk je altijd in dezelfde richting ten opzichte van de sterren. Stel dat je altijd naar links kijkt: als de aarde op 1 januari links van de zon staat, kijk je na een half jaar, wanneer de aarde rechts van de zon staat, precies van de zon af! -->

## Gravitatie-energie

De zwaartekracht kennen we inmiddels als de gravitatiekracht.

Bij berekeningen met een relatief klein hoogteverschil spraken we van de **zwaarte-energie**. Maar als we verder van de aarde af gaan, verandert de gravitatiekracht flink, en spreken we niet meer van de zwaarte-energie, maar van de **gravitatie-energie** ($E_g$).

De arbeid die nodig is om een voorwerp omhoog te brengen vanaf een afstand $r_1$ naar een afstand $r_2$ is gelijk aan de oppervlakte onder de $F_g,r$-grafiek tussen $r_1$ en $r_2$. De toename van de gravitatie-energie van een voorwerp is dus even groot als de arbeid die verricht wordt tegen de gravitatiekracht bij het optillen.

Bij energie-omzettingen van de zwaarte- of gravitatie-energie gaat het altijd om veranderingen in de hoeveelheid energie. Het maakt dus niet uit waar je het nulpunt legt. Voor zwaarte-energie doen we dit vaak op het aardoppervlak, zodat het voorwerp daar geen zwaarte-energie heeft. Bij de gravitatie-energie is het handig om dit nulpunt 'in het oneindige' te leggen. We zeggen dus dat een voorwerp op oneindig grote afstand een gravitatie-energie van 0 heeft. Hierdoor heeft de gravitatie-energie altijd een negatieve waarde.

Voor de gravitatie-energie geldt

$$E_g = -G \frac{mM}{r}$$

Hierin is $E_g$ de gravitatie-energie (in $\mathrm{J}$), $G$ de gravitatieconstante, $m$ de massa van het voorwerp (in $\mathrm{kg}$), $M$ de massa van het hemellichaam (in $\mathrm{kg}$) en $r$ de onderlinge afstand (in $\mathrm{m}$).

### Ontsnappingssnelheid

De **ontsnappingssnelheid** ($v_0$) is de snelheid waarbij een voorwerp dat je recht omhoog wegschiet niet meer terugkomt. De kinetische energie bij het lanceren is dan minstens even groot als de totale arbeid die tegen de gravitatiekracht in verricht moet worden.

Bij de minimale ontsnappingssnelheid heeft een voorwerp in het oneindige geen kinetische energie meer (de snelheid op dat punt is immers 0, en dus de kinetische energie ook). In het oneindige is ook de gravitatie-energie 0. Dit kunnen we invullen in een energievergelijking.

$$E_{k,A} + E_{g,A} = E_{k,B} + E_{g,B}$$

Hierin is punt $A$ het punt op het aardoppervlak en punt $B$ in het oneindige. Omdat $E_{k,B} + E_{g,B}$ gelijk is aan 0, kunnen we de formules voor de kinetische energie en de gravitatie-energie invullen en herschrijven naar een formule voor de ontsnappingssnelheid.

$$\frac{1}{2}mv^2 - G\frac{mM}{R} = 0 \rightarrow v_0 = \sqrt{\frac{2GM}{R}}$$

Hierin is $v_0$ de ontsnappingssnelheid (in $\mathrm{m}/\mathrm{s}$), $G$ de gravitatieconstante, $M$ de massa van het hemellichaam (in $\mathrm{kg}$) en $R$ de straal van het hemellichaam (in $\mathrm{m}$).

De ontsnappingssnelheid is groter naarmate de massa van de planeet groter is en groter naarmate de straal van de planeet kleiner is. De ontsnappingssnelheid is niet afhankelijk van de massa van het gelanceerde voorwerp.

> Een zwaarder voorwerp heeft wel meer energie nodig om te ontsnappen, maar het heeft bij dezelfde snelheid ook meer kinetische energie. Die twee houden elkaar precies in balans. Dit is hetzelfde als waarom alle voorwerpen even snel vallen: een zwaarder voorwerp wordt harder aangetrokken, maar heeft ook meer traagheid, zodat de versnelling gelijk blijft.
