package main

import (
	"github.com/moovweb/gokogiri"
	"github.com/moovweb/gokogiri/xpath"
	"os"
	"io/ioutil"
	"fmt"
)

func main() {
	content, err := ioutil.ReadFile(os.Args[1])
	doc, err := gokogiri.ParseHtml(content)
	if err != nil {
		panic(err)
	}
	defer doc.Free()
	xp := doc.DocXPathCtx()
	defer xp.Free()
	xps := xpath.Compile("//div[@id='content']/article")
	ss, err := doc.Root().Search(xps)
	if err != nil {
		panic(err)
	}
	for _, s := range(ss) {
		ioutil.WriteFile(os.Args[1], []byte(fmt.Sprintf("%s", s)), 0644)
	}
}
