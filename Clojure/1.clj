(ns projecteuler)

;; yield n if it is multiple of either 3 or 5, 0 otherwise
(defn is-mult-3-or-5
  [n]
  (if (or (== (mod n 3) 0) (== (mod n 5) 0)) n 0))

(defn sum-mults-3-or-5
  [n]
  (reduce (fn [s, i] (+ s (is-mult-3-or-5 i))) 0 (range n)))
