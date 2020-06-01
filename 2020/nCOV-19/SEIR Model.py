import scipy.integrate as spi
import numpy
import numpy as np
import pylab as pl

# Initial conditions
# 인구수 51780579

S0 = 910822 # (감염 대상군) 양성판정 + 검사중 + 음성판정
E0 = 23294 # (접촉군) 검사중
I0 = 11468 # (감염군) 확진자
R0 = 10675 # (회복군) 완치자 + 사망자(270)

nu = mu = 1/(70*365) # 자연사망율 반영

# Time vector
t = numpy.linspace(0,100,100)

N = S0 + I0 + R0 # 모집단

S0_ = S0/N
E0 =  E0/N
I0 = I0/N
R0 = R0/N

beta = 0.1934 # 중국논문에 나온 beta 값
gamma = 1/14
sigma = 0.25


Input = (S0_, E0 , I0)

def SEIR(INT, t):
    '''The main set of equation'''
    Y = np.zeros((3))
    X = INT  # S0,   I0
    Y[0] = mu - beta * X[0] * X[2] - mu * X[0]
    Y[1] = beta * X[0] * X[2] - sigma * X[1] - mu * X[1]
    Y[2] = sigma * X[1] - gamma * X[2] - mu * X[2]  # (자연사망자 제외)
    return Y  # for spicy.odeint


t_start = 0.0;
t_end = 150;
t_inc = 1.0
t_range = np.arange(t_start, t_end + t_inc, t_inc)
SEIR = spi.odeint(SEIR, Input, t_range)

Rec = 1. - (SEIR[:, 0] + SEIR[:, 1] + SEIR[:, 2])

pl.figure(figsize=(15, 10))
pl.subplot(311)
pl.plot(SEIR[:, 0], '-g', label='(S) Susceptibles');
pl.legend(loc=0)
pl.title('Prediction of nCOV-19 SEIR model')
pl.xlabel('Time(days)')
pl.ylabel('Susceptibles')

pl.subplot(312)
pl.plot(SEIR[:, 1], '-b', label='(E) Exposed')
pl.plot(SEIR[:, 2], '-r', label='(I) Infectious');
pl.legend(loc=0)
pl.xlabel('Time(days)')
pl.ylabel('Infectious')

pl.subplot(313)
pl.plot(Rec, '-k', label='(R) Recovereds')
pl.xlabel('Time(days)')
pl.legend(loc=0)
pl.ylabel('Recovereds')
pl.show()