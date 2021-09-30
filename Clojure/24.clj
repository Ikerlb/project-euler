;; get nth factorial
(defn factorial
  [n]
  (apply * (map #(* 1N %) (range 1 (inc n)))))

;; should probably do
;; a macro for this
(defn in-range
  [mn n mx]
  (and (>= n mn) (< n mx)))

;; remove elem in coll
(defn vec-remove 
  [pos coll]
  (into (subvec coll 0 pos) (subvec coll (inc pos))))

(defn divmod
  [a b]
  [(quot a b) (mod a b)])

;; get nth permutation 
;; (obv in permutation)
;; order
(defn nth-perm
  [sv n]
  (loop [sv sv n n res []]
    (if (zero? n)
      (concat res sv)
      (let [[d m] (divmod n (factorial (dec (count sv))))]
        (recur
          (vec-remove d sv)
          m 
          (conj res (sv d)))))))

(nth-perm (vec (range 10)) 999999)
