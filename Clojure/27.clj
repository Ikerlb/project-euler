;; n² + an + b
;; n(n + a) + b    
;; abs(b) <= 1000 
;; abs(a) < 1000
;; n >= 0
;; for n == 0, n(n + a) + b = b so b should be prime

;; b should be prime
;; in particular it
;; it should be odd

;; n(n + a) + b => n(n + a) should be even
;; n(n + a) = n² + na
;; n(n + a) if n is even => na should be even => a can be both even or odd
;; n(n + a) if n is odd (n + a) should be even => since n is odd a should be odd

(defn is-prime?
  [n]
  (if (zero? (mod n 2))
    (== n 2)
    (let [upto (Math/ceil (Math/sqrt n))]
      (loop [i 3]
        (cond
          (> i upto) true
          (zero? (mod n i)) false
          :else (recur (+ i 2)))))))


;; could do sieve but
;; i'm kinda tired
(defn primes-upto
  [n]
  (filter
    is-prime?
    (range 2 (inc n))))

(defn consecutive-primes
  [a b]
  (loop [i 0N]
    (let [v (+ (* i (+ i a)) b)]
      (cond
        (and (>= v 0)(is-prime? v)) (recur (inc i))
        :else i))))

(apply *
  (apply max-key
    #(apply consecutive-primes %)
    (for [a (range -999 1000 2)
          b (primes-upto 1001)]
      (list a b))))
