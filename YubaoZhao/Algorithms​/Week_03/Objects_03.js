// Objects Day 3
//
// Most Repeated Character
// Given a string, return the character that's used most often, along with the number of times it's repeated.

function mostRepeatedChar(str) {
    var char = {},
        mostRepeated = {},
        max = 0;
    for(var i = 0; i < str.length; i++) {
        if(char[str[i]]) {
            char[str[i]] += 1;
        }
        else {
            char[str[i]] = 1;
        }
        if(char[str[i]] >= max) {
            max = char[str[i]];
        }
    }
    for(item in char) {
        if(char[item] == max) {
            mostRepeated[item] = max;
        }
    }
    return mostRepeated;
}

str = prompt("Please input a string:","");
console.log("The string you input: \"%s\"",str);
obj = mostRepeatedChar(str);
console.log("Most Repeated Character:");
for(item in obj) {
    console.log("\"%s\" repeated %d times.",item,obj[item]);
}
