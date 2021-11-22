(defn add-multiples-upto
  [m e coll]
  (loop [i (* m m) coll coll]
    (if (> i e)
      coll 
      (recur (+ i m) (conj coll i)))))

(defn sieve
  [upto]
  (loop [i 2 primes #{} not-primes #{}]
    (cond
      (== i upto) primes
      (contains? not-primes i) (recur
                                 (inc i)
                                 primes
                                 not-primes)
      :else (recur
              (inc i)
              (conj primes i)
              (add-multiples-upto i upto not-primes)))))

;; tail recurse this thing
(defn pow
  [n k]
  (if (zero? k)
    1
    (let [h (pow n (quot k 2))]
      (if (odd? k)
        (* h h n)
        (* h h)))))

(defn divmod
  [n d]
  [(quot n d) (mod n d)])

(defn rotate-digits
  [n nd]
  (let [[d m] (divmod n 10)]
    (+ d (* m (pow 10 (dec nd))))))

(defn number-of-digits
  [n]
  (loop [n n res 0]
    (if (zero? n) 
      res
      (recur (quot n 10) (inc res)))))

(defn all-digits-rotations
  [n]
  (let [nd (number-of-digits n)]
    (loop [rot (rotate-digits n nd) res [n]]
      (if (== rot n)
        res 
        (recur (rotate-digits rot nd) (conj res rot))))))

(defn is-circular?
  [n primes]
  (every? #(contains? primes %) (all-digits-rotations n)))

;; if upto is 110 for instance
;; then 109 will be checked
;; which when rotated yields
;; 901 which is bigger than 101
;; so we have to calculate sieve
;; upto the highest number possible
;; given those digits
(defn circular-primes
  [upto]
  (let [primes
        (sieve (dec (pow 10 (number-of-digits upto))))]
    (filter #(is-circular? % primes) (range 1 upto))))

(time (count (circular-primes 1000000)))
