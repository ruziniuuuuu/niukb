import numpy as np
import matplotlib.pyplot as plt

class GridWorld:
    def __init__(self, size=4):
        self.size = size
        self.state_size = size * size
        self.action_space = [0, 1, 2, 3]  # 上、右、下、左
        self.reset()
        
    def reset(self):
        self.state = 0  # 起始位置在左上角
        return self.state
        
    def step(self, action):
        x = self.state // self.size
        y = self.state % self.size
        
        # 根据动作移动
        if action == 0:    # 上
            x = max(0, x - 1)
        elif action == 1:  # 右
            y = min(self.size - 1, y + 1)
        elif action == 2:  # 下
            x = min(self.size - 1, x + 1)
        elif action == 3:  # 左
            y = max(0, y - 1)
            
        self.state = x * self.size + y
        
        # 判断是否到达目标（右下角）
        done = self.state == self.size * self.size - 1
        reward = 100 if done else -1
        
        return self.state, reward, done

class SARSA:
    def __init__(self, state_size, action_size, learning_rate=0.1, gamma=0.9, epsilon=0.1):
        self.state_size = state_size
        self.action_size = action_size
        self.q_table = np.zeros((state_size, action_size))
        self.alpha = learning_rate  # 学习率
        self.gamma = gamma         # 折扣因子
        self.epsilon = epsilon     # ε-贪婪策略的参数
        
    def get_action(self, state):
        if np.random.random() < self.epsilon:
            return np.random.choice(self.action_size)
        return np.argmax(self.q_table[state])
    
    def update(self, state, action, reward, next_state, next_action):
        old_value = self.q_table[state][action]
        next_q = self.q_table[next_state][next_action]
        new_value = old_value + self.alpha * (reward + self.gamma * next_q - old_value)
        self.q_table[state][action] = new_value

def train():
    env = GridWorld(size=4)
    agent = SARSA(state_size=env.state_size, 
                  action_size=len(env.action_space))
    
    episodes = 500
    rewards_history = []
    
    for episode in range(episodes):
        state = env.reset()
        action = agent.get_action(state)
        total_reward = 0
        done = False

        while not done:
            next_state, reward, done = env.step(action)
            next_action = agent.get_action(next_state)
            agent.update(state, action, reward, next_state, next_action)
            
            total_reward += reward
            state = next_state
            action = next_action
        
        rewards_history.append(total_reward)
        
        if (episode + 1) % 50 == 0:
            print(f"Episode {episode + 1}, Total Reward: {total_reward}")
    
    plt.plot(rewards_history)
    plt.xlabel('Episode')
    plt.ylabel('Total Reward')
    plt.title('SARSA Learning Curve')
    plt.show()
    
    print("\nFinal Q-table:")
    print(agent.q_table)

if __name__ == "__main__":
    train()