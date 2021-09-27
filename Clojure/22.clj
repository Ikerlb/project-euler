(require '[clojure.string :as string])

(defn read-file
  [f]
  (with-open
    [r (clojure.java.io/reader f)]
    (into [] (line-seq r))))

(def raw-string
  (string/join
    ""
    (read-file "./22.txt")))

(def names
  (sort
    (string/split
      (string/replace
        raw-string
        #"\""
        "")
      #",")))

(defn score
  [s]
  (*
   (inc i) 
   (apply
     +
     (map #(inc (- (int %) (int \A))) s))))

(apply + (map-indexed score names))
