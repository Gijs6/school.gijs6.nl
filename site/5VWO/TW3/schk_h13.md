---
subject: SCHK
title: H13
description: Zuren & basen 2
---

## Zwakke zuren en basen

De **sterkte** van een zuur geeft aan hoe graag het zuur een $\ce{H+}$ wil weggeven: een **sterk zuur** geeft graag $\ce{H+}$ af, een **zwak zuur** minder graag. Hetzelfde geldt voor basen: een **sterke base** neemt graag $\ce{H+}$ op, een **zwakke base** minder graag.

### Zwak of sterk?

In Binas 49 staat een overzicht van de sterktes van zuren en basen. Het sterkste zuur staat linksbovenin, en hoe verder naar beneden, hoe zwakker het zuur. De (theoretische) grens ligt bij $\ce{H3O+}$: alles erboven is sterk, alles eronder zwak.

Bij basen ligt de grens bij $\ce{OH-}$: alles eronder is sterk, daarboven zwak.

## Zuren oplossen

Als je het sterke zuur $\ce{HZ}$ oplost in water, lost het eerst op:

$$\ce{HZ (l) ->[{opl.}] HZ (aq)}$$

Omdat het een sterk zuur is, **ioniseert** $\ce{HZ (aq)}$ volledig. De totale reactie is dus:

$$\ce{HZ (l) ->[{opl.}] HZ (aq) + H2O (l) -> H3O+ + Z-}$$

Je schrijft een $\ce{HZ}$-oplossing dus als $\ce{H3O+ + Z-}$, niet als $\ce{HZ (aq)}$. Het ion $\ce{Z-}$ dat overblijft na het afstaan van $\ce{H+}$ heet de **geconjugeerde base** van $\ce{HZ}$.

Bij het zwakke zuur $\ce{HB}$ verloopt het oplossen hetzelfde:

$$\ce{HB (l) ->[{opl.}] HB (aq)}$$

Maar een zwak zuur ioniseert niet volledig. Er ontstaat een evenwicht:

$$\ce{HB (l) ->[{opl.}] HB (aq) <--> H3O+ + B-}$$

De schrijfwijze van een $\ce{HB}$-oplossing is dus $\ce{HB (aq)}$.

## Basen oplossen

Basen zijn onderdeel van een zout, en zouten ioniseren altijd volledig bij het oplossen in water. Na het oplossen kan de base een $\ce{H+}$ opnemen uit water. Hoe sterker de base, hoe beter dit gaat.

De base $\ce{NaH}$ is sterk en ioniseert volledig:
$$\ce{NaH (s) -> Na+ + H-}$$
$$\ce{H- + H2O (l) -> H2 (g) + OH-}$$
Samen: $\ce{NaH (s) + H2O (l) -> Na+ + H2 (g) + OH-}$

De base $\ce{Na2CO3}$ is zwak, en de ionisatie verloopt slechts gedeeltelijk:
$$\ce{Na2CO3 (s) -> 2 Na+ + {CO3}^{2-}}$$
$$\ce{{CO3}^{2-} + H2O (l) <--> HCO3- + OH-}$$

## pH berekenen

### Sterke zuren en basen

Bij sterke zuren en basen geldt:

- $\mathrm{pH} = -\log [\ce{H3O+}]$
- $[\ce{H3O+}] = 10^{-\mathrm{pH}}$
- $\mathrm{pOH} = -\log [\ce{OH-}]$
- $[\ce{OH-}] = 10^{-\mathrm{pOH}}$
- $\mathrm{pH} + \mathrm{pOH} = 14$

> Het aantal significante cijfers in de concentratie bepaalt het aantal decimalen van de p(O)H.

### Zwakke zuren en basen

Bij een zwak zuur ioniseert het niet volledig, dus is $[\ce{H3O+}]$ kleiner dan de concentratie van het opgeloste zuur. Om de pH te berekenen, stel je een BOEC-schema op voor de oplossingsreactie. Bij een **meerwaardig zuur** (dat meerdere $\ce{H+}$ kan afstaan) zijn de verdere ionisatiestappen te verwaarlozen, dus kijk je alleen naar de eerste.

> Voorbeeld: bereken de pH van een $\ce{HF}$-oplossing van 0,100 M.
>
> De oplossingsreactie is:
>
> $$\ce{HF (aq) + H2O (l) <--> H3O+ + F-}$$
>
> Stel dat $x$ de concentratie is die ioniseert. Het BOEC-schema wordt dan (water is weggelaten):
>
> |                      | $\ce{HF (aq)}$ | $\ce{H3O+}$ | $\ce{F-}$ |
> | -------------------- | -------------- | ----------- | --------- |
> | **B**egin (mol)      | 0,100          | 0           | 0         |
> | **O**mzetting (mol)  | $-x$           | $+x$        | $+x$      |
> | **E**venwicht (mol)  | $0{,}100 - x$  | $x$         | $x$       |
> | **C**oncentratie (M) | $0{,}100 - x$  | $x$         | $x$       |
>
> De **zuurconstante** $K_z$ (in Binas 49) is voor $\ce{HF}$ gelijk aan $6{,}3 \cdot 10^{-4}$. Dit invullen:
>
> $$K_z = \frac{[\ce{H3O+}][\ce{F-}]}{[\ce{HF}]} = \frac{x \cdot x}{0{,}100 - x} = 6{,}3 \cdot 10^{-4}$$
>
> Je kunt $x$ op twee manieren uitrekenen.
>
> **Door te verwaarlozen**
>
> Als $x$ heel klein is, kun je zeggen dat $0{,}100 - x \approx 0{,}100$:
>
> $$x^2 = 6{,}3 \cdot 10^{-4} \times 0{,}100 = 6{,}3 \cdot 10^{-5}$$
> $$x = \sqrt{6{,}3 \cdot 10^{-5}} = 7{,}9 \cdot 10^{-3}~\mathrm{M}$$
>
> **Met de ABC-formule**
>
> Herschrijf de vergelijking:
>
> $$x^2 + 6{,}3 \cdot 10^{-4} \cdot x - 6{,}3 \cdot 10^{-5} = 0$$
>
> Met de ABC-formule (alleen de positieve oplossing):
>
> $$x = \frac{-6{,}3 \cdot 10^{-4} + \sqrt{(6{,}3 \cdot 10^{-4})^2 + 4 \cdot 6{,}3 \cdot 10^{-5}}}{2} = 7{,}6 \cdot 10^{-3}~\mathrm{M}$$
>
> Zodra je $x$ hebt berekend, kun je de pH berekenen (aangezien $x = [\ce{H3O+}]$):
>
> $$\mathrm{pH} = -\log(x)$$

Bij een zwakke base werkt het hetzelfde, alleen gebruik je de **baseconstante** $K_b$ (ook in Binas 49) en is $x = [\ce{OH-}]$. Je berekent dan eerst de pOH en daarna de pH via $\mathrm{pH} = 14 - \mathrm{pOH}$.

## Verhouding bij een ingesteld pH

Naast dat je de pH bij een bepaalde concentratie kunt berekenen, kun je ook de verhouding tussen zuur en base berekenen bij een gegeven pH.

Stel je hebt een $\ce{HNO2}$-oplossing bij een pH van 2,0, en je wilt de verhouding $[\ce{NO2-}] : [\ce{HNO2}]$ berekenen. Je stelt dan eerst de reactievergelijking op:

$$\ce{HNO2 + H2O (l) <--> H3O+ + NO2-}$$

Vervolgens stel je de evenwichtsvoorwaarde op:

$$K_z = \frac{[\ce{H3O+}][\ce{NO2-}]}{[\ce{HNO2}]}$$

Je kunt dit herschrijven als:

$$\frac{K_z}{[\ce{H3O+}]} = \frac{[\ce{NO2-}]}{[\ce{HNO2}]}$$

Uit de pH volgt $[\ce{H3O+}] = 10^{-2{,}0} = 0{,}010~\mathrm{M}$. De $K_z$ van $\ce{HNO2}$ staat in Binas 49. Dit invullen geeft de verhouding:

$$\frac{[\ce{NO2-}]}{[\ce{HNO2}]} = \frac{5{,}6 \cdot 10^{-4}}{0{,}010} = 5{,}6 \cdot 10^{-2}$$

De verhouding $[\ce{NO2-}] : [\ce{HNO2}]$ is dus $0{,}056 : 1$.

## Omzettingspercentage

Het omzettingspercentage geeft aan hoeveel procent van het zuur geïoniseerd is. Je berekent eerst de verhouding (zoals hierboven), en vult die daarna in, waarbij $\ce{HA}$ het zuur is en $\ce{A-}$ de geconjugeerde base:

$$\text{omzettingspercentage} = \frac{[\ce{A-}]}{[\ce{HA}] + [\ce{A-}]} \cdot 100\%$$

> Voorbeeld: bereken het omzettingspercentage van $\ce{HF}$ bij een pH van 2,5.
>
> Eerst de verhouding berekenen. Uit de pH volgt $[\ce{H3O+}] = 10^{-2{,}5} = 3{,}2 \cdot 10^{-3}~\mathrm{M}$:
>
> $$\frac{[\ce{F-}]}{[\ce{HF}]} = \frac{K_z}{[\ce{H3O+}]} = \frac{6{,}3 \cdot 10^{-4}}{3{,}2 \cdot 10^{-3}} = 0{,}20$$
>
> De verhouding $[\ce{F-}] : [\ce{HF}]$ is dus $0{,}20 : 1$. Dit invullen:
>
> $$\text{omzettingspercentage} = \frac{0{,}20}{1 + 0{,}20} \cdot 100\% = 17\%$$

## Buffers

Een **bufferoplossing** is een oplossing van een zwak zuur met zijn geconjugeerde base, in ongeveer even grote hoeveelheden. De pH verandert niet (of amper) als er zuur, base of water wordt toegevoegd. De bufferwerking is het beste als de concentratie van het zwakke zuur zo dicht mogelijk bij de concentratie van de geconjugeerde base ligt.

De pH van een bufferoplossing kun je op twee manieren berekenen: met de evenwichtsvoorwaarde of met de **bufferformule**.

Als je de concentratie van het zwakke zuur $[\ce{HB}]$ en de concentratie van de geconjugeerde base $[\ce{B-}]$ weet, kun je deze invullen in de (omgebouwde) evenwichtsvoorwaarde:

$$[\ce{H3O+}] = K_z \cdot \frac{[\ce{HB}]}{[\ce{B-}]}$$

De bufferformule is:

$$\mathrm{pH} = \mathrm{p}K_z - \log \frac{n_z}{n_b} = \mathrm{p}K_z + \log \frac{n_b}{n_z}$$

Hierin is $n_z$ het aantal mol zwak zuur en $n_b$ het aantal mol geconjugeerde base.

## Zuur-base reacties

Bij het opstellen van zuur-basereacties moet je goed opletten wat je beginstoffen zijn. Kijk dus goed of je te maken hebt met een sterk of zwak zuur en wat de bijbehorende oplossing is.

Bij een zuur-basereactie zijn er twee mogelijkheden: een aflopende reactie of geen reactie. Bij een zuur-basereactie kan er nooit een evenwicht zijn. Dat kan alleen bij een zwak zuur of zwakke base die je oplost in water.

Als het zuur boven de base staat in Binas 49, is er een aflopende reactie. Als het zuur onder de base staat, is er geen reactie. Als het zuur en de base op dezelfde regel staan, heb je geen zuur-basereactie, maar een oplossing van een zwak zuur met zijn geconjugeerde base. Er is dan wel een evenwicht.

Voor meerwaardige zuren geldt dat er $\ce{H+}$-overdracht plaatsvindt zolang het zuur boven de base staat.

> Voorbeeld: $\ce{H3PO4}$ (fosforzuur) met $\ce{NH3}$.
>
> Per stap kijk je of het zuur boven $\ce{NH3}$ staat:
>
> - $\ce{H3PO4}$ staat boven $\ce{NH3}$, dus er is een reactie: $\ce{H3PO4 + NH3 -> H2PO4- + NH4+}$
> - $\ce{H2PO4-}$ staat ook boven $\ce{NH3}$, dus er is weer een reactie: $\ce{H2PO4- + NH3 -> HPO4^{2-} + NH4+}$
> - $\ce{HPO4^{2-}}$ staat onder $\ce{NH3}$, dus er is geen reactie meer.
>
> Fosforzuur reageert dus in twee stappen met ammoniak. De volledige reactie is:
>
> $$\ce{H3PO4 + 2 NH3 -> HPO4^{2-} + 2 NH4+}$$

## Titraties

Met een titratie kun je de concentratie (en dus de pH) van een oplossing bepalen. Een titratie bestaat uit de volgende stappen:

1. Pak met een pipet een beetje van de oplossing
2. Doe hier een indicator bij
3. Druppel met een buret het zuur of de base in de oplossing, tot de kleur van de oplossing omslaat
4. Lees op de buret af hoeveel mL je hebt toegevoegd

Op het **equivalentiepunt** is het aantal mol zuur gelijk aan het aantal mol base:

$$n_\text{zuur} = n_\text{base}$$

Omdat $n = c \cdot V$ geldt:

$$c_\text{zuur} \cdot V_\text{zuur} = c_\text{base} \cdot V_\text{base}$$

Hierin is $V_\text{zuur}$ het volume dat je met de pipet hebt afgemeten, en $V_\text{base}$ het volume dat je uit de buret hebt laten lopen. Hiermee kun je de onbekende concentratie berekenen.

Je voert een titratie minimaal twee keer uit. De afwijking tussen de twee metingen moet kleiner zijn dan 2,5%, anders meet je opnieuw:

$$\text{afwijking} = \frac{|V_1 - V_2|}{V_1 + V_2} \times 100\%$$

### Terugtitraties

Bij stoffen die tijdens de titratie kunnen verdampen of wegreageren, gebruik je een **terugtitratie** (zoals bij $\ce{NH3}$). Je voegt dan eerst een overmaat $\ce{H3O+}$ toe:

$$\ce{NH3 + H3O+ -> NH4+ + H2O (l)}$$

Er blijft nu een klein beetje $\ce{H3O+}$ over. Het aantal mol $\ce{NH3}$ is gelijk aan het aantal mol $\ce{H3O+}$ dat gereageerd heeft:

$$n_{\ce{NH3}} = n_{\ce{H3O+},\text{begin}} - n_{\ce{H3O+},\text{over}}$$

Het aantal mol $\ce{H3O+}$ aan het begin bereken je uit de concentratie en het volume:

$$n_{\ce{H3O+},\text{begin}} = [\ce{H3O+}] \cdot V_{\ce{H3O+},\text{begin}}$$

Het aantal mol $\ce{H3O+}$ dat overblijft bepaal je door terug te titreren met $\ce{OH-}$:

$$\ce{H3O+ + OH- -> 2 H2O (l)}$$

Op het omslagpunt geldt $n_{\ce{H3O+},\text{over}} = n_{\ce{OH-}}$, en $n_{\ce{OH-}}$ bereken je uit de concentratie en het volume van de gebruikte $\ce{OH-}$-oplossing.

### Titratiecurve

Een **titratiecurve** is een grafiek van de pH tegen het toegevoegde volume. De curve heeft een S-vorm, waarbij het equivalentiepunt in het midden van de steile stijging ligt.

### Indicator kiezen

Je kiest een indicator waarvan het **omslagtraject** (het pH-gebied waarin de kleur verandert) rondom het equivalentiepunt valt. De pH bij het equivalentiepunt hangt af van de combinatie zuur en base:

| Zuur  | Base  | pH bij equivalentiepunt |
| ----- | ----- | ----------------------- |
| Sterk | Sterk | 7                       |
| Sterk | Zwak  | < 7                     |
| Zwak  | Sterk | > 7                     |
| Zwak  | Zwak  | onvoorspelbaar          |

Met een zwak zuur en een zwakke base kun je geen titratie uitvoeren, omdat er geen scherpe sprong in de titratiecurve is.
