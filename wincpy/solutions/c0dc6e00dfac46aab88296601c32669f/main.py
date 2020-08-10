from helpers import random_koala_fact

def unique_koala_facts(num_requested):
    loops, max_loops = 0, 1000
    facts = []
    while len(facts) < num_requested:
        fact = random_koala_fact()
        if fact not in facts:
            facts.append(fact)
        if loops > max_loops:
            break
        loops += 1
    return facts

def num_joey_facts():
    first_fact = random_koala_fact()
    times_seen_first_fact = 0
    num_joey_facts = 0
    # Using a set instead of a list for unique_facts would be better if you are
    # familiar with it.
    unique_facts = []

    while times_seen_first_fact < 10:
        fact = random_koala_fact()
        if fact == first_fact:
            times_seen_first_fact += 1
        if fact not in unique_facts:
            unique_facts.append(fact)
            if 'joey' in fact.lower():
                num_joey_facts += 1
    return num_joey_facts

def koala_weight():
    fact = random_koala_fact()
    while 'kg' not in fact.lower():
        fact = random_koala_fact()
    return int(fact.split('kg')[0].split(' ')[-1])


print(unique_koala_facts(20))
print(num_joey_facts())
print(koala_weight())
