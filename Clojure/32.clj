;; if either of the operands
;; is of size 4, then the other
;; operand MUST be of size 1
;; to allow for the remaining
;; numbers (the result) to be
;; at least 4. this gives us
;; a hard bound which we can
;; very comfortably work with

;; alternatively if we get 
;; a bound on the product itself
;; we can work our way backwards
;; if the number of digits
;; of the product is (denoted d(n))
;; d(n*m)=5 -> d(m) + d(n) should be 4
;; this however cannot happen
(* 100 100)

(defn divmod
  [n d]
  [(quot n d) (mod n d)])

(defn digits
  [n]
  (if (zero? n)
    (list 0)
    (loop [n n res ()]
      (cond
        (zero? n) res
        :else (let [[d m] (divmod n 10)]
                (recur d (conj res m)))))))

(defn are-pandigital?
  [a b]
  (let [ads (digits a)
        bds (digits b)
        pds (digits (* a b))
        s (into #{} (concat ads bds pds))]
    (and
      (not (contains? s 0))
      (== (count s) 9))))


;; returns multiples
;; lesser than  
;; square root
(defn multiples
  [n]
  (let [upto (int (Math/sqrt n))]
    (loop [i 2 res ()]
      (cond
        (== i upto) res
        (zero? (mod n i)) (recur
                            (inc i)
                            (conj res [(quot n i) i]))
        :else (recur (inc i) res)))))

(defn is-pandigital?
  [n]
  (some
    #(apply are-pandigital? %)
    (multiples n)))

;; TODO: tail recur this thingy
(defn combinations
  [l k]
  (cond
    (zero? k) (list (list))
    (empty? l) (list)
    :else (concat
            (map
              #(conj % (first l))
              (combinations (rest l) (dec k)))
            (combinations (rest l) k))))


(defn slice
  [coll s e]
  (take
    (- e s) 
    (drop
      s
      coll)))

(defn insert-in-all-indices
  [l e]
  (let [c (count l)]
   (map
     #(concat
        (slice l 0 %1)
        (list e)
        (slice l %1 c))
     (range (inc c)))))


;; TODO: tail recur this thingy
(defn permutations
  [l]
  (if (empty? l)
    (list (list)) 
    (mapcat
      #(insert-in-all-indices %1 (first l))
      (permutations (rest l)))))

;; maybe do this without permutations
;; and combinations
(defn combine-and-permute 
  [l k]
  (mapcat permutations (combinations l k)))

(defn to-number
  [l]
  (loop [l l res 0]
    (if (empty? l)
      res
      (recur
        (rest l)
        (+ (* res 10) (first l))))))

;; maybe faster with permutations
;; and combinations? idk
(time
  (apply
    +
    (filter
      is-pandigital?
      (range 1000 10000))))

;; it is at least
;; twice as fast
;; O.o
(time
  (apply
    +
    (filter
      is-pandigital?
      (map
        to-number
        (combine-and-permute (range 1 10) 4)))))
