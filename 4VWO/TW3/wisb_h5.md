---
layout: default
title: WISB - H5 - Samenvatting
test_code: 4A-WISB-T06
---

# Wiskunde B: Hoofdstuk 5 (Machten, exponenten en logaritmen)

## Rekenregels machten

- $a^p \cdot a^q=a^{p+q}$
- $\frac{a^p}{a^q}=a^{p-q}$
- $(a^p)^q=a^{pq}$
- $(ab)^p=a^pb^p$
- $a^0=1$
- $a^1=a$
- $a^{-p}=\frac{1}{a^p}$
- $a^{\frac{1}{q}}=\sqrt[q]{a}$
- $a^{\frac{p}{q}}=\sqrt[q]{a^p}$

Voor de vergelijking $x^{\frac{a}{b}}=c$ met $c>0$ en $x>0$ geldt $x^{\frac{a}{b}}=c$ geeft $x=c^{\frac{b}{a}}$.
Deze regel kun je ook toepassen om de variabele $x$ vrij te maken bij $y=ax^p$.

> Voorbeeld:  
> $y=19x^{-3 \frac{1}{2}}$  
> $19x^{-3 \frac{1}{2}}=y$  
> $19x^{-\frac{7}{2}}=y$  
> $x^{-\frac{7}{2}}=\frac{1}{19}y$  
> $x=(\frac{1}{19}y)^{-\frac{2}{7}}$  
> $x=(\frac{1}{19})^{-\frac{2}{7}}\cdot y^{-\frac{2}  {7}}$  
> $x=19^{\frac{2}{7}}\cdot y^{-\frac{2}{7}}$

## Standaardfuncties

De functies $f(x)=ax^n$ zijn **standaardfuncties**, en de bijbehorende grafieken zijn **standaardgrafieken**.
Bij even waarden van $n$ is de grafiek lijnsymmetrisch met de $y$-as. Bij oneven waarden van $n$ is de grafiek puntsymmetrisch met de oorsprong als punt van symmetrie.

Een grafiek kun je verschuiven: er ontstaat dan een **beeldgrafiek**. Deze verschuiving heet een **translatie**.
$$y=ax^n \xrightarrow{\text{translatie}~(p,~q)} y=a(x-p)^n+q$$
Voor een horizontale translatie van $p$ naar rechts vervang je x dus door $x-p$, en voor een horizontale translatie van  $p$ naar links vervang je x dus door $x+p$.
Voor een verticale translatie van $q$ tel je $q$ op bij de functiewaarde.
Voor een **vermenigvuldiging ten opzichte van de $x$-as** vermenigvuldig je de functiewaarde.
$$y=x^n \xrightarrow{\text{verm.}~x\text{-as met}~a} y=ax^n$$
Translaties en vermenigvuldigingen zijn voorbeelden van **transformaties**.

## Wortelfuncties

De eenvoudigste **wortelfunctie** is $f(x)=\sqrt{x}$. Dit is een **standaardfunctie**, en de grafiek is dus ook een **standaardgrafiek**. De grafiek is een halve parabool die de $y$-as in het **randpunt** $O(0,~0)$ raakt. Het domein (alle waarden op de $x$-as) van $f$ is $D_f=[0,\rightarrow \rangle$ en het bereik (alle waarden op de $y$-as) is $B_f=[0,\rightarrow \rangle$.

Om het domein te vinden van een wortelfunctie als $g(x)=-9+\sqrt{5+3x}$ ga je als volgt te werk:

- Onder het wortelteken moet een niet-negatief getal staan, want de wortel van een negatief getal heeft geen reële uitkomst, dus  
  $5+3x\geq 0$  
  $3x\geq -5$  
  $x\geq -\frac{5}{3}$  
- De $x$-coördinaat van het randpunt is dus $-\frac{5}{3}$, want hier begint de grafiek.
- Dus $D_g=[-\frac{5}{3},\rightarrow \rangle$
- De $y$-coördinaat van het randpunt krijg je door $g(-\frac{5}{3})=-9+\sqrt{5+3\cdot -\frac{5}{3}}=-9+\sqrt{0}=-9$.
- Het randpunt is dus $(-\frac{5}{3},~-9)$.

Je kunt de variabele $x$ vrijmaken bij een wortelfunctie als $y=2+\sqrt{x-3}$:  
$y-2=\sqrt{x-3}$  
$(y-2)^2=x-3$  
...  
$x=y^2-4y+7$

> Bij het vrijmaken van een variabele hoef je geen voorwaarden te vermelden.

## Exponentiele functies

De functies $f(x)=g^x$ met $g>0$ en $g\neq 1$ zijn **exponentiele standaardfuncties**.

Exponentiële standaardfuncties hebben een **asymptoot**: een lijn waarmee de grafiel op den duur vrijwel samenvalt.

De functie $f(x)=2^x$ valt samen met de $x$-as, dus de $x$-as is de **horizontale asymptoot**. Het bereik van deze functie is $B_f=\langle 0, \rightarrow \rangle$. Het domein bestaat uit alle reële getallen, dus $D_f=\mathbb{R}$.

Hieronder een overzicht van transformaties op $y=g^x$

- $y=g^x \xrightarrow{\text{verm.}~x\text{-as met}~a} y=a\cdot g^x$ (asymptoot $y=0$)
- $y=g^x \xrightarrow{\text{verm.}~y\text{-as met}~b} y=g^{\frac{1}{b}\cdot x}$ (asymptoot $y=0$)
- $y=g^x \xrightarrow{\text{translatie}~(0,~q)} y=g^x+q$ (asymptoot $y=q$)
- $y=g^x \xrightarrow{\text{translatie}~(p,~0)} y=g^{x-p}$ (asymptoot $y=0$)

Je kunt vergelijkingen als $y=120\cdot 3^{2x-1}$ herleiden tot de vorm $y=b\cdot g^x$. je maakt dan gebruik van de regels $(a^p)^q=a^{pq}$ en $a^p \cdot a^q=a^{p+q}$. Voorbeeld: $2^{3x-4}=2^{3x}\cdot 2^4=(2^3)^x\cdot 16=8^x\cdot 16$.

Een **exponentiele vergelijking** als $2^{12+x}=\sqrt{2}$ kun je oplossen met de regel $g^A=g^B$ geeft $A=B$. Om zo'n vergelijking op te lossen moeten beide leden dus hetzelfde grondtal hebben. Soms moet je eerst herleiden om 2 leden met een gelijk grondtal te krijgen.

> Voorbeeld:  
> $3^{x+2}=72+3^x$  
> $3^x\cdot 3^2=72+3^x$  
> $9\cdot 3^x-3^x=72$  
> $8\cdot 3^x=72$  
> $3^x=9$  
> $3^x=3^2$  
> $x=2$  

## Logaritmen

Als je wilt weten tot welke macht je een getal moet heffen om een bepaalde uitkomst te krijgen, moet je gebruik maken van een **logaritme**. Zo is $^2\log(8)$ het getal waar je 7 tot moet heffen om 8 te krijgen, dus $^2\log(8)=3$, want $2^3=8$.

$$^a\log(b)=c\longrightarrow b=a^c$$

In $^a\log(b)$ is $a$ het grondtal van de logaritme.
