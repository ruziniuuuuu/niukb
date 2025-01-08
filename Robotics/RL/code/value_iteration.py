import numpy as np
import matplotlib.pyplot as plt

class GridWorld:
    def __init__(self, size=4):
        self.size = size
        self.actions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右、下、左、上
        self.states = [(i, j) for i in range(size) for j in range(size)]
        self.terminal_states = [(0, 0), (size - 1, size - 1)]
        self.obstacles = [(1, 1)]
        
    def get_reward(self, state):
        if state == (0, 0):
            return 1
        elif state == (self.size - 1, self.size - 1):
            return 10
        else:
            return -0.1
            
    def get_next_state(self, state, action):
        next_state = (state[0] + action[0], state[1] + action[1])
        if (next_state[0] >= 0 and next_state[0] < self.size and 
            next_state[1] >= 0 and next_state[1] < self.size and
            next_state not in self.obstacles):
            return next_state
        return state

def value_iteration(env, gamma=0.99, theta=1e-6):
    # 初始化值函数
    V = {state: 0 for state in env.states}
    
    iteration = 0
    while True:
        delta = 0
        V_old = V.copy()
        
        # 对每个状态进行更新
        for state in env.states:
            if state in env.terminal_states:
                continue
                
            # 计算所有动作的值
            action_values = []
            for action in env.actions:
                next_state = env.get_next_state(state, action)
                reward = env.get_reward(next_state)
                action_values.append(reward + gamma * V_old[next_state])
            
            # 取最大值作为新的状态值
            V[state] = max(action_values)
            delta = max(delta, abs(V[state] - V_old[state]))
        
        iteration += 1
        if delta < theta:
            break
            
    return V, iteration

def visualize_value_function(V, env):
    value_grid = np.zeros((env.size, env.size))
    for state in env.states:
        value_grid[state[0], state[1]] = V[state]
    
    plt.figure(figsize=(8, 6))
    plt.imshow(value_grid, cmap='RdYlBu')
    plt.colorbar(label='Value')
    for i in range(env.size):
        for j in range(env.size):
            plt.text(j, i, f'{value_grid[i,j]:.2f}', 
                    ha='center', va='center')
    plt.title('Value Function')
    plt.show()

# 运行示例
env = GridWorld(size=4)
V, num_iterations = value_iteration(env)
print(f"收敛于 {num_iterations} 次迭代后")
visualize_value_function(V, env)