---
subject: WISB
title: H9
description: Exponentiële & logaritmische functies
---

## Logaritmes

De **logaritme** is de omgekeerde bewerking van machtsverheffen. ${}^g\!\log(x)$ geeft antwoord op de vraag 'tot welke macht moet ik $g$ verheffen om $x$ te krijgen?'.

$${}^g\!\log(x) = a \iff g^a = x$$

Bijvoorbeeld: ${}^2\!\log(8) = 3$ omdat $2^3 = 8$.

Hieruit volgen twee eigenschappen: ${}^g\!\log(g^a) = a$ en $g^{{}^g\!\log(x)} = x$.

Voor logaritmes gelden de volgende rekenregels (met $g > 0$, $g \neq 1$, $a > 0$ en $b > 0$):

- ${}^g\!\log(a) + {}^g\!\log(b) = {}^g\!\log(a \cdot b)$
- ${}^g\!\log(a) - {}^g\!\log(b) = {}^g\!\log\left(\frac{a}{b}\right)$
- $p \cdot {}^g\!\log(a) = {}^g\!\log(a^p)$
- ${}^g\!\log(a) = \frac{{}^p\!\log(a)}{{}^p\!\log(g)}$ (waarbij $p$ elk getal kan zijn)
- ${}^{\frac{1}{g}}\!\log(a) = -^g\!\log(a)$

Als er geen grondtal bij de logaritme staat, mag je uitgaaan van ${}^{10}\!\log$.

Bij het oplossen van **logaritmische vergelijkingen** werk je naar een vorm waarin beide zijden een logaritme met hetzelfde grondtal zijn. Dan geldt ${}^g\!\log(A) = {}^g\!\log(B) \implies A = B$.

Let op: de input van een logaritme moet altijd positief zijn, dus je moet goed checken of je uitkomst voldoet!

## Exponentiële groei

Bij **exponentiële groei** wordt de hoeveelheid per tijdseenheid met een vaste **groeifactor** $g$ vermenigvuldigd. Hierbij hoort de formule $N = b \cdot g^t$, waarin $b$ de beginhoeveelheid is, $g$ de groeifactor per tijdseenheid en $t$ de tijd. Als $g > 1$ is er sprake van groei, als $0 < g < 1$ van afname.

De groeifactor per $n$ tijdseenheden is $g^n$.

De **verdubbelingstijd** $T$ vind je door $g^T = 2$ op te lossen: $T = {}^g\!\log(2)$.  
De **halveringstijd** vind je door $g^T = \frac{1}{2}$ op te lossen: $T = {}^g\!\log\left(\tfrac{1}{2}\right)$.

## Het getal e en de natuurlijke logaritme

Het getal $e$ ontstaat uit de limiet:

$$e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n \approx 2{,}718$$

Het getal $e$ heeft de bijzondere eigenschap dat de afgeleide van $e^x$ gelijk is aan zichzelf: $f(x) = e^x$ geeft $f'(x) = e^x$.

De logaritme met grondtal $e$ heet de **natuurlijke logaritme**: $\ln(x) = {}^e\!\log(x)$. De functie $y = \ln(x)$ is de inverse van $y = e^x$. De grafiek is stijgend met de $y$-as als verticale asymptoot, domein $(0, \rightarrow)$ en bereik $\mathbb{R}$.

Elke exponentiële functie kun je schrijven met grondtal $e$: $g^x = e^{\ln(g) \cdot x}$.

## Differentiëren

Voor exponentiële functies geldt:

- $f(x) = e^x$ geeft $f'(x) = e^x$
- $f(x) = g^x$ geeft $f'(x) = g^x \cdot \ln(g)$

Voor logaritmische functies geldt:

- $f(x) = \ln(x)$ geeft $f'(x) = \frac{1}{x}$
- $f(x) = {}^g\!\log(x)$ geeft $f'(x) = \frac{1}{x \cdot \ln(g)}$
