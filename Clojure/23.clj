(defn sum-of-proper-divisors
  [n]
  (loop [i (int (Math/sqrt n)) res 1]
    (cond
      (== i 1) res
      (not (zero? (mod n i))) (recur (dec i) res)
      :else (let [q (quot n i)]
              (if (== q i)
                (recur (dec i) (+ res i))
                (recur (dec i) (+ (+ i q) res)))))))

(defn is-abundant?
  [n]
  (> (sum-of-proper-divisors n) n))

(defn abundants
  [lim]
  (filter is-abundant? (range 1 (inc lim))))

;; kinda brute-forceish
;; but well we'll try
;; to do better afterwards
(defn two-sum
  [t s]
  (loop [sq s]
    (cond
      (empty? sq) false
      (contains? s (- t (first sq))) true
      :else (recur (rest sq)))))

(def abundant-set (into #{} (abundants 28123)))

(defn sum-of-two-abundant?
  [n s]
  (cond
    (> n 28123) true
    :else (two-sum n s)))

(time (apply +
       (remove
         #(sum-of-two-abundant? % abundant-set)
         (range 28123))))
