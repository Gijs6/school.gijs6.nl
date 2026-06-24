---
subject: WISB
title: H12
description: Goniometrische formules
---

## Goniometrische vergelijkingen

Bij het oplossen van goniometrische vergelijkingen werk je met de **herleidingsformules** naar de standaardvorm $\sin(A) = \sin(B)$, $\cos(A) = \cos(B)$ of $\tan(A) = \tan(B)$:

- $\sin(-A) = -\sin(A)$
- $\cos(-A) = \cos(A)$
- $-\sin(A) = \sin(A + \pi)$
- $-\cos(A) = \cos(A + \pi)$
- $\sin(A) = \cos(A - \tfrac{1}{2}\pi)$
- $\cos(A) = \sin(A + \tfrac{1}{2}\pi)$
- $\sin^2(A) + \cos^2(A) = 1$
- $\tan(A) = \frac{\sin(A)}{\cos(A)}$

In standaardvorm geldt:

- $\sin(A) = \sin(B)$ geeft $A = B + k \cdot 2\pi \lor A = \pi - B + k \cdot 2\pi$
- $\cos(A) = \cos(B)$ geeft $A = B + k \cdot 2\pi \lor A = -B + k \cdot 2\pi$
- $\tan(A) = \tan(B)$ geeft $A = B + k \cdot \pi$

Bij vergelijkingen met zowel $\sin^2$ als $\cos$ schrijf je $\sin^2(A) = 1 - \cos^2(A)$ om alles in $\cos$ uit te drukken. Daarna stel je $\cos(x) = u$.

## Verschil-, som- en verdubbelingsformules

De **verschilformules** zijn:

$$\cos(t - u) = \cos(t)\cos(u) + \sin(t)\sin(u)$$

$$\sin(t - u) = \sin(t)\cos(u) - \cos(t)\sin(u)$$

De **somformules** zijn:

$$\cos(t + u) = \cos(t)\cos(u) - \sin(t)\sin(u)$$

$$\sin(t + u) = \sin(t)\cos(u) + \cos(t)\sin(u)$$

Uit de somformules met $t = u = A$ volgen de **verdubbelingsformules**:

$$\sin(2A) = 2\sin(A)\cos(A)$$

$$\cos(2A) = \cos^2(A) - \sin^2(A) = 2\cos^2(A) - 1 = 1 - 2\sin^2(A)$$

Alle drie de vormen zijn gelijkwaardig. Hieruit volgt ook $2\sin^2(A) = 1 - \cos(2A)$.

## Lijn- en puntsymmetrie

De grafiek van $f$ is **lijnsymmetrisch** in de lijn $x = a$ als voor elke $p$ geldt:

$$f(a - p) = f(a + p)$$

Bij symmetrie in de y-as ($a = 0$) geldt $f(-p) = f(p)$.

De grafiek van $f$ is **puntsymmetrisch** in het punt $(a, b)$ als voor elke $p$ geldt:

$$f(a - p) + f(a + p) = 2b$$

Bij puntsymmetrie in de oorsprong $O$ geldt $f(-p) + f(p) = 0$.

## Goniometrische parameterkrommen

Als $x(t)$ en $y(t)$ allebei sinus- of cosinusfuncties zijn, wordt de baan oneindig vaak doorlopen als $t$ over $\mathbb{R}$ loopt. Daarom beperk je $t$ tot een interval, bijvoorbeeld $[0, 2\pi]$. Hoe vaak de baan wordt doorlopen hangt af van de periodes van $x(t)$ en $y(t)$.

Voor snelheid en hoeken gebruik je de snelheidsvector $\vec{v}(t) = \bigl(\begin{smallmatrix} x'(t) \\ y'(t) \end{smallmatrix}\bigr)$ en de formules uit [H10](../TW3/wisb_h10):

$$v(t) = \sqrt{(x'(t))^2 + (y'(t))^2}$$

$$\cos\!\left(\angle(\vec{v}, \vec{r})\right) = \frac{|\vec{v} \cdot \vec{r}|}{|\vec{v}| \cdot |\vec{r}|}$$

## Formules bij parametervoorstellingen

Je kunt nagaan of een parameterkromme overeenkomt met $y = f(x)$ door $x = x(t)$ en $y = y(t)$ te substitueren en te vereenvoudigen met de herleidings- of verdubbelingsformules. Omdat $x = x(t)$ een sinus of cosinus is, geldt $-1 \leq x \leq 1$: je krijgt maar een deel van de grafiek.

**Keerpunten** zijn punten waarbij de bewegingsrichting omkeert. In een keerpunt hebben $x(t)$ en $y(t)$ allebei een extremum, dus geldt $x'(t) = 0$ en $y'(t) = 0$ tegelijk.

## Meebewegende punten

De bewegingsvergelijkingen van een meebewegende punt $S$ vind je door $\vec{s}$ uit te drukken in $\vec{p}$ en een gedraaide versie $\vec{p}_L$. Bij 90° linksom draaien geldt:

$$\vec{p} = \begin{pmatrix} a \\ b \end{pmatrix} \implies \vec{p}_L = \begin{pmatrix} -b \\ a \end{pmatrix}$$

Door de bewegingsvergelijkingen van $P$ in te vullen, vind je die van $S$.
