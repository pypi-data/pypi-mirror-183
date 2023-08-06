import autopysta as ap
import matplotlib.pyplot as pt
from numpy import cos,sin
from autopysta import AutopystaException
#from exceptions import BaseException


print(ap.version())
vl = 120.0/3.6
vlc= 10

pc=ap.p_gipps(1,-1,6.5,vlc,0.8,-1)
mc=ap.gipps(pc)
pa=ap.p_gipps(1.7,-3.4,6.5,vl,0.8,-3.2)
ma=ap.gipps(pa)
mi=ap.newell()

known_trajectory = []
known_trajectory2 = []
for i in range(1000):
    known_trajectory.append(ap.point(i/10.0, i - 100*cos(i/100.), 10+10*sin(i/10.), 0.1, 3)) # tiempo, posicionX, vel, ac, pista
    known_trajectory2.append(ap.point(i/10.0, 100 + i - 100*cos(i/100.), 10+10*sin(i/10.), 0.1, 1)) # tiempo, posicionX, vel, ac, pista
    
try:
    my_car = ap.vehicle(known_trajectory)
    my_car2 = ap.vehicle(known_trajectory2)
except BaseException as exc:
    print (exc.args[0])
#except RuntimeError as e:
#    print e.args[0]

vv=[ap.vehicle(mc,100,vlc,1),
    #my_car, my_car2,
    ap.vehicle(mc,100,vlc,2),
    ap.vehicle(mc,40,0,1)
    ]
#vv=[]

geo = ap.geometry(1000, 2, 300, 700)
ccrr=[ap.fixed_demand_creator(ma, 0.5, 10), #20, 0, 10), 
      ap.fixed_demand_creator(ma, 0.45), #20, 0), 
      ap.fixed_demand_creator(mc, 0.42)] #20, 0)]

#lcm = ap.no_lch()
lcm  = ap.lcm_gipps()


    #ERROR AS -0.1 us not valid
    #Testing if I can get custom exceptions to work
try:
    s = ap.simulation(lcm, 90, geo, ccrr, vv, -0.1)
except AutopystaException as e:
    print(e)


try:
    r = s.run()
    r.plot_x_vs_t(1) #plot all lanes
    r.plot_x_vs_t(2)
    r.plot_x_vs_t(3)
except AutopystaException as e:
    print(e.args[0])
except BaseException as e:
    print("[BaseException]:", e.args[0])

     




