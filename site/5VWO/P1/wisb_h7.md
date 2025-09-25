---
layout: summary
title: WISB - H7 - Samenvatting
data-source: manual
subject: WISB
test_material: H7 (Meetkunde met coördinaten)
icon: fa-solid fa-calculator
---

# Wiskunde B: Hoofdstuk 7 (Meetkunde met coördinaten)

## Lijnen

Stelsels kun je op [verschillende manieren oplossen](../../4VWO/P3/wisb_h4#getallenparen-en-stelsels).

Voor de lijnen $ax+by=c$ en $px+qy=r$ geldt:

| Soort stelsel     | Voorwaarde                                     | Oplossingen   | Lijnen       |
| ----------------- | ---------------------------------------------- | ------------- | ------------ |
| **Strijdig**      | $$\frac{a}{p} = \frac{b}{q} \neq \frac{c}{r}$$ | Geen          | Evenwijdig   |
| **Afhankelijk**   | $$\frac{a}{p} = \frac{b}{q} = \frac{c}{r}$$    | Oneindig veel | Vallen samen |
| **Onafhankelijk** | $$\frac{a}{p} \neq \frac{b}{q}$$               | 1             | Snijden      |

De lijn door de punten $(a, 0)$ en $(0, b)$ met $a \neq 0 \land b \neq 0$ heeft de vergelijking: $\frac{x}{a}+\frac{y}{b}=1$

## Hoeken

Een **richtingshoek** van een lijn is de hoek waarmee je de $x$-as moet draaien om deze lijn te laten samenvallen met de as. We nemen altijd de hoek waarvoor geldt $-90^{\circ} < \alpha \leq 90^{\circ}$.

Voor de richtingshoek $\alpha$ van de lijn $k$ geldt: $\tan (\alpha) = \text{rc}_k \land -90^{\circ} < \alpha \leq 90^{\circ}$

De hoek tussen twee lijnen vind je door hun richtingshoeken van elkaar af te trekken. We nemen altijd de hoek waarvoor geldt $0^{\circ} \leq \varphi \leq 90^{\circ}$.

Voor de hoek $\varphi$ tussen twee lijnen met richtingshoeken $\alpha$ en $\beta$, waarbij $\alpha > \beta$, geldt:

- $\varphi = \alpha - \beta$ als $\alpha - \beta \leq 90^{\circ}$
- $\varphi = 180^{\circ} - (\alpha - \beta)$ als $\alpha - \beta > 90^{\circ}$

## Afstanden

### Afstand tussen twee punten

De afstand tussen twee punten bereken je met de stelling van Pythagoras. Hierbij is de afstand de schuine zijde, en de verschillen in coördinaten zijn de lengtes van de rechthoekszijden.

Voor de afstand tussen de punten $A(x_A, y_A)$ en $B(x_B, y_B)$ geldt:
$$d(A, B) = \sqrt{(x_B-x_A)^2 + (y_B-y_A)^2}$$

De coördinaten van het midden $M$ van het lijnstuk $AB$ zijn het gemiddelde van de coördinaten van $A$ en $B$:
$$x_M = \frac{1}{2}(x_A + x_B) \quad\quad y_M = \frac{1}{2}(y_A + y_B)$$

### Loodrechte lijnen

Voor twee lijnen die loodrecht op elkaar staan geldt: $\text{rc}_k \cdot \text{rc}_l = -1$

Voor de lijn $ax+by=c$ met $b \neq 0$ geldt: $\text{rc} = -\frac{a}{b}$

Voor de lijn $bx - ay = d$ met $a \neq 0$ geldt: $\text{rc} = \frac{b}{a}$

Hieruit volgt dat de lijnen $ax+by=c$ en $bx-ay=d$ loodrecht op elkaar staan.

### Afstand van een punt tot een lijn

Bij de afstand van een punt tot een lijn speelt de **loodrechte projectie** een rol. Dit is de lijn vanuit het punt die loodrecht op de lijn staat. De afstand van een punt $P$ tot de lijn $l$ is de afstand van $P$ tot zijn loodrechte projectie $P'$ op $l$.

De afstand kan sneller worden berekend met de **afstandsformule**. Voor een punt $P(x_P, y_P)$ en een lijn $k: ax + by = c$ geldt:
$$d(P, k) = \frac{\lvert ax_P + by_P - c \rvert}{\sqrt{a^2 + b^2}}$$

## Cirkelvergelijkingen

De cirkel met middelpunt $M(x_M, y_M)$ en straal $r$ heeft vergelijking:
$$(x - x_M)^2 + (y - y_M)^2 = r^2$$

Als de lijn $k$ de cirkel $c$ met middelpunt $M$ en straal $r$ raakt in punt $A$, dan geldt: $MA \perp k$ en $d(M, k) = r$.

Bij raaklijnen van cirkels is het dus belangrijk dat de afstand van het middelpunt tot de lijn gelijk is aan de straal.
