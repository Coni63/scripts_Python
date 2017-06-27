""" Determiner PI en lancer de flechette """

import threading
import random
import queue
import time 


def throw_arrow(p, sample_size):
    for _ in range(sample_size):
        x = random.random() * 2 - 1
        y = random.random() * 2 - 1
        p.put(x**2 + y**2 <= 1)


def count_arrow(current_queue, time_out = False):
    global count_in, count_out
    while not current_queue.empty():
        try:
            val = current_queue.get(block = True, timeout = time_out)
            if val:
                count_in += 1
            else:
                count_out += 1
        except:
            pass


def Methode_1(sample_size, Q1, Q2, file):
    print("Without Threading")

    global count_in, count_out

    count_in = 0
    count_out = 0

    start = time.time()

    for i in range(Q1):
        throw_arrow(file, sample_size)

    duration1 = time.time() - start
    print("time for throwing arrows : {} s".format(duration1))

    start2 = time.time()
    count_arrow(file)
    duration2 = time.time() - start2
    print("time for counting arrows : {} s".format(duration2))

    duration_total = time.time() - start
    print("total time : {} s".format(duration_total))
    print( "{} arrows in and {} arrows out".format( count_in, count_out ) )
    print( "Estimation of Pi : {}". format( (count_in * 4) / (sample_size * Q1) ))

    print("\n")
    return [duration1, duration2, duration_total]


def Methode_2(sample_size, Q1, Q2, file):
    print("Serial Threading")

    global count_in, count_out
    count_in = 0
    count_out = 0

    print("{} throwing thread and {} counting Thread". format(Q1, Q2))

    start = time.time()

    threads1 = []
    for i in range(Q1):
        t = threading.Thread(target=throw_arrow, args = [file, sample_size])
        threads1.append(t)
        t.start()
        t.join()

    duration1 = time.time() - start
    print("time for throwing arrows : {} s".format(duration1))

    start2 = time.time()

    threads2 = []
    for i in range(Q2):
        t2 = threading.Thread(target=count_arrow, args=[file])
        threads2.append(t2)
        t2.start()
        t2.join()

    duration2 = time.time() - start2
    print("time for counting arrows : {} s".format(duration2))

    duration_total = time.time() - start
    print("total time : {} s".format(duration_total))
    print( "{} arrows in and {} arrows out".format( count_in, count_out ) )
    print( "Estimation of Pi : {}". format( (count_in * 4) / (sample_size * Q1) ))

    print("\n")
    return [duration1, duration2, duration_total]


def Methode_3(sample_size, Q1, Q2, file):
    print("Parallel Threading")

    global count_in, count_out
    count_in = 0
    count_out = 0

    print("{} throwing thread and {} counting Thread". format(Q1, Q2))

    start = time.time()

    start = time.time()

    threads1 = []
    for i in range(Q1):
        t = threading.Thread(target=throw_arrow, args = [file, sample_size])
        threads1.append(t)
        t.start()

    start2 = time.time()

    threads2 = []
    for i in range(Q2):
        t2 = threading.Thread(target=count_arrow, args=[file, 0.005])
        threads2.append(t2)
        t2.start()

    for each in threads1:
        each.join()

    duration1 = time.time() - start
    print("time for throwing arrows : {} s".format(duration1))

    for each in threads2:
        each.join()

    duration2 = time.time() - start2
    print("time for counting arrows : {} s".format(duration2))

    duration_total = time.time() - start
    print("total time : {} s".format(duration_total))
    print( "{} arrows in and {} arrows out".format( count_in, count_out ) )
    print( "Estimation of Pi : {}". format( (count_in * 4) / (sample_size * Q1) ))

    print("\n")
    return [duration1, duration2, duration_total]


def main(sample = 100, Thread1 = 50, Thread2 = 14):
    q = queue.Queue()

    count_in = 0
    count_out = 0

    sample_per_thread = sample
    Q1 = Thread1
    Q2 = Thread2

    print("throwing {} arrows".format(Q1 * sample_per_thread))
    print("\n")

    timer = Methode_1(sample_per_thread, Q1, Q2, q)
    timer2 = Methode_2(sample_per_thread, Q1, Q2, q)
    timer3 = Methode_3(sample_per_thread, Q1, Q2, q)

    return [timer, timer2, timer3]

if __name__ == "__main__":
    main()