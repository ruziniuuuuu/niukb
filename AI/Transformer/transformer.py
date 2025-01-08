import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class SimpleTransformer(nn.Module):
    def __init(self, input_dim, hidden_dim, output_dim, num_layers):
        super(SimpleTransformer, self).__init__()

        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.num_layers = num_layers

        # Input embedding: Convert input to hidden dimension
        self.embedding = nn.Linear(input_dim, hidden_dim)

        # Transformer layers
        self.transformer_layers = nn.ModuleList([
            TransformerLayer(hidden_dim) for _ in range(num_layers)
        ])

        # Output layer
        self.output_layer = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        # x shape: (batch_size, seq_length, input_dim)

        # Apply input embedding
        x = self.embedding(x) # Shape: (batch_size, seq_length, hidden_dim)

        # Apply transformer layers
        for layer in self.transformer_layers:
            x = layer(x)
        
        # Apply output layer
        output = self.output_layer(x) # Shape: (batch_size, seq_length, output_dim)

        return output
        

class TransformerLayer(nn.Module):
    def __init__(self, hidden_dim, dropout=0.1):
        super(TransformerLayer, self).__init__()

        # Self-attention layer
        self.self_attention = SelfAttention(hidden_dim)

        # Feedforward neural network
        self.ffn = nn.Sequential([
            nn.Linear(hidden_dim, hidden_dim * 4),
            nn.ReLU(),
            nn.Linear(hidden_dim * 4, hidden_dim)
        ])

        # Layer Normalization
        self.norm1 = nn.LayerNorm(hidden_dim)
        self.norm2 = nn.LayerNorm(hidden_dim)

        # Dropout
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        # Apply self-attention with residual connection and layer norm
        attn_output = self.self_attention(x)
        x = self.norm1(x + self.dropout(attn_output))

        # Apply ffn with residual connection and layer norm
        ffn_output = self.ffn(x)
        x = self.norm2(x + self.dropout(ffn_output))

        return x

class SelfAttention(nn.Module):
    def __init__(self, hidden_dim):
        super(SelfAttention, self).__init__()

        self.hidden_dim = hidden_dim

        # Define query, key, and value projections
        self.query = nn.Linear(hidden_dim, hidden_dim)
        self.key = nn.Linear(hidden_dim, hidden_dim)
        self.value = nn.Linear(hidden_dim, hidden_dim)

        # Scaling factor for dot product attention
        self.scale = math.sqrt(hidden_dim)
        
    def forward(self, x):
        # x shape: (batch_size, seq_length, hidden_dim)

        # Generate Q, K, and V
        Q = self.query(x)       # (batch_size, seq_length, hidden_dim)
        K = self.key(x)         # (batch_size, seq_length, hidden_dim)
        V = self.value(x)       # (batch_size, seq_length, hidden_dim)

        # Compute attention scores
        attn_scores = torch.matmul(Q, K.transpose(-2, -1)) / self.scale
        # Shape: (batch_size, seq_length, seq_length)

        # Apply softmax to get attn weights
        attn_weights = F.softmax(attn_scores, dim=-1)

        # Apply attn weights to values
        output = torch.matmul(attn_weights, V)
        # Shape: (batch_size, seq_length, hidden_dim)

        return output

