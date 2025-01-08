import numpy as np
import random
import matplotlib.pyplot as plt

class GridWorld:
    def __init__(self, size=4):
        self.size = size
        self.state = 0
        self.goal = size * size - 1
        self.state_size = size * size
        self.action_space = [0, 1, 2, 3]

    def reset(self):
        self.state = 0
        return self.state
    
    def step(self, action):
        x = self.state // self.size
        y = self.state % self.size

        if action == 0: # up
            x = max(0, x - 1)
        elif action == 1: # right
            y = min(self.size - 1, y + 1)
        elif action == 2: # down
            x = min(self.size - 1, x + 1)
        elif action == 3: # left
            y = max(0, y - 1)

        self.state = x * self.size + y

        if self.state == self.goal:
            reward = 100
            done = True
        else:
            reward = -1
            done = False

        return self.state, reward, done
    
class QLearning:
    def __init__(self, state_size, action_size, learning_rate=0.1, gamma=0.9, epsilon=0.1):
        self.state_size = state_size
        self.action_size = action_size
        self.learning_rate = learning_rate
        self.gamma = gamma
        self.epsilon = epsilon

        self.q_table = np.zeros((state_size, action_size))

    def get_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, self.action_size - 1)
        else:
            return np.argmax(self.q_table[state])
        
    def update(self, state, action, reward, next_state):
        old_value = self.q_table[state, action]
        next_max = np.max(self.q_table[next_state])
        new_value = old_value + self.learning_rate * (reward + self.gamma * next_max - old_value)
        self.q_table[state, action] = new_value

def train():
    env = GridWorld(size=20)
    agent = QLearning(state_size=env.state_size, action_size=len(env.action_space))

    episodes = 1000
    rewards_history = []
    for episode in range(episodes):
        state = env.reset()
        done = False
        total_reward = 0

        while not done:
            action = agent.get_action(state)
            next_state, reward, done = env.step(action)
            agent.update(state, action, reward, next_state)
            state = next_state
            total_reward += reward

        rewards_history.append(total_reward)

        if episode % 10 == 0:
            print(f"Episode {episode + 1}, Total Reward: {total_reward}")

    plt.plot(rewards_history)
    plt.xlabel("Episode")
    plt.ylabel("Total Reward")
    plt.title("Training Progress")
    plt.show()

if __name__ == "__main__":
    train()