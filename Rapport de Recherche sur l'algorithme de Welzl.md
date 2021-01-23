# Rapport de recherche sur l'algorithme de Welzl 

## Introduction

Le problème abordé ici est le problème du cercle minimum couvrant, aussi parfois appelé le problème du bureau de poste. Cela consiste a trouver un cercle de rayon minimum englobant un ensemble fini de points répartis dans un espace euclidien en deux dimensions, le problème peut être étendue a une troisième dimension mais nous resteront ici cantonné a la version deux dimensions. Ce problème a été soulevé pour la première fois par *James Joseph Sylvester (1814-1897)* en 1857.

Ce problème a de nombreuses applications pour permettre la modélisation de l'accès a une ressource (alors symbolisée par le centre du cercle minimum) a un ensemble de bénéficiaires (alors symbolisé par les points de l'ensemble fournit en entrée) on comprend alors sa deuxième dénomination : le problème du bureau de poste, la ressource étant ici un bureau de poste et les bénéficiaires les personnes ayant besoin d'être desservis par des tournées. Une troisième dénomination : le problème de la bombe, provenant du monde militaire nous montre que ce problème peut servir a modéliser le point d'impact d'une bombe (Le centre du cercle minimum) et l'ensemble d'objectif (les points de l'ensemble).

Pour résoudre le problème deux lemmes doivent être admis :

- Si un cercle de diamètre égale à la distance de deux points de la liste couvre tout autre point de la liste, alors ce cercle est un cercle couvrant de rayon minimum.
- Si on se place dans un espace en deux dimensions il n'existe un et un seul cercle minimum passant par 3 points non-colinéaires

### Structures de données

Dans les algorithmes sont utilisées plusieurs structures de donnée :

- Tableau : Conteneur de donnée permettant d'accéder a la donnée directement via leurs indices.
- Point : Objet mathématique ayant dans un repère en deux dimensions une position x et une position y toutes deux étant des réels
- Cercle : Objet géométrique caractérisé par un point étant a égale distance de tous les points composant son contour et un rayon qui est la distance entre le centre et le contour

### Objectif

Nous allons ici chercher a prouver qu'il est possible de résoudre ce problème a l'aide d'un algorithme, celui de Welzl, qui a une complexité de $O(n)$ et pour cela nous allons nous appuyer sur les résultats fournit par un algorithme naïf appliquant la méthode essai-erreur. Sa complexité est de $O(n^4)$ néanmoins il fournit fournit toujours le bon résultat. C'est donc en comparant leurs résultats expérimentaux et leur temps d'exécution que nous pourrons évaluer l'efficacité de Welzl.

### Algorithmes

#### Naïf

Pour cet algorithmes admettons **points** l'ensemble de $n$ points mis en entrée et $c$ le cercle couvrant minimum de rayon $r$.

```
Pour tout point p dans points :
	Pour tout point q dans points :
		c = cercle de centre (p+q)/2 de diamètre |pq|
		Si c couvre tous les points de points alors : 
			retourner c
resultat = cercle de rayon infini
Pour tout point p dans points :
	Pour tout point q dans points :
		Pour tout point r dans points :
			c = cercle circonscrit de p, q et r
			Si c couvre Points et que c < Resultat alors :
				reusltat = c
				
Retourner c
```

Cet algorithme va donc d'abord essayer toutes les paires de sommet et générer un cercle avec puis vérifier si ce dernier est couvrant. Si toutes ces tentatives échouent alors il sera tenté de construire un cercle a partir de trous les triplets de points.

##### Coûts

- 1 - 5 : $O(n^3)$
  - 3 : $O(1)$
  - 4-  5 : $O(n)$
- 6 : $O(1)$
- 7 - 13 : $O(n^3)$
  - 10 : $O(1)$
  - 11 - 12 : $O(n)$
- 14 : $O(1)$

Au total $O(n^3 + n^4 + 1) = O(n^4)$

#### Welzl

Pour cet algorithme nous admettons **P** l'ensemble des points et **R** l'ensemble des points se trouvant sur le contour du cercle couvrant minimum qui est donc vide au départ de l'algorithme.

Et en sortie le cercle couvrant minimum.

C'est algorithme récursif et cette dernière se termine lorsque nous arrivons dans un cas trivial, tel que trouver le cercle couvrant minimum passant par :

- 1 point, il est alors confondu avec son centre 
- 2 points, ce sont alors les extrémités de son diamètre
- 3 points, ce sont alors les sommets du triangle inscrit dans le cercle couvrant minimum

```
B_MINDISK : 
===========
Si P vide ou |R| < 3:
	Retourner Cercle de contour R
Sinon :
	choisir aléatoirement p dans P
	Retirer p de P
	D = B_MINDISK(P, R)
	Si D existe et p n'est pas dans D :
		Ajouter p dans R
		D = B_MINDISK(P, R)
Retourner D
```

##### Coût

Cet algorithme est en O(n)

## Résultats



## Discussion

## Conclusion

