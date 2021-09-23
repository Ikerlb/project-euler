;; get the nth triangle number
(defn nth-triangle-number
  [n]
  (/ (* n (+ n 1)) 2))

;; returns the number of
;; divisors of number n
;; should be carefull
;; with perfect squares
;; as they have odd number
;; of divisors
(defn num-divisors
  [n]
  (loop [i (int (Math/floor (Math/sqrt n)))
         r 0]
    (if (zero? i)
      r
      (if (zero? (mod n i))
        (if (== (/ n i) i)
          (recur (dec i) (inc r))
          (recur (dec i) (+ r 2)))
        (recur (dec i) r)))))

;; just checking if these constructs are in fact lazy xd
(take 10 (map nth-triangle-number (iterate inc 0)))

(defn first-number-more-than-k-divisors
  [k]
  (first
    (filter
      #(> (num-divisors %) k)
      (map nth-triangle-number (iterate inc 1)))))

(time (first-number-more-than-k-divisors 500))
