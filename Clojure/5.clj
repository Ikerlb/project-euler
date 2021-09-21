;; takes gcd of two numbers
;; if more than two numbers
;; it applies them sequentially
;; (gcd is associative so no prob)
(defn gcd
  ([n m]
   (loop [n n m m]
     (if (zero? m)
       n
       (recur m (mod n m)))))
  ([n m & more]
    (apply gcd (gcd n m) more))) 

;; takes mcm of two numbers
;; if more than two numbers
;; it applies them sequentially
;; (mcm is associative so no prob)
(defn mcm
  ([n m] (/ (* n m) (gcd n m)))
  ([n m & more]
   (apply mcm (mcm n m) more)))


(apply mcm (range 1 20))
