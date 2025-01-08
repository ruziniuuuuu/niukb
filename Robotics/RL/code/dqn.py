import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from collections import deque
import random
import matplotlib.pyplot as plt
import gymnasium as gym

class DQN(nn.Module):
    def __init__(self, input_size, output_size):
        super(DQN, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(input_size, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, output_size)
        )
    
    def forward(self, x):
        return self.network(x)

class ReplayBuffer:
    def __init__(self, capacity):
        self.buffer = deque(maxlen=capacity)
    
    def push(self, state, action, reward, next_state, done):
        self.buffer.append((state, action, reward, next_state, done))
    
    def sample(self, batch_size):
        samples = random.sample(self.buffer, batch_size)
        states, actions, rewards, next_states, dones = zip(*samples)
        return states, actions, rewards, next_states, dones
    
    def __len__(self):
        return len(self.buffer)

class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        
        # Check if CUDA is available and set device
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Using device: {self.device}")
        
        self.policy_net = DQN(state_size, action_size).to(self.device)
        self.target_net = DQN(state_size, action_size).to(self.device)
        self.target_net.load_state_dict(self.policy_net.state_dict())
        
        # Adjusted hyperparameters for CartPole
        self.learning_rate = 0.001
        self.gamma = 0.99
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.batch_size = 32
        self.memory = ReplayBuffer(5000)
        
        self.optimizer = optim.Adam(self.policy_net.parameters(), lr=self.learning_rate)
        
    def select_action(self, state):
        if random.random() < self.epsilon:
            return random.randrange(self.action_size)
        
        with torch.no_grad():
            state = torch.FloatTensor(state).unsqueeze(0).to(self.device)
            q_values = self.policy_net(state)
            return q_values.argmax().item()
    
    def train(self):
        if len(self.memory) < self.batch_size:
            return
        
        # Sample from memory
        states, actions, rewards, next_states, dones = self.memory.sample(self.batch_size)
        
        # Convert to tensors and move to device
        states = torch.FloatTensor(states).to(self.device)
        actions = torch.LongTensor(actions).to(self.device)
        rewards = torch.FloatTensor(rewards).to(self.device)
        next_states = torch.FloatTensor(next_states).to(self.device)
        dones = torch.FloatTensor(dones).to(self.device)
        
        # Calculate current Q values
        current_q_values = self.policy_net(states).gather(1, actions.unsqueeze(1))
        
        # Calculate target Q values
        with torch.no_grad():
            next_q_values = self.target_net(next_states).max(1)[0]
            target_q_values = rewards + (1 - dones) * self.gamma * next_q_values
        
        # Calculate loss and update
        loss = nn.MSELoss()(current_q_values.squeeze(), target_q_values)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        
        # Update epsilon
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)
        
    def update_target_network(self):
        self.target_net.load_state_dict(self.policy_net.state_dict())

def train_dqn(visualize=True):
    env = gym.make('CartPole-v1')
    agent = DQNAgent(state_size=4, action_size=2)
    
    episodes = 500
    target_update = 10
    rewards_history = []
    
    for episode in range(episodes):
        state, _ = env.reset()
        total_reward = 0
        terminated = False
        truncated = False
        
        while not (terminated or truncated):
            action = agent.select_action(state)
            next_state, reward, terminated, truncated, _ = env.step(action)
            
            agent.memory.push(state, action, reward, next_state, terminated)
            agent.train()
            
            state = next_state
            total_reward += reward
            
        if episode % target_update == 0:
            agent.update_target_network()
            
        rewards_history.append(total_reward)
        
        if episode % 10 == 0:
            avg_reward = np.mean(rewards_history[-10:])
            print(f"Episode {episode}, Average Reward: {avg_reward:.2f}")
            
            # Early stopping if the agent performs well
            if avg_reward > 499:
                print(f"Environment solved in {episode} episodes!")
                break
    
    # Plot training curve
    plt.figure(figsize=(10, 5))
    plt.plot(rewards_history)
    plt.title('Training Reward Curve')
    plt.xlabel('Episode')
    plt.ylabel('Total Reward')
    plt.show()
    
    return agent, env

def visualize_policy(agent, env, episodes=5):
    """
    Visualize the trained policy for a few episodes
    
    Args:
        agent: trained DQN agent
        env: gymnasium environment
        episodes: number of episodes to visualize
    """
    for episode in range(episodes):
        state, _ = env.reset()
        total_reward = 0
        terminated = False
        truncated = False
        
        # Render the environment
        env = gym.make('CartPole-v1', render_mode='human')
        state, _ = env.reset()
        
        while not (terminated or truncated):
            # Render each frame
            env.render()
            
            # Select action using the trained policy (no exploration)
            with torch.no_grad():
                state_tensor = torch.FloatTensor(state).unsqueeze(0)
                q_values = agent.policy_net(state_tensor)
                action = q_values.argmax().item()
            
            # Take action in the environment
            state, reward, terminated, truncated, _ = env.step(action)
            total_reward += reward
            
        print(f"Episode {episode + 1}: Total Reward = {total_reward}")
    
    env.close()

if __name__ == "__main__":
    # Train the agent
    agent, env = train_dqn(visualize=True)
    
    # Visualize the trained policy
    visualize_policy(agent, env) 