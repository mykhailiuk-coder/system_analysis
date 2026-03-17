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
