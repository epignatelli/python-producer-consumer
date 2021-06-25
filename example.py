def producer(q):
    while True:
        print("Producing", q.qsize())
        for _ in range(30):
            q.put(list(range(10)))
    return

def consumer(q):
    while True:
        print("Consuming", q.qsize())
        x = [q.get() for _ in range(3)]
    return

m = mp.Manager()
#  use a manager queue to synchronise it between proceses
queue = m.Queue(100)

p = mp.Process(target=producer, args=(queue,), daemon=True)
c = mp.Process(target=consumer, args=(queue,), daemon=True)

try:
    print("Starting")
    p.start()
    c.start()
except:
    print("Failed")
finally:
    p.join()
    c.join()
return
