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

;; aux function that returns
;; the index of the element
;; that is to go next
;; given the sorted vector of 
;; possible digits and 0 <= n < (count sv)!
(defn nth-perm-aux
  [v n]
  (let [m (factorial (dec (count v)))]
    (loop [i 0]
      (cond
        (in-range (* m i) n (* m (inc i))) [i (* m i)]
        :else (recur (inc i))))))

;; get nth permutation 
;; (obv in permutation)
;; order
(defn nth-perm
  [sv n]
  (loop [sv sv n n res []]
    (if (zero? n)
      (concat res sv)
      (let [[i nn] (nth-perm-aux sv n)]
        (recur
          (vec-remove i sv)
          (- n nn)
          (conj res (sv i)))))))

(nth-perm (vec (range 10)) 999999)
