;; very similar to problem 8
(defn sieve-upto
  ([upto]
    (loop [u upto i 3 np #{} p [2]]
      (if (> i u)
        p
        (if (contains? np i)
          (recur u (+ i 2) np p)
          (recur
            u
            (+ i 2)
            (into np (range (* i i) u i))
            (conj p i)))))))

(time (def sieve (sieve-upto 2000000)))
(apply + sieve)
