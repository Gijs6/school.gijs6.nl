---
subject: NAT
title: H1 & H6
description: Elektriciteit & onderzoeksvaardigheden
---

## Lading, energie en vermogen

Elektriciteit is **bewegende lading**. Verschillende ladingen trekken elkaar aan, dezelfde ladingen stoten elkaar af. De kleinste lading is de **elementaire lading** $e$ ($1{,}6 \cdot 10^{-19}\,\mathrm{C}$). Stroom kan alleen lopen als de stroomkring gesloten is. **Geleiders** zijn materialen die stroom doorlaten. **Isolatoren** laten geen stroom door. De stroomsterkte meet je met een **stroommeter** (in serie) en de spanning met een **spanningsmeter** (parallel).

Het **vermogen** is de hoeveelheid elektrische energie die per seconde wordt verbruikt.

$$P = U \cdot I$$

Hierin is $P$ het vermogen (in $\mathrm{W}$), $U$ de spanning (in $\mathrm{V}$) en $I$ de stroomsterkte (in $\mathrm{A}$).

$$W = P \cdot t$$

Hierin is $W$ de energie (in $\mathrm{J}$), $P$ het vermogen (in $\mathrm{W}$) en $t$ de tijd (in $\mathrm{s}$). Energie kun je ook meten in $\mathrm{kWh}$ ($1\,\mathrm{kWh} = 3{,}6\,\mathrm{MJ}$).

Het **rendement** van een apparaat is het deel van de ingaande energie dat wordt omgezet in nuttige energie.

$$\eta = \frac{W_\text{nut}}{W_\text{in}}$$

Hierin is $\eta$ het rendement (als getal; als percentage: $\times 100\%$), $W_\text{nut}$ de nuttige energie (in $\mathrm{J}$) en $W_\text{in}$ de ingaande energie (in $\mathrm{J}$).

## Spanning en stroomsterkte

In een metalen geleider zorgen **vrije elektronen** voor de stroom. In vloeistoffen kunnen ook **ionen** de stroom geleiden.

De **spanning** ($U$) geeft aan hoeveel elektrische energie elke coulomb lading heeft ($1\,\mathrm{V} = 1\,\mathrm{J}/\mathrm{C}$). De **stroomsterkte** ($I$) geeft aan hoeveel lading er per seconde langs een punt gaat ($1\,\mathrm{A} = 1\,\mathrm{C}/\mathrm{s}$). Per afspraak loopt de stroom van plus naar min, terwijl elektronen van min naar plus bewegen. Om schakelingen overzichtelijk te tekenen maak je gebruik van een **schakelschema**.

## Weerstand

De **weerstand** bepaalt hoeveel stroom er loopt bij een bepaalde spanning. Voor de weerstand geldt de **wet van Ohm**:

$$R = \frac{U}{I}$$

Hierin is $R$ de weerstand (in $\mathrm{\Omega}$), $U$ de spanning (in $\mathrm{V}$) en $I$ de stroomsterkte (in $\mathrm{A}$).

De **soortelijke weerstand** laat zien hoe goed of slecht een materiaal geleidt. Hoe langer en dunner de draad, hoe hoger de weerstand. De weerstand hangt vaak af van de temperatuur. Apparaten of draden waarbij de weerstand constant is, noem je **ohmse weerstanden**. Veel draden en apparaten hebben geen constante weerstand, omdat bij hogere spanningen de draden warm worden en dus een andere weerstand krijgen.

Een **schuifweerstand** is een speciale weerstand waarvan je de waarde makkelijk kan aanpassen. Een schuifweerstand kan op 2 manieren gebruikt worden: van A naar B (weerstand aanpasbaar) of van A naar C (weerstand vast). Een schuifweerstand kun je ook gebruiken om in een combinatieschakeling de spanning aan te passen. Een deel van de spanning wordt dan verdeeld over het lampje en het eerste deel van de schuifweerstand, en de rest valt over het rechterdeel. Door de grootte van het rechterdeel aan te passen, verandert de spanning over het lampje.

De weerstand van **halfgeleiders** kan worden aangepast door atomen toe te voegen. Een voorbeeld is de **diode**: een halfgeleider die stroom in één richting doorlaat. In de doorlaatrichting neemt het aantal vrije elektronen toe, in de sperrichting is het aantal vrije elektronen klein en loopt er geen stroom.

Er zijn ook speciale halfgeleidende weerstanden waarvan de weerstand afhankelijk is van omgevingsfactoren:

| Component | Effect |
| :-------- | :----- |
| **LDR** | Meer licht → lagere weerstand |
| **NTC** | Hogere temperatuur → lagere weerstand |
| **PTC** | Hogere temperatuur → hogere weerstand |

## Schakelingen in huis

In een huis zijn alle apparaten parallel aan elkaar geschakeld, zodat elk apparaat 230 V ontvangt. In een parallelschakeling wordt de stroomsterkte verdeeld tussen alle vertakkingen (**stroomdeling**). Elk apparaat heeft dus zijn eigen stroomkring. In een serieschakeling wordt de spanning juist over elk apparaat verdeeld (**spanningsdeling**). De stroomsterkte is dan overal hetzelfde.

|                   | Serieschakeling                           | Parallelschakeling                                                  |
| :---------------- | :---------------------------------------- | :------------------------------------------------------------------ |
| **Spanning**      | $U_\text{tot} = U_1 + U_2 + \ldots$      | $U_\text{tot} = U_1 = U_2 = \ldots$                                |
| **Stroomsterkte** | $I_\text{tot} = I_1 = I_2 = \ldots$      | $I_\text{tot} = I_1 + I_2 + \ldots$                                |
| **Weerstand**     | $R_\text{tot} = R_1 + R_2 + \ldots$      | $\frac{1}{R_\text{tot}} = \frac{1}{R_1} + \frac{1}{R_2} + \ldots$ |

In **combinatieschakelingen** gelden 2 wetten: de **wet van behoud van lading** (bij een splitsing blijft de totale stroom even groot) en de **wet van behoud van energie** (de energie van de bron is gelijk aan de totale energie die in de schakeling wordt omgezet). De formules pas je toe op de afzonderlijke delen.

Als er te veel apparaten op een **groep** worden aangesloten, kan de stroomsterkte boven 16 A uitkomen: **overbelasting**. Bij **kortsluiting** raken 2 elektriciteitsdraden elkaar, waardoor de stroom een "shortcut" neemt. De weerstand wordt dan heel klein en de stroomsterkte enorm groot. De **zekeringen** in de meterkast beveiligen elke groep door de stroom uit te zetten als de stroomsterkte te groot wordt.

Een **aardlekschakelaar** vergelijkt constant de ingaande en uitgaande stroomsterkte. Als het verschil groter is dan 30 mA, zet hij de stroom voor **het hele huis** uit.

## Significantie

Elk getal bestaat uit een aantal **significante cijfers**. Het aantal significante cijfers geeft aan hoe nauwkeurig iets gemeten is. Zo is 12,900 km nauwkeuriger dan 12,9 km. Bij het tellen van significante cijfers tellen alle cijfers mee, behalve nullen aan de voorkant. Het getal 0302,54030 heeft dus 8 significante cijfers. Het getal $8{,}74 \cdot 10^{23}$ heeft 3 significante cijfers.

Bij vermenigvuldigen en delen **moet** je afronden op het kleinste aantal significante cijfers van de gegevens. Voorbeeld: $3{,}44 \times 19{,}00 = 65{,}4$.  
Bij optellen en aftrekken let je op het aantal **decimalen**, niet op significante cijfers.

## Verbanden

Een **verband** beschrijft de relatie tussen 2 grootheden. In een formule (zoals $F = C \cdot u$) heb je een **afhankelijke grootheid** (gevolg), een **onafhankelijke grootheid** (oorzaak) en een constante. Bij een onderzoek pas je de onafhankelijke grootheid aan en kijk je wat dat doet met de afhankelijke grootheid.  
De meetgegevens presenteer je in een tabel: de onafhankelijke grootheid in de eerste kolom, de afhankelijke in de tweede, berekeningen in de overige kolommen. Noteer altijd eenheden bij meetgegevens en houd rekening met de **significantie**.

Hieronder staat een overzicht van verbanden. Hierin is $c$ de constante, $a$ de afhankelijke grootheid en $b$ de onafhankelijke grootheid.

|                                   | Formule                                           | Formule constante              | Vorm grafiek                                                            |
| :-------------------------------- | :------------------------------------------------ | :----------------------------- | :---------------------------------------------------------------------- |
| **Evenredig verband**             | $a = c \cdot b$                                   | $c = \frac{a}{b}$              | Een rechte lijn door de oorsprong                                       |
| **Omgekeerd evenredig verband**   | $a = \frac{c}{b}$, dus $a = c \cdot \frac{1}{b}$ | $c = a \cdot b$                | Een hyperbool, wel symmetrisch                                          |
| **Kwadratisch verband**           | $a = c \cdot b^2$                                 | $c = \frac{a}{b^2}$            | Een parabool door de oorsprong                                          |
| **Omgekeerd kwadratisch verband** | $a = \frac{c}{b^2}$, dus $a = c \cdot \frac{1}{b^2}$ | $c = a \cdot b^2$          | Lijkt op een hyperbool, maar is **niet** symmetrisch                    |
| **Wortelverband**                 | $a = c \cdot \sqrt{b}$                            | $c = \frac{a}{\sqrt{b}}$       | Lijkt op een omgekeerde parabool, een steeds minder hard stijgende lijn |

Een afwijkend verband is het **lineaire verband** met de formule $a = c \cdot b + d$. Deze lijn gaat niet door de oorsprong (als $d \neq 0$). De richtingscoëfficiënt $c$ bepaal je met 2 punten op de grafiek: $c = \frac{\Delta a}{\Delta b}$.

Met een **coördinatentransformatie** kun je bepalen met welk verband je te maken hebt. Een rechte lijn door de oorsprong is altijd een evenredig verband. Door de assen aan te passen (bij een kwadratisch verband: $b^2$ op de x-as, bij omgekeerd kwadratisch: $\frac{1}{b^2}$) krijg je een rechte lijn als het verband klopt.

De constante van een formule kun je bepalen door op 1 punt de grafiek af te lezen en dit in de bijbehorende formule in te vullen. Als je bij een wortelverband $a = 10$ en $b = 30$ afleest, weet je dat $c = \frac{a}{\sqrt{b}} = \frac{10}{\sqrt{30}} = 1{,}8$.

Bij het tekenen van **grafieken** gelden er een aantal regels:

- Logische schaalverdeling zodat punten goed verspreid zijn
- Grootheden en eenheden langs de assen
- Soepele lijn door zoveel mogelijk punten
- Cirkels om de punten (de punten zijn niet oneindig nauwkeurig)
