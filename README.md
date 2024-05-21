# Doble intèrpret de JSBach

Aquesta és una implementació del doble interpret per el llenguatge JSBach, la pràcitca de LP del Juny del 2022. Les especificacions del llenguatge es poden trobar a l'[enunciat](https://github.com/jordi-petit/lp-jsbach-2022#especificació-de-jsbach).

## Instal·lació

Per instal·lar l'intèrpret cal tenir Python 3.7 (o més) instal·lat i un entorn amb `antlr4-python3-runtime==4.10`.
Aquesta llibreria es pot instal·lar amb:

```{sh}
pip install antlr4-python3-runtime==4.10
```

Per tal que l'intèrpret també generi les partitures i fitxers d'àudio caldrà tenir instal·lat Lilypond, Timidity++ i ffmpeg.

Des de mac es pot fer:

```{sh}
brew install lilypond
brew install timidity
brew install ffmpeg
```

per instal·lar els programes que generen la música.

També caldrà instal·lar ANTLR seguint la [guia oficial](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md) per tal de generar els visitadors base i els mòduls d'anàlisi lèxic a partir de la gramàtica definida a `JSBach.g4`.

## Com s'executa

Per invocar l'interpret i executar un script en JSBach hem de fer:

```{sh}
python jsbach.py <nom-del-programa>.jsb
```

Aquesta comanda executarà la funció Main dins del nostre programa. En cas que volguem executar una funció diferent només caldrà passar-la com a paràmetre:

```{sh}
python jsbach.py hanoi.jsb Hanoi
```

## Decisions de disseny i d'implementació

Per complir les condicions que proposava l'enunciat, la gramàtica d'aquest llenguatge està feta de manera que la regla `root` llegeix almenys un procediment, on cada procediment està format per la capçalera (on hi ha els paràmetres que pren) i almenys una instrucció. Les instruccions són les especificades a l'enunciat.

El visitador per aquesta gramàtica en primer lloc guarda la informació de tots els procediments en un diccionari de procediments. Cada procediment es representa per un diccionari amb dues claus: arguments i instruccions. Els arguments són una llista de strings que indiquen els noms dels arguments, i les instruccions son una altra llista que guarda els contextos de les instruccions.

La gestió de l'estat s'ha implementat amb una cua LIFO (o pila) i un diccionari que guarda l'estat actual; en la inicialització, aquests objectes estan buits. Quan es crida un procediment, l'estat actual s'empila i es crea un estat nou a partir dels paràmetres passats (és a dir, s'evaluen les expresions que s'han passat com a paràmetres i se'ls dona el nom corresponent al seu argument). Per resoldre l'estat després d'executar el procediment, s'assigna el valor del primer element de la pila a l'estat actual. Aquesta acció treu de la pila l'estat vell. Després, per complir amb el requeriment que __les llistes es passen per referència__ es modifica l'estat que s'havia tret de la pila. Per fer-ho s'agafen les llistes que teníem a l'estat vell (abans del procediment) i es mira si alguna s'havia passat com a paràmetre amb nom _x_. Llavors s'assigna el valor de la llista _x_ en l'estat del procediment a la variable (llista) que s'havia passat com a _x_. Els diccionaris per representar l'estat són _defaultdicts_ de Python amb valor per defecte 0.

Els errors de tipus es detecten al visitador en temps d'execució. La gramàtica defineix expresions `expr` que poden ser passades com a paràmetres a procediments i instruccions. Segons cada instrucció es comprova que el tipus rebut és l'esperat, i si no s'aixeca un error de tipus en temps d'execució. Per exemple, les llistes no poden ser comparades, ni sumades (o altres operacions d'enters) entre elles. Si s'intenta fer una operació així, salta un error de tipus.

### Notes

Malgrat en l'enunciat apareixien alguns exemples d'operacions per notes, no s'acaben d'especificar tots els detalls. També s'esmenta que una nota és una constant per un enter, però les notes en aquesta implementació tenen una durada asociada de manera que una nota és en realitat un parell: (constant identificatiu de la nota, durada de la nota)

* Per comparar notes, només es té en compte la constant, no la duració.
* Es poden operar notes amb enters sempre i quan el primer operand sigui una nota i el segon un enter. La nota resultant manté la duració i canvia només la constant identificativa. Si en algun moment una nota surt del range [A0, C8] (en el domini dels enters [0, 51]) s'aixeca un error de tipus. Per això no és recomenable fer gaires operacions amb notes ja que poden saltar errors. Una altra manera per solucionar el fet que si es deixen fer operacions amb notes el resultat pot sortir del rang seria aplicar mòdul 52 al resultat; en aquest cas podem trobar loops infinits com el següent exemple:

```{jsb}
Main |:
    note <- A0
    while note <= C8 |:
        <:> note
        note <- note + 1
    :|
:|
```

Per aquesta raó s'ha decidit que les notes més altes que C8 no existeixen en JSBach i salten errors quan intentem definir-ne una.

#### Autor: Jordi Puig Rabat
