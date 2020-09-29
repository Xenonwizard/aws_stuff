package main

import (
	"crypto/sha512"
	"encoding/hex"
	"fmt"
	"log"
	"net/http"
	"os"
	"time"
)

func main() {
	handler := http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		challengeArray, ok := r.URL.Query()["id"]

		if !ok || len(challengeArray[0]) < 1 {

			orderArray, ok := r.URL.Query()["order"]

			if !ok || len(orderArray[0]) < 1 {

				fmt.Fprintf(w, "Ok")
				return
			}

			appendToFile("Order UUID " + orderArray[0])

			fmt.Fprintf(w, "Order")
			return
		}

		challenge := challengeArray[0]
		answer := calculateAnswer(challenge)

		appendToFile("Unicorn served")

		fmt.Fprintf(w, answer)
		return
	})
	http.Handle("/", maxClients(handler, 1))

	log.Fatal(http.ListenAndServe(":80", nil))
}

func maxClients(h http.Handler, n int) http.Handler {
	sema := make(chan struct{}, n)

	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		sema <- struct{}{}
		defer func() { <-sema }()

		h.ServeHTTP(w, r)
	})
}

func calculateAnswer(challenge string) string {
	sha512 := sha512.New()
	sha512.Write([]byte(challenge))
	answer := hex.EncodeToString(sha512.Sum(nil))
	time.Sleep(time.Duration(2) * time.Second)

	return answer
}

func appendToFile(VerboseMessage string) {
	f, err := os.OpenFile("access.log", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		panic(err)
	}
	if _, err := f.Write([]byte(VerboseMessage + "\n")); err != nil {
		panic(err)
	}
	if err := f.Close(); err != nil {
		panic(err)
	}
	return
}
