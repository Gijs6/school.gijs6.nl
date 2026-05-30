---
subject: WISB
title: H11
description: Integreren
hidden: true
---

## Primitieven

Een functie $F(x)$ waarvoor geldt dat $F'(x) = f(x)$ heet een **primitieve functie** van $f$. Dit noteer je vaak met een hoofdletter: $F' = f$.

Omdat de afgeleide van een constante nul is, is de primitieve nooit uniek. Alle functies van de vorm $F(x) + c$ zijn primitieven van $f$. De constante $c$ heet de **integratieconstante**. Zo zijn $5x^3$, $5x^3 + 3$ en $5x^3 - 7$ allemaal primitieven van $f(x) = 15x^2$.

Primitiveren is het omgekeerde van differentiëren.

### Standaardfuncties

| Standaardfunctie $f(x)$ | Primitieve $F(x)$                         | Voorwaarde  |
| ----------------------- | ---------------------------------------- | ----------- |
| $ax^n$                  | $a \cdot \frac{1}{n+1} x^{n+1} + c$      | $n \neq -1$ |
| $g^x$                   | $\frac{g^x}{\ln(g)} + c$                 |             |
| $e^x$                   | $e^x + c$                                |             |
| $\frac{1}{x}$           | $\ln|x| + c$                             |             |
| $\ln(x)$                | $x\ln(x) - x + c$                        |             |
| $^g\!\log(x)$           | $\frac{1}{\ln(g)}(x\ln(x) - x) + c$      |             |
| $\sin(x)$               | $-\cos(x) + c$                           |             |
| $\cos(x)$               | $\sin(x) + c$                            |             |

## Integreren

Een **integraal** is de exacte oppervlakte van een vlakdeel onder een grafiek. Om die te berekenen heb je een primitieve nodig.

Een integraal noteer je als:

$$\int_a^b f(x) \mathrm{d}x$$

Dit heet een **bepaalde integraal**. Hierin is $a$ de ondergrens, $b$ de bovengrens, $f(x)$ de **integrand** en $\mathrm{d}x$ de integratievariabele (bij een functie $B(q)$ wordt dat $\mathrm{d}q$).

De oppervlakte van een vlakdeel bereken je met de **hoofdstelling van de integraalrekening**:

$$\int_a^b f(x) \mathrm{d}x = \left[F(x)\right]_a^b = F(b) - F(a)$$

Je bepaalt eerst de primitieve $F(x)$ van $f(x)$, en berekent dan $F(b) - F(a)$. De integratieconstante $c$ valt daarbij weg, dus neem $c = 0$.

De resulterende formule is de oppervlakte $O(V)$ van het vlakdeel $V$ boven de x-as, onder $f(x)$, tussen $x = a$ en $x = b$ (met $a < b$).
