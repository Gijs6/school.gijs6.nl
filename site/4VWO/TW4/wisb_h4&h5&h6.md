---
subject: WISB
details_short: H4 & H5 & H6
details_medium: Hoofdstuk 4 & hoofdstuk 5 & hoofdstuk 6
details_extra: Vergelijkingen & herleidingen, machten & exponenten & logaritmen, differentiaalrekening
---

## Getallenparen en stelsels

De algemene vorm van een lineaire vergelijking in $x$ en $y$ is $ax + by = c$. Je kunt hieruit $x$ of $y$ vrijmaken.  
De getallenparen $(4, -1)$ en $(-12, 5)$ zijn oplossingen van $3x + 8y = 4$.  
Het paar $(2, -1)$ is oplossing van zowel $2x + y = 3$ als $x - 2y = 4$, oftewel van het stelsel:

$$
\begin{cases}
2x + y = 3 \\
x - 2y = 4
\end{cases}
$$

Om een stelsel op te lossen maak je eerst $x$ of $y$ vrij in een vergelijking. Daarna vervang je deze uitdrukking in de andere vergelijking en los je op. Met dit antwoord bereken je de andere variabele.

Je kunt ook oplossen door **elimineren door optellen of aftrekken**:

$$
\begin{cases}
8x + y = 2 \\
4x + y = 5
\end{cases}
$$

Hier trek je de vergelijkingen van elkaar af, zodat $y$ wegvalt. Kies steeds wat handiger is: optellen of aftrekken. Dit werkt ook bij complexere stelsels.

Een andere methode is **elimineren na vermenigvuldigen**. Vermenigvuldig beide vergelijkingen zodat bij optellen of aftrekken een variabele wegvalt. Bijvoorbeeld:

$$
\begin{cases}
3x - 4y = 7 \\
2x + 3y = 15
\end{cases}
$$

Na optellen of aftrekken valt er geen variabele weg. Vermenigvuldig de bovenste vergelijking met 2 en de onderste met 3:

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

De getallen waarmee je vermenigvuldigt noteer je tussen verticale strepen.

## Hogeregraadsvergelijkingen

De vergelijking $x^2 = 5$ heeft oplossingen $x = \sqrt{5}$ en $x = -\sqrt{5}$. $\sqrt{5}$ is de tweede machtswortel, want $(\sqrt{5})^2 = 5$. Bij het wortelteken staat eigenlijk een verborgen 2: $\sqrt{a} = \sqrt[2]{a}$ (alleen als er geen getal bij het wortelteken staat). Er bestaan ook hogere machtswortels, zoals derde machtswortels. Bijvoorbeeld: $x^3 = 20$ heeft oplossing $x = \sqrt[3]{20}$.

In de tabel staat het aantal oplossingen van $x^n = a$:

| $x^n = a$  |               $a > 0$                |            $a < 0$             |
| :--------: | :----------------------------------: | :----------------------------: |
|  $n$ even  | 2 oplossingen: $x = \pm \sqrt[n]{a}$ |     geen reële oplossingen     |
| $n$ oneven |    1 oplossing: $x = \sqrt[n]{a}$    | 1 oplossing: $x = \sqrt[n]{a}$ |

Sommige hogeregraadsvergelijkingen kun je algebraïsch oplossen door ontbinden in factoren, bijvoorbeeld door een factor buiten haakjes te halen of te substitueren.  
In $x^4 - 3x^2 + 2 = 0$ kun je $x^2 = u$ substitueren. Dan krijg je $u^2 - 3u + 2 = 0$, die je oplost met de product-som-methode. (Let op: je hebt $u$ opgelost, niet $x$!)

De **modulusvergelijking** $\|x\| = 5$ heeft oplossingen $x = 5$ of $x = -5$.

## Regels binnen (gebroken) vergelijkingen

- $AB = 0 \implies A = 0 \lor B = 0$
- $A^2 = B^2 \implies A = B \lor A = -B$
- $AB = AC \implies A = 0 \lor B = C$
- $AB = A \implies A = 0 \lor B = 1$
- $\frac{A}{B} = 0 \implies A = 0 \land B \neq 0$
- $\frac{A}{B} = C \implies A = BC \land B \neq 0$
- $\frac{A}{B} = \frac{C}{D} \implies AD = BC \land B \neq 0 \land D \neq 0$
- $\frac{A}{B} = \frac{C}{B} \implies A = C \land B \neq 0$
- $\frac{A}{B} = \frac{A}{C} \implies (A = 0 \lor B = C) \land B \neq 0 \land C \neq 0$

## Wortelvergelijkingen en herleidingen

De 3 stappen voor het algebraïsch oplossen van wortelvergelijkingen zijn: **isoleren**, **kwadrateren**, **controleren**.  
Eerst isoleer je de wortel. Vervolgens kwadrateer je beide leden om de wortel te elimineren. Daarna los je op, bijvoorbeeld met de abc-formule. Tot slot controleer je of de oplossingen voldoen, want niet alle antwoorden passen in de originele vergelijking.

Bij het herleiden van breuken kun je teller en noemer ontbinden en delen door dezelfde factor, die dan wegvalt.

Bij het ontbinden kun je gebruik maken van de merkwaardige producten:

- $A^2 + 2AB + B^2 = (A + B)^2$
- $A^2 - 2AB + B^2 = (A - B)^2$
- $A^2 - B^2 = (A + B)(A - B)$

Let bij breuken op dat je niet deelt door 0. Bijvoorbeeld bij $\frac{x^2 - 2}{x + 130}$ geldt $x \neq -130$.

Regels voor breuken:

- $\frac{A}{B} + C = \frac{A + BC}{B}$
- $\frac{A}{B} + \frac{C}{D} = \frac{AD + BC}{BD}$
- $A \cdot \frac{B}{C} = \frac{AB}{C}$
- $\frac{A}{B} \cdot \frac{C}{D} = \frac{AC}{BD}$
- $\frac{A}{\frac{B}{C}} = \frac{AC}{B}$ mits $C \neq 0$ (delen door een breuk is vermenigvuldigen met het omgekeerde)
- $\frac{\frac{A}{B}}{C} = \frac{A}{BC}$

Bij de vergelijking $\frac{x^2-3x+5}{x}$ mag je $x$ niet wegstrepen, want dat mag alleen bij de **factoren** van een teller of noemer. Wel kun je $x$ bij deze vergelijking **uitdelen**:

$$\frac{x^2-3x+5}{x}$$

$$\frac{x^2}{x}-\frac{3x}{x}+\frac{5}{x}$$

$$x-3+\frac{5}{x}$$

## Rekenregels machten

- $a^p \cdot a^q = a^{p+q}$
- $\frac{a^p}{a^q} = a^{p-q}$
- $(a^p)^q = a^{pq}$
- $(ab)^p = a^p b^p$
- $a^0 = 1$
- $a^1 = a$
- $a^{-p} = \frac{1}{a^p}$
- $a^{\frac{1}{q}} = \sqrt[q]{a}$
- $a^{\frac{p}{q}} = \sqrt[q]{a^p}$

Voor $x^{\frac{a}{b}} = c$ met $x > 0$ en $c > 0$ geldt:  
$$x = c^{\frac{b}{a}}$$  
Gebruik deze regel om $x$ vrij te maken bij $y = ax^p$.

> Voorbeeld:  
> $y = 19x^{-3\frac{1}{2}}$  
> $19x^{-\frac{7}{2}} = y$  
> $x^{-\frac{7}{2}} = \frac{1}{19}y$  
> $x = \left(\frac{1}{19}y\right)^{-\frac{2}{7}} = 19^{\frac{2}{7}} \cdot y^{-\frac{2}{7}}$  

## Standaardfuncties

De functies $f(x)=ax^n$ zijn **standaardfuncties**, en de bijbehorende grafieken zijn **standaardgrafieken**.  
Bij even waarden van $n$ is de grafiek lijnsymmetrisch met de $y$-as.  
Bij oneven waarden van $n$ is de grafiek puntsymmetrisch met de oorsprong als punt van symmetrie.

Een grafiek kun je verschuiven: er ontstaat dan een **beeldgrafiek**. Deze verschuiving heet een **translatie**.  
$$y=ax^n \xrightarrow{\text{translatie}~(p,~q)} y=a(x-p)^n+q$$  
Voor een horizontale translatie van $p$ naar rechts vervang je $x$ dus door $x-p$, en voor een horizontale translatie van $p$ naar links vervang je $x$ dus door $x+p$.  
Voor een verticale translatie van $q$ tel je $q$ op bij de functiewaarde.

Voor een **vermenigvuldiging ten opzichte van de $x$-as** vermenigvuldig je de functiewaarde:  
$$y=x^n \xrightarrow{\text{verm.}~x\text{-as met}~a} y=ax^n$$  
Translaties en vermenigvuldigingen zijn voorbeelden van **transformaties**.

## Wortelfuncties

De eenvoudigste **wortelfunctie** is $f(x)=\sqrt{x}$. Dit is een **standaardfunctie**, en de grafiek is dus ook een **standaardgrafiek**.  
De grafiek is een halve parabool die de $y$-as in het **randpunt** $O(0,~0)$ raakt.  
Het domein van $f$ is $D_f=[0,\rightarrow \rangle$ en het bereik is $B_f=[0,\rightarrow \rangle$.

Om het domein te vinden van een wortelfunctie als $g(x)=-9+\sqrt{5+3x}$ ga je als volgt te werk:

- Onder het wortelteken moet een niet-negatief getal staan, want de wortel van een negatief getal heeft geen reële uitkomst, dus  
  $5+3x\geq 0$  
  $3x\geq -5$  
  $x\geq -\frac{5}{3}$  
- De $x$-coördinaat van het randpunt is dus $-\frac{5}{3}$, want hier begint de grafiek.
- Dus $D_g=[-\frac{5}{3},\rightarrow \rangle$
- De $y$-coördinaat van het randpunt krijg je door $g(-\frac{5}{3})=-9+\sqrt{5+3\cdot -\frac{5}{3}}=-9+\sqrt{0}=-9$
- Het randpunt is dus $(-\frac{5}{3},~-9)$

Je kunt de variabele $x$ vrijmaken bij een wortelfunctie als $y=2+\sqrt{x-3}$:  
$y-2=\sqrt{x-3}$  
$(y-2)^2=x-3$  
...  
$x=y^2-4y+7$

> Voorwaarden hoef je niet te vermelden bij het vrijmaken.

## Exponentiële functies

Functies van de vorm $f(x) = g^x$ met $g > 0$, $g \neq 1$ zijn **exponentiële standaardfuncties**.

Voorbeeld: $f(x) = 2^x$

Exponentiële standaardfuncties hebben een **asymptoot**: een lijn waarmee de grafiek op den duur vrijwel samenvalt.

De functie $f(x)=2^x$ nadert de $x$-as, dus de $x$-as is de **horizontale asymptoot**.  
Het bereik is $B_f=\langle 0, \rightarrow \rangle$ en het domein is $D_f=\mathbb{R}$.

Hieronder een overzicht van transformaties op $y=g^x$:

- $y=g^x \xrightarrow{\text{verm.}~x\text{-as met}~a} y=a\cdot g^x$ (asymptoot $y=0$)
- $y=g^x \xrightarrow{\text{verm.}~y\text{-as met}~b} y=g^{\frac{1}{b}\cdot x}$ (asymptoot $y=0$)
- $y=g^x \xrightarrow{\text{translatie}~(0,~q)} y=g^x+q$ (asymptoot $y=q$)
- $y=g^x \xrightarrow{\text{translatie}~(p,~0)} y=g^{x-p}$ (asymptoot $y=0$)

Je kunt vergelijkingen als $y=120\cdot 3^{2x-1}$ herleiden tot de vorm $y=b\cdot g^x$. Je maakt dan gebruik van de regels $(a^p)^q=a^{pq}$ en $a^p \cdot a^q=a^{p+q}$.  
Voorbeeld: $2^{3x-4}=2^{3x}\cdot 2^{-4}=(2^3)^x\cdot \frac{1}{16}=8^x\cdot \frac{1}{16}$

Een **exponentiële vergelijking** als $2^{12+x}=\sqrt{2}$ kun je oplossen met de regel: $g^A=g^B$ geeft $A=B$.  
Om zo'n vergelijking op te lossen moeten beide leden hetzelfde grondtal hebben. Soms moet je eerst herleiden.

> Voorbeeld:  
> $3^{x+2}=72+3^x$  
> $3^x\cdot 3^2=72+3^x$  
> $9\cdot 3^x - 3^x = 72$  
> $8\cdot 3^x = 72$  
> $3^x = 9$  
> $3^x = 3^2$  
> $x = 2$

## De logaritme

Om te weten tot welke macht je een bepaald getal moet heffen om een bepaalde uitkomst te krijgen, gebruik je een **logaritme**.  
Dus voor $2^n=16$ geeft de logaritme met grondtal 2 de macht. Dus $^2\log (16) = 4$, want $2^4=16$.
Dus $^g\log(x)$ is de expoent van een macht met grondtal $g$ waarbij de uitkomst $x$ is.

$$^g\log(x) = y \implies x=g^y$$

## De afgeleide

De afgeleide geeft voor elke $x$ de richtingscoëfficiënt van de raaklijn aan de grafiek in dat punt.

Het berekenen van de afgeleide heet **differentiëren**.

De definitie van de afgeleide is $f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$, maar er zijn standaardregels:

- $f(x) = a$ geeft $f'(x) = 0$
- $f(x) = ax$ geeft $f'(x) = a$
- $f(x) = ax^n$ geeft $f'(x) = anx^{n-1}$
- $f(x) = c \cdot g(x)$ geeft $f'(x) = c \cdot g'(x)$
- $s(x) = f(x) + g(x)$ geeft $s'(x) = f'(x) + g'(x)$
- $v(x) = f(x) - g(x)$ geeft $v'(x) = f'(x) - g'(x)$
- $p(x) = f(x) \cdot g(x)$ geeft $p'(x) = f'(x) \cdot g(x) + f(x) \cdot g'(x)$
- $q(x) = \frac{t(x)}{n(x)}$ geeft $q'(x) = \frac{t'(x) \cdot n(x) - t(x) \cdot n'(x)}{n(x)^2}$

Als de functie als breuk staat, schrijf je de afgeleide ook als breuk. Dit geldt ook bij negatieve exponenten.

## Extreme waarden

Bij een extreme waarde is de raaklijn horizontaal, dus helling 0.  
Omdat de afgeleide de helling geeft, bepaal je extreme waarden door $f'(x) = 0$ op te lossen.

> Controleer met je GR of het om een maximum of minimum gaat.

Een **buigpunt** is een punt waar de helling verandert, bijvoorbeeld van toenemend stijgend naar afnemend stijgend.  
Op een buigpunt heeft de afgeleide een extreme waarde.  
Gebruik de tweede afgeleide $f''(x)$ om het buigpunt te vinden.

De raaklijn in een buigpunt heet de **buigraaklijn**.

## Kettingregel

De functie $f(x) = (2x^2 - 8x)^6$ is een **samengestelde functie**, opgebouwd uit $v(x) = 2x^2 - 8x$ en $u(v) = v^6$.

Voor samengestelde functies gebruik je de **kettingregel**:  
$$f(x) = u(v(x)) \implies f'(x) = u'(v(x)) \cdot v'(x)$$

Voor $f(x) = (2x^2 - 8x)^6$ is de afgeleide:  
$$f'(x) = 6(2x^2 - 8x)^5 \cdot (4x - 8)$$

> Onthoud:  
> $g(x) = \sqrt{x}$ geeft $g'(x) = \frac{1}{2\sqrt{x}}$

## Kromme door toppen

De toppen van de functie $f_p(x) = -\frac{1}{3}x^3 + 1\frac{1}{2}x^2 + p x - 5$ liggen op een kromme.

Bereken $f_p'(x)$ en stel gelijk aan 0:  
$f_p'(x) = -x^2 + 3x + p = 0 \Rightarrow p = x^2 - 3x$  
Invullen in de originele functie geeft:  
$$y = -\frac{1}{3}x^3 + 1\frac{1}{2}x^2 + (x^2 - 3x)\cdot x - 5 = \frac{2}{3}x^3 - 1\frac{1}{2}x^2 - 5$$  
Dit is de kromme waarop de toppen liggen.

## Raken en snijden

De grafieken van $f(x)$ en $g(x)$ **raken** elkaar in $A$ als:  
$$f(x) = g(x) \land f'(x) = g'(x)$$  
Dus: gelijke $y$-waarde én gelijke helling.

Twee lijnen $k$ en $l$ snijden elkaar loodrecht als:  
$$\mathrm{rc}_k \cdot \mathrm{rc}_l = -1 \quad (\mathrm{rc}_k \neq 0,~\mathrm{rc}_l \neq 0)$$

De grafieken van $f(x)$ en $g(x)$ **snijden** elkaar loodrecht in $A$ als:  
$$f(x) = g(x) \land f'(x)\cdot g'(x) = -1$$
