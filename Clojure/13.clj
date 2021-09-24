(require '[clojure.string :as string])

(defn read-file
  [f]
  (with-open
    [r
     (clojure.java.io/reader f)]
    (into [] (line-seq r))))

(def nums 
  (map
    bigint 
    (read-file "./Clojure/13.txt")))

(defn first-k-digits-of-sum
  [nums k]
  (string/join
    ""
    (take k (str (apply + nums)))))

(first-k-digits-of-sum nums 10)


