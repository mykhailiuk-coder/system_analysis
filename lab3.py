# task 1
import numpy as np
import matplotlib.pyplot as plt

# час спостереження
T = 100.0 
# кількість точок
n_steps = 1000   
# кількість процесів
n_paths = 10       

h = T / n_steps   
t = np.linspace(0, T, n_steps)

draws = np.random.normal(0, np.sqrt(h), size=(n_steps, n_paths))
draws[0, :] = 0
W_paths = np.cumsum(draws, axis=0)

t_limit = np.linspace(3, T, 500) 
y = np.sqrt(2 * t_limit * np.log(np.log(t_limit)))

plt.figure(figsize=(10, 6))

plt.plot(t, W_paths, linewidth=1, alpha=0.7)

plt.plot(t_limit, y, 'r--', linewidth=2, label=r'$\sqrt{2t \ln(\ln t)}$')
plt.plot(t_limit, -y, 'r--', linewidth=2)

plt.title("Вінеровий процес та закон повторного логарифма")
plt.xlabel("Час (t)")
plt.ylabel("W(t)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# task 2
import numpy as np
import matplotlib.pyplot as plt

s0 = 10      
mu = 0.05    
sigma = 0.2  

T = 10       
n_steps = 1000
n_paths = 3
dt = T / n_steps 

t = np.linspace(0, T, n_steps)

draws = np.random.normal(0, np.sqrt(dt), size=(n_steps, n_paths))
draws[0, :] = 0
W_paths = np.cumsum(draws, axis=0)

t_col = t[:, np.newaxis] 
s = s0 * np.exp((mu - sigma**2 / 2) * t_col + sigma * W_paths)

plt.figure(figsize=(10, 6))
plt.plot(t, s)
plt.axhline(s0, color='black', linestyle='--', alpha=0.3) # Лінія старту
plt.xlabel("Час")
plt.ylabel("Ціна активу")
plt.grid(True, alpha=0.3)
plt.show()

# task 3
import numpy as np
import matplotlib.pyplot as plt

lam = 2        
T = 10         
n_steps = 1000
dt = T / n_steps

t = np.linspace(0, T, n_steps)

p = np.random.uniform(size=n_steps) < (lam * dt)

poisson_process = np.cumsum(p)

plt.figure(figsize=(10, 5))
plt.step(t, poisson_process, where='post') 
plt.xlabel("Час")
plt.ylabel("Кількість подій (N_t)")
plt.grid(True, alpha=0.3)
plt.show()
