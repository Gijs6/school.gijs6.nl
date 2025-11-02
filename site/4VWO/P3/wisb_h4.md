---
subject: WISB
short: H4
title: Hoofdstuk 4
description: Vergelijkingen & herleidingen
---

## Getallenparen en stelsels

De algemene vorm van een lineaire vergelijking met $x$ en $y$ is $ax+by=c$. Uit deze verglijking kun je $x$ of $y$ vrijmaken.  
De getallenparen $(x, y) = (4, -1)$ en $(x, y) = (-12, 5)$ zijn oplossingen van de vergelijking $3x+8y=4$.  
Het getallenpaar $(x, y) = (2, -1)$ is zowel een oplossing van $2x+y=3$ als van $x-2y=4$. Je kunt ook zeggen dat $(2, -1)$ de oplossing is van het onderstaande stelsel.

$$
\begin{cases}
2x + y = 3 \\
x - 2y = 4
\end{cases}
$$

Om een stelsel op te lossen maak je eerst een vergelijking $x$ of $y$ vrij. Vervolgens substitueer je de formule voor de vrijgemaakte variabele in de andere vergelijking. Vervolgens gebruik je dit antwoord om de andere variabele te berekenen.

Je kunt stelsels ook oplossen door **elimineren door optellen of aftrekken**.

$$
\begin{cases}
8x + y = 2 \\
4x + y = 5
\end{cases}
$$

Bij het bovenstaande stelsel trek je de vergelijkingen van elkaar af, want dan valt de $y$ weg. Kijk goed wat handiger is: optellen of aftrekken.  
Je kunt dit ook toepassen bij moeilijkere stelsels.

Je kunt stelsels ook oplossen door **elimineren na vermenigvuldigen**. Dan ga je eerst beide vergelijkingen vermenigvuldigen om er voor te zorgen dat er een variabele wegvalt bij het optellen of aftrekken.  
Bij het stelsel

$$
\begin{cases}
3x - 4y = 7 \\
2x + 3y = 15
\end{cases}
$$
valt er na optellen of aftrekken geen enkele variabele weg. Maar als je de bovenste vergelijking met 2 vermenigvuldigt en de onderste vergelijking met 3, dan wel:

$$
\left.
\begin{cases}
3x - 4y = 7 \\
2x + 3y = 15
\end{cases}
\right.
\left|
\begin{matrix}
2 \\
3
\end{matrix}
\right|
=
\begin{cases}
6x - 8y = 14 \\
6x + 9y = 45
\end{cases}
$$

Je noteert de getallen waar je mee vermenigvuldigt tussen verticale strepen.

## Hogeregraadsvergelijkingen

De vergelijking $x^2 = 5$ heeft de oplossingen $x=5$ en $x=-5$. Je weet dat $\sqrt{5}$ de **tweedemachtswortel** van 5 is, want $(\sqrt{5})^2 = 5$. In dit geval staat er bij het wortelteken staat eigenlijk een "verborgen 2": $\sqrt{a} = \sqrt[2]{a}$ (dit geldt dus alleen als er geen getalletje bij het wortelteken staat!). Er zijn ook **hogeremachtswortels**, zoals derdemachtswortels. De vergelijking $x^3 = 20$ heeft als oplossing $x=\sqrt[3]{20}$.  
In de tabel zie je hoeveel oplossingen de vergelijking $x^n = a$ kan hebben.

|   $x^n = a$   |                        $a > 0$                         |            $a < 0$             |
| :-----------: | :----------------------------------------------------: | :----------------------------: |
|  $n$ is even  | 2 oplossingen: $x = \sqrt[n]{a}$ en $x = -\sqrt[n]{a}$ |    geen (reële) oplossingen    |
| $n$ is oneven |             1 oplossing: $x = \sqrt[n]{a}$             | 1 oplossing: $x = \sqrt[n]{a}$ |

Sommige hogeregraadsvergelijkingen kun je algebraïsch oplossen door te ontbinden in factoren. Soms door een factor buiten haakjes te brengen of door te substitueren. Binnen de vergelijking $x^4-3x^2+2=0$ kun je $x^2$ substitueren met $u$. Je krijgt dan $u^2-3u+2=0$. Deze kun je vervolgens oplossen met de product-som-methode. (Let op! Je hebt dan $u$ opgelost; nog niet $x$!)

De **modulusvergelijking** $\| x \| = 5$ heeft als oplossing $ x = 5 \lor x = -5 $

## Regels binnen (gebroken) vergelijkingen

* $AB = 0$ geeft $A = 0 \lor B = 0$
* $A^2=B^2$ geeft $A=B \lor A=-B$
* $AB=AC$ geeft $A=0 \lor B=C$
* $AB=A$ geeft $A=0 \lor B=1$  
* $\frac{A}{B} = 0$ geeft $A=0 \land B \neq 0$
* $\frac{A}{B} = C$ geeft $A=BC \land B \neq 0$
* $\frac{A}{B}=\frac{C}{D}$ geeft $AD=BC \land B \neq 0 \land D \neq 0$
* $\frac{A}{B}=\frac{C}{B}$ geeft $A=C \land B \neq 0$
* $\frac{A}{B}=\frac{A}{C}$ geeft $(A=0 \lor B=C) \land B \neq 0 \land C \neq 0$

## Wortelvergelijkingen en herleidingen

De 3 stappen voor het algebraïsch oplossen van wortelvergelijkingen zijn **isoleren**, **kwadrateren** en **controleren**. Eerst isoleer je de wortelvorm; je zet deze in het linker- of rechterlid en je haalt de rest naar het andere lid. Vervolgens kwadrateer je het linker- en rechterlid om de wortel weg te werken. Daarna kun je de vergelijking oplossen met bijv de abc-formule. Tenslotte zet je de verkregen uitkomsten in de oorspronkelijke vergelijkingen om te kijken of de uitkomst **voldoet**, want niet alle uitkomsten kloppen per se in de originele formule.

Bij het herleiden van een breuk kun je de teller en noemer ontbinden in factoren en vervolgens de teller en de noemer te delen door dezelfde factor. Deze factor valt dan weg.

Bij het ontbinden kun je gebruik maken van de merkwaardige producten:

* $A^2+2AB+B^2=(A+B)^2$
* $A^2-2AB+B^2=(A-B)^2$  
* $A^2-B^2=(A+B)(A-B)$

Bij breuken moet je er wel op letten dat je niet deelt door 0. Bij de vergelijking $\frac{x^2-2}{x+130}$ moet dus gelden dat $x+130 \neq 0$, dus $x \neq -130$.

Bij het herleiden van breuken gebruik je de volgende regels:

* $\frac{A}{B}+C=\frac{A+BC}{B}$
* $\frac{A}{B}+\frac{C}{D}=\frac{AD+BC}{BD}$  
* $A \cdot \frac{B}{C}=\frac{AB}{C} $
* $\frac{A}{B} \cdot \frac{C}{D}=\frac{AC}{BD}$  
* $\frac{A}{(\frac{B}{C})}=\frac{AC}{B}$ mits $C \neq 0$ (*delen door een breuk is vermenigvuldigen met het omgekeerde*)
* $\frac{(\frac{A}{B})}{C}=\frac{A}{BC}$

Bij de vergelijking $\frac{x^2-3x+5}{x}$ mag je $x$ niet wegstrepen, want dag mag alleen bij de **factoren** van een teller of noemer. Wel kun je $x$ bij deze vergelijking **uitdelen**:

$$\frac{x^2-3x+5}{x}$$

$$\frac{x^2}{x}-\frac{3x}{x}+\frac{5}{x}$$

$$x-3+\frac{5}{x}$$
