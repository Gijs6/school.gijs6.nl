---
layout: summary
title: NAT - H5 - Samenvatting
test_code: 4A-NAT-T07
---

# Natuurkunde: Hoofdstuk 5 (Ioniserende straling)

## Röntgenstraling

**Röntgenstraling** is een vorm van elektromagnetische straling. Net als zichtbaar licht bestaat het uit **fotonen** (energiepakketjes). Door de hoge frequentie heeft röntgenstraling relatief veel energie en kan het dwars door je lichaam heen gaan.

Deze fotonenergie is evenredig met de frequentie:

$$E_f = hf$$

Hierin is $E_f$ de fotonenergie (in $\text{J}$), $h$ de constante van Planck ($\approx 6{,}626 \cdot 10^{-34} \ \text{J} \ \text{s}$) en $f$ de frequentie (in $\text{Hz}$).  
Soms wordt **elektronvolt** ($\text{eV}$) gebruikt als eenheid voor energie: $1 \ \text{eV}= 1{,}6 \cdot 10^{-19} \ \text{J}$.

Het **ioniserend vermogen** is het vermogen om elektronen uit atomen los te maken.  
Het **doordringend vermogen** is het gemak waarmee straling door huid en weefsel gaat.

![De eerste röntgenfoto ooit (img-medium)](images/nat_h5_rontgenfotohand.jpg)

Op röntgenfoto's zie je donkere en lichte gebieden. Donkere gebieden ontstaan door **transmissie** (veel straling doorgelaten), lichte gebieden door **absorptie** (veel straling geabsorbeerd).

Bij absorptie van fotonen wordt de energie gebruikt om atomen te ioniseren.  
Hoeveel straling wordt geabsorbeerd hangt af van het materiaal en de dikte.

### Halveringsdikte

De **intensiteit** is de hoeveelheid energie die per seconde door 1 vierkante meter gaat.

De **halveringsdikte** ($d_{1/2}$) is de materiaaldikte die **de helft van de straling doorlaat**. Deze hangt af van de stof en van de stralingsenergie.

Een laag met dikte $d_{1/2}$ laat 50% dus door. Een laag van 2 keer $d_{1/2}$ laat 25% door, want eerst blijft de helft over, dan weer de helft daarvan. Bij 3 keer $d_{1/2}$ is dat nog 12,5%.

De doorgelaten intensiteit na $n$ halveringsdiktes is dus:

$$I=I_0 \cdot (\frac{1}{2})^n$$

Hierin is $I$ de doorgelaten intensiteit, $I_0$ de invallende intensiteit, en $n$ het aantal halveringsdiktes.  
De intensiteit staat vaak in $\text{W}/\text{m}^2$, maar soms in procenten.

$n$ is het dus aantal keer dat de dikte $d$ in $d_{1/2}$ past:

$$n=\frac{d}{d_{1/2}}$$

Invullen geeft:

$$I=I_0 \cdot (\frac{1}{2})^{d/d_{1/2}}$$

## Kernstraling

Sommige stoffen zijn **radioactief**. Er zijn verschillende soorten **kernstraling** (straling afkomstig uit atoomkernen van radioactieve stoffen): $\alpha$-straling, $\beta$-straling en $\gamma$-straling.

|                       | $\alpha$-straling                          | $\beta$-straling                                       | $\gamma$-straling                           |
| --------------------- | ------------------------------------------ | ------------------------------------------------------ | ------------------------------------------- |
| Bestaat uit...        | 2 protonen en 2 neutronen (heliumkern)     | Elektronen of positronen                               | Fotonen                                     |
| Doordringend vermogen | Klein (wordt al tegengehouden door papier) | Matig (wordt al tegengehouden een klein laagje metaal) | Goed (kan zelfs door een flinke plaat lood) |
| Ioniserend vermogen   | Groot                                      | Matig                                                  | Klein                                       |

## Verval en activiteit

Bij het **vervallen** van een (instabiele) kern wordt er een $\alpha$-deeltje, een $\beta$-deeltje of een $\gamma$-foton uitgezonden (**emissie**).  
De **activiteit** van een radioactieve bron is het aantal kernen dat per seconde vervalt (eenheid **becquerel** = vervallen kernen per seconde). De activiteit van een bron wordt steeds kleiner, omdat er steeds minder kernen zijn die kunnen vervallen.  
Dit vervallen is een toevalsproces. In werkelijkheid schommelt de activiteit een beetje heen en weer.

De tijdsduur waarin de activiteit halveert noem je de **halveringstijd** ($t_{1/2}$). De halveringstijd is een eigenschap van een isotoop.  
Aan de hand van de halveringstijd kun je de activiteit van een radioactieve bron na $n$ halveringstijden berekenen:

$$A=A_0 \cdot (\frac{1}{2})^n$$

Hierin is $A$ de activiteit (in $\text{Bq}$), $A_0$ de beginactiviteit (in $\text{Bq}$), en $n$ het aantal halveringstijden.  

$n$ is dus hoe vaak de tijd in de halveringstijd past:

$$n=\frac{t}{t_{1/2}}$$

Hierin is $t$ het tijdstip en $t_{1/2}$ de halveringstijd (in dezelfde eenheid).  
Invullen geeft:

$$A=A_0 \cdot (\frac{1}{2})^{t/t_{1/2}}$$

## Isotopen

De atomen van radiocative stoffen hebben **instabiele** atoomkernen.  
Het **atoomnummer** ($Z$) is gelijk aan het aantal protonen in de kern, en geeft dus ook de lading van de kern aan. Het **massagetal** ($A$) is het aantal kerndeeltjes in de kern.  
Bij radioactief verval gelden 2 **behoudswetten**: behoud van massa en elektrische lading.

Je kunt een kern noteren als $\ce{^{\text{Massagetal}}_{\text{Atoomnummer}}\text{Symbool}}$, zoals $\ce{^{131}_{53}I}$ voor jodium-131.

Atomen van hetzelfde element maar met een verschillend aantal neutronen noem je **isotopen**.

## Vervalvergelijkingne

In een **vervalvergelijking** staat de verandering die plaatsvindt bij radioactiev verval. Je moet rekening houden met de behoudswetten.

Bij **alfaverval** zendt de kern een $\ce{^{4}_{2}He}$-deeltje uit, zoals bij uranium-238:  
$\ce{^{238}_{92}U -> ^{234}_{90}Th + ^{4}_{2}He}$

Er zijn 2 vormen van **betaverval**: $\beta ^+$ en $\beta ^-$:

- Bij $\beta ^+$-verval ontstaat uit een neutron een **positron** en een proton.  
  $\ce{^{1}_{1}p -> ^{1}_{0}n + ^{0}_{1}e}$  
  $\beta ^+$-verval komt voor bij kernen met te weinig neutronen en een overschot aan protonen.

  $\ce{^{11}_{6}C -> ^{11}_{5}B + ^{0}_{1}e}$

  > Een positron is het **antideeltje** van het elektron: het heeft dezelfde massa en lading, maar die lading is positief. Positronen bestaan vaak maar heel kort. Als het uitgestoten positron op een elektron botst, vindt er **annihilatie** plaats: er onstaan 2 fotonen in tegengestelde richting. Ook kunnen antideeltjes ontstaan uit materie en antimaterie (**paarvoriming**).
- Bij $\beta ^-$-verval ontstaat uit een proton een neutron en een elektron.  
  $\ce{^{1}_{0}n -> ^{1}_{1}p + ^{0}_{-1}e}$  
  $\beta ^-$-verval komt voor bij kernen met te weinig protonen en een overschot aan neutronen.

  $\ce{^{14}_{6}C -> ^{14}_{7}N + ^{0}_{-1}e}$

Bij **gammastraling** ontstaan gammafotonen (zonder massa en lading) door een overschot aan energie. De samenstelling van de kern verandert dan niet.

Ook **kernreacties** kun je beschrijven met een vergelijking.  

- Bij **protonenstraling** onstaan protonen, bijvoorbeeld bij het botsen van stikstof-14 en een $\alpha$-deeltje:  
  $\ce{^{14}_{7}N + ^{4}_{2}He -> ^{17}_{8}O + ^{1}_{1}p}$  
- Bij **neutronenstraling** ontstaan juist neutronen:  
  $\ce{^{9}_{4}Be + ^{4}_{2}He -> ^{12}_{6}C + ^{1}_{0}n}$

## Aantal instabiele kernen

Voor het aantal instabiele kernen op tijdstip $t$ geldt bijna dezelfde formule als voor de activiteit, want het aantal kernen en de activiteit nemen op dezelfde manier af.

$$N = N_0 \cdot (\frac{1}{2})^{t/t_{1/2}}$$

Hierin is $N$ het aantal kernen, $N_0$ het aantal kernen op $t=0$, $t$ het tijdstip en $t_{1/2}$ de halveringstijd (beide in dezelfde eenheid).
