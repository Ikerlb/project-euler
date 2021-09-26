(require '[clojure.string :as string])

(defn read-file
  [f]
  (with-open
    [r
     (clojure.java.io/reader f)]
    (into [] (line-seq r))))

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


(defn aux-propagate
  [i p n]
  (cond
    (== i 0) (+ (nth p 0) n)
    (== (inc i) (inc (count p))) (+ (nth p (dec i)) n)
    :else (+ n (max (nth p i) (nth p (dec i))))))


(defn propagate
  [p l]
  (map-indexed
    #(aux-propagate %1 p %2)
    l))  


(apply max
  (reduce
    propagate
    (parse-triangle 
      (string/join
        "\n"
        (read-file "./67.txt")))))
