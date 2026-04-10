git# 🃏 Card Memory Game (Starter Project)

A beginner-friendly "Card Flipping Memory Game" (짝맞추기 게임) built with Python and Streamlit. Find all the matching pairs with the fewest moves!

## 📁 File Structure

```text
card_game/
├── app.py             # Main Streamlit application and UI logic (Grid rendering)
├── game_logic.py      # Core game mechanics (Card and MemoryGame classes)
├── requirements.txt   # Project dependencies
├── agent.md           # Instructions/Rules definition file
└── README.md          # Project documentation
```

## 🚀 How to Run

1. **Ensure you have Python installed.**
2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```
4. **Open your browser** and navigate to the URL provided in the terminal (usually `http://localhost:8501`).

## ✨ Currently Implemented Features

- **Object-Oriented Design**: Clean implementation of `Card` and `MemoryGame` entities matching classic memory card mechanics.
- **State Management**: Uses Streamlit's `st.session_state` to track card flips, matches, and moves persistently across clicks.
- **Smart Interactions**: Card matches resolve immediately updating the score, while incorrect pairs stay visible until the next click so players can memorise them.
- **Emoji Grid UI**: Uses Streamlit columns and auto-resizing buttons to create a responsive 4x4 card grid, with injected CSS for larger card sizes.

## 💡 Ideas for Expansion

Want to improve the game? Here are a few beginner-friendly ideas to try building:
- **Difficulty Levels**: Add a selectbox to choose grid sizes (e.g., 4x4, 6x6).
- **Time Limits & Leaderboards**: Track how fast the user finishes and display a top score.
- **Visuals**: Replace emoji symbols with local image files using `st.image()`.
