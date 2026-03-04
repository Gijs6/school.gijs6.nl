---
subject: NLT
title: Medicijnen
---

## Ontdekking van een geneesmiddel

> We hebben het in deze module over ziektes waarbij er een bepaald eiwit niet goed werkt

Het ontdekken van een geneesmiddel gaat in 3 stappen. **Target finding**: het vinden van het eiwit dat niet goed werkt, de **target** (of het **doeleiwit**). Daarna **lead finding**: het vinden van een **lead** (een **biologisch actieve stof**, ook wel **farmacon**) die het doeleiwit kan beïnvloeden. En **lead optimisation**: het optimaliseren van de lead.

### Preklinisch en klinisch onderzoek

Als je een lead hebt gevonden, ga je vervolgens deze stappen door:

1. **Preklinisch onderzoek**  
   Dit bestaat uit **in vitro** (gekweekte menselijke cellen in een lab) en **in vivo** (proefdieren) onderzoek.
2. **Klinisch onderzoek**  
   Dit onderzoek bestaat uit 4 fasen:
   - In **fase I** onderzoek je welke dosis effectief is bij een groep gezonde vrijwilligers.
   - In **fase II** stel je bij een kleine groep patiënten die aan de ziekte lijden de werking vast.
   - In **fase III** onderzoek je op grote schaal met **dubbelblind onderzoek** (onderzoek waarbij de onderzoekers en de patiënt niet weten of zij een medicijn krijgen of een placebo (een nepmiddel zonder enige werking)), zodat goed kan worden onderzocht of het medicijn überhaupt effect heeft. In deze fase wordt ook onderzoek gedaan naar de **effectmaat**: de drempelwaarde vanaf waar een medicijn effectief is. Op basis van het onderzoek uit deze fase wordt door de autoriteiten besloten of het geneesmiddel op de markt mag worden gebracht.
   - In **fase IV** gebeurt **post-marketing surveillance**: het in de gaten houden van bijwerkingen en de veiligheid van het geneesmiddel, nadat het middel al op de markt is gekomen.

### Patenten en preparaten

Het ontwikkelen van geneesmiddelen is heel duur. Met een **patent** heeft de houder het exclusieve recht om het geneesmiddel te maken en te verkopen, zodat bedrijven hun kosten kunnen terugverdienen. Een geneesmiddel waarop een patent zit heet een **specialité**. Als een patent verlopen is, mogen alle bedrijven het geneesmiddel maken. Deze geneesmiddelen noem je **loco-preparaten** (of **generieke preparaten**).

Een **me-too-preparaat** is een medicijn dat hetzelfde doeleiwit target als een bestaand medicijn, maar een ander leadmolecuul gebruikt. Het voordeel is dat je de target finding kunt overslaan.

Door dit (deels commerciële) systeem hebben medicijnen vaak 2 namen: een **generieke** (wetenschappelijke) naam, en de **merknaam** (verzonnen door de fabrikant).

**Farmacognosie** is onderzoek naar de geneeskrachtige werking van planten. Onderzoekers proberen dan de werkzame stof te isoleren en extraheren voor het maken van medicijnen.

## Moleculaire communicatie

Een **ligand** is een stof die kan binden aan een receptor (het is dus een boodschapper). Hierbij ontstaat een **ligand-receptorcomplex**.
Een **agonist** is een ligand dat iets stimuleert, terwijl een **antagonist** juist remt door de receptor te blokkeren.

Een medicijn kan zich aangrijpen op:

1. Een **GPCR** (een **G-eiwit-gekoppelde receptor**)
2. Enzymen, transporteiwitten, kanalen en pompen
3. Rechtstreeks (denk aan het toevoegen van een base om de pH van je maag te laten stijgen, of chemo)

Een groot deel van de medicijnen bindt zich aan een GPCR. Deze receptoren zijn lange ketens van aminozuren die 7 keer door het celmembraan slingeren.
Nadat een medicijn zich aan een GPCR heeft gekoppeld, ontstaat er een cascade van reacties, waarna een **second messenger** in de cel ontstaat. Vaak is dit **cAMP**. De concentratie cAMP laat zien of een medicijn een agonist is: bij een agonist neemt de concentratie cAMP toe.

## Affiniteit en dosis-respons

Als een ligand (L) zich bindt aan een receptor (R), ontstaat een ligand-receptorcomplex (LR). Dit is een evenwichtsreactie (want er binden steeds liganden en er verbreken steeds bindingen):

$$\ce{L + R <-->[{k_1}][{k_2}] LR}$$

$k_1$ is de snelheidsconstante voor de reactie naar rechts en $k_2$ voor die naar links.

Voor de reactiesnelheden geldt:

$v_\mathrm{naar\ rechts} = k_1 \cdot \ce{[L]} \cdot \ce{[R]}$  
$v_\mathrm{naar\ links} = k_2 \cdot \ce{[LR]}$

Bij een evenwicht zijn deze snelheden even groot:

$k_1 \cdot \ce{[L]} \cdot \ce{[R]} = k_2 \cdot \ce{[LR]}$

Dit kun je herschrijven als:

$\frac{k_2}{k_1}=\frac{\ce{[L]} \cdot \ce{[R]}}{\ce{[LR]}}=K_d$

$K_d$ is de **dissociatieconstante**.

Als de helft van het totale aantal receptoren gebonden is aan een ligand, geldt dat $\ce{[R]} = \ce{[LR]}$. Als je deze dan wegstreept uit de formule hierboven, krijg je $K_d = \ce{[L]}$.

De dissociatieconstante is dus een maat voor hoe graag het ligand aan de receptor wil binden: hoe lager de $K_d$, hoe 'liever' ze willen binden.
Je kunt de affiniteit ook aangeven met de $pD_2$ ($pD_2 = -\log(K_d)$). Nu geldt het omgekeerde: hoe hoger de $pD_2$, hoe groter de affiniteit.

De concentratie/hoeveelheid van het ligand is de **dosis**. We gaan ervan uit dat $\ce{[LR]}$ evenredig is met de **respons**.
De relatie tussen $\ce{[LR]}$ en $\ce{[L]}$ zet je uit in een **dosis-responsecurve**: je zet het logaritme van $\ce{[L]}$ op de x-as en $\ce{[LR]}$ op de y-as. De $K_d$ lees je dan makkelijk af: het is de concentratie van het ligand bij de helft van de respons.

In een dosis-responsecurve geldt ook: hoe meer links de curve ligt (dus hoe lager de $K_d$), hoe efficiënter het medicijn, want dan heb je bij een lagere concentratie al dezelfde respons.

## Maagzuurremmers

### Maagzuurproductie

Soms moet de pH in de maag worden verhoogd. De lage pH in de maag ontstaat doordat de cellen in de wand van de maag met een **protonpomp** ($\ce{H+}$/$\ce{K+}$-ATPase) $\ce{H+}$-ionen de maag in pompen (en $\ce{K+}$-ionen uit de maag).

De protonpomp gebruikt ATP als energiebron en wordt geactiveerd door kinase, dat op zijn beurt wordt geactiveerd door $\ce{Ca^{2+}}$.

Deze calciumionen kunnen op 3 manieren in de cel komen:

1. Als je voedsel eet, sturen je hersenen een signaal naar de maagwand om **acetylcholine** (ACh) te maken. ACh bindt zich aan zijn receptor aan de buitenkant van de maagwandcel, waardoor de concentratie cAMP stijgt en het proces om de calciumionenconcentratie te verhogen in gang wordt gezet.
2. ACh bindt zich ook aan ECL-cellen op de maagwand, die vervolgens **histamine** produceren. Histamine bindt zich aan zijn receptor aan de buitenkant van de maagwandcel, waardoor er meer cAMP in de cel komt en de calciumionenconcentratie stijgt.
3. Als je voedsel in je maag hebt, produceren cellen in het onderste deel van de maag het hormoon **gastrine**. Gastrine bindt zich aan zijn receptor aan de buitenkant van de maagwandcel, waardoor cAMP wordt gemaakt, waardoor de calciumionenconcentratie stijgt.

De remming van dit proces gebeurt door de stof $\mathrm{PGE_2}$. Deze stof bindt zich aan zijn receptor aan de buitenkant van de maagwandcellen, waardoor de vorming van het enzym **adenylylcyclase** wordt geremd, waardoor er minder cAMP is, en dus uiteindelijk minder calciumionen.

### Medicijnen tegen maagzuur

Om de maagzuurproductie te remmen, kun je meerdere dingen doen:

1. **PPI's** (proton pump inhibitors) blokkeren de protonpomp, waardoor er minder $\ce{H+}$ de maag in komt.
2. **Histaminereceptor-antagonisten** blokkeren de histaminereceptoren, waardoor de calciumionenconcentratie daalt, waardoor de concentratie kinase daalt, waardoor de werking van de protonpomp afneemt.
3. **$\mathrm{PGE_2}$-receptoragonisten** activeren de $\mathrm{PGE_2}$-receptoren, waardoor adenylylcyclase wordt geremd en er minder cAMP is, waardoor de calciumionenconcentratie daalt.
4. **Gastrinereceptor-antagonisten** bestaan echter niet, omdat de andere manieren al heel effectief zijn.

## Farmacokinetiek

**Farmacokinetiek** bestudeert wat het lichaam doet met een geneesmiddel. Dit gaat in een aantal fasen:

1. **Farmaceutische fase**
2. **Absorptiefase**
3. **Distributiefase**
4. **Metabolische fase**
5. **Farmacodynamische fase**
6. **Excretie- en eliminatiefase**

De fasen worden samengevat in de afkorting **ADMET**: **a**bsorptie, **d**istributie, **m**etabolisering, **e**liminatie en **t**oxicologie (geen fase, maar wel belangrijk).

### Farmaceutische fase

De farmaceutische fase gaat over de **toediening**. Dit kan op veel manieren, zoals een tablet/pil, zetpil, puffer, zalf, pleister, injectie, infuus, drankje, neusspray, oogdruppels, oordruppels, etc.

Een **slow-release-preparaat** is een medicijn dat in een capsule is verpakt, waardoor het geleidelijk vrijkomt.

### Absorptiefase

Hoe apolairder (dus beter vetoplosbaar) het geneesmiddel is, hoe beter het wordt opgenomen (de celmembranen zijn gemaakt van fosfolipiden). Zodra het geneesmiddel via de darmen in het bloed is gekomen, bevindt het zich in het interne milieu.

De **biologische beschikbaarheid** (F) geeft aan welk gedeelte van de toegediende dosis van een geneesmiddel uiteindelijk in de bloedsomloop terechtkomt.

### Verdelingsfase

Als je een medicijn opneemt, komt het niet alleen in je bloed terecht, maar het kan ook in vetweefsel ophopen of aan bloedeiwitten binden. De concentratie in het bloed daalt hierdoor, waardoor het lijkt alsof het medicijn zich over een veel groter volume heeft verdeeld: het **schijnbaar verdelingsvolume** ($V_d$).

$$V_d = \frac{D \cdot F}{C_t}$$

Hierin is $V_d$ het schijnbaar verdelingsvolume, $D$ de dosis, $F$ de biologische beschikbaarheid en $C_t$ de concentratie in het bloedplasma op een bepaald tijdstip $t$.

### Metabolische fase

In de lever worden veel geneesmiddelen uit het bloed gehaald en door enzymen gemetaboliseerd (omgezet in andere stoffen). De eerste keer dat het medicijn door de lever stroomt, wordt een deel meteen omgezet: het **first pass effect**.

Stoffen met een hoog first pass effect hebben na toediening een lage biologische beschikbaarheid (en dus een lage effectiviteit).

Sommige geneesmiddelen worden toegediend in een vorm die pas effect heeft nadat ze door de lever in een actieve stof zijn omgezet: **pro-drugs**.

### Eliminatiefase

Het verwijderen van een geneesmiddel uit het lichaam (**eliminatie**) gebeurt op 2 manieren: metabolisme en **excretie**.

Hierbij horen 2 belangrijke begrippen: **klaring** en de **halfwaardetijd**. Beide zijn voor elk medicijn anders.

De **klaring** ($\mathrm{Cl}$) is het plasmavolume dat per tijdseenheid wordt 'gezuiverd' van medicijn.

$$\mathrm{Cl} = \frac{\ln(2) \cdot V_d}{t_{1/2}}$$

Hierin is $\mathrm{Cl}$ de klaring, $V_d$ het schijnbaar verdelingsvolume en $t_{1/2}$ de halfwaardetijd.

De **halfwaardetijd** ($t_{1/2}$) is de tijd die nodig is om de helft van het medicijn uit het bloed te verwijderen.

Na 5 keer de halfwaardetijd is het medicijn volledig uit het lichaam verdwenen. Als je een nieuwe dosis toedient voordat die 5 halfwaardetijden voorbij zijn (dus als het **dosisinterval**, de tijd tussen twee doses, kleiner is dan $5 \cdot t_{1/2}$), hoopt het medicijn zich op: **accumulatie**.

#### Eerste-ordekinetiek

Bij de **eerste-ordekinetiek** werken de lever en nieren niet op volle kracht. De snelheid van de afbraak van een medicijn is dan recht evenredig met de concentratie van het medicijn in het bloed: hoe meer medicijn er in je bloed zit, hoe sneller het lichaam het medicijn afbreekt.

De concentratie op tijdstip $t$ is dan:

$$C_t = C_0 \cdot \left(\frac{1}{2}\right)^{t/t_{1/2}}$$

Hierin is $C_t$ de concentratie op tijdstip $t$, $C_0$ de beginconcentratie en $t_{1/2}$ de halfwaardetijd.

Bij de eerste-ordekinetiek is de halfwaardetijd onafhankelijk van de beginconcentratie.

#### Nulde-ordekinetiek

Bij de **nulde-ordekinetiek** werken de lever en nieren op maximale kracht en kunnen ze niet sneller. De afbraaksnelheid is dan constant: per tijdstap wordt er evenveel afgebroken, ongeacht hoeveel medicijn er in je bloed zit. De halfwaardetijd is dan *wel* afhankelijk van de beginconcentratie.

#### Steady state

Als er sprake is van accumulatie, ontstaat er na een tijdje een evenwicht: de **steady state**. De snelheid van toedienen is dan even groot als de snelheid van de afbraak, en de concentratie in het bloed schommelt stabiel rond een vaste waarde: de **steady-state-concentratie** ($C_{ss}$). Je bereikt de steady state na 5 keer de halfwaardetijd, ongeacht het dosisinterval of de dosis.

Voor de steady state geldt:

$$C_{ss} \cdot \mathrm{Cl} = \frac{D \cdot F}{\tau}$$

Hierin is $C_{ss}$ de steady-state-concentratie, $\mathrm{Cl}$ de klaring, $D$ de dosis, $F$ de biologische beschikbaarheid en $\tau$ het dosisinterval.

