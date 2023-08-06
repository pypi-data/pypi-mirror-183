# Autopysta
Autopysta is a python library for modeling 2-D highway traffic, it's written natively on C++ for better performance and wrapped in SWIG to be used in Python

- ## **Important**
    Only Python 3.8 works on Windows, other versions are not working due to problems with the .dll

    For Linux you can use any version from Python 3.8 onwards and there's also legacy support for python 2.7

    The 3.8 version is al compatible with Google Colaboratory

- ## Details
    The package comes with a .so file (Linux), a .pyd file (Windows) and a .py that uses those files depending on your OS

    There is no Mac OS support at the moment, but an implementation is planned for future realeses

- ## How to use

    ### Installation
    You can install Autopysta using the pip installer
    >`pip install autopysta`

    To begin using Autopysta you just need to import the module on Python:
    >`import autopysta`
    
    And now you can use all the functions available on the library

- ## Examples
   A quick implementation of Autopysta:
    ```
    import autopysta as ap


    geo = ap.geometry(1000, 1, 0, 1000)

    newell = ap.newell()

    # Since this example doesn't use lane changes we use the no lane change as our model
    lcm = ap.no_lch()

    creators_list = [ap.fixed_state_creator(newell, 20, 10),]

    total_time = 120

    # total_time must be a multiple of dt
    dt = 1.2

    pre_made_vehicles = []

    # We run the simulation
    simulation = ap.simulation(lcm, total_time, geo, creators_list, pre_made_vehicles, dt)

    results = simulation.run()

    # And plot the results
    results.plot_x_vs_t()
    ```
    This gives us the following output :
    >`INITIAL STATE SIMULATION`\
    >`[simulation.cpp] Out of loops, getting the answer ready`

    And the plot :
    ![autopysta_example](images/autopysta.png)

- ## Functions

    | Syntax | Description |
    |-------- | ------------- |
    |geometry(length, lanes, merge, diverge)|Set geometry of the simulated highway|
    |gipps()|Creates a Gipps model manager with default values|
    |lcm_gipps()|Creates a Gipps lane-changing model manager with default values|
    |lcm_gipps(p)|Creates a Gipps lane-changing model with a set of parameters|
    |newell()|Creates a Newell model manager with default values|
    |newell(p)|Create Newell model with a set of parameters|
    |p_gipps(an, bn, sn, vn, tau, bg)| Creates set of parameters with max acceleration, max deceleration, jam spacing, free-flow speed, reaction time, leader's max deceleration|
    |p_lcm_gipps()|Creates a Gipps lane-changing set of parameters with default values|
    |p_lcm_gipps(pvlow, pvhigh)|Creates a Gipps lane-changing set of parameters with free-flow speed to overtake and free-flow speed to change back to right lane|
    |p_newell(u, w, kj)| Creates set of parameters with free-flow speed, wave speed, jam density|
    |point(t, x, v, a, lane)| Point with initial time, position, speed, acceleration and lane|
    |simulation(d, T, g, c, dt)| Start simulation with lane changing model, total simulation, geometry, vehicle creator and timestep|
    |simulation.run()|Runs simulation object|
    | vehicle(hist_X, lane) | Create vehicle with only one lane and trajectory defined by every X in hist_X array |
    | vehicle(hist_X, lanes) | Create vehicle with multiple lanes allowed and trajectory defined by every X in hist_X array  |
    |vehicle(hist_point)|Create a vehicle with a trajectory defined by an array of points (the points include their lane)|
    |vehicle(m, x, v, lane)|Create a vehicle with the model, initial postion, initial speed and initial lane|
    |vehicle(m, p)|Create a vehicle with initial model and point|
    |version()| Autopysta version|

- ## Exceptions
    Autopysta has it's own set of custom exceptions written entirely in c++. 
    
    To use them import AutopystaException from the autopysta module
    > `from autopysta import AutopystaException`

    - ### Example
        ```
        import autopysta as ap
        from autopysta import AutopystaException

        #geometry's first parameter is length (which can't be smaller than 0)
        try:
            geo = ap.geometry(-100, 1, 30, 70)
        except AutopystaException as e:
            print(e)
        ```
        Running this code will throw the following exception:
        > `[autopysta module] [error #901]: Wrong parameters. Dt should be greater than zero.`
