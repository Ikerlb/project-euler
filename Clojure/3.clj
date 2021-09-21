(ns projecteuler)

;; divide by n d as much as you can
;; should probably use loop-recur
(defn divide-by 
  [nm, div]
  (loop [n nm d div]
    (if (== (mod n d) 0) (recur (/ n d) d) n)))

;; ok this is cool!
(defn prime-factors
  [upto]
  (loop [n upto i 2 l nil] 
    (if (= i (inc (int (Math/sqrt upto))))
      (if (= n 1) l (cons n l))
      (if (= (mod n i) 0)
        (recur (divide-by n i) (inc i) (cons i l))
        (recur (divide-by n i) (inc i) l)))))

;; return maximum of prime factors
(apply max (prime-factors 600851475143))
