import scipy.integrate
import numpy
import matplotlib.pyplot as plt

# 2020년 2월 18일 기준 (31번 확진자 신천지 방문)

# Initial conditions
# pop = 51780579 # 총인구수

S0 = 910822 # 양성판정 + 검사중 + 음성판정
E0 = 23294 # 검사중
I0 = 11468 # 확진자
R0 = 10675 # 완치자 + 사망자(270)

# Time vector
t = numpy.linspace(0, 100, 100)

N = S0 + I0 + R0  # 모집단

S0_ = S0 / N
I0 = I0 / N
R0 = R0 / N

beta = 0.1934 # S ->I 감염율

ramda = 1 / 14 # I ->R 회복율
gamma = 0.25


# ODEs 전염병예측모델에서 가장 전통적인 SIR 모델을 정의함
def SIR_model(y, t, beta, ramma):
    S, I, R = y

    dS_dt = -beta * S * I
    dI_dt = beta * S * I - ramma * I
    dR_dt = ramma * I

    return ([dS_dt, dI_dt, dR_dt])


# Result
solution = scipy.integrate.odeint(SIR_model, [S0_, I0, R0], t, args=(beta, ramda))
solution = numpy.array(solution)

# plot result
plt.figure(figsize=(10, 6))
plt.plot(t, solution[:, 0], label="S(Susceptibles)")
plt.plot(t, solution[:, 1], label="I (Infectious)")
plt.plot(t, solution[:, 2], label="R(Recovereds)")
plt.grid()
plt.legend()
plt.xlabel("Time")
plt.ylabel("Proportion")
plt.title("SIR model")
plt.box(False)
plt.show()