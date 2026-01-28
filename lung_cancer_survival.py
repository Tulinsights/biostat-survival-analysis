from lifelines import KaplanMeierFitter
from lifelines.datasets import load_lung
import matplotlib.pyplot as plt

# 1. Load the built-in dataset
data = load_lung()
# Time = 'time' (days), Event = 'status' (1=dead, 0=censored)

kmf = KaplanMeierFitter()

# 2. Fit the model for the entire cohort
kmf.fit(durations=data['time'], event_observed=data['status'])

# 3. Plot the Survival Function
kmf.plot_survival_function()
plt.title('Survival Function of Lung Cancer Patients')
plt.xlabel('Days since enrollment')
plt.ylabel('Survival Probability')
plt.show()

# 4. Professional Biostat Touch: Compare Sexes
kmf_m = KaplanMeierFitter()
kmf_f = KaplanMeierFitter()

male = (data['sex'] == 1)
kmf_m.fit(data['time'][male], data['status'][male], label='Male')
kmf_f.fit(data['time'][~male], data['status'][~male], label='Female')

kmf_m.plot_survival_function()
kmf_f.plot_survival_function()
plt.title('Survival Comparison by Sex')
