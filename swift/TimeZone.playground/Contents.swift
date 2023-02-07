import UIKit

var greeting = "Hello, playground"

//let date2 = Date.now
//
//
//public func getDateISOValue(date: Date,
//                            timezone: TimeZone) -> String? {
//
//    let dateISO = "YYYY-MM-DDThh:mm:ssTZD"
//    let TimeISO = "YYYY-MM-DDThh:mm:ssTZD"
//    let dateFormatter = DateFormatter()
//    dateFormatter.locale = Locale(identifier: "en_US_POSIX")
//    dateFormatter.timeZone = TimeZone(abbreviation: "MT")
//
//    dateFormatter.dateFormat = dateISO
//    print(dateFormatter.string(from: date))
//    return dateFormatter.string(from: date)
//}
//
//getDateISOValue(date: date2, timezone: .current)


// The default timeZone for ISO8601DateFormatter is UTC
let utcISODateFormatter = ISO8601DateFormatter()

// Printing a Date
let date = Date()
print(utcISODateFormatter.string(from: date))

// Parsing a string timestamp representing a date
let dateString = "2020-05-31T04:32:27Z"
let dateNow = Date.now
let utcDate = utcISODateFormatter.date(from: dateString)
let utcDateNow = utcISODateFormatter.string(from: dateNow)



// Properly convert Date to UTC
let utcISOFormat = ISO8601DateFormatter()
let utcDateTrial = utcISOFormat.string(from: Date.now)
