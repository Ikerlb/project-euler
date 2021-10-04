(require '[clojure.string :as string])

(defn divmod
  [n d]
  [(int (/ n d)) (mod n d)])

(defn slice
  [lst l r]
  (take
    (- r l)
    (drop l lst)))

(defn reciprocal-format-decimal-part
  [n d]
  (loop [n n i 0 m {} l []]
    (let
      [[dv md] (divmod n d)]
      (cond
        (zero? n) (string/join "" (conj l 0))
        (contains? m n) (str
                          (string/join
                            ""
                            (take (m n) l))
                          (format
                            "(%s)"
                            (string/join
                              ""
                              (slice
                                l
                                (m n)
                                (count l)))))
        :else (recur
                (* md 10)
                (inc i)
                (assoc m n i)
                (conj l dv))))))

(defn reciprocal-format
  [n d]
  (let
    [[dv md] (divmod n d)]
    (format
      "%d.%s"
      dv
      (reciprocal-format-decimal-part (* md 10) d))))


(apply max-key #(count (% 1))
  (map 
    #(vector %1 (reciprocal-format 1 %1))
    (range 2 1000)))
