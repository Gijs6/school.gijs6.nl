---
title: WISB - H4 - Samenvatting
indexname: WISB - H4 (Vergelijkingen en herleidingen)
layout: default
---

# Wiskunde B: Hoofdstuk 4 (Vergelijkingen en herleidingen)

## Getallenparen en stelsels

De algemene vorm van een lineaire vergelijking met $$x$$ en $$y$$ is $$ax+by=c$$. Uit deze verglijking kun je $$x$$ of $$y$$ vrijmaken.  
De getallenparen $$(x, y) = (4, -1)$$ en $$(x, y) = (-12, 5)$$ zijn oplossingen van de vergelijking $$3x+8y=4$$.  
Het getallenpaar $$(x, y) = (2, -1)$$ is zowel een oplossing van $$2x+y=3$$ als van $$x-2y=4$$. Je kunt ook zeggen dat $$(2, -1)$$ de oplossing is van het stelsel $$\left\{\begin{array}{left} 2x + y = 3 \\ x - 2y = 4 \\  \end{array}\right.$$. Om een stelsel op te lossen maak je eerst een vergelijking $$x$$ of $$y$$ vrij. Vervolgens substitueer je de formule voor de vrijgemaakte variabele in de andere vergelijking. Vervolgens gebruik je dit antwoord om de andere variabele te berekenen.

Je kunt stelsels ook oplossen door **elimineren door optellen of aftrekken**. Bij het stelsel $$\left\{\begin{array}{left} 8x+y=2 \\ 4x+y=5 \\  \end{array}\right.$$ trek je de vergelijkingen van elkaar af, want dan valt de $$y$$ weg. Kijk goed wat handiger is: optellen of aftrekken.  
Je kunt dit ook toepassen bij moeilijkere stelsels.

Je kunt stelsels ook oplossen door **elimineren na vermenigvuldigen**. Dan ga je eerst beide vergelijkingen vermenigvuldigen om er voor te zorgen dat er een variabele wegvalt bij het optellen of aftrekken.  
Bij het stelsel $$\left\{\begin{array}{left} 3x-4y=7 \\ 2x+3y=15 \\  \end{array}\right.$$ valt er na optellen of aftrekken geen enkele variabele weg. Maar als je de bovenste vergelijking met 2 vermenigvuldigt en de onderste vergelijking met 3, dan wel: $$\left\{\begin{array}{left} 3x - 4y = 7 \\ 2x + 3y = 15 \\  \end{array}\left|\begin{array}{cc} 2 \\ 3 \\  \end{array}\right|\right. = \left\{\begin{array}{left} 6x - 8y = 14 \\ 6x + 9y = 45 \\  \end{array}\right.$$
Je noteert de getallen waar je mee vermenigvuldigt tussen verticale strepen.

## Hogeregraadsvergelijkingen

De vergelijking $$x^2 = 5$$ heeft de oplossingen $$x=5$$ en $$x=-5$$. Je weet dat $$\sqrt{5}$$ de **tweedemachtswortel** van 5 is, want $$(\sqrt{5})^2 = 5$$. In dit geval staat er bij het wortelteken staat eigenlijk een "verborgen 2": $$\sqrt{a} = \sqrt[2]{a}$$ (dit geldt dus alleen als er geen getalletje bij het wortelteken staat!). Er zijn ook **hogeremachtswortels**, zoals derdemachtswortels. De vergelijking $$x^3 = 20$$ heeft als oplossing $$x=\sqrt[3]{20}$$.  
In de tabel zie je hoeveel oplossingen de vergelijking $$x^n = a$$ kan hebben.

| $$x^n = a$$ |                         $$a > 0$$                          |            $$a < 0$$             |
| :---------: | :--------------------------------------------------------: | :------------------------------: |
|  n is even  | 2 oplossingen: $$x = \sqrt[n]{a}$$ en $$x = -\sqrt[n]{a}$$ |   geen (reeële) oplossingen      |
| n is oneven |              1 oplossing: $$x = \sqrt[n]{a}$$              | 1 oplossing: $$x = \sqrt[n]{a}$$ |

Sommige hogeregraadsvergelijkingen kun je algebraïsch oplossen door te ontbinden in factoren. Soms door een factor buiten haakjes te brengen of door te substitueren. Binnen de vergelijking $$x^4-3x^2+2=0$$ kun je $$x^2$$ substitueren met $$u$$. Je krijgt dan $$u^2-3u+2=0$$. Deze kun je vervolgens oplossen met de product-som-methode. (Let op! Je hebt dan $$u$$ opgelost; nog niet $$x$$!)

De **modulusvergelijking** $$ \left|x\right| = 5 $$ heeft als oplossing $$ x = 5 \vee x = -5 $$

## Regels binnen (gebroken) vergelijkingen

* $$AB = 0$$ geeft $$A = 0 \vee B = 0$$
* $$A^2=B^2$$ geeft $$A=B \vee A=-B$$
* $$AB=AC$$ geeft $$A=0 \vee B=C$$
* $$AB=A$$ geeft $$A=0 \vee B=1$$  
* $$\frac{A}{B} = 0$$ geeft $$A=0 \wedge B \neq 0$$
* $$\frac{A}{B} = C$$ geeft $$A=BC \wedge B \neq 0$$
* $$\frac{A}{B}=\frac{C}{D}$$ geeft $$AD=BC \wedge B \neq 0 \wedge D \neq 0$$
* $$\frac{A}{B}=\frac{C}{B}$$ geeft $$A=C \wedge B \neq 0$$
* $$\frac{A}{B}=\frac{A}{C}$$ geeft $$(A=0 \vee B=C) \wedge B \neq 0 \wedge C \neq 0$$

## Wortelvergelijkingen en herleidingen

De 3 stappen voor het algebraïsch oplossen van wortelvergelijkingen zijn **isoleren**, **kwadrateren** en **controleren**. Eerst isoleer je de wortelvorm; je zet deze in het linker- of rechterlid en je haalt de rest naar het andere lid. Vervolgens kwadrateer je het linker- en rechterlid om de wortel weg te werken. Daarna kun je de vergelijking oplossen met bijv de abc-formule. Tenslotte zet je de verkregen uitkomsten in de oorspronkelijke vergelijkingen om te kijken of de uitkomst **voldoet**, want niet alle uitkomsten kloppen per se in de originele formule.

Bij het herleiden van een breuk kun je de teller en noemer ontbinden in factoren en vervolgens de teller en de noemer te delen door dezelfde factor. Deze factor valt dan weg.

Bij het ontbinden kun je gebruik maken van de merkwaardige producten:

* $$A^2+2AB+B^2=(A+B)^2$$
* $$A^2-2AB+B^2=(A-B)^2$$  
* $$A^2-B^2=(A+B)(A-B)$$

Bij breuken moet je er wel op letten dat je niet deelt door 0. Bij de vergelijking $$\frac{x^2-2}{x+130}$$ moet dus gelden dat $$x+130 \neq 0$$, dus $$x \neq -130$$.

Bij het herleiden van breuken gebruik je de volgende regels:

* $$\frac{A}{B}+C=\frac{A+BC}{B}$$
* $$\frac{A}{B}+\frac{C}{D}=\frac{AD+BC}{BD}$$  
* $$A \cdot \frac{B}{C}=\frac{AB}{C} $$
* $$\frac{A}{B} \cdot \frac{C}{D}=\frac{AC}{BD}$$  
* $$\frac{A}{(\frac{B}{C})}=\frac{AC}{B}$$ mits $$C \neq 0$$ (*delen door een breuk is vermenigvuldigen met het omgekeerde*)
* $$\frac{(\frac{A}{B})}{C}=\frac{A}{BC}$$


Functies die we tot nu toe behandeld hebben bij het vak wiskunde gaan van $$x$$ naar $$y$$: je vult een waarde in voor $$x$$ en je krijgt er 1 waarde voor $$y$$ uit. Je kunt ook functies hebben die **van $$y$$ naar $$x$$ gaan**. Deze functies kun je bijvoorbeeld krijgen als inverse functie van een "normale" (dus van $$x$$ naar $$y$$) functie. Om een inverse functie te maken, vervang $$x$$ en $$y$$ in de formule en maak je de variabele die je wil vrij. Voor de functie $$f(x) = 3x + 2$$ krijg je dus als inverse:

$$y=3x+2$$

$$x=3y+2$$

$$x-2=3y$$

$$y=\frac{x-2}{3}$$

$$f^{inv}(x)=\frac{x-2}{3}$$



De grafieken van inverse functies zijn elkaars spiegelbeelden in de lijn $$x = y$$.