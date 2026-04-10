import streamlit as st
import time
from game_logic import MemoryGame

# Page configuration
st.set_page_config(page_title="Card Memory Game", page_icon="🃏")

# Custom CSS for bigger buttons and centering
st.markdown("""
<style>
    div.stButton > button {
        height: 100px;
        font-size: 40px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🃏 Card Memory Game")

# Difficulty Settings
st.sidebar.title("⚙️ Settings")
difficulty = st.sidebar.selectbox("Difficulty", ["Easy", "Medium", "Hard"], index=1)

diff_settings = {
    "Easy": 6,   # 12 cards
    "Medium": 8, # 16 cards
    "Hard": 12   # 24 cards
}

pairs_count = diff_settings[difficulty]
cols_count = 4

if 'current_difficulty' not in st.session_state:
    st.session_state.current_difficulty = difficulty

# Restart if difficulty changed
if st.session_state.current_difficulty != difficulty:
    st.session_state.current_difficulty = difficulty
    if 'game' in st.session_state:
        del st.session_state.game
    st.rerun()

# Initialize game in session state
if 'game' not in st.session_state:
    st.session_state.game = MemoryGame(pairs_count=pairs_count)
    st.session_state.previewing = True
    st.session_state.start_time = None
    st.session_state.final_time = None

game = st.session_state.game

# Timer logic
if st.session_state.get('previewing', False):
    time_display = 0
elif st.session_state.get('final_time') is not None:
    time_display = int(st.session_state.final_time - st.session_state.get('start_time', time.time()))
elif st.session_state.get('start_time') is not None:
    time_display = int(time.time() - st.session_state.start_time)
else:
    time_display = 0
time_str = f"{time_display // 60:02d}:{time_display % 60:02d}"

# Display stats
col1, col2, col3 = st.columns(3)
col1.metric("Moves", game.moves)
col2.metric("Matches", f"{game.matches} / {game.pairs_count}")
col3.metric("Time", time_str)

st.markdown("---")

if st.session_state.get('previewing', False):
    st.info("⏱️ 5초 동안 카드의 위치를 기억하세요!")

# Draw the grid
cols = st.columns(cols_count)

for i, card in enumerate(game.cards):
    col_idx = i % cols_count
    with cols[col_idx]:
        if st.session_state.get('previewing', False):
            # All cards face up during preview
            st.button(card.symbol, key=f"preview_btn_{i}", disabled=True, use_container_width=True)
        elif card.is_matched:
            # Show the matched symbol
            st.button(card.symbol, key=f"card_{i}", disabled=True, use_container_width=True)
        elif card.is_flipped:
            # Show the flipped symbol
            st.button(card.symbol, key=f"card_{i}", disabled=True, use_container_width=True)
        else:
            # Face down button
            if st.button("❓", key=f"btn_{i}", use_container_width=True):
                game.flip_card(i)
                # If a second card was just picked, check if it's a match immediately.
                # This ensures the score updates instantly if they got it right.
                if game.second_pick is not None:
                    card1 = game.cards[game.first_pick]
                    card2 = game.cards[game.second_pick]
                    if card1.symbol == card2.symbol:
                        game.check_match()
                        if game.is_game_over() and st.session_state.get('final_time') is None:
                            st.session_state.final_time = time.time()
                st.rerun()

st.markdown("---")

# Handle preview delay dynamically rendering previously computed UI elements
if st.session_state.get('previewing', False):
    time.sleep(5)
    st.session_state.previewing = False
    st.session_state.start_time = time.time()
    st.rerun()

# End Game Message
if game.is_game_over() and not st.session_state.get('previewing', False):
    st.success(f"🎉 Congratulations! You won in {game.moves} moves!")
    st.balloons()

# Restart Button
if st.button("🔄 Restart Game", use_container_width=True):
    st.session_state.game = MemoryGame(pairs_count=pairs_count)
    st.session_state.previewing = True
    st.session_state.start_time = None
    st.session_state.final_time = None
    st.rerun()
