---
subject: WISB
title: H10
description: Vectoren
---

## Vectoren

Een **vector** is een lijnstuk met een richting en een lengte. De vector van $O$ naar $A(5, 3)$ schrijf je als $\overrightarrow{OA} = \bigl(\begin{smallmatrix} 5 \\ 3 \end{smallmatrix}\bigr)$. De getallen 5 en 3 heten de **kengetallen**: ze geven aan hoeveel stappen je in de $x$- en $y$-richting zet. Een vector die in de oorsprong $O$ begint, schrijf je ook wel met een kleine letter: $\vec{a} = \overrightarrow{OA}$.

De lengte van een vector bereken je met de stelling van Pythagoras:

$$\left|\begin{pmatrix} p \\ q \end{pmatrix}\right| = \sqrt{p^2 + q^2}$$

**Gelijke vectoren** hebben dezelfde richting en lengte, het maakt niet uit waar ze beginnen. **Tegengestelde vectoren** hebben dezelfde lengte maar een tegengestelde richting: $\bigl(\begin{smallmatrix} a_x \\ a_y \end{smallmatrix}\bigr)$ en $-\bigl(\begin{smallmatrix} a_x \\ a_y \end{smallmatrix}\bigr)$ zijn tegengesteld.

## Rekenen met vectoren

De **somvector** is de optelsom van twee vectoren. Grafisch doe je dit met de parallelogrammethode of de kop-staartmethode:

$$\vec{a} + \vec{b} = \begin{pmatrix} a_x + b_x \\ a_y + b_y \end{pmatrix}$$

Je kunt een vector ook vermenigvuldigen met een getal $c$:

$$c \cdot \vec{a} = \begin{pmatrix} c \cdot a_x \\ c \cdot a_y \end{pmatrix}$$

Als $c > 0$ blijft de richting hetzelfde en verandert alleen de lengte. Als $c < 0$ keert de richting om.

Je kunt een vector **ontbinden** in componenten: je schrijft de vector als optelsom van twee andere vectoren. Als je ontbindt in **onderling loodrechte componenten** (een horizontale en een verticale component), bereken je de lengte van elke component met sinus en cosinus.

## Vectoren draaien

De vector $\vec{a} = \bigl(\begin{smallmatrix} p \\ q \end{smallmatrix}\bigr)$ 90° draaien geeft:

- Rechtsom: $\vec{a}_R = \bigl(\begin{smallmatrix} q \\ -p \end{smallmatrix}\bigr)$
- Linksom: $\vec{a}_L = \bigl(\begin{smallmatrix} -q \\ p \end{smallmatrix}\bigr)$

## Vectorvoorstelling van een lijn

Met een **vectorvoorstelling** beschrijf je alle punten op een lijn. Elk punt $P$ op de lijn $l$ voldoet aan:

$$\overrightarrow{OP} = \vec{s} + t \cdot \vec{r}$$

Hierin is $\vec{s}$ de **steunvector** (begint in $O$ en wijst naar een vast punt op de lijn) en $\vec{r}$ de **richtingsvector** (evenwijdig aan de lijn). Bij $t = 0$ zit je op het eindpunt van $\vec{s}$, door $t$ te veranderen schuif je langs de lijn.

De vectorvoorstelling van de lijn door $A$ en $B$ is:

$$\begin{pmatrix} x \\ y \end{pmatrix} = \vec{a} + t \cdot (\vec{b} - \vec{a})$$

Hierin is $\vec{r}_{AB} = \vec{b} - \vec{a}$ de richtingsvector. Bij $t = 0$ zit je in $A$, bij $t = 1$ in $B$.

Twee vectoren zijn **evenwijdig** als ze dezelfde (of tegengestelde) richting hebben, dus als de ene een veelvoud is van de andere. Je schrijft dit als:

$$\begin{pmatrix} b_x \\ b_y \end{pmatrix} = c \cdot \begin{pmatrix} a_x \\ a_y \end{pmatrix} \quad (c \neq 0)$$

### Parametervoorstelling

Je kunt de vectorvoorstelling ook schrijven als een **parametervoorstelling** door de $x$- en $y$-vergelijking apart te noteren. Bijvoorbeeld voor $\bigl(\begin{smallmatrix} x \\ y \end{smallmatrix}\bigr) = \bigl(\begin{smallmatrix} 3 \\ 4 \end{smallmatrix}\bigr) + t \cdot \bigl(\begin{smallmatrix} 2 \\ 2 \end{smallmatrix}\bigr)$:

$$x = 3 + 2t \wedge y = 4 + 2t$$

De variabele $t$ heet de **parameter**.

Om te controleren of een punt op de lijn ligt, vul je de coördinaten in en los je $t$ op uit een van de twee vergelijkingen. Daarna controleer je of die $t$ ook klopt in de andere vergelijking.

Om de vergelijking van de lijn te vinden, elimineer je $t$. Dat doe je door de twee vergelijkingen zo te vermenigvuldigen dat de $t$-termen gelijk worden, en ze dan van elkaar af te trekken.

## Hoeken tussen vectoren

Het **inproduct** van $\vec{a} = \bigl(\begin{smallmatrix} a_x \\ a_y \end{smallmatrix}\bigr)$ en $\vec{b} = \bigl(\begin{smallmatrix} b_x \\ b_y \end{smallmatrix}\bigr)$ is:

$$\vec{a} \cdot \vec{b} = a_xb_x + a_yb_y$$

Met de cosinusregel in de driehoek $OAB$ volgt voor de hoek $\varphi$ tussen twee vectoren:

$$\cos\!\left(\angle(\vec{a}, \vec{b})\right) = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}| \cdot |\vec{b}|}$$

Dit geldt alleen als $\vec{a} \neq \vec{0}$ en $\vec{b} \neq \vec{0}$. $\vec{0} = \bigl(\begin{smallmatrix} 0 \\ 0 \end{smallmatrix}\bigr)$ is de **nulvector**.

Als het inproduct nul is, is $\cos(\varphi) = 0$, dus $\varphi = 90°$: de vectoren staan loodrecht op elkaar. Dus:

$$\vec{a} \cdot \vec{b} = 0 \iff \vec{a} \perp \vec{b}$$

Dit geldt ook voor de 90°-gedraaide vectoren:

$$\bigl(\begin{smallmatrix} p \\ q \end{smallmatrix}\bigr) \perp \bigl(\begin{smallmatrix} q \\ -p \end{smallmatrix}\bigr) \quad \text{en} \quad \bigl(\begin{smallmatrix} p \\ q \end{smallmatrix}\bigr) \perp \bigl(\begin{smallmatrix} -q \\ p \end{smallmatrix}\bigr)$$

Voor de hoek tussen twee snijdende lijnen $k$ en $l$ neem je de absolute waarde, zodat je altijd de kleinste hoek krijgt:

$$\cos(\angle(k, l)) = \frac{|\vec{r}_k \cdot \vec{r}_l|}{|\vec{r}_k| \cdot |\vec{r}_l|}$$

Een vector die loodrecht op een lijn staat, heet een **normaalvector** van die lijn. De vector $\vec{n} = \bigl(\begin{smallmatrix} a \\ b \end{smallmatrix}\bigr)$ is een normaalvector van de lijn $l: ax + by = c$. De kengetallen van de normaalvector zijn dus de coëfficiënten van $x$ en $y$ in de vergelijking.

## Bewegingsvectoren

De baan van een bewegend punt beschrijf je met **bewegingsvergelijkingen**: twee vergelijkingen die de $x$- en $y$-positie als functie van de tijd $t$ geven:

$$\begin{cases} x(t) = f(t) \\ y(t) = g(t) \end{cases}$$

Deze vergelijkingen vormen een **parametervoorstelling van de baan**, die ook wel een **parameterkromme** heet.

De **plaatsvector** $\vec{r}(t)$ wijst vanuit $O$ naar de positie van het punt op tijdstip $t$:

$$\vec{r}(t) = \overrightarrow{OP} = \begin{pmatrix} x(t) \\ y(t) \end{pmatrix}$$

De **snelheidsvector** is de afgeleide van de plaatsvector. De richting van $\vec{v}(t)$ is de richting waarin het punt op dat moment beweegt, en de lengte is de snelheid:

$$\vec{v}(t) = \begin{pmatrix} x'(t) \\ y'(t) \end{pmatrix}$$

De **baansnelheid** is de lengte van de snelheidsvector:

$$v(t) = |\vec{v}(t)| = \sqrt{(x'(t))^2 + (y'(t))^2}$$

De **versnellingsvector** is de afgeleide van de snelheidsvector:

$$\vec{a}(t) = \begin{pmatrix} x''(t) \\ y''(t) \end{pmatrix}$$
