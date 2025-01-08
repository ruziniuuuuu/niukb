import numpy as np
import matplotlib.pylab as plt

class SGD:
    def __init__(self, lr = 0.01, momentum=0.0):
        self.lr = lr
        self.momentum = momentum
        self.velocity = None
    
    def update(self, params, grads):
        if self.velocity is None:
            self.velocity = {}
            for key, value in params.items():
                self.velocity[key] = np.zeros_like(value)

        for key in params.keys():
            self.velocity[key] = self.momentum * self.velocity[key] - self.lr * grads[key]
            params[key] += self.velocity[key]

        return params
    
# def example():
#     # A simple opt problem: f(x) = x^2
#     sgd = SGD(lr = 0.1, momentum=0.5)
#     x = {'w': np.array([5.0])} # init value

#     for _ in range(10):
#         # compute the grad: f'(x) = 2*x
#         grad = {'w': 2 * x['w']}
#         x = sgd.update(x, grad)
#         print(f"x = {x['w']}, f(x) = {x['w']**2}")
        

# if __name__ == "__main__":
#     example()

def optimize_and_collect(lr, momentum, n_iterations=50):
    """
    Run SGD optimization and collect history of x values
    """
    sgd = SGD(lr=lr, momentum=momentum)
    x = {'w': np.array([5.0])}  # initial value
    history = [x['w'][0]]
    
    for _ in range(n_iterations):
        grad = {'w': 2 * x['w']}  # gradient of f(x) = x^2
        x = sgd.update(x, grad)
        history.append(x['w'][0])
    
    return history

# Set different learning rates and momentum values to compare
learning_rates = [0.1, 0.2]
momentums = [0.0, 0.5, 0.9]

# Create a 2x2 subplot
fig, axes = plt.subplots(len(learning_rates), len(momentums), figsize=(12, 8))
fig.suptitle('SGD Optimization: f(x) = x^2', fontsize=14)

# Run optimization for each combination of parameters
for i, lr in enumerate(learning_rates):
    for j, momentum in enumerate(momentums):
        history = optimize_and_collect(lr, momentum)
        
        # Plot the optimization trajectory
        axes[i, j].plot(history, '-o', markersize=3)
        axes[i, j].set_title(f'lr={lr}, momentum={momentum}')
        axes[i, j].set_xlabel('Iterations')
        axes[i, j].set_ylabel('x value')
        axes[i, j].grid(True)
        
        # Add horizontal line at y=0 (optimal value)
        axes[i, j].axhline(y=0, color='r', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()

# Print final values
print("\nFinal x values after 50 iterations:")
print("-" * 40)
print("lr\tmomentum\tfinal x\t\tf(x)")
print("-" * 40)

for lr in learning_rates:
    for momentum in momentums:
        history = optimize_and_collect(lr, momentum)
        final_x = history[-1]
        print(f"{lr}\t{momentum}\t\t{final_x:.6f}\t{final_x**2:.6f}")