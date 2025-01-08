import numpy as np
import matplotlib.pyplot as plt

class CliffWalking:
    def __init__(self):
        self.height = 4
        self.width = 12
        self.start_state = (3, 0)  # 左下角
        self.goal_state = (3, 11)  # 右下角
        self.current_state = self.start_state
        
        # 动作空间：上(0)、右(1)、下(2)、左(3)
        self.action_space = [0, 1, 2, 3]
        self.state_size = self.height * self.width
        
    def reset(self):
        self.current_state = self.start_state
        return self._state_to_index(self.current_state)
    
    def _state_to_index(self, state):
        return state[0] * self.width + state[1]
    
    def step(self, action):
        x, y = self.current_state
        
        # 根据动作移动
        if action == 0:    # 上
            x = max(0, x - 1)
        elif action == 1:  # 右
            y = min(self.width - 1, y + 1)
        elif action == 2:  # 下
            x = min(self.height - 1, x + 1)
        elif action == 3:  # 左
            y = max(0, y - 1)
            
        self.current_state = (x, y)
        
        # 判断是否掉入悬崖
        if x == 3 and 1 <= y <= 10:  # 悬崖区域
            reward = -100
            done = True
            self.current_state = self.start_state
        # 判断是否到达目标
        elif self.current_state == self.goal_state:
            reward = 0
            done = True
        else:
            reward = -1
            done = False
            
        return self._state_to_index(self.current_state), reward, done

class SARSA:
    def __init__(self, state_size, action_size, learning_rate=0.1, gamma=0.9, epsilon=0.3):
        self.q_table = np.zeros((state_size, action_size))
        self.alpha = learning_rate
        self.gamma = gamma
        self.epsilon = epsilon
        self.action_size = action_size
        
    def get_action(self, state):
        if np.random.random() < self.epsilon:
            return np.random.choice(self.action_size)
        return np.argmax(self.q_table[state])
    
    def update(self, state, action, reward, next_state, next_action):
        old_value = self.q_table[state][action]
        next_q = self.q_table[next_state][next_action]
        new_value = old_value + self.alpha * (reward + self.gamma * next_q - old_value)
        self.q_table[state][action] = new_value

class QLearning:
    def __init__(self, state_size, action_size, learning_rate=0.1, gamma=0.9, epsilon=0.3):
        self.q_table = np.zeros((state_size, action_size))
        self.alpha = learning_rate
        self.gamma = gamma
        self.epsilon = epsilon
        self.action_size = action_size
        
    def get_action(self, state):
        if np.random.random() < self.epsilon:
            return np.random.choice(self.action_size)
        return np.argmax(self.q_table[state])
    
    def update(self, state, action, reward, next_state):
        old_value = self.q_table[state][action]
        next_max = np.max(self.q_table[next_state])
        new_value = old_value + self.alpha * (reward + self.gamma * next_max - old_value)
        self.q_table[state][action] = new_value

def train_and_compare():
    env = CliffWalking()
    sarsa_agent = SARSA(state_size=env.state_size, action_size=len(env.action_space))
    q_agent = QLearning(state_size=env.state_size, action_size=len(env.action_space))
    
    episodes = 500
    sarsa_rewards = []
    q_rewards = []
    
    # 训练SARSA
    for episode in range(episodes):
        state = env.reset()
        action = sarsa_agent.get_action(state)
        total_reward = 0
        done = False
        
        while not done:
            next_state, reward, done = env.step(action)
            next_action = sarsa_agent.get_action(next_state)
            sarsa_agent.update(state, action, reward, next_state, next_action)
            
            total_reward += reward
            state = next_state
            action = next_action
            
        sarsa_rewards.append(total_reward)
        
    # 训练Q-learning
    for episode in range(episodes):
        state = env.reset()
        total_reward = 0
        done = False
        
        while not done:
            action = q_agent.get_action(state)
            next_state, reward, done = env.step(action)
            q_agent.update(state, action, reward, next_state)
            
            total_reward += reward
            state = next_state
            
        q_rewards.append(total_reward)
    
    # 绘制结果对比
    plt.figure(figsize=(10, 5))
    plt.plot(sarsa_rewards, label='SARSA')
    plt.plot(q_rewards, label='Q-Learning')
    plt.xlabel('Episode')
    plt.ylabel('Total Reward')
    plt.title('SARSA vs Q-Learning in Cliff Walking')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    train_and_compare()