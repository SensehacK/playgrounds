//: Playground - noun: a place where people can play

import UIKit

var str = "Hello, playground"



func shortNameFromName2( name : String ) -> String {
    
    let lowerString = name.lowercased()

    let indexStartOfText = lowerString.index(lowerString.startIndex, offsetBy: 1)
    let subString1 = lowerString.substring(from: indexStartOfText)
    
    print(subString1)
    return subString1
    
}






func shortNameFromName( name : String ) -> String {
    
    var subString2 = ""
    let charSet = CharacterSet(charactersIn: "aeiou")
    
    if let index = name.lowercased().rangeOfCharacter(from: charSet)?.lowerBound {
        subString2 =  name.substring(from: index)
        print(subString2)
    }
    return subString2
}


//var ret = shortNameFromName(name: "Kautilya")



var ret = shortNameFromName(name: "Kysrutilya")
print(ret)

let bananaFanaTemplate = [
    "<FULL_NAME>, <FULL_NAME>, Bo B<SHORT_NAME>",
    "Banana Fana Fo F<SHORT_NAME>",
    "Me My Mo M<SHORT_NAME>",
    "<FULL_NAME>"].joined(separator: "\n")


func lyricsForName(lyricsTemplate: String, fullName: String) -> String {
    
    let short_name = shortNameFromName(name: fullName)
    
    let new_lyrics = lyricsTemplate.replacingOccurrences(of: "<FULL_NAME>", with: fullName)
    
    print(new_lyrics)
    let newer_lyrics = new_lyrics.replacingOccurrences(of: "<SHORT_NAME>", with: short_name)
    
    print(newer_lyrics)
    
    return newer_lyrics
}


lyricsForName(lyricsTemplate: bananaFanaTemplate, fullName: "Kautilya")