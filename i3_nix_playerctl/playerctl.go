package main

import (
	"fmt"
	"log"
	"os"
	"os/exec"
	"strings"
	"time"
)

const MAXLEN = 30

func executeCommand(cmd string) string {
	var command string
	args := strings.Split(cmd, " ") // first arg is acctual command
	if len(args) > 1 {
		command = args[0]
		args = args[1:]
	} else {
		command = cmd
	}
	out, err := exec.Command(command, args...).Output()
	if err != nil {
		log.Fatal(err)
	}
	return strings.Trim(string(out), " \n")
}

func getTitle(player string) string {
	cmd := fmt.Sprintf("playerctl -p %s metadata title", player)
	out := executeCommand(cmd)
	if out == "(null)" {
		out = ""
	}
	return out
}

func getStatus(player string) string {
	cmd := fmt.Sprintf("playerctl -p %s status", player)
	out := executeCommand(cmd)
	return out
}

func getVolume(player string) string {
	args := strings.Split(fmt.Sprintf("volume -p %s", player), " ")
	out, err := exec.Command("playerctl", args...).Output()
	if err != nil {
		log.Fatal(err)
	}
	return strings.Trim(string(out), " \n")
}

func printSongTitle(title, volume string) {
	var maxLen int64
	maxLen = MAXLEN - 3 //for player chars

	l := int64(len(title))
	if volume != "" {
		l = l + 3
	}

	if l == 0 { // if empty
		fmt.Println(" ")
	} else if l > maxLen { // if len is greater than maxlen
		i := time.Now().Unix() % (l - maxLen)

		if i+maxLen >= l {
			i = l - maxLen
		}

		if volume == "" {
			fmt.Println(title[i : i+maxLen+1])
		} else {
			fmt.Println(title[i:i+maxLen+1-3] + " " + volume)
		}
	} else { // if len is ok
		if volume == "" {
			fmt.Println(title)
		} else {
			fmt.Println(title + " " + volume)
		}
	}
}

func printColor(status string) {
	switch status {
	case "Playing":
		fmt.Println("#00AFFF")
		fmt.Println("#00AFFF")
	case "Paused":
		fmt.Println("#9616DB")
		fmt.Println("#9616DB")
	default:
		fmt.Println("#FF0000")
		fmt.Println("#FF0000")
	}
}

func defaultPrint(title, player string) {
	printSongTitle(title, "")
	printColor(getStatus(player))
}

func main() {
	player := os.Getenv("BLOCK_INSTANCE")
	buttonValue := os.Getenv("BLOCK_BUTTON")

	if player == "" {
		player = "audacious"
	}

	status := getStatus(player)
	title := getTitle(player)

	if buttonValue != "" {
		switch buttonValue {
		case "1":
			executeCommand(fmt.Sprintf("playerctl -p %s play-pause", player))
			defaultPrint(title, player)
		case "2":
			if player == "audacious" {
				executeCommand(fmt.Sprintf("killall audacious"))
				defaultPrint(title, player)
			}
		case "3":
			executeCommand(fmt.Sprintf("playerctl -p %s stop", player))
			defaultPrint(title, player)
		case "4":
			executeCommand(fmt.Sprintf("playerctl -p %s volume 0.05+", player)) // if step is higher, it won't go near 100%
			printSongTitle(title, getVolume(player))
			printColor(status)
		case "5":
			executeCommand(fmt.Sprintf("playerctl -p %s volume 0.05-", player)) // if step is higher, it won't go near 100%
			printSongTitle(title, getVolume(player))
			printColor(status)
		case "8":
			executeCommand(fmt.Sprintf("playerctl -p %s next", player))
			defaultPrint(title, player)
		case "9":
			executeCommand(fmt.Sprintf("playerctl -p %s previous", player))
			defaultPrint(title, player)
		}
	} else {
		defaultPrint(title, player)
	}
}
