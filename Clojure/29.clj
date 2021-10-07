(defn sq
  [n]
  (* n n))

;; standar non-tail-recursive
(defn pow
  [n p]
  (cond
    (zero? p) 1
    (even? p) (sq (pow n (int (/ p 2))))
    :else (* (sq (pow n (int (/ p 2)))) n)))

;; noice
;; note to self:
;; n**(2k) = ((n²)**k)
;; ((n²)**k) = ((n²)**(k/2))² if k is even
;; ((n²)**k) = (((n²)**(k/2))²)*n if k is odd
(defn pow-tr
  [n p]
  (loop [n n p p acc 1N]
    (cond
      (zero? p) acc
      (even? p) (recur
                  (sq n)
                  (int (/ p 2))
                  acc)
      :else (recur
              (sq n)
              (int (/ p 2))
              (* acc n)))))



;; uhmm not much thinking
;; went through this
(count
  (into #{}
    (map 
      #(apply pow-tr %)
      (for [a (range 2 101)
            b (range 2 101)]
        (list (biginteger a) (biginteger b))))))
