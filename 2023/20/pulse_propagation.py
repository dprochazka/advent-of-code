from dataclasses import dataclass
from enum import Enum, auto
from collections import Counter, deque, defaultdict

ADDR_BROADCASTER = "broadcaster"


class Pulse(Enum):
    LO = auto()
    HI = auto()


@dataclass(frozen=True)
class Packet:
    sender: str
    receiver: str
    signal: Pulse


class Module:
    def __init__(self, address, receivers):
        self.address = address
        self.receivers = receivers

    def produce(self, signal: Pulse):
        for r in self.receivers:
            yield Packet(self.address, r, signal)


class Broadcaster(Module):
    def __init__(self, receivers):
        self.address = ADDR_BROADCASTER
        self.receivers = receivers

    def broadcast(self):
        for r in self.receivers:
            yield Packet(self.address, r, Pulse.LO)


class FlipFlop(Module):
    def __init__(self, address, receivers):
        super().__init__(address, receivers)
        self.state = False  # OFF

    def _flip_state(self):
        self.state = not self.state

    def __call__(self, packet: Packet):
        if packet.signal == Pulse.HI:
            return
        elif self.state:
            self._flip_state()
            yield from self.produce(Pulse.LO)
        else:
            self._flip_state()
            yield from self.produce(Pulse.HI)


class Conjunction(Module):
    def __init__(self, address, receivers, inputs):
        super().__init__(address, receivers)
        self.inputs = inputs
        self.memory = {i: 0 for i in inputs}

    def _charged(self):
        return all(m == Pulse.HI for m in self.memory.values())

    def __call__(self, packet: Packet):
        self.memory[packet.sender] = packet.signal
        if self._charged():
            yield from self.produce(Pulse.LO)
        else:
            yield from self.produce(Pulse.HI)


class Handler:
    def __init__(self, network):
        self.network = network
        self.broadcaster = self.network[ADDR_BROADCASTER]
        self.queue = deque()
        self.pulse_counter = Counter()

    @property
    def counts(self):
        return self.pulse_counter[Pulse.LO], self.pulse_counter[Pulse.HI]

    def __call__(self, pushes):
        self.pulse_counter.update({Pulse.LO: pushes})
        for _ in range(pushes):
            self.queue.extend(self.broadcaster.broadcast())
            while len(self.queue) > 0:
                packet = self.queue.popleft()
                self.pulse_counter.update({packet.signal: 1})
                if module := self.network.get(packet.receiver):
                    self.queue.extend(module(packet))


def parse_input(lines):
    def parse_line(line):
        mod, out = line.split(" -> ")
        out = out.split(", ")
        if mod[0] in "&%":
            return mod[0], mod[1:], out
        else:
            return None, mod, out

    forward_map = {}
    reverse_map = defaultdict(list)
    for line in lines:
        _, addr, out = parse_line(line)
        forward_map[addr] = out
        for o in out:
            reverse_map[o].append(addr)

    network = {}
    for line in lines:
        t, addr, out = parse_line(line)
        if t == "%":
            network[addr] = FlipFlop(addr, forward_map[addr])
        elif t == "&":
            network[addr] = Conjunction(addr, forward_map[addr], reverse_map[addr])
        else:
            network[ADDR_BROADCASTER] = Broadcaster(forward_map[addr])
    return network


def pulse_propagation_one(lines):
    h = Handler(parse_input(lines))
    h(1000)
    return h.counts[0] * (h.counts[1])


if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = [line.rstrip() for line in input_file]
    print(pulse_propagation_one(lines))
