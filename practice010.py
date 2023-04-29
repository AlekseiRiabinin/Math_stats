# import libraries
import warnings
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statistics import mean
from bioinfokit.analys import stat

# ignore wornings
warnings.filterwarnings('ignore')

# 1) Провести дисперсионный анализ для определения того, 
# есть ли различия среднего роста среди взрослых футболистов, хоккеистов и штангистов.
# Даны значения роста в трех группах случайно выбранных спортсменов:
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.

# initial data
data = {
    'fA': [173, 175, 180, 178, 177, 185, 183, 182], 
    'fB': [177, 179, 180, 188, 177, 172, 171, 184, 180],
    'fC': [172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170]
}

# avg values
avg_A = mean(data['fA'])
avg_B = mean(data['fB'])

# lists of avg values
arr_A = [avg_A, avg_A, avg_A]
arr_B = [avg_B, avg_B]

# add avg to each dataset
data['fA'] = data['fA'] + arr_A
data['fB'] = data['fB'] + arr_B

# create dataframe
df = pd.DataFrame(data=data)

# reshape the dataframe suitable for statsmodels package 
df_melt = pd.melt(df.reset_index(), id_vars=['index'], value_vars=['fA', 'fB', 'fC'])

# replace column names
df_melt.columns = ['index', 'treatments', 'value']

# generate a boxplot to see the data distribution by treatments 
# using boxplot there is a detection of the difference between treatments
ax = sns.boxplot(x='treatments', y='value', data=df_melt, color='#99c2a2')
ax = sns.swarmplot(x="treatments", y="value", data=df_melt, color='#7d0013')
# plt.show()

# stats f_oneway functions takes the groups as input and returns ANOVA F and p value
fvalue, pvalue = stats.f_oneway(df['fA'], df['fB'], df['fC'])
print(f'\nf-value: {fvalue}\np-value: {pvalue}\n')

# Ordinary Least Squares (OLS) model
model = ols('value ~ C(treatments)', data=df_melt).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print('ANOVA table (OLS)\n----------------')
print(anova_table)
print()

# ANOVA table using bioinfokit
res = stat()
res.anova_stat(df=df_melt, res_var='value', anova_model='value ~ C(treatments)')
print('ANOVA table (bioinfokit)\n------------------------')
print(res.anova_summary)
print()

# perform multiple pairwise comparison (Tukey's HSD)
# unequal sample size data, tukey_hsd uses Tukey-Kramer test
# Note: p-value 0.001 from tukey_hsd output should be interpreted as <=0.001
res = stat()
res.tukey_hsd(df=df_melt, res_var='value', xfac_var='treatments', anova_model='value ~ C(treatments)')
print('Tukey-Kramer test\n-----------------')
print(res.tukey_summary)
print()

# QQ-plot
sm.qqplot(res.anova_std_residuals, line='45')
# plt.xlabel("Theoretical Quantiles")
# plt.ylabel("Standardized Residuals")
# plt.show()

# histogram
# plt.hist(res.anova_model_out.resid, bins='auto', histtype='bar', ec='k') 
# plt.xlabel("Residuals")
# plt.ylabel('Frequency')
# plt.show()

# Shapiro-Wilk test can be used to check the normal distribution of residuals
w, pvalue = stats.shapiro(model.resid)
print('Shapiro-Wilk test\n-----------------')
print(f'w: {w}\np-value: {pvalue}\n')

# Bartlett’s test to check the Homogeneity of variances
w, pvalue = stats.bartlett(df['fA'], df['fB'], df['fC'])
print('Bartlett’s test\n---------------')
print(f'w: {w}\np-value: {pvalue}\n')

# if there is a stacked table, the Bartlett's test is performed
res = stat()
res.bartlett(df=df_melt, res_var='value', xfac_var='treatments')
print('Bartlett’s test (stacked table)\n-------------------------------')
print(res.bartlett_summary)
print()

# if there is a stacked table, the Levene's test is performed
res = stat()
res.levene(df=df_melt, res_var='value', xfac_var='treatments')
print('Levene’s test (stacked table)\n-----------------------------')
print(res.levene_summary)
print()
