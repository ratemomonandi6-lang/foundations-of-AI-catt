@@ -1 +1,33 @@
%A simple illustration of a Family Tree constising of One parent
%4 Children
%And 4 GrandChildren
%The First Part is always about the factual information
%Facts
parent(nelson, sharon).
parent(nelson, robert).
parent(nelson, rose).
parent(nelson, ketty).
parent(sharon, viki).
parent(robert, dany).
parent(rose, mike).
parent(ketty, mercy).

male(nelson).
male(robert).
male(dany).
male(mike).

female(sharon).
female(rose).
female(ketty).
female(viki).
female(mercy).


%Rules
%A description of how the members relate to each other
grandparent(X, Z):- parent(X, Y) , parent(X, Y), parent(Y,Z).
aunt(X,Z):- parent(B,X), parent(B,Y), parent(Y,Z), female(X).
uncle(X,Z):- parent(B,X), parent(B,Y), parent(Y,Z), male(X).
niece(X,Z):- parent(A,Y), parent(A,Z), parent(Y,X),female(X).