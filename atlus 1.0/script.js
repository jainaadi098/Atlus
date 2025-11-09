// --- Game State Variables ---
let playerName = '';
let currentTurn = 1;
let currentLetter = '';
let usedWords = new Set();

// --- DOM Element References ---
const introScreen = document.getElementById('intro-screen');
const gameScreen = document.getElementById('game-screen');
const gameOverScreen = document.getElementById('game-over-screen');
const wordInput = document.getElementById('wordInput');
const feedback = document.getElementById('feedback');
const currentLetterDisplay = document.getElementById('currentLetter');
const wordList = document.getElementById('wordList');
const currentTurnDisplay = document.getElementById('currentTurn');
// Note: We hide the turnsLeftDisplay as it's no longer needed

/**
 * 1. Initializes the game after the player enters their name.
 */
function startGame() {
    const nameInput = document.getElementById('nameInput');
    playerName = nameInput.value.trim();

    if (playerName.length < 2) {
        alert("Please enter a valid name to start the game.");
        return;
    }

    // Set the initial state
    currentLetter = playerName.slice(-1).toLowerCase(); // Last letter of name
    usedWords.add(playerName.toLowerCase()); // Add the name as the first "word"

    // Update the DOM to start the game
    document.getElementById('welcomeMessage').textContent = `Hi, ${playerName}! Play until you make a mistake!`;
    currentLetterDisplay.textContent = currentLetter.toUpperCase();

    // Hide turn limit elements since it's an infinite game
    document.getElementById('turnsLeftDisplay').parentNode.style.display = 'none';

    // Transition screens
    introScreen.style.display = 'none';
    gameScreen.style.display = 'block';
    wordInput.focus();
}

/**
 * 2. Checks the word entered by the player.
 */
function checkWord() {
    const word = wordInput.value.trim().toLowerCase();
    wordInput.value = ''; // Clear the input field immediately
    feedback.style.visibility = 'hidden';

    // Validation Check 1: Empty or too short
    if (word.length < 2) {
        setFeedback('Please enter a word with at least two letters.', 'error');
        return;
    }

    // Validation Check 2: Correct starting letter
    if (word[0] !== currentLetter) {
        gameOver(`Game Over! Your word "${word.toUpperCase()}" must start with "${currentLetter.toUpperCase()}"!`);
        return;
    }

    // Validation Check 3: Word hasn't been used before
    if (usedWords.has(word)) {
        gameOver(`Game Over! The word "${word.toUpperCase()}" was already used.`);
        return;
    }

    // --- Success: Update Game State ---
    
    // 1. Update the letter
    currentLetter = word.slice(-1); // Get the last letter of the new word

    // 2. Add to used words and history list
    usedWords.add(word);
    addWordToHistory(word);

    // 3. Update turn counter
    currentTurn++;

    // 4. Update UI for the next turn
    setFeedback('✅ Correct! Keep going.', 'success');
    currentLetterDisplay.textContent = currentLetter.toUpperCase();
    currentTurnDisplay.textContent = currentTurn;
    wordInput.focus();
}

/**
 * Helper function to display feedback messages.
 */
function setFeedback(message, type) {
    feedback.textContent = message;
    feedback.style.visibility = 'visible';
    
    // Change background based on type (success or error)
    if (type === 'error') {
        feedback.style.backgroundColor = '#f8d7da'; // Light Red
        feedback.style.color = '#721c24'; // Dark Red
    } else if (type === 'success') {
        feedback.style.backgroundColor = '#d4edda'; // Light Green
        feedback.style.color = '#155724'; // Dark Green
    }
}

/**
 * Helper function to add a word to the history list.
 */
function addWordToHistory(word) {
    const listItem = document.createElement('li');
    // Display the word with its first and last letter capitalized for emphasis
    const displayWord = word[0].toUpperCase() + word.slice(1, -1) + word.slice(-1).toUpperCase();
    listItem.textContent = displayWord;
    wordList.appendChild(listItem);
}

/**
 * 3. Ends the game and displays the final score.
 */
function gameOver(message) {
    document.getElementById('gameOverTitle').textContent = '💔 Game Over!';
    // The final score is the current turn number minus 1 (since the game ends on the mistake turn)
    document.getElementById('finalScore').innerHTML = `${message}<br>Congratulations !! You Score <strong style="color: #dc3545;">${currentTurn - 1}</strong> Points.`;

    gameScreen.style.display = 'none';
    gameOverScreen.style.display = 'block';
}

// Allow pressing Enter to submit the word instead of clicking the button
wordInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        checkWord();
    }
});