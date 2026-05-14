#Question no.1

import simpy
import random

WAIT_TIMES = []

# Customer process
def customer(env, name, server, service_time):
    arrival_time = env.now
    print(f"{name} arrives at {arrival_time:.2f}")

    with server.request() as request:
        yield request

        wait = env.now - arrival_time
        WAIT_TIMES.append(wait)

        print(f"{name} starts service at {env.now:.2f}")
        yield env.timeout(service_time)

        print(f"{name} leaves at {env.now:.2f}")

# Customer generator
def customer_generator(env, server, inter_arrival, service_time):
    i = 0
    while True:
        yield env.timeout(random.randint(1, inter_arrival))
        i += 1
        env.process(customer(env, f"Customer {i}", server, service_time))

# Main simulation
env = simpy.Environment()

server = simpy.Resource(env, capacity=1)

env.process(customer_generator(env, server, 3, 4))

env.run(until=20)




#Question no.2

import simpy
import random

WAIT_TIMES = []

def customer(env, name, server, service_time):
    arrival_time = env.now
    print(f"{name} arrives at {arrival_time:.2f}")

    with server.request() as request:
        yield request

        wait = env.now - arrival_time
        WAIT_TIMES.append(wait)

        print(f"{name} starts service at {env.now:.2f}")
        yield env.timeout(service_time)

        print(f"{name} leaves at {env.now:.2f}")

def customer_generator(env, server, inter_arrival, service_time):
    i = 0
    while True:
        yield env.timeout(random.randint(1, inter_arrival))
        i += 1
        env.process(customer(env, f"Customer {i}", server, service_time))

env = simpy.Environment()

# Two servers
server = simpy.Resource(env, capacity=2)

env.process(customer_generator(env, server, 3, 4))

env.run(until=20)



#Question no.3

inter_arrival = 2
service_time = 5



#Question no.4

import simpy
import random

WAIT_TIMES = []

def customer(env, name, server, service_time):
    arrival = env.now

    with server.request() as request:
        yield request

        wait = env.now - arrival
        WAIT_TIMES.append(wait)

        yield env.timeout(service_time)

def customer_generator(env, server, inter_arrival, service_time):
    i = 0
    while True:
        yield env.timeout(random.randint(1, inter_arrival))
        i += 1
        env.process(customer(env, f"Customer {i}", server, service_time))

env = simpy.Environment()

server = simpy.Resource(env, capacity=1)

env.process(customer_generator(env, server, 3, 4))

env.run(until=30)

average_wait = sum(WAIT_TIMES) / len(WAIT_TIMES)

print("Average Waiting Time =", average_wait)
