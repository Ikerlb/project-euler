;; get prime numbers lesser
;; or equal than upto
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

;; almost feels like cheating
;; hehe, but i'm truly out
;; of ideas here.
(time (def s (sieve-upto 1000000))))
