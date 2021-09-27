(require '[clojure.set :as s])

;; i don't like this
;; but its better than
;; what i had earlier
(defn divisors
  [n]
  (loop [i (int (Math/sqrt n)) res [1]]
      (cond
        (== i 1) res
        (not (zero? (mod n i))) (recur (dec i) res)
        :else (let
                [q (quot n i)]
                (if (== q i)
                  (recur (dec i) (conj res i))
                  (recur (dec i) (concat res [i q])))))))

;; simply sum the divisors 
(defn sum-of-divisors
  [n]
  (apply + (divisors n)))

;; memoize not really necesary
(def d sum-of-divisors)
(def d (memoize sum-of-divisors))

;; nums are small enough for 
;; this kinda brute forceish 
;; algorithm
(defn get-amicable-numbers
  [upto]
  (loop [a upto res #{}]
    (if (== a 1)
      res 
      (let
        [b (d a) db (d b)]
        (if (and (== db a) (not (== a b)))
          (recur (dec a) (conj (conj res a) b))
          (recur (dec a) res))))))

(apply + (get-amicable-numbers 10000))
