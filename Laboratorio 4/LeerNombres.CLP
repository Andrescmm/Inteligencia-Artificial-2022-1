(defrule leer-personas
=> 
(open personas.txt fichero)

(assert(persona(readline fichero)))
(assert(persona(readline fichero)))
(close fichero)
)