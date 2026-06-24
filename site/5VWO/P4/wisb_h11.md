---
subject: WISB
title: H11
description: Integreren
---

## Primitieven

Een **primitieve** van $f$ is een functie $F$ waarvoor $F'(x) = f(x)$. Je schrijft dit ook als $F' = f$.

Alle functies van de vorm $F(x) + c$ zijn primitieven van $f$, want de afgeleide van een constante is nul. De constante $c$ heet de **integratieconstante**. Zo zijn $5x^3$, $5x^3 + 3$ en $5x^3 - 7$ allemaal primitieven van $f(x) = 15x^2$.

Primitiveren is het omgekeerde van differentiëren.

### Standaardfuncties

| Standaardfunctie $f(x)$ | Primitieve $F(x)$                         | Voorwaarde  |
| ----------------------- | ---------------------------------------- | ----------- |
| $ax^n$                  | $a \cdot \frac{1}{n+1} x^{n+1} + c$      | $n \neq -1$ |
| $g^x$                   | $\frac{g^x}{\ln(g)} + c$                 |             |
| $e^x$                   | $e^x + c$                                |             |
| $\frac{1}{x}$           | $\ln\lvert x \rvert + c$                 |             |
| $\ln(x)$                | $x\ln(x) - x + c$                        |             |
| $^g\!\log(x)$           | $\frac{1}{\ln(g)}(x\ln(x) - x) + c$      |             |
| $\sin(x)$               | $-\cos(x) + c$                           |             |
| $\cos(x)$               | $\sin(x) + c$                            |             |

## Integreren

Een **bepaalde integraal** geeft de exacte oppervlakte van een vlakdeel onder een grafiek:

$$\int_a^b f(x) \, \mathrm{d}x$$

Hierin is $a$ de **ondergrens**, $b$ de **bovengrens** en $f(x)$ de **integrand**. De integratievariabele is $\mathrm{d}x$ (bij een functie $B(q)$ wordt dat $\mathrm{d}q$).

De oppervlakte van een vlakdeel bereken je met de **hoofdstelling van de integraalrekening**:

$$\int_a^b f(x) \, \mathrm{d}x = \left[F(x)\right]_a^b = F(b) - F(a)$$

Je bepaalt eerst de primitieve $F(x)$ van $f(x)$, en berekent dan $F(b) - F(a)$. De integratieconstante $c$ valt daarbij weg, dus neem $c = 0$.

Dit geeft de oppervlakte $O(V)$ van vlakdeel $V$ boven de x-as, onder $f$, met $a < b$.

## Kettingregel bij primitieven

Als $F$ een primitieve is van $f$, dan zijn de primitieven van $f(ax + b)$ gelijk aan $\frac{1}{a}F(ax + b) + c$.

Zo worden de standaardformules algemener:

| Functie $f(x)$       | Primitieve $F(x)$                               |
| -------------------- | ----------------------------------------------- |
| $(ax + b)^n$         | $\frac{1}{a} \cdot \frac{1}{n+1}(ax+b)^{n+1} + c$ |
| $e^{ax+b}$           | $\frac{1}{a}e^{ax+b} + c$                       |
| $\frac{1}{ax+b}$     | $\frac{1}{a}\ln\lvert ax+b \rvert + c$          |
| $\sin(ax+b)$         | $-\frac{1}{a}\cos(ax+b) + c$                    |
| $\cos(ax+b)$         | $\frac{1}{a}\sin(ax+b) + c$                     |

## Oppervlakte tussen twee grafieken

Als vlakdeel $V$ wordt ingesloten door de grafieken van $f$ en $g$ (met $f(x) \geq g(x)$ op $[a, b]$) en de lijnen $x = a$ en $x = b$, dan geldt:

$$O(V) = \int_a^b (f(x) - g(x)) \, \mathrm{d}x$$

Je neemt altijd de bovenste min de onderste grafiek. Als de bovenste grafiek de x-as is, geldt $f(x) = 0$ en krijg je dus $O(V) = -\int_a^b g(x) \, \mathrm{d}x$.

## Omwentelingslichamen

Een **omwentelingslichaam** $L$ krijg je als een vlakdeel om een as wentelt. Als $V$ boven de x-as ligt, ingesloten door $f$, de x-as en de lijnen $x = a$ en $x = b$, dan geldt:

$$I(L) = \pi \int_a^b (f(x))^2 \, \mathrm{d}x$$

Als $V$ tussen twee grafieken ligt ($f(x) \geq g(x) \geq 0$), neem je de buitenste inhoud min de binnenste:

$$I(L) = \pi \int_a^b \left((f(x))^2 - (g(x))^2\right) \, \mathrm{d}x$$

### Wentelen om de y-as

Als $V$ rechts van de y-as ligt, ingesloten door $f$, de y-as en de lijnen $y = a$ en $y = b$, dan geldt bij wentelen om de y-as:

$$I(L) = \pi \int_a^b x^2 \, \mathrm{d}y$$

Hierin druk je $x^2$ uit in $y$ via de inverse van $f$. Soms is het handiger om de inhoud te berekenen als een cilinder min een omwentelingslichaam.
