(defn is-leap-year?
  [y]
  (cond
    (zero? (mod y 400)) true
    (zero? (mod y 100)) false
    (zero? (mod y 4)) true
    :else false))

(defn leap-year 
  [months y]
  (if (is-leap-year? y)
    (assoc months 1 29)
    (assoc months 1 28)))

(defn step
  [d m y months]
  (if (and (== d 30) (== m 11))
    [0 0 (inc y) (leap-year months (inc y))]
    [(mod (inc d) (months m))
      (+ m (quot (inc d) (months m)))
      y
      months]))

(def months {0 31
             1 28
             2 31
             3 30
             4 31
             5 30
             6 31
             7 31
             8 30
             9 31
             10 30
             11 31})

(defn days-elapsed-range
  [s e months]
  (take-while
    #(not
       (and
         (== (% 0) (e 0))
         (== (% 1) (e 1))
         (== (% 2) (e 2))))
    (iterate #(apply step %) (conj s months))))

(defn take-every-k
  [k s]
  (loop [s s i (dec k) res []]
    (cond
      (empty? s) res
      (zero? i) (recur (rest s) (dec k) (conj res (first s)))
      :else (recur (rest s) (dec i) res))))

;; take every 7 from the range
;; [1 jan 1900, 1 jan 2001)
;; then drop all from year 1900
;; then just check all that have day 1
(count
  (filter #(== (% 0) 0)
    (drop-while
      #(== (% 2) 1900)
      (take-every-k
        7
        (days-elapsed-range
          [0 0 1900]
          [0 0 2001]
          months)))))
