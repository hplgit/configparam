from scitools.std import *
import ODESolver

v0 = 0.05
dtau = 0.05
T = 10
n = int(round(T/dtau))
t_points = linspace(0, T, n+1)
method = ODESolver.RungeKutta4(lambda v, tau: v*(1-v))
method.set_initial_condition(v0)
v, tau = method.solve(t_points)
plot(tau, v, title='Scaled logistic equation',
     savefig='tmp_logistic.eps')

def u_and_t(v, tau, alpha, R):
    return alpha*tau, R*v

figure()
for R in 100, 500, 1000:
    t, u = u_and_t(v, tau, alpha=1, R=R)
    plot(t, u, legend='R=%g' % R)
    hold('on')
savefig('tmp_logistic_R.eps')

figure()
for alpha in 1, 5, 10:
    t, u = u_and_t(v, tau, alpha=alpha, R=1000)
    plot(t, u, legend='alpha=%g' % alpha)
    hold('on')
savefig('tmp_logistic_alpha.eps')
