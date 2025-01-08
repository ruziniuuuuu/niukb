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
    
def policy_evaluation(env, policy, V, gamma=0.99, theta=1e-6):
    """
    Evaluate a policy by computing the value function
    """
    while True:
        delta = 0
        for state in env.states:
            if state in env.terminal_states:
                continue

            v = V[state]

            action = policy[state]
            next_state = env.get_next_state(state, action)
            reward = env.get_reward(next_state)

            V[state] = reward + gamma * V[next_state]

            delta = max(delta, abs(v - V[state]))

        if delta < theta:
            break

    return V

def policy_imrovement(env, V, policy, gamma=0.99):
    """
    Improve policy based on current value function
    """
    policy_stable = True

    for state in env.states:
        if state in env.terminal_states:
            continue

        old_action = policy[state]
        action_values = []
        for action in env.actions:
            next_state = env.get_next_state(state, action)
            reward = env.get_reward(next_state)
            action_values.append(reward + gamma * V[next_state])

        # Update policy with best action
        policy[state] = env.actions[np.argmax(action_values)]

        if old_action != policy[state]:
            policy_stable = False

    return policy, policy_stable

def policy_iteration(env, gamma=0.9, theta=1e-6):
    """
    Main policy iteration algo
    """
    # Init value function and policy
    V = {state: 0 for state in env.states}
    # Init policy randomly
    policy = {
        state: env.actions[np.random.randint(len(env.actions))]
        for state in env.states
    }

    iteration = 0
    while True:
        # policy evaluation
        V = policy_evaluation(env, policy, V, gamma, theta)

        # policy Improvement
        policy, policy_stable = policy_imrovement(env, V, policy, gamma)

        iteration += 1
        if policy_stable:
            break

    return policy, V, iteration

def visualize_policy(policy, env):
    """
    Visualize the policy with arrows
    """
    action_symbols = {
        (0, 1): '→',   # right
        (1, 0): '↓',   # down
        (0, -1): '←',  # left
        (-1, 0): '↑'   # up
    }
    
    plt.figure(figsize=(8, 6))
    plt.grid(True)
    plt.xlim(-0.5, env.size-0.5)
    plt.ylim(-0.5, env.size-0.5)
    
    for state in env.states:
        if state in env.terminal_states:
            plt.text(state[1], env.size-1-state[0], 'G', 
                    ha='center', va='center')
        elif state in env.obstacles:
            plt.text(state[1], env.size-1-state[0], 'X', 
                    ha='center', va='center')
        else:
            action = policy[state]
            plt.text(state[1], env.size-1-state[0], 
                    action_symbols[action], ha='center', va='center')
    
    plt.title('Optimal Policy')
    plt.show()

# Run example
if __name__ == "__main__":
    env = GridWorld(size=4)
    optimal_policy, V, num_iterations = policy_iteration(env)
    print(f"Converged after {num_iterations} iterations")
    
    # Visualize results
    visualize_policy(optimal_policy, env)
    from value_iteration import visualize_value_function
    visualize_value_function(V, env)