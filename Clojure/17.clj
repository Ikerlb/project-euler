(require '[clojure.string :as string])

(def digits {0 "zero"
             1 "one"
             2 "two"
             3 "three"
             4 "four"
             5 "five"
             6 "six"
             7 "seven"
             8 "eight"
             9 "nine"})

(def teens {10 "ten"
            11 "eleven"
            12 "twelve"
            13 "thirteen"
            14 "fourteen"
            15 "fifteen"
            16 "sixteen"
            17 "seventeen"
            18 "eighteen"
            19 "nineteen"})

(def tens {2 "twenty"
           3 "thirty"
           4 "forty"
           5 "fifty"
           6 "sixty"
           7 "seventy"
           8 "eighty"
           9 "ninety"})

(defn spell-tens
  [n]
  (cond
    (< n 10) (digits n)
    (< n 20) (teens n)
    :else (if (zero? (mod n 10))
            (tens (quot n 10))
            (str
              (tens (quot n 10))
              " "
              (digits (mod n 10))))))

(defn spell-thousands
  [n]
  (cond
    (< n 100) (spell-tens n)
    (zero? (mod n 100)) (str
                         (digits (quot n 100))
                         " hundred")
    :else (str
            (digits (quot n 100))
            " hundred and "
            (spell-tens (mod n 100)))))

(defn letters-when-written
  [n]
  (count
    (string/replace
      (string/join " " (map spell-thousands (range 1 n)))
      #" "
      "")))

(+ (letters-when-written 1000) (count "onethousand"))

