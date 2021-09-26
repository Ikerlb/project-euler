(require '[clojure.string :as string])

(def raw-string "75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23")

(defn s-to-int
  [s]
  (Integer/parseInt s))

(defn parse-line
  [l]
  (map s-to-int (string/split l #" ")))

(defn parse-triangle
  [s]
  (map
    parse-line
    (string/split s #"\n")))

;; divide this into
;; functions because
;; it is ugleeeeeeeeeeeeeeeeey
(defn propagate
  ([p l] (propagate p l 0 []))
  ([p l i res]
  (cond
    (== i 0) (recur p l (inc i) (conj res (+
                                           (nth p 0)
                                           (nth l 0))))
    (== (inc i) (count l)) (conj res (+
                                      (nth p (dec i))
                                      (nth l i)))
    :else (recur p l (inc i) (conj
                               res
                               (+ (max
                                    (nth p i)
                                    (nth p (dec i)))
                                  (nth l i)))))))


(map-indexed #(println %1 %2) [1 2 3 4])

(defn aux-propagate
  [i p n]
  (println (+ (nth p 0) n))
  (cond
    (i == 0) (+ (nth p 0) n)
    (== (inc i) (inc (count p))) (+ (nth p (dec i)) n)
    :else (+ n (max (nth p i) (nth p (dec i))))))

(map-indexed println [10 2 3 4123])

(propagate [75] [7237 1234])

(defn propagate
  [p l]
  (map-indexed
    #(aux-propagate %1 p %2)
    l))  


(apply max
  (reduce
    propagate
    (parse-triangle raw-string)))

(map-indexed println [1 2 3 4])
