import numpy as np
import matplotlib.pyplot as plt
from numpy.random import default_rng

# Das ist die Aufgabe 5 aus Sheet03


class LCG:
    """A linear congruential generator"""

    def __init__(self, seed=0, a=1664525, c=1013904223, m=2**32):
        """store seed and LCG properties"""
        self.a = a
        self.c = c
        self.m = m
        # Value from previous iteration
        self.state = seed

    def advance(self):
        """
        advance the state of this random generator by one step
        Blatt 3, Aufgabe 1
        """
        a = self.a
        c = self.c
        m = self.m
        x = self.state
        y = (a * x + c) % m
        self.state = y
        # Fügen Sie hier Ihren Code ein, um den LCG korrekt zu implementieren

    def random_raw(self, size=None):
        """
        Draw raw LCG random numbers, meaning no transformation is happening
        """
        # if size is not given, just return a single number
        if size is None:
            self.advance()
            return self.state

        numbers = np.empty(size, dtype="uint64")
        # get a 1d-reference to the nd-array so we can fill it in
        # simple loop
        flat = numbers.flat

        for i in range(numbers.size):
            self.advance()
            flat[i] = self.state

        return numbers

    def uniform(self, low=0, high=1, size=None):
        """
        Draw uniforn random numbers by converting them from the raw numbers"""
        raw = self.random_raw(size=size)

        # Fügen Sie hier ihren Code ein, um die rohen Zufallszahlen
        # zu kontinuierlich gleichverteilten Zufallszahlen zwischen
        # low und high zu transformation
        # Von Niv: für eine Transformation in eine uniform Distribution gilt nach Vorlesung: (high-low)*u=y
        # hiermit gilt:
        a = raw
        m = max(a)
        b = min(a)
        raw = a * (high - low) / (m - b)
        result = raw
        return result


a = [1, 7]
for i in range(0, len(a)):
    Test = LCG(0, a=a[i], c=3, m=1024)
    seed = Test.state
    Test.advance()
    c = 0
    while seed != Test.state:
        Test.advance()
        c += 1
    print(f"Die Periodenlänge für {a[i]} beträgt {c}")

# Hier für Teilaufgabe d)
Testd = LCG(0, a=1601, c=3456, m=10000)
c = Testd.uniform(0, 1, 100000)
print(c.dtype)
fig, ax = plt.subplots(constrained_layout=True)
# limit = [0, 1]
bins = 100
hist_options = dict(
    bins=bins,
    # range=limit,
    histtype="step",
)
# plt.hist(c, label="Uniform-Distribution", **hist_options)
# plt.show()
# Oder
y, binEdges = np.histogram(c, bins=bins)
bin_centers = 0.5 * (binEdges[:-1] + binEdges[1:])
yerr = np.sqrt(y)
width = np.diff(binEdges)
ax.bar(bin_centers, y, width=width, yerr=yerr)
# Hat eine UNabhängigkeit von seed.......
# Kreiere scatter.plot
# c ist x[j], d ist x[j+1], e ist x[j+2]
print(c[1:])
c_2d = c[:-1]
d = c[1:]
fig2, ax2 = plt.subplots(constrained_layout=True)

ax2.scatter(
    c_2d,
    d,
    s=5,  # smaller dots,
    alpha=0.2,  # some transparency for this many points
    linewidth=0,  # no border around points
)
fig3 = plt.figure()
ax3 = fig3.add_subplot(1, 1, 1, projection="3d")
c_3d = c[:-2]
d_3d = d[:-1]
e = c[2:]
ax3.scatter(c_3d, d_3d, e, s=5, alpha=0.3)

plt.show()

# Für e) nutze diesselben Plots nur mit  np.random.default_rng
