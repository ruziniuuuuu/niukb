import gymnasium as gym
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from torch.distributions import Categorical

# Policy Network - Neural network that outputs action probabilities
class PolicyNetwork(nn.Module):
    def __init__(self, input_size, output_size):
        super(PolicyNetwork, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(input_size, 128),
            nn.ReLU(),
            nn.Linear(128, output_size),
            nn.Softmax(dim=-1)
        )
    
    def forward(self, x):
        return self.network(x)

class PolicyGradient:
    def __init__(self, env_name='CartPole-v1', learning_rate=0.01, gamma=0.99):
        # Initialize environment
        self.env = gym.make(env_name, render_mode="rgb_array")
        self.gamma = gamma
        
        # Create policy network
        self.policy = PolicyNetwork(
            input_size=self.env.observation_space.shape[0],
            output_size=self.env.action_space.n
        )
        self.optimizer = optim.Adam(self.policy.parameters(), lr=learning_rate)
        
        # Storage for episode data
        self.rewards_history = []
    
    def select_action(self, state):
        # Convert state to tensor and get action probabilities
        state = torch.FloatTensor(state)
        probs = self.policy(state)
        
        # Sample action from probability distribution
        distribution = Categorical(probs)
        action = distribution.sample()
        
        # Return action and log probability
        return action.item(), distribution.log_prob(action)
    
    def train_episode(self):
        states, actions, rewards = [], [], []
        state, _ = self.env.reset()
        done = False
        
        # Collect trajectory
        while not done:
            action, log_prob = self.select_action(state)
            next_state, reward, terminated, truncated, _ = self.env.step(action)
            done = terminated or truncated
            
            # Store transition
            states.append(state)
            actions.append(log_prob)
            rewards.append(reward)
            
            state = next_state
        
        # Calculate returns
        returns = []
        G = 0
        for r in reversed(rewards):
            G = r + self.gamma * G
            returns.insert(0, G)
        returns = torch.tensor(returns)
        
        # Normalize returns
        returns = (returns - returns.mean()) / (returns.std() + 1e-8)
        
        # Calculate loss and update policy
        policy_loss = []
        for log_prob, G in zip(actions, returns):
            policy_loss.append(-log_prob * G)
        
        policy_loss = torch.stack(policy_loss).sum()
        
        self.optimizer.zero_grad()
        policy_loss.backward()
        self.optimizer.step()
        
        return sum(rewards)
    
    def train(self, num_episodes=1000):
        for episode in range(num_episodes):
            episode_reward = self.train_episode()
            self.rewards_history.append(episode_reward)
            
            if episode % 100 == 0:
                avg_reward = np.mean(self.rewards_history[-100:])
                print(f'Episode {episode}, Average Reward: {avg_reward:.2f}')
    
    def plot_training_results(self):
        # Plot the rewards history
        plt.figure(figsize=(10, 5))
        plt.plot(self.rewards_history)
        plt.title('Training Progress')
        plt.xlabel('Episode')
        plt.ylabel('Episode Reward')
        plt.grid(True)
        plt.show()

# Training example
if __name__ == "__main__":
    # Create and train the agent
    agent = PolicyGradient()
    agent.train(num_episodes=1000)
    
    # Plot the results
    agent.plot_training_results()
    
    # Test the trained policy
    state, _ = agent.env.reset()
    done = False
    total_reward = 0
    
    while not done:
        action, _ = agent.select_action(state)
        state, reward, terminated, truncated, _ = agent.env.step(action)
        done = terminated or truncated
        total_reward += reward
        agent.env.render()
    
    print(f'Test Episode Reward: {total_reward}')
