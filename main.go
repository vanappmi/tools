package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"

	"github.com/spf13/viper"
	yaml "gopkg.in/yaml.v2"
)

type repo struct {
	Charts struct {
		Name string `yaml:"name"`
		Repo string `yaml:"repo"`
		Tags string `yaml:"tags"`
	} `yaml:"Charts"`
}

func main() {

	viper.SetConfigName("config")
	viper.AddConfigPath(currentdir())
	err := viper.ReadInConfig() // Find and read the config file
	if err != nil {             // Handle errors reading the config file
		log.Fatal(err)
	}

	C := repo{}

	err = viper.Unmarshal(&C)
	if err != nil {
		log.Fatalf("unable to decode into struct, %v", err)
	}

	fmt.Println(C)

	// Change value in map and marshal back into yaml
	C.Charts.Tags = "realtag"

	fmt.Println(C)

	d, err := yaml.Marshal(&C)
	if err != nil {
		log.Fatalf("error: %v", err)
	}

	fmt.Println(string(d))

	// write to file
	f, err := os.Create("/tmp/dat2")
	if err != nil {
		log.Fatal(err)
	}

	err = ioutil.WriteFile("changed.yaml", d, 0644)
	if err != nil {
		log.Fatal(err)
	}

	f.Close()

}

func currentdir() (cwd string) {
	cwd, err := os.Getwd()
	if err != nil {
		log.Fatal(err)
	}

	return cwd
}
