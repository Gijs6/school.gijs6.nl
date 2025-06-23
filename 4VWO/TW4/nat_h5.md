---
layout: summary
title: NAT - H5 - Samenvatting
test_code: 4A-NAT-T07
---

# Natuurkunde: Hoofdstuk 5 (Ioniserende straling)

## Röntgenstraling

**Röntgenstraling** is een vorm van elektromagnetische straling. Net als zichtbaar licht bestaat het uit **fotonen** (energiepakketjes). Door de hoge frequentie heeft röntgenstraling relatief veel energie en kan het dwars door je lichaam heen gaan.

De fotonenergie is evenredig met de frequentie:

$$E_f = hf$$

Hierin is $E_f$ de fotonenergie (in $\text{J}$), $h$ de constante van Planck ($\approx 6{,}626 \cdot 10^{-34} \ \text{J} \ \text{s}$) en $f$ de frequentie (in $\text{Hz}$).  
Soms wordt **elektronvolt** ($\text{eV}$) gebruikt als eenheid voor energie: $1 \ \text{eV}= 1{,}6 \cdot 10^{-19} \ \text{J}$.

Het **ioniserend vermogen** is het vermogen om elektronen uit atomen los te maken.  
Het **doordringend vermogen** is het gemak waarmee straling door huid en weefsel dringt.

![De eerste röntgenfoto ooit (img-medium)](images/nat_h5_rontgenfotohand.jpg)

Op röntgenfoto's zie je donkere en lichte gebieden. Donkere gebieden ontstaan door **transmissie** (veel straling doorgelaten), lichte gebieden door **absorptie** (veel straling geabsorbeerd).

Bij absorptie van fotonen wordt de energie gebruikt om atomen te ioniseren.  
Hoeveel straling wordt geabsorbeerd hangt af van het materiaal en de dikte.

### Halveringsdikte

De **intensiteit** is de hoeveelheid energie die per seconde door 1 vierkante meter gaat.

De **halveringsdikte** ($d_{1/2}$) is de materiaaldikte die **de helft van de straling doorlaat**. Deze hangt af van de stof en van de stralingsenergie.

Een laag met dikte $d_{1/2}$ laat dus 50% door. Een laag van 2 keer $d_{1/2}$ laat 25% door,  want eerst blijft de helft over. Bij 3 keer $d_{1/2}$ is dat nog 12,5%, enzovoort.

De doorgelaten intensiteit na $n$ halveringsdiktes is:

$$I = I_0 \cdot \left(\frac{1}{2}\right)^n$$

Hierin is $I$ de doorgelaten intensiteit, $I_0$ de invallende intensiteit, en $n$ het aantal halveringsdiktes.  
De intensiteit staat vaak in $\text{W}/\text{m}^2$, maar soms in procenten.

$n$ is het aantal keren dat de dikte $d$ in $d_{1/2}$ past:

$$n = \frac{d}{d_{1/2}}$$

Invullen geeft:

$$I = I_0 \cdot \left(\frac{1}{2}\right)^{d/d_{1/2}}$$

## Kernstraling

Sommige stoffen zijn **radioactief**. Er zijn verschillende soorten **kernstraling** (straling afkomstig uit atoomkernen van radioactieve stoffen): $\alpha$-straling, $\beta$-straling en $\gamma$-straling.

|                       | $\alpha$-straling                          | $\beta$-straling                                       | $\gamma$-straling                           |
| --------------------- | ------------------------------------------ | ------------------------------------------------------ | ------------------------------------------- |
| Bestaat uit...        | 2 protonen en 2 neutronen (heliumkern)     | Elektronen of positronen                               | Fotonen                                     |
| Doordringend vermogen | Klein (wordt al tegengehouden door papier) | Matig (wordt al tegengehouden door een dun laagje metaal) | Groot (kan zelfs door een dikke loodplaat) |
| Ioniserend vermogen   | Groot                                      | Matig                                                  | Klein                                       |

## Verval en activiteit

Bij het **vervallen** van een (instabiele) kern wordt er een $\alpha$-deeltje, een $\beta$-deeltje of een $\gamma$-foton uitgezonden (**emissie**).  
De **activiteit** van een radioactieve bron is het aantal kernen dat per seconde vervalt (eenheid: **becquerel** = vervallen kernen per seconde). De activiteit daalt na verloop van tijd omdat er steeds minder instabiele kernen zijn.

Dit verval is een toevalsproces; in werkelijkheid schommelt de activiteit een beetje.

De tijdsduur waarin de activiteit halveert noem je de **halveringstijd** ($t_{1/2}$). De halveringstijd is een eigenschap van een isotoop.  
Aan de hand van de halveringstijd kun je de activiteit van een radioactieve bron na $n$ halveringstijden berekenen:

$$A=A_0 \cdot (\frac{1}{2})^n$$

Hierin is $A$ de activiteit (in $\text{Bq}$), $A_0$ de beginactiviteit (in $\text{Bq}$), en $n$ het aantal halveringstijden.  

$n$ is dus hoe vaak de tijd in de halveringstijd past:

$$n=\frac{t}{t_{1/2}}$$

Hierin is $t$ het tijdstip en $t_{1/2}$ de halveringstijd (in dezelfde eenheid).  
Invullen geeft:

$$A = A_0 \cdot \left(\frac{1}{2}\right)^{t/t_{1/2}}$$

## Isotopen

De atomen van radioactieve stoffen hebben **instabiele** atoomkernen.  
Het **atoomnummer** ($Z$) is het aantal protonen in de kern, en geeft dus ook de lading van de kern aan. . Het **massagetal** ($A$) is het totaal aantal kerndeeltjes.

Bij radioactief verval gelden 2 **behoudswetten**: behoud van massa (massagetal) en behoud van elektrische lading (atoomnummer).

Je noteert een kern als $\ce{^{A}_{Z}X}$, bijvoorbeeld: $\ce{^{131}_{53}I}$.

Atomen van hetzelfde element met een verschillend aantal neutronen heten **isotopen**.

## Vervalvergelijkingen

In een **vervalvergelijking** staat de verandering die plaatsvindt bij radioactief verval.

- **Alfaverval**: de kern zendt een $\ce{^{4}_{2}He}$-deeltje uit:  
  $\ce{^{238}_{92}U -> ^{234}_{90}Th + ^{4}_{2}He}$

- **Bètaverval**:

  - Bij $\beta ^+$-verval ontstaat uit een neutron een **positron** en een proton.  
    $\ce{^{1}_{1}p -> ^{1}_{0}n + ^{0}_{1}e}$  
    $\beta ^+$-verval komt voor bij kernen met te weinig neutronen en een overschot aan protonen.

    $\ce{^{11}_{6}C -> ^{11}_{5}B + ^{0}_{1}e}$

    > Een positron is het **antideeltje** van het elektron: het heeft dezelfde massa en lading, maar die lading is positief. Positronen bestaan vaak maar heel kort. Als het uitgestoten positron op een elektron botst, vindt er **annihilatie** plaats: er onstaan 2 fotonen in tegengestelde richting. Ook kunnen antideeltjes ontstaan uit materie en antimaterie (**paarvoriming**).

  - Bij $\beta ^-$-verval ontstaat uit een proton een neutron en een elektron.  
    $\ce{^{1}_{0}n -> ^{1}_{1}p + ^{0}_{-1}e}$  
    $\beta ^-$-verval komt voor bij kernen met te weinig protonen en een overschot aan neutronen.

- **Gammastraling**: hierbij wordt een foton uitgezonden. De samenstelling van de kern verandert niet.

Ook **kernreacties** kun je beschrijven met een vergelijking.  

- Bij **protonenstraling** onstaan protonen, bijvoorbeeld bij het botsen van stikstof-14 en een $\alpha$-deeltje:  
  $\ce{^{14}_{7}N + ^{4}_{2}He -> ^{17}_{8}O + ^{1}_{1}p}$  
- Bij **neutronenstraling** ontstaan juist neutronen:  
  $\ce{^{9}_{4}Be + ^{4}_{2}He -> ^{12}_{6}C + ^{1}_{0}n}$

## Aantal instabiele kernen

Voor het aantal instabiele kernen op tijdstip $t$ geldt bijna dezelfde formule als voor de activiteit, want het aantal kernen en de activiteit nemen op dezelfde manier af.

$$N = N_0 \cdot \left(\frac{1}{2}\right)^{t/t_{1/2}}$$

Hierin is $N$ het aantal kernen, $N_0$ het aantal kernen op $t=0$, $t$ het tijdstip en $t_{1/2}$ de halveringstijd (beide in dezelfde eenheid).

De activiteit van een radioactieve bron is het aantal instabiele atoomkernen dat per seconde vervalt. Dat is dus gelijk aan de helling van een N,t-diagram, want het gaat om de afname op dat moment.  
De activieit is dus gelijk aan de helling van de raaklijn (of de afgeleide) van een N,t-diagram.

$$A = -\left(\frac{\Delta N}{\Delta t}\right)_{\text{raaklijn}}$$  
$$A = -\frac{dN}{dt}$$  
$$A_{\text{gem}} = -\frac{\Delta N}{\Delta t}$$

Je kunt de afgeleide ook uitschrijven als:

$$A = \frac{\ln(2) \cdot N}{t_{1/2}}$$

Hierin is $A$ de activiteit (in $\text{Bq}$), $\ln(2)$ is de natuurlijke logartime van 2 ($\approx 0{,}693$), $N$ het aantal instabiele atoomkernen en $t_{1/2}$ de halveringstijd (in $\text{s}$).

### Atoommassa's

Soms moet je de massa van 1 enkel atoom van een element weten. In Binas zie je de atoommassa in de **atomaire massa-eenheid** ($\text{u}$). $1 \ \text{u} = 1{,}66 \cdot 10^{-27} \ \text{kg}$.

## Dosis

UV-straling, rontgenstraling en gammestraling kunne door hun ioniserend vermogen schadelijk zijn voor het lichaam. Hetzelfde geldt voor $\alpha$-straling en $\beta$-straling.  
De **stralingsenergie** van ionisernede straling wordt in het lichaam opgenomen.  
De **dosis** is de geabosrbeerde stralingsenergie per kg van het voorwerp, gemeten in **gray** ($\text{Gy} = \text{J} \ \text{kg}^{-1}$).  

$$D = \frac{E_{\text{str}}}{m}$$

Hierin is $D$ de dosis (in $\text{Gy}$), $E_{str}$ de stralingsenergie (in $\text{J}$) en $m$ de massa van het voorwerp (in $\text{kg}$).

Maar niet elke soort straling doet even veel schade. Om "schade" te meten kun je beter de **equivalente dosis** gebruiken, gemeten in **sievert** ($\text{Sv} = \text{J} \ \text{kg}^{-1}$).

$$H = w_R \cdot D$$

Hierin is $H$ de equivalente dosis (in $\text{Sv}$), $w_R$ de **stralingsweegfactor** (zonder eenheid) en $D$ de dosis (in $\text{Gy}$).

> Ookal zijn zowel $\text{Sv}$ en $\text{Gy}$ in principe gelijk aan $\text{J} \ \text{kg}^{-1}$, betekenen ze dus niet hetzelfde!

De stralingsweegfactor (zie ook Binas 27D3) verschilt per type straling:

| Soort | $w_R$ |
| ----- | ----- |
| $\alpha$-straling | 20 |
| $\beta$-straling | 1 |
| $\gamma$-straling | 1 |
| rongtenstraling | 1 |

Bij een hoge equivalente dosis is het effect van ioniserende straling vrijwel direct meetbaar. Bij een lagere equivalente dosis is er kans op tumorvorming op langere termijn.

## Sralingsbelasting

De **achtergrondstraling** bestaat uit **kosmische straling** (uit het heelal) en straling van radioactieve stoffen op aarde, in lucht en in (bouw)materialen.

**Uitwendige bestraling** komt van bronnen buiten het lichaam.  
**Inwendige bestraling** ontstaat door opname van radioactieve stoffen. Dan is er sprake van **besmetting**.
