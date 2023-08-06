import autopysta as ap

geo = ap.geometry(1000, 1, 0, 1000)

newell = ap.newell()

lcm = ap.no_lch()

creators_list = [ap.fixed_state_creator(newell, 20, 10),]

total_time = 120
dt = 1.2

pre_made_vehicles = []

simulation = ap.simulation(lcm, total_time, geo, creators_list, pre_made_vehicles, dt)

results = simulation.run()

results.plot_x_vs_t()