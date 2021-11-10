;; there must be a limit
;; for how high a number 
;; can equal its factorial

;; (10**(a-1)) > (a*(9!))

(defn _factorial
  [n]
  (reduce * (range 1 (inc n))))

(def ! (memoize _factorial))

(defn sq
  [n]
  (* n n))

(defn ** 
  [n k]
  (loop [n n k k acc 1]
    (if (zero? k)
      acc
      (recur (sq n) (quot k 2) (if (odd? k) (* acc n) acc)))))

(defn divmod
  [n d]
  [(quot n d) (mod n d)])

(defn digits
  [n]
  (loop [n n acc ()]
    (if (zero? n)
      acc
      (recur (quot n 10) (conj acc (mod n 10))))))

(def digs (last (take-while #(<= (** 10 (dec %)) (* % (! 9))) (iterate inc 1))))

(count
  (filter
    #(== (apply + (map ! (digits %))) %)
    (range 1 (** 10 (inc digs)))))
