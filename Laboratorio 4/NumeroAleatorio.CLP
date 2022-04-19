(defrule pregunta-numero
=>
(bind ?aux 100)
(while (neq ?aux 17)
(printout t "¿Escoge un numero del 1 aL 100? " crlf)
(bind ?aux (read))

(if (> ?aux 17)
then
(printout t "El numero que buscas es menor" crlf))

(if (< ?aux 17)
then
(printout t "El numero que buscas es mayor" crlf))
))