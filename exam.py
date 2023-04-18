import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.rcParams["font.size"] = 12
plt.rcParams['xtick.labelsize'] = 12.
plt.rcParams['ytick.labelsize'] = 12.
plt.rcParams['axes.unicode_minus'] = False

CHART_NAME = 'bandi'
cnt, PNG, UNDERBAR = 0, '.png', '_'
filename = 'mpg.csv'

mpg = pd.read_csv(filename, encoding='CP949')

def FileSave():
    global cnt
    cnt += 1
    savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
    plt.savefig(savefile, dpi=400)
    print(savefile + ' 파일이 저장되었습니다.')

import seaborn as sbn
ax = plt.subplots()
sbn.scatterplot(data=mpg[mpg['class'] == 'suv'], x='displ', y='cty')
ax = sbn.rugplot(data=mpg[mpg['class'] == 'suv'], x='displ', y='cty')
ax.set_title('Scatter plot and Rug plot [Jeonggyu-Hwang 202337139]')
ax.set_xlabel('Engine size')
ax.set_ylabel('Mileage')
FileSave()

print("mpg['drv'].unique()")
print(mpg['drv'].unique())
