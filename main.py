import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ライフゲームの初期状態を生成する関数
def create_initial_state(rows, cols, density=0.2):
    return np.random.choice([1, 0], size=(rows, cols), p=[density, 1 - density])

# ライフゲームの次の状態を計算する関数
def compute_next_state(curr_state):
    rows, cols = curr_state.shape
    next_state = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            live_neighbors = np.sum(curr_state[max(0, i-1):min(rows, i+2), max(0, j-1):min(cols, j+2)]) - curr_state[i, j]
            if curr_state[i, j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    next_state[i, j] = 0
                else:
                    next_state[i, j] = 1
            else:
                if live_neighbors == 3:
                    next_state[i, j] = 1

    return next_state

# ライフゲームのアニメーションを作成する関数
def animate_life_game(initial_state, generations):
    fig, ax = plt.subplots()
    ax.set_xticks([])
    ax.set_yticks([])

    def update(frame):
        nonlocal initial_state
        ax.clear()
        ax.set_title(f"Generation {frame}")
        ax.imshow(initial_state, cmap='binary')
        initial_state = compute_next_state(initial_state)

    ani = animation.FuncAnimation(fig, update, frames=generations, interval=200)
    plt.show()

if __name__ == "__main__":
    rows = 20
    cols = 20
    generations = 16
    initial_state = create_initial_state(rows, cols, density=0.2)
    animate_life_game(initial_state, generations)
