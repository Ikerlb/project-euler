(defn sum-of-digits
  [n]
  (loop [n n acc 0]
    (cond
      (zero? n) acc
      :else (recur (quot n 10) (+ acc (mod n 10))))))

(defn fact
  [n]
  (apply * (map #(* 1N %) (range 1 n))))

(sum-of-digits (fact 100))
