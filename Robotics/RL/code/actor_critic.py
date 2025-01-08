import gymnasium as gym
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from torch.distributions import Categorical

# Actor network: Policy network that outputs action probabilities
class Actor(nn.Module):
    def __init__(self, state_dim, action_dim):
        super(Actor, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(state_dim, 64),
            nn.ReLU(),
            nn.Linear(64, action_dim),
            nn.Softmax(dim=-1)
        )
    
    def forward(self, state):
        return self.network(state)

# Critic network: Value network that estimates state values
class Critic(nn.Module):
    def __init__(self, state_dim):
        super(Critic, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(state_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 1)
        )
    
    def forward(self, state):
        return self.network(state)

class ActorCritic:
    def __init__(self, env_name="CartPole-v1"):
        # Initialize environment
        self.env = gym.make(env_name)
        self.state_dim = self.env.observation_space.shape[0]
        self.action_dim = self.env.action_space.n
        
        # Initialize Actor and Critic networks
        self.actor = Actor(self.state_dim, self.action_dim)
        self.critic = Critic(self.state_dim)
        
        # Setup optimizers
        self.actor_optimizer = optim.Adam(self.actor.parameters(), lr=0.001)
        self.critic_optimizer = optim.Adam(self.critic.parameters(), lr=0.001)
        
        # Training parameters
        self.gamma = 0.99  # discount factor
        
        # For plotting
        self.reward_history = []
    
    def select_action(self, state):
        # Convert state to tensor
        state = torch.FloatTensor(state)
        
        # Get action probabilities from actor
        action_probs = self.actor(state)
        
        # Sample action from probability distribution
        dist = Categorical(action_probs)
        action = dist.sample()
        
        return action.item(), dist.log_prob(action)
    
    def train(self, num_episodes=1000):
        for episode in range(num_episodes):
            state = self.env.reset()[0]  # Get initial state
            episode_reward = 0
            
            while True:
                # Select action
                action, log_prob = self.select_action(state)
                
                # Take action in environment
                next_state, reward, terminated, truncated, _ = self.env.step(action)
                done = terminated or truncated
                
                # Convert states to tensor for critic
                state_tensor = torch.FloatTensor(state)
                next_state_tensor = torch.FloatTensor(next_state)
                
                # Get value estimates
                value = self.critic(state_tensor)
                next_value = self.critic(next_state_tensor)
                
                # Calculate TD error (Advantage)
                td_error = reward + self.gamma * next_value * (1 - done) - value
                
                # Calculate losses
                actor_loss = -log_prob * td_error.detach()
                critic_loss = td_error.pow(2)
                
                # Update networks
                self.actor_optimizer.zero_grad()
                actor_loss.backward()
                self.actor_optimizer.step()
                
                self.critic_optimizer.zero_grad()
                critic_loss.backward()
                self.critic_optimizer.step()
                
                episode_reward += reward
                state = next_state
                
                if done:
                    break
            
            self.reward_history.append(episode_reward)
            
            # Print progress
            if (episode + 1) % 50 == 0:
                avg_reward = np.mean(self.reward_history[-50:])
                print(f"Episode {episode + 1}, Average Reward: {avg_reward:.2f}")
    
    def plot_rewards(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.reward_history)
        plt.title('Training Rewards over Episodes')
        plt.xlabel('Episode')
        plt.ylabel('Total Reward')
        plt.grid(True)
        plt.show()

# Training example
if __name__ == "__main__":
    ac = ActorCritic()
    ac.train()
    ac.plot_rewards()
