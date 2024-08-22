package hello

import (
	"strings"
	"testing"
)

func TestSayHello(t *testing.T) {
	param := []string{"Shri", "Kant"}
	want := "Hello, " + strings.Join(param, ", ") + "!"
	got := Say(param)

	if want != got {
		t.Errorf("wanted %s, got %s", want, got)
	}
}
