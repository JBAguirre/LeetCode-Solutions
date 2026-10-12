// Date Completed
// August 28, 2026

// Approach
// Since the last word only matters, the iteration starts at the last word which the
// letters are then iterated to count the number of letters until the iteration stops at a space.

// Time complexity:
// O(N)

// Space complexity:
// O(N)

// Code
function lengthOfLastWord(s: string): number {
let newtext = s.trim();
let wordSize: number = 0;
for (let i = newtext.length - 1; i >= 0; i--){
    if (newtext[i] == " "){
        break;
    }
    wordSize++;
}
return wordSize;
};